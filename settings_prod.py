MONGO_HOST = 'localhost'
MONGO_PORT = 10047
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PUT']
X_DOMAINS = '*'
X_HEADERS = ['User', 'Content-Type']
DOMAIN = {
  'api/comment': {
    'schema': {
      'username': {
          'type': 'string',
           'unique': True
      },
      'comment': {
          'type': 'string'
      },
      'id': {
          'type': 'integer',
          'unique': True
      },
      'date': {
          'type': 'datetime'
      },
        }
    },
  'additional_lookup': {
    'url': 'regex("[\w]+")',
    'field': 'username',
  }

}