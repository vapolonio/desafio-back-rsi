from eve import Eve
from eve.auth import BasicAuth
from pymongo.collection import Collection
from cerberus import Validator
from flask import Flask, request, jsonify, request
from .auth import Autenticacao, criptografrar_senha, esconder_senhas

app = Eve(__name__, auth=Autenticacao)

# pylint: disable=no-member
app.on_insert_usuario += criptografrar_senha

app = Eve(__name__, auth=Autenticacao)


@app.route('/conta/adicionarSaldo', methods=['POST'])
def addValue():
    print(request.data)
    conta = request.json['conta']
    valor = request.json['valor']
    colecao_conta_origem: Collection = app.data.driver.db['conta']
    colecao_conta_origem.update_one({'id': conta}, {'$inc': {'saldo': valor}})
    return jsonify({"message": "success"})


@app.route('/transferir', methods=['POST'])
def transferValue():
    accOrigin = request.json['accOrigin']
    accDest = request.json['accDest']
    value = request.json['value']
    colecao_conta_origem: Collection = app.data.driver.db['conta']
    contaOrigem = colecao_conta_origem.find_one({
        'id': accOrigin,
    })
    colecao_conta_destino: Collection = app.data.driver.db['conta']
    contaDestino = colecao_conta_destino.find_one({
        'id': accDest,
    })
    if contaOrigem is not None and contaDestino is not None and value is not None:
        if contaOrigem["saldo"] < value:
            return jsonify({"message": "Saldo insuficiente"})
        colecao_conta_origem.update_one(
            {"_id": contaOrigem['_id']},
            {"$set": {
                'saldo': contaOrigem['saldo'] - value
            }},
            upsert=False)
        colecao_conta_destino.update_one(
            {"_id": accDest['_id']},
            {"$set": {
                'saldo': contaOrigem['saldo'] + value
            }},
            upsert=False)
        return jsonify({"message": "success"})
    return jsonify({"message": "erro"})


application = app
