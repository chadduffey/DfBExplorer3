from flask import render_template, session, redirect, url_for, current_app
from flask.ext.login import login_user, logout_user, login_required, current_user
from .. import db
from ..models import User
from ..email import send_email
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated():
    	return render_template('main/main.html', user=current_user)
    return render_template('index.html')