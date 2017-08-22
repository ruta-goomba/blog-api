MONGO_HOST = 'ec2-52-17-83-242.eu-west-1.compute.amazonaws.com'
MONGO_PORT = 10047
RESOURCE_METHODS = ['GET', 'POST']
X_DOMAINS = '*'
X_HEADERS = ['User-Agent', 'Host', 'Content-Type']
DOMAIN = {
  'user': {
    'schema': {
      'firstname': {
        'type': 'string'
      },
      'lastname': {
        'type': 'string'
      },
      'username': {
          'type': 'string',
           'unique': True
      },
      'password': {
          'type': 'string'
      },
      'phone': {
          'type': 'string'
      }
        }
    },
  'additional_lookup': {
    'url': 'regex("[\w]+")',
    'field': 'username',
  }

}