import os
from eve import Eve

if os.environ.get("ENV"):
  settings = 'settings_dev.py'
else:
  settings = 'settings_prod.py'

app = Eve(settings=settings)

if __name__ == '__main__':
    app.run()