from flask.ext.login import current_user

import urllib2
import json

#temp fix :
dfbpwd = "Bearer 5POVRTzm3ZAAAAAAAAAEgqjNbM7EsI57hc9BCnPBGr_BFT__N5DIuwlwZS3zeiUW"

def basicInfo():
	#dfbpwd = current_user.dfbpassword
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
	#dfbpwd = current_user.dfbpassword
	request = urllib2.Request('https://api.dropbox.com/1/team/members/list')
	request.add_header('Content-type', 'application/json')
	request.add_header('Authorization', dfbpwd)
	body = str('{}')
	request.add_data(body)
	response = urllib2.urlopen(request)
	data = response.read()
	converted_data = json.loads(data)
	return converted_data

def teamStorage():
	#dfbpwd = current_user.dfbpassword
	request = urllib2.Request('https://api.dropbox.com/1/team/reports/get_storage')
	request.add_header('Content-type', 'application/json')
	request.add_header('Authorization', dfbpwd)
	body = str('{}')
	request.add_data(body)
	response = urllib2.urlopen(request)
	data = response.read()
	converted_data = json.loads(data)
	return converted_data

def deleteMember(member_id):
	try:
		#dfbpwd = current_user.dfbpassword
		request = urllib2.Request('https://api.dropbox.com/1/team/members/remove')
		request.add_header('Content-type', 'application/json')
		request.add_header('Authorization', dfbpwd)
		body = str('{"member_id": "' + member_id + '"}')
		request.add_data(body)
		response = urllib2.urlopen(request)
		data = response.read()
		converted_data = json.loads(data)
		return converted_data
	except:
		return "failed"

def addMember(member_email, member_given_name, member_surname, member_external_id):
	try:
		#dfbpwd = current_user.dfbpassword
		request = urllib2.Request('https://api.dropbox.com/1/team/members/add')
		request.add_header('Content-type', 'application/json')
		request.add_header('Authorization', dfbpwd)
		body = str('{"member_email": "' + member_email + '", "member_given_name": "' + member_given_name + '", "member_surname": "' + member_surname + '", "member_external_id": "' + member_external_id + '"}')
		request.add_data(body)
		response = urllib2.urlopen(request)
		data = response.read()
		converted_data = json.loads(data)
		return converted_data
	except:
		return "failed"

def listGroups():
	#dfbpwd = current_user.dfbpassword
	request = urllib2.Request('https://api.dropbox.com/1/team/groups/list')
	request.add_header('Content-type', 'application/json')
	request.add_header('Authorization', dfbpwd)
	body = str('{}')
	request.add_data(body)
	response = urllib2.urlopen(request)
	data = response.read()
	converted_data = json.loads(data)
	return converted_data

def listMembersOfGroup(group_id):
	#dfbpwd = current_user.dfbpassword
	request = urllib2.Request('https://api.dropbox.com/1/team/groups/get_info')
	request.add_header('Content-type', 'application/json')
	request.add_header('Authorization', dfbpwd)
	body = str('{"group_ids": ["' + group_id + '"] }') #g:e4f395453ce6dd900000000000000180
	request.add_data(body)
	response = urllib2.urlopen(request)
	data = response.read()
	converted_data = json.loads(data)
	return converted_data	

def getDeviceEvents():
	#temp fix. 
	dfbpwd = "Bearer 5POVRTzm3ZAAAAAAAAABvn6tAxMvpd_gUX2ANaasiQeuzjaOC2P_N2SkhZf3c1En"
	#dfbpwd = current_user.dfbpassword
	request = urllib2.Request('https://api.dropbox.com/1/team/log/get_events')
	request.add_header('Content-type', 'application/json')
	request.add_header('Authorization', dfbpwd)
	body = str('{"category": "devices"}')
	request.add_data(body)
	response = urllib2.urlopen(request)
	data = response.read()
	converted_data = json.loads(data)
	return converted_data

def getAllEvents():
	#dfbpwd = current_user.dfbpassword
	
	#temp fix. 
	dfbpwd = "Bearer 5POVRTzm3ZAAAAAAAAABvn6tAxMvpd_gUX2ANaasiQeuzjaOC2P_N2SkhZf3c1En"
	request = urllib2.Request('https://api.dropbox.com/1/team/log/get_events')
	request.add_header('Content-type', 'application/json')
	request.add_header('Authorization', dfbpwd)
	body = str('{}')
	request.add_data(body)
	response = urllib2.urlopen(request)
	data = response.read()
	converted_data = json.loads(data)
	return converted_data