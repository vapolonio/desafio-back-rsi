from eve import Eve
from eve.auth import BasicAuth
from pymongo.collection import Collection

app = None


class Autenticacao(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        clientes: Collection = app.data.driver.db['accounts']
        res = clientes.find_one({
            'cpf': username,
            'password': password,
        })
        return res is not None


app = Eve(__name__, auth=Autenticacao)
application = app
