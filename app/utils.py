#algorithms for password

from passlib.context import CryptContext


#setting password as bcryt
pwd_context= CryptContext(schemes=['bcrypt'],deprecated='auto')


#Hashing function:
def hash(password:str):
    return pwd_context.hash(password)


#function to copmare the hash password