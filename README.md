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
 
 # Rodando a aplicação
  ```bash
 flask run
 ```
 # Resultado no Swagger

 http://localhost:5000
 
 <span>
     <img src="https://user-images.githubusercontent.com/85804895/135732868-01f77528-a4fe-4cd1-83d2-72771979046d.png", width=900>
</span>

 <span>
     <img src="https://user-images.githubusercontent.com/85804895/135732892-574f7f34-6d41-45c2-a2a6-46e45ec6d41b.png", width=900>
</span>

 <span>
     <img src="https://user-images.githubusercontent.com/85804895/135732906-08dac296-0b5b-4331-b44c-e3cb089ba9ed.png", width=900>
</span>

 <span>
     <img src="https://user-images.githubusercontent.com/85804895/135732914-440dd629-b97f-4eb1-8c42-216140cf8258.png", width=900>
</span>


