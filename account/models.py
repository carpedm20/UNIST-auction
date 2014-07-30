from django.db import models
from django.contrib.auth.models import AbstractBaseUser

import hashlib

class AccountManager(models.Manager):
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        user = self.model(username=username,
                          email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)

class Account(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True, db_index=True)
    email = models.EmailField(max_length=256, null=True, blank=True, db_index=True)

    ko_name = models.CharField(max_length=100, null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    profile_image_url = models.URLField(null=True, blank=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'

    def __unicode__(self):
        return self.username

    def is_authenticated(self):
        return True

    @property
    def korean_name(self):
        if self.ko_name:
            return self.ko_name

        facebook = self.social_auth.filter(provider='facebook')

        if facebook:
            import requests, json

            facebook = facebook[0]

            url = "https://api.facebook.com/method/fql.query?query=select+name+from+profile+where+id=%s&access_token=%s&locale=ko_KR&format=json"\
                % (facebook.extra_data['id'],
                   facebook.extra_data['access_token'])

            self.ko_name = json.loads(requests.get(url).text)[0]['name']
            self.save()
        else:
            return None

    @property
    def get_username(self):
        if self.naver:
            return self.username.split("@")[0]

        social_auths = self.social_auth.filter(provider='twitter')

        if len(social_auths) != 0:
            return self.social_auth.get(provider='twitter').extra_data['screen_name'] 
        else:
            return self.username

        social_auths = self.social_auth.filter(provider='google-oauth2')

        if len(social_auths) != 0:
            return self.social_auth.get(provider='google-oauth2').extra_data['id'] 
        else:
            return self.username
    @property
    def get_profile_url(self):
        social_auths = self.social_auth.filter(provider='twitter')

        if len(social_auths) != 0:
            return "https://twitter.com/%s" % self.get_username 

        social_auths = self.social_auth.filter(provider='facebook')

        if len(social_auths) != 0:
            return "https://facebook.com/%s" % self.get_username

        else:
            return None

    @property
    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.username).hexdigest()

    @property
    def gravatar_small_url(self):
        return "http://www.gravatar.com/avatar/%s?s=20" % hashlib.md5(self.username).hexdigest()

    @property
    def gravatar_middle_url(self):
        return "http://www.gravatar.com/avatar/%s?s=33" % hashlib.md5(self.username).hexdigest()

    @property
    def account_id(self):
        return self.username.split('@')[0]

