MONGO_HOST = 'localhost'
MONGO_PORT = 10047
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PUT']
X_DOMAINS = 'ruta-sakalauskaite.me'
X_HEADERS = ['User', 'Content-Type']
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