from flask import render_template
from flask import Blueprint


templates_bp = Blueprint('templates', __name__,
                         template_folder='./templates',
                         static_folder='./server/static')

@templates_bp.route('/')
def index_template():
    return render_template('index.jinja2')

@templates_bp.route('/api')
def api_template():
    return '# Doc to API'
    
