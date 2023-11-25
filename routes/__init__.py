from flask import Blueprint

routes = Blueprint('routes', __name__)
from .login import *
from .home import *
from .dashboard import *
from .booking import *
