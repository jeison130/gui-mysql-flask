from src.models.user import UsersModel
from src.dto.user import UserDTO

class UserController():
    def list(self):
        usersModel = UsersModel()
        data = usersModel.lists()

        return data

    def create(self, user: UserDTO):
        usersModel = UsersModel()
        usersModel.create(user) 

        #Enviamos un correo