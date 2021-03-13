from src import app
from src.controllers.user import UserController
from flask import make_response, jsonify, request
from src.dto.user import UserDTO

userController = UserController()

@app.route('/users', methods=['GET'])
def usuariosDos():
    users = userController.list()
    return make_response(jsonify(users), 200)

@app.route('/users', methods=['POST'])
def createUser():
    name = request.json['name']
    lastname = request.json['lastname']
    phone = request.json['phone']
    email = request.json['email']
    password = request.json['password']

    user = UserDTO(name, lastname, phone, email, password)

    userController.create(user)

    return make_response('', 201)