from flask import Flask
from api.database import db
from flask_migrate import Migrate
from werkzeug.exceptions import NotFound,MethodNotAllowed
from api.models.models import Video
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from api.config.config import config_dict



def create_app(config=config_dict['dev']):
    app=Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    migrate=Migrate(app,db)
    # engine = create_engine('sqlite:///db.sqlite')
    # session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    # jwt=JWTManager(app) 

    # api = Api(app)

    # # api.add_namespace()
    # api.add_namespace(auth_namespace, path='/auth')
    # api.add_namespace(contact_namespace, path='/contacts')
    # api.add_namespace(messages_namespace,path='/messages')

    
    # @api.errorhandler(NotFound)
    # def not_found(error):
    #     return{"error": "Not Found"},404
    
    # @api.errorhandler(MethodNotAllowed)
    # def method_not_allowed(error):
    #     return {"error": "Method Not Allowed"},405

    @app.shell_context_processor
    def make_shell_context():
        return{
            'db':db,
            'Video': Video
        }

    return app 