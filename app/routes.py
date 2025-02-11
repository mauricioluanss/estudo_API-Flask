from app import app
from app.models import mongo
from flask import request, jsonify
from flask_pymongo import PyMongo

@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    data = request.json
    if not data:
        return jsonify({"error": "nenhum dado enviado."}), 400
    
    usuario = {
        "nome": data.get("nome"),
        "email": data.get("email"),
        "senha": data.get("senha")
        }
    result = mongo.db.usuarios.insert_one(usuario)
    return jsonify({"message": "Usuário cadastrado!", "id": str(result.inserted_id)})
