cliente = {
    'nome': {
        'type': 'string',
        'minlength': 10,
        'required': True,
    },
    'cpf': {
        'type': 'string',
        'unique': True,
        'required': True,
        'regex': r'^\d{11}$',
    },
    'cep': {
        'type': 'string',
        'regex': r'^\d{8}$',
    },
    'numEndereco': {
        'type': 'integer',
        'min': 0,
        'max': 99999,
    },
    'telefone': {
        'type': 'string',
        'regex': r'^\d{10,11}$',
    },
    'email': {
        'type': 'string',
        'regex': r'^\S+@\S+\.\S+$'
    },
}
