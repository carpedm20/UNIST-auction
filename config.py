FACEBOOK_APP_ID='387661514698415'
FACEBOOK_API_SECRET='0e4e65e38f54da96e9421284e5b89b04'

FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'display': 'popup'}
FACEBOOK_EXTRA_DATA = [('username', 'username'), ('name','name')]

#########################
# SOCIAL AUTH settings
#########################

LOGIN_URL = '/account/sign_in/'
LOGOUT_URL = '/account/sign_out/'
LOGIN_REDIRECT_URL = '/account/close/'

SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook', 'twitter', 'google-oauth2', 'naver')

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

SOCIAL_AUTH_USER_MODEL = 'account.Account'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
SOCIAL_AUTH_UID_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'social_auth.backends.pipeline.user.update_user_details',

    'account.pipelines.get_user_avatar',
)
