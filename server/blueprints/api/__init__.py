from flask import Blueprint

from .routes import example


bp = Blueprint('api', __name__)

bp.add_url_rule('/api/v1/', view_func=example)
# bp.add_url_rule('/api/v1/login', view_func=login, methods=['GET', 'POST'])

def init_app(app):
    app.register_blueprint(bp)
