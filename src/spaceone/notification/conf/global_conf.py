DATABASE_AUTO_CREATE_INDEX = True
DATABASES = {
    'default': {
        # 'db': '',
        # 'host': '',
        # 'port': 0,
        # 'username': '',
        # 'password': '',
        # 'ssl': False,
        # 'ssl_ca_certs': ''
    }
}

CACHES = {
    'default': {},
    'local': {
        'backend': 'spaceone.core.cache.local_cache.LocalCache',
        'max_size': 128,
        'ttl': 300
    }
}

IDENTITY = {
    'token': {
        'token_timeout': 1800,
        'refresh_timeout': 3600,
        'refresh_ttl': 12,
        'refresh_once': True
    }
}

HANDLERS = {
    # 'authentication': [{
    #     'backend': 'spaceone.core.handler.authentication_handler.AuthenticationGRPCHandler',
    #     'uri': 'grpc://localhost:50051/v1/Domain/get_public_key'
    # }],
    # 'authorization': [{
    #     'backend': 'spaceone.core.handler.authorization_handler.AuthorizationGRPCHandler',
    #     'uri': 'grpc://localhost:50051/v1/Authorization/verify'
    # }],
    # 'mutation': [{
    #     'backend': 'spaceone.core.handler.mutation_handler.SpaceONEMutationHandler'
    # }],
    # 'event': []
}

CONNECTORS = {
    'PluginServiceConnector': {
    },
    'SpaceConnector': {
        'backend': 'spaceone.core.connector.space_connector.SpaceConnector',
        'endpoints': {
            'identity': 'grpc://identity:50051',
            'plugin': 'grpc://plugin:50051',
            'repository': 'grpc://repository:50051',
            'secret': 'grpc://secret:50051',
            'config': 'grpc://config:50051',
        }
    },
}

ENDPOINTS = [
    # {
    #     'service': 'notification',
    #     'name': 'Identity Service',
    #     'endpoint': 'grpc://<endpoint>>:<port>/v1'
    # },
]

INSTALLED_PROTOCOL_PLUGINS = [
    # {
    #     'name': 'Email',
    #     'plugin_info': {
    #         'plugin_id': 'plugin-email-noti-protocol',
    #         'version': '1.0',
    #         'options': {},
    #         'secret_data': {}
    #         'schema': 'email_smtp'
    #     },
    #     'tags':{
    #         'description': 'email'
    #     }
    # }
]

DEFAULT_QUOTA = {
    # ex: 'PROTOCOL_PLUGIN_ID': {'month': QUOTA, 'day': QUOTA},
    # 'plugin-slack-noti-protocol': {'month': -1, 'day': -1},
    # 'plugin-jira-noti-protocol': {'month': -1, 'day': -1},
    # 'plugin-mzc-sms-noti-protocol': {'month': 3000, 'day': 100},
    # 'plugin-mzc-voicecall-noti-protocol': {'month': 3000, 'day': 100},
    # 'plugin-telegram-noti-protocol': {'month': -1, 'day': -1},
    # 'plugin-email-noti-protocol': {'month': 30000, 'day': 1000},
}