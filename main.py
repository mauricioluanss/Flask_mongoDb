from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv() #carrega meu arquivo .env

app = Flask(__name__)

#--------Realiza conexão com o Mongo-----------------------------------------
mongo_uri = os.getenv('mongo_uri') #minha uri de conexão está no .env

app.config['MONGO_URI'] = mongo_uri

mongo = PyMongo(app)
db = mongo.db

#--------Rota POST para inputar dados no banco-------------------------------
@app.route('/input', methods=['POST'])
def input_db():
    dados = {
        "usuario": request.json.get('usuario'),
        "email": request.json.get('email')
    }
    if not all (dados.values()):
        return jsonify({'erro': 'é necessário preencher todas as chaves.'}), 400
    
    mongo.db['users'].insert_one(dados)
    return jsonify({'mensagem': 'dados enviados com sucesso', 'dados': dados}), 200


#--------Rota GET para consulta dos dados inputados no banco-----------------
@app.route('/', methods=['GET'])
def get():
    dados = mongo.db['users'].find()
    return jsonify(dados)

#executa meu server
if (__name__) == '__main__':
    app.run(debug=True)