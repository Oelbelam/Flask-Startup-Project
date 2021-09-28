class Config :
    TESTING = True
    DEBUG = True
    ENV = 'devlopement'

class Developement(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/newApp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret"  # Change this!
    CORS_HEADERS = 'Content-Type'