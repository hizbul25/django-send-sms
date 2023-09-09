## django-universal-sms

Send SMS from Django application using any SMS service provider just writing a single line of code.

## Features

- Support all standard SMS service provider
- SMS configuration from django admin panel
- There is SMS Log listing page
- You can also test SMS sending from admin panel
- Enough test coverage

## Installation

### pip

```bash
pip install django-universal-sms
```

## Install apps in `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    '...',
    'send_sms',
]
```

### migration

```bash
python manage.py migrate
```

## Configuration

- Go to admin panel by login with you admin credentials
- Find out **SMS Settings** menu under **SEND SMS** and click on it.
- There you'll see couple of fields to fill it up using SMS service provider credentials.
  ![Here is the example](/media/SMS_Settings.png).
- Carfefully compelete this part and save it.

## Usage

Whenever you need to send SMS just use following code:

```bash
from send_sms.views import send_sms

send_sms(['mobile_number'], 'Your Message')
```

For each successful sending SMS you can see the log from **SMS Log** under under **SEND SMS** menu.

## Support

Feel free to ask for the support over the email hizbul.ku[at]gmail.com.
