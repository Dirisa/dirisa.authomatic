# -*- coding: utf-8 -*-
"""
|oauth2| Providers
-------------------

Providers which implement the |oauth2|_ protocol.

.. autosummary::
    
    SAEON
    
"""

import logging
from authomatic.providers.oauth2 import OAuth2, PROVIDER_ID_MAP
import authomatic.core as core


class SAEON(OAuth2):
    """
    SAEON |oauth2| provider.
    
    * Dashboard: https://github.com/settings/developers
    * Docs: http://developer.github.com/v3/#authentication
    * API reference: http://developer.github.com/v3/
    
    .. note::
        
        GitHub API `documentation <http://developer.github.com/v3/#user-agent-required>`_ sais:
        
            all API requests MUST include a valid ``User-Agent`` header.
        
        You can apply a default ``User-Agent`` header for all API calls in the config like this:
        
        .. code-block:: python
            :emphasize-lines: 6
        
            CONFIG = {
                'github': {
                    'class_': oauth2.GitHub,
                    'consumer_key': '#####',
                    'consumer_secret': '#####',
                    'access_headers': {'User-Agent': 'Awesome-Octocat-App'},
                }
            }

    Supported :class:`.User` properties:

    * email
    * id
    * link
    * location
    * name
    * picture
    * username

    Unsupported :class:`.User` properties:

    * birth_date
    * city
    * country
    * first_name
    * gender
    * last_name
    * locale
    * nickname
    * phone
    * postal_code
    * timezone
    
    """
    
    user_authorization_url = "https://identity.saeon.nimbusservices.co.za/oauth2/connect/authorize"
    access_token_url = "https://identity.saeon.nimbusservices.co.za/oauth2/connect/token"
    user_info_url = "https://identity.saeon.nimbusservices.co.za/oauth2/connect/userinfo"
    
    same_origin = False

    supported_user_attributes = core.SupportedUserAttributes(
        email=True,
        id=True,
        username=True,
        name=True,
        link=True,
        location=False,
        picture=False,
    )
    
    @staticmethod
    def _x_user_parser(user, data):
        logging.debug('_x_user_parser: data = %s' % data)
        user.username = data.get('preferred_username')
        user.email = data.get('email')
        user.id = data.get('email')
        user.fullname = "%s %s" % (
                data.get('given_name'), data.get('family_name'))
        user.name = user.fullname
        user.link = 'http://www.saeon.ac.za' #data.get('html_url')
        #user.picture = data.get('avatar_url')
        logging.debug('_x_user_parser: user = %s' % user)
        return user
    
    @classmethod
    def _x_credentials_parser(cls, credentials, data):
        if data.get('token_type') == 'Bearer':
            credentials.token_type = cls.BEARER
        return credentials


# The provider type ID is generated from this list's indexes!
# Always append new providers at the end so that ids of existing providers don't change!
PROVIDER_ID_MAP.append(SAEON)
"""
{
"github": {
"id": 1,
"display": {
"title": "Github",
"cssclasses": {
"button": "plone-btn plone-btn-default",
"icon": "glypicon glyphicon-github"
},
"as_form": false
},
"propertymap": {
"email": "email",
"link": "home_page",
"location": "location",
"name": "fullname"
},
"class_": "authomatic.providers.oauth2.GitHub",
"consumer_key": "72e58bdabddb908dd7ee",
"consumer_secret": "038a5045919ee6b845ea06dc9d55054386331333",
"access_headers": {
"User-Agent": "Plone (pas.plugins.authomatic)"
}
},
"yahoo": {
"id": 2,
"display": {
"title": "Yahoo",
"cssclasses": {
"button": "plone-btn plone-btn-default",
"icon": "glypicon glyphicon-github"
},
"as_form": false
},
"propertymap": {
"email": "email",
"link": "home_page",
"location": "location",
"name": "fullname"
},
"class_": "authomatic.providers.oauth1.Yahoo",
"consumer_key": "dj0yJmk9M3phT1hNTHNMeXQ1JmQ9WVdrOU5uRTRZa2hITjJzbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD04Zg--",
"consumer_secret": "269ae9ee48e7973717f71a016e4c36dd5f8ed9cc",
"access_headers": {
"User-Agent": "Plone (pas.plugins.authomatic)"
}
},
"saeon": {
"id": 10,
"display": {
"title": "SAEON",
"cssclasses": {
"button": "plone-btn plone-btn-default",
"icon": "glypicon glyphicon-github"
},
"as_form": false
},
"propertymap": {
"email": "email",
"link": "home_page",
"location": "location",
"name": "fullname"
},
"class_": "dirisa.authomatic.saeon.SAEON",
"consumer_key": "WebTide Authorization Code",
"consumer_secret": "WebT1de",
"access_headers": {
"User-Agent": "Plone (pas.plugins.authomatic)"
},
"scope": ["openid profile email"]
}
}
"""
