from desafio_rsi.schema.usuario import usuario
from desafio_rsi.schema.conta import conta
from desafio_rsi.schema.extrato import extrato
from os import environ

DOMAIN = {
    'usuario': {
        'item_title': 'usuario', 
        'schema': usuario,
        'public_item_methods': ['POST']
    },
    'conta': {
        'item_title': 'conta', 
        'schema': conta
    },
    'extrato': {
        'item_title': 'extrato',
        'schema': extrato,
        'resource_methods': ['GET'],
        'item_methods': ['GET'],
    }
}

MONGO_DBNAME = 'bytecycle'
MONGO_URI = environ.get('MONGODB_URI', 'mongodb://localhost')

DATE_FORMAT = '%Y-%m-%d'
HATEOAS=False
OPTIMIZE_PAGINATION_FOR_SPEED=True
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
X_DOMAINS = '*'
X_HEADERS = ['Accepts', 'Expects', 'Content-Type']
