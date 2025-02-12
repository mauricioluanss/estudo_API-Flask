from app import app
from app.models.mongo import mongo
from flask import request, jsonify, render_template

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    data = request.form
    
    if not data:
        return jsonify({"error": "nenhum dado enviado."}), 400
    
    usuario = {
        "nome": data.get("nome"),
        "email": data.get("email"),
        "senha": data.get("senha")
        }
    try:
        result = mongo.db.users.insert_one(usuario)
        return jsonify({"message": "Usuário cadastrado!", "id": str(result.inserted_id)})
    except Exception as e:
        return jsonify({"error": f"Erro ao inserir usuário: {e}"}), 500