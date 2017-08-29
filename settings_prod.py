MONGO_HOST = 'ec2-34-251-123-3.eu-west-1.compute.amazonaws.com'
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