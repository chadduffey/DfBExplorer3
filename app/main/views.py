from flask import render_template, session, redirect, url_for, current_app
from flask.ext.login import login_user, logout_user, login_required, current_user
from .. import db
from ..models import User
from ..email import send_email
from . import main
from ..dfbapi import basicInfo, teamMembers

import urllib2
import json

@main.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated():
    	try:
			#Dropbox Basics
			converted_data = basicInfo()
			totalLicences=converted_data["num_licensed_users"]
			licencesInUse = converted_data["num_provisioned_users"]
			remainingLicences = totalLicences - licencesInUse
			#team members
			allTeamMembers = teamMembers()
			allTeamMembers = allTeamMembers.get("members")
			return render_template('main/main.html', 
									user=current_user, 
									dbTeamName=converted_data["name"], 
									remainingLicences=remainingLicences,
	    							totalLicences=converted_data["num_licensed_users"], 
	    							licencesInUse=converted_data["num_provisioned_users"], 
	    							teamId=converted_data["team_id"],
	    							teamMembers = allTeamMembers)
        except:
			return render_template('main/main.html', 
									user="Authentication Error", 
									dbTeamName="Error", 
									remainingLicences=5,
	    							totalLicences=10, 
	    							licencesInUse=5, 
	    							teamId=123,
	    							teamMembers="Error")
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