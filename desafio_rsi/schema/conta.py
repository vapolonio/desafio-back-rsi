conta = {
    'nome': {
        'type': 'string',
        'minlength': 10,
        'required': True,
    },
    'valor': {
        'type': 'float',
    },
    'cpf': {
        'type': 'objectId',
        'data_relation': {
            'resource': 'clientes',
            'field': 'cpf',
            'embeddable': False
        },
        'required': True,
    }
}
