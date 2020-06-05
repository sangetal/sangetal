import logging

from flask import Flask

from sangetal.config import SangetalConfig
from sangetal.extensions import db, migrate, jwt, api


logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    
    config = SangetalConfig()
    app.config.from_mapping(config)
    
    register_extensions(app)
    
    return app
    
def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    api.init_app(app)
