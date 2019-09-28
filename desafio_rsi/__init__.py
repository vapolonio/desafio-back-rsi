from eve import Eve
from .auth import Autenticacao, criptografrar_senha

app = Eve(__name__, auth=Autenticacao)

# pylint: disable=no-member
app.on_insert_clientes += criptografrar_senha

application = app
