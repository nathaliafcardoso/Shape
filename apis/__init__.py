from flask import Flask
from config import RunConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from apis.models.equipment import equipment
from apis.models.model import db
from apis.models.vessel import vessel

app = Flask(__name__)
app.config.from_object(RunConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

router = app.register_blueprint()
router = app.register_blueprint(url_prefix='/vessel')
router = app.register_blueprint(url_prefix='/equipment')