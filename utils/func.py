from account.models import Account
from django.contrib.auth.models import User

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

#val = URLValidator(verify_exists=False)
val = URLValidator()

def url_slasher(url):
    if url[-1] != '/':
        url += '/'
    if url[0] == '/':
        url = url[1:]

    return url

def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc

    reference : http://stackoverflow.com/questions/1551382/user-friendly-time-format-in-python
    """
    from datetime import datetime
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff / 60) + " minutes ago"
        if second_diff < 86400:
            return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"

def isURL(url):
    try:
        val(url)
        return True
    except ValidationError, e:
        return False

def normalize(url):
    if not url.startswith(("http://", "https://")):
        return "http://" + url
    return url

def get_account_from_uid(uid):
    try:
        account = Account.objects.get(id=uid)

        return account
    except:
        msg = "Error: Failed to find '%s' account " % uid
        raise Exception(msg)

def get_account_from_user(user):
    try:
        return Account.objects.get(user=user)
    except:
        return None

def get_account_from_usernme(username):
    try:
        user = Account.objects.get(username=username)
        return Account.objects.get(user=user)
    except:
        return None

