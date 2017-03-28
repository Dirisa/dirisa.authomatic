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
        link=False,
        location=False,
        name=True,
        picture=False,
        username=True
    )
    
    @staticmethod
    def _x_user_parser(user, data):
        user.username = data.get('name')
        #user.picture = data.get('avatar_url')
        #user.link = data.get('html_url')
        return user
    
    @classmethod
    def _x_credentials_parser(cls, credentials, data):
        import pdb; pdb.set_trace()
        if data.get('token_type') == 'bearer':
            credentials.token_type = cls.BEARER
        return credentials


# The provider type ID is generated from this list's indexes!
# Always append new providers at the end so that ids of existing providers don't change!
PROVIDER_ID_MAP.append(SAEON)

