from flask import request , render_template
from . import core

@core.route('/')
def index_page():
    return render_template('core/index.html')