from django.core.exceptions import ObjectDoesNotExist, ValidationError

from send_sms.models import SMS_Log, SMSParameters, SMSSettings

# Create your views here.


def validate_receiver_nos(receiver_list):
    validated_receiver_list = []
    for d in receiver_list:
        if not d:
            break

        # remove invalid character
        for x in [" ", "-", "(", ")"]:
            d = d.replace(x, "")

        validated_receiver_list.append(d)

    if not validated_receiver_list:
        raise ValidationError("Please enter valid mobile nos")

    return validated_receiver_list


def send_sms(receiver_list: list, msg: str, sender_name="", success_msg=True):

    import json

    if isinstance(receiver_list, str):
        receiver_list = json.loads(receiver_list)
        if not isinstance(receiver_list, list):
            receiver_list = [receiver_list]

    receiver_list = validate_receiver_nos(receiver_list)

    arg = {
        "receiver_list": receiver_list,
        "message": msg.encode("utf-8"),
        "success_msg": success_msg,
    }
    if SMSSettings.objects.first():
        send_via_gateway(arg)
    else:
        raise ObjectDoesNotExist("Please Update SMS Settings")


def send_via_gateway(arg):
    ss = SMSSettings.objects.first()
    headers = get_headers()
    use_json = headers.get("Content-Type") == "application/json"

    message = arg.get("message")
    args = {ss.message_parameter: message}
    parameters = SMSParameters.objects.filter(sms_settings=ss)
    for d in parameters:
        if not d.header:
            args[d.parameter] = d.value

    success_list = []
    for d in arg.get("receiver_list"):
        args[ss.receiver_parameter] = d
        status = send_request(ss.sms_gateway_url, args,
                              headers, ss.use_post, use_json)

        if 200 <= status < 300:
            success_list.append(d)

    if len(success_list) > 0:
        args.update(arg)
        create_sms_log(args, success_list)
        if arg.get("success_msg"):
            print(f"SMS sent to following numbers: {', '.join(success_list)}")


def get_headers(sms_settings=None):
    if not sms_settings:
        sms_settings = SMSSettings.objects.first()
        parameters = SMSParameters.objects.filter(sms_settings=sms_settings)

    headers = {"Accept": "text/plain, text/html, */*"}
    for d in parameters:
        if d.header == True:
            headers.update({d.parameter: d.value})

    return headers


def send_request(gateway_url, params, headers=None, use_post=False, use_json=False):
    import requests

    if not headers:
        headers = get_headers()
    kwargs = {"headers": headers}

    if use_json:
        kwargs["json"] = params
    elif use_post:
        kwargs["data"] = params
    else:
        kwargs["params"] = params

    if use_post:
        response = requests.post(gateway_url, **kwargs)
    else:
        response = requests.get(gateway_url, **kwargs)
    response.raise_for_status()
    return response.status_code


def create_sms_log(args, sent_to):
    log = SMS_Log.objects.create(message=args['message'].decode(
        "utf-8"), sent_to=', '.join(sent_to))
    log.save()
