#this is a scratchpad to be launched independently of the app itself to test app calls and string work
'''
import urllib2
import json

request = urllib2.Request('https://api.dropbox.com/1/team/get_info')

request.add_header('Content-type', 'application/json')

request.add_header('Authorization','Bearer Roti84bECDUAAAAAAAACOhZz6DJtV9g4kWxk2_6gc7GOObK7nrmz1c4ITHm1wlOE')

body = str('{}')

request.add_data(body)

response = urllib2.urlopen(request)

data = response.read()

#use the JSON libraries to use the data a bit more neatly...
converted_data = json.loads(data)

#print it out, to prove, that we are smashing the API :)
print "Team name is: " + converted_data["name"]
print "The total number of licences is: " + str(converted_data["num_licensed_users"])
print "The total number of licences in use: " + str(converted_data["num_provisioned_users"])
print "The Dropbox team ID is: " + converted_data["team_id"]
'''
import urllib2
import json

def teamStorage():
	dfbpwd = "Bearer 5POVRTzm3ZAAAAAAAAABTtqrqiasvx-jR2W5LyEFfKRBmi41ORoyT_rxgq5-761M"
	request = urllib2.Request('https://api.dropbox.com/1/team/reports/get_storage')
	request.add_header('Content-type', 'application/json')
	request.add_header('Authorization', dfbpwd)
	body = str('{}')
	request.add_data(body)
	response = urllib2.urlopen(request)
	data = response.read()
	converted_data = json.loads(data)
	return converted_data

data = teamStorage()
sharedStorage = data.get("shared_usage")
for entry in sharedStorage:
	print entry #["profile"]["email"]

