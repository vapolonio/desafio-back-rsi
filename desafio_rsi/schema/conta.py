conta = {
    'id': {
        'type': 'string',
        'minlength': 1,
        'required': True,
        'unique': True
    },
    'saldo': {
        'type': 'float',
    },
    'cpf': {
        'type': 'string',
        'data_relation': {
            'resource': 'usuario',
            'field': 'cpf',
            'embeddable': False
        },
        'unique': True,
        'required': True,
    }
}
