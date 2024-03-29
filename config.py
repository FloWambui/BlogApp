import os

class Config:
    '''
    General configuration parent class
    '''
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://flora:wambui@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'



    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True



class ProdConfig(Config):
    # uri = os.getenv('DATABASE_URL')
    # if uri and uri.startswith('postgres://'):
    #     uri = uri.replace('postgres://', 'postgresql://', 1)    
    # SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://flora:wambui@localhost/blog'
DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://flora:wambui@localhost/blog_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://flora:wambui@localhost/blog'
    

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}