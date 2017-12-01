from flask import redirect, render_template, sessions, url_for

from .models import User, Role
from .forms import LoginForm
from .. import db
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


