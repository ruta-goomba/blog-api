MONGO_HOST = 'localhost'
MONGO_PORT = 27017
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PUT']
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