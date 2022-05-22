from enum import unique
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin, LoginManager
from LittleUSA import db, login
#UserMixin class provides the implementation of this properties. Its the reason you can call for example is_authenticated to check if login credentials provide is correct or not instead of having to write a method to do that yourself.
#UserMixin: on the other hand, it is used to call properties(is_authenticated,...)






class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id= db.Column(db.Integer, primary_key= True)
    email = db.Column(db.String(80), unique= True)
    username= db.Column(db.String(100), unique= True)
    password_hash= db.Column(db.String())

    def set_password(self, password): #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        self.password_hash= generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



#this function is used to link Flask_login and database
@login.user_loader
def load_user(id):
    return UserModel.query.get(int(id))
    
