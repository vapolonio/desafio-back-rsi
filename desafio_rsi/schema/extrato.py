extrato = {
    'conta': {
        'type': 'string',
        'data_relation': {
            'resource': 'conta',
            'field': 'cpf',
            'embeddable': False
        },
        'required': True,
    },
    "data": {
        "type": "datetime",
        'required': True
    },
    'valor': {
        'type': 'float',
        'required': True,
    },
    'descricao': {
        'type': 'string',

    }
}
