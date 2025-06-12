from api.api_user import getUserById
#когда будет допилина игра используем @login_required

class UserLogin():
    async def fromBD(self, user_id):
        self.__user = await getUserById(user_id)
        return self
    
    def create(self, user):
        self.__user = user
        return self
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymouse(self):
        return False
    
    def get_id(self):
        return str(self.__user.id)