MONGO_HOST = 'localhost'
MONGO_PORT = 27017
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PUT']
DOMAIN = {
  'api/comment': {
    'schema': {
      'username': {
          'type': 'string'
      },
      'comment': {
          'type': 'string'
      },
      'topic': {
          'type': 'string'
      },
      'created': {
          'type': 'string'
      },
      'show': {
          'type': 'boolean'
      }
    }
  }
}