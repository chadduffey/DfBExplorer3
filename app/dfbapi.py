from flask.ext.login import current_user

import urllib2
import json

def basicInfo():
	dfbpwd = current_user.dfbpassword
	request = urllib2.Request('https://api.dropbox.com/1/team/get_info')
	request.add_header('Content-type', 'application/json')
	request.add_header('Authorization', dfbpwd)
	body = str('{}')
	request.add_data(body)
	response = urllib2.urlopen(request)
	data = response.read()
	converted_data = json.loads(data)
	return converted_data

def teamMembers():
	dfbpwd = current_user.dfbpassword
	request = urllib2.Request('https://api.dropbox.com/1/team/members/list')
	request.add_header('Content-type', 'application/json')
	request.add_header('Authorization', dfbpwd)
	body = str('{}')
	request.add_data(body)
	response = urllib2.urlopen(request)
	data = response.read()
	converted_data = json.loads(data)
	return converted_data