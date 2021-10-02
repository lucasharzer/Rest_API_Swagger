from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restx import Api, fields, Resource


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

banco = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api()

# inicialização
api.init_app(app)


# dados do usuario
class Usuario(banco.Model):
    id = banco.Column(banco.Integer, primary_key=True, autoincrement=True)
    nome = banco.Column(banco.String)
    idade = banco.Column(banco.Integer)
    email = banco.Column(banco.String)
    senha = banco.Column(banco.String)


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nome', 'idade', 'email', 'senha')

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

# informações no Swagger: Padrão

# Models
modelo = api.model('usuario', {
    'nome': fields.String('Digite seu Nome'),
    'idade': fields.Integer('Digite sua idade'),
    'email': fields.String('Digite seu Email'),
    'senha': fields.String('Digite sua Senha')
})


# GET
@api.route('/get')
class Listar_Todos(Resource):
    def get(self):
        return jsonify(usuarios_schema.dump(Usuario.query.all()))


# GET{id}
@api.route('/get/<int:id>')
class Listar_por_Id(Resource):
    def get(self, id):
        return jsonify(usuario_schema.dump(Usuario.query.get(id)))


# POST
@api.route('/post')
class Cadastrar(Resource):
    @api.expect(modelo)
    def post(self):
        usuario = Usuario(nome = request.json['nome'], 
                        idade = request.json['idade'], 
                        email = request.json['email'], 
                        senha = request.json['senha']
                    ) 

        banco.session.add(usuario)
        banco.session.commit()

        return {
            'message': 'Usuário criado com sucesso!'
        }


# PUT{id}
@api.route('/put/<int:id>')
class Atualizar(Resource):
    @api.expect(modelo)
    def put(self, id):
        usuario = Usuario.query.get(id)
        usuario.nome = request.json['nome']
        usuario.idade = request.json['idade']
        usuario.email = request.json['email']
        usuario.senha = request.json['senha']

        banco.session.commit()

        return {
            'message': 'Usuario atualizado com sucesso!'
        }


# DELETE{id}
@api.route('/delete/<int:id>')
class Deletar(Resource):
    def delete(self, id):
        usuario = Usuario.query.get(id)

        banco.session.delete(usuario)
        banco.session.commit()

        return {
            'message': 'usuario deletado com sucesso!'
        }
