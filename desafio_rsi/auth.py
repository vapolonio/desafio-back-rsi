from flask import current_app as app
from eve.auth import BasicAuth
from pymongo.collection import Collection


def criptografrar_senha(usuarios):
    for usuario in usuarios:
        usuario['password'] = usuario['password'].upper()
    return usuarios


class Autenticacao(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        clientes: Collection = app.data.driver.db['clientes']
        res = clientes.find_one({
            'cpf': username,
            'password': password,
        })
        return res is not None


autenticacao_exemple = Autenticacao()
