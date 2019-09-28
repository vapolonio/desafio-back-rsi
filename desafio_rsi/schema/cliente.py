cliente = {
    "bairro": {
        "type": "string"
    },
    "cidade": {
        "type": "string"
    },
    "complemento": {
        "type": "string"
    },
    "cpf": {
        "type": "string",
        "unique": True,
        "required": True
        # TODO regex
    },
    "dataNascimento": {
        "type": "date",
        "required": True
    },
    "email": {
        "type": "string"
    },
    "estado": {
        "type": "string",
        "minlength": 2,
        "maxlength": 2
    },
    "nome": {
        "type": "string",
        "required": True
    },
    "numero": {
        "type": "integer"
    },
    "pais": {
        "type": "string"
    },
    "password": {
        "type": "string",
        "required": True,
        "minlength": 6
    },
    "rua": {
        "type": "string"
    },
    "sobrenome": {
        "type": "string",
        "required": True
    }
}
