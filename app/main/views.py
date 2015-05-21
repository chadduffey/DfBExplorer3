from flask import render_template, session, redirect, url_for, current_app
from flask.ext.login import login_user, logout_user, login_required, current_user
from .. import db
from ..models import User
from ..email import send_email
from . import main

import urllib2
import json

@main.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated():
		#Dropbox Basics
		request = urllib2.Request('https://api.dropbox.com/1/team/get_info')
		request.add_header('Content-type', 'application/json')
		request.add_header('Authorization','Bearer Roti84bECDUAAAAAAAACOhZz6DJtV9g4kWxk2_6gc7GOObK7nrmz1c4ITHm1wlOE')
		body = str('{}')
		request.add_data(body)
		response = urllib2.urlopen(request)
		data = response.read()
		converted_data = json.loads(data)
		dbTeamName = converted_data["name"]
		totalLicences = converted_data["num_licensed_users"]
		licencesInUse = converted_data["num_provisioned_users"]
		teamId = converted_data["team_id"]
		remainingLicences = totalLicences - licencesInUse
		return render_template('main/main.html', user=current_user, dbTeamName=dbTeamName, remainingLicences=remainingLicences,
    							totalLicences=totalLicences, licencesInUse=licencesInUse, teamId=teamId)
    return render_template('index.html')

@main.route('/sharing_activity', methods=['GET', 'POST'])
def sharing_activity():
	return render_template('main/sharing_activity.html')


@main.route('/team_storage', methods=['GET', 'POST'])
def team_storage():
	return render_template('main/team_storage.html')


@main.route('/group_membership', methods=['GET', 'POST'])
def group_membership():
	return render_template('main/group_membership.html')


@main.route('/team_management', methods=['GET', 'POST'])
def team_management():
	return render_template('main/team_management.html')


@main.route('/devices', methods=['GET', 'POST'])
def devices():
	return render_template('main/devices.html')


@main.route('/team_audit', methods=['GET', 'POST'])
def team_audit():
	return render_template('main/team_audit.html')