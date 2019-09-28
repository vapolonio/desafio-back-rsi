from desafio_rsi.schema.cliente import cliente
from desafio_rsi.schema.conta import conta
from os import environ

DOMAIN = {
    'clientes': {
        'item_title': 'cliente', 
        'schema': cliente
    },
    'conta': {
        'item_title': 'conta', 
        'schema': conta
    }
}

MONGO_DBNAME = 'bytecycle'
MONGO_URI = environ.get('MONGODB_URI', 'mongodb://localhost')

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
HATEOAS=False
OPTIMIZE_PAGINATION_FOR_SPEED=True
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
X_DOMAINS = '*'
X_HEADERS = ['Accepts', 'Expects', 'Content-Type']
