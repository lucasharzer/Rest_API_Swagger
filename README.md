# Descrição

Rest API de usuários com python, flask, flask-sqlalchemy (banco de dados), flask-marshmallow, marshmallow-sqlalchemy e flask-restx aplicada no Swagger. Nessa API, um usuario tem os seguintes dados (Id, Nome, Idade, Email e Senha) e é possível: Listar todos os usuários ( GET ), listar usuários por id ( GET{id} ), deletar usuários por id ( DELETE{id} ), atualizar usuários por id ( PUT{id} ) e cadastrar usuários inserindo todos os dados ( POST ).

Obs: o arquivo requirements.txt possui todos os pacotes e suas respectivas versões usadas para executar a API.

# Comandos no terminal para configuração

- Instalar os pacotes: 

```bash
python setup.py develop
```
- Configurar o app:

Para Windows:
```bash
set FLASK_APP=app.py 
```
```bash
set FLASK_DEBUG=True
```
Para Linux:
```bash
export FLASK_APP=app.py
```
```bash
export FLASK_DEBUG=True
```

- Criar o banco de dados:
 ```bash
 python
 ```
  ```bash
 from app import banco
 ```
  ```bash
 banco.create_all()
 ```
  ```bash
 exit()
 ```



