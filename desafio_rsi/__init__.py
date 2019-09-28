from eve import Eve
from eve.auth import BasicAuth
from pymongo.collection import Collection
from cerberus import Validator
from flask import Flask, request, jsonify
from .auth import Autenticacao, criptografrar_senha

app = Eve(__name__, auth=Autenticacao)

# pylint: disable=no-member
app.on_insert_clientes += criptografrar_senha

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

@app.route('/transferir', methods=['POST'])
def transferValue(accOrigin, accDest, value):
    colecao_conta_origem: Collection = app.data.driver.db['conta']
    contaOrigem = colecao_conta_origem.find_one({
            'id': accOrigin,
    })
    colecao_conta_destino: Collection = app.data.driver.db['conta']
    contaDestino = colecao_conta_destino.find_one({
            'id': accDest,
    })
    if contaOrigem is not None and contaDestino is not None value is not None:
        if contaOrigem["saldo"] < value:
           return jsonify({"message": "Saldo insuficiente"})
        colecao_conta_origem.update_one(
            {"_id": contaOrigem['_id']},
            {"$set": {
                'saldo': contaOrigem['saldo'] - value
        }}, upsert=False)
        colecao_conta_destino.update_one(
            {"_id": accDest['_id']},
            {"$set": {
            'saldo': contaOrigem['saldo'] + value
        }}, upsert=False)
        return jsonify({"message": "success"})

application = app
