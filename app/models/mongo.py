from flask_pymongo import PyMongo
from app import app
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv('MONGO_URI')

if not mongo_uri:
    print("Erro: Variável de ambiente 'mongo_uri' não encontrada.")
else:
    print("Conectando ao MongoDB com o URI:", mongo_uri)

app.config['MONGO_URI'] = mongo_uri

mongo = PyMongo(app)

try:
    mongo.cx.admin.command('ping')
    print("Conexão com MongoDB estabelecida com sucesso.")
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")

