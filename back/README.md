Start with the Makefile

## Expose django project to be accessed by Vue:

### Setting up CORS
- `pip install django-cors-headers`
- used to determine the whitelist that can be accessed
- on the settings.py file:
    . on the INSTALLED _APPS -> add 'corsheaders'
    . on MIDDLEWARE add:
        '''
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        '''
    . then setup CORS after MIDDLEWARE:
        '''
        CORS_ORIGIN_ALLOW_ALL = False
        CORS_ORIGIN_WHITELIST = (
            'http://localhost:4200',
        )
        '''
- Now django accept calls from 'http://localhost:4200'

