from flask import render_template, session, redirect, url_for, current_app
from flask.ext.login import login_user, logout_user, login_required, current_user
from .. import db
from ..models import User
from ..email import send_email
from . import main
from ..dfbapi import (basicInfo, teamMembers, teamStorage, 
						deleteMember, addMember, listGroups, getDeviceEvents)

from forms import AddUserForm

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
	if current_user.is_authenticated():
		try:
			data = teamStorage()
			total_usage = data.get("total_usage")
			member_storage_map = data.get("member_storage_map")
			shared_usage = data.get("shared_usage")
			unshared_usage = data.get("unshared_usage")
			shared_folders = data.get("shared_folders")
			start_date = data.get("start_date")
			return render_template('main/team_storage.html', 
											total_usage=total_usage,
											member_storage_map=member_storage_map,
											shared_usage=shared_usage,
											unshared_usage=unshared_usage,
											shared_folders=shared_folders,
											start_date=start_date)
		except:
			return render_template('main/team_storage.html', 
											total_usage=[1,200,3000],
											member_storage_map=1,
											shared_usage=1,
											unshared_usage=1,
											shared_folders=1,
											start_date=1/1/1)


@main.route('/group_membership', methods=['GET', 'POST'])
def group_membership():
    if current_user.is_authenticated():
	    try:
			data = listGroups()
			groups = data.get("groups")
			return render_template('main/group_membership.html', groups=groups)
	    except:
		    return render_template('main/group_membership.html')


@main.route('/team_management', methods=['GET', 'POST'])
def team_management():
	form = AddUserForm()
	allTeamMembers = teamMembers()
	allTeamMembers = allTeamMembers.get("members")
	if form.validate_on_submit():
		member_email = form.member_email.data
		member_given_name = form.member_given_name.data
		member_surname = form.member_surname.data
		member_external_id = form.member_external_id.data
		newguy = addMember(member_email, member_given_name, member_surname, member_external_id)
		return redirect('/')
	return render_template('main/team_management.html', form=form, teamMembers=allTeamMembers)

@main.route('/delete_user/<member_id>', methods=['GET', 'POST'])
def delete_user(member_id):
	ok = deleteMember(member_id)
	return redirect('/team_management')


@main.route('/devices', methods=['GET', 'POST'])
def devices():
	allEvents = getDeviceEvents()
	deviceEvents = allEvents.get("events")
	return render_template('main/devices.html', deviceEvents=deviceEvents)


@main.route('/team_audit', methods=['GET', 'POST'])
def team_audit():
	return render_template('main/team_audit.html')