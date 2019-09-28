from desafio_rsi.schema.cliente import cliente
from os import environ

DOMAIN = {'clientes': {'item_title': 'cliente', 'schema': cliente}}

MONGO_DBNAME = 'bytecycle'
MONGO_URI = environ.get('MONGODB_URI', 'mongodb://localhost')

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
HATEOAS=False
OPTIMIZE_PAGINATION_FOR_SPEED=True
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
X_DOMAINS = '*'
X_HEADERS = ['Accepts', 'Expects', 'Content-Type']
