from flask import current_app as app
from eve.auth import BasicAuth
from pymongo.collection import Collection
import bcrypt


def criptografrar_senha(usuarios):
    for usuario in usuarios:
        salt = bcrypt.gensalt()
        usuario['senha'] = bcrypt.hashpw(usuario['senha'].encode('utf-8'),
                                         salt)
    return usuarios


def esconder_senhas(usuarios):
    for usuario in usuarios:
        del usuario['senha']
    return usuarios


class Autenticacao(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        clientes: Collection = app.data.driver.db['usuario']
        res = clientes.find_one({'cpf': username})
        return res is not None and bcrypt.checkpw(password.encode('utf-8'),
                                                  res['senha'])


autenticacao_exemple = Autenticacao()
