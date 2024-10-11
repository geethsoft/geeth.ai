from flask import Flask

# Initialize the app
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('src.config.app_config.Config')

# Register blueprints or import routes here
#from src.controllers.api.chats_controller import chats
#app.register_blueprint(chats, url_prefix='/chats')

################# Ollama models #################
from ai.llms.llama_bot.__init__ import models
app.register_blueprint(models, url_prefix = '/models')

########## employee CRUD operations ###############
from .schema.main import db_crud
app.register_blueprint(db_crud, url_prefix = '/empdb')