from eve import Eve
from eve.auth import BasicAuth
from pymongo.collection import Collection
from cerberus import Validator
from flask import Flask, request, jsonify

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

@app.route('/conta/adicionarSaldo', methods=['POST'])
def addValue():
    print(request.data)
    return jsonify({"message": "success"})

application = app
