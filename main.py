from app.routes import app
from app.routes import cadastrar_usuario

if __name__ == '__main__':
    cadastrar_usuario()
    app.run(debug=True) #funcao para iniciar servidor web flask. Fonte: routes.py e __init__.py