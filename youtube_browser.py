#Requires: apiclient; oauth2client; httplib2
import httplib2
import os
import sys
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

#point to authentication info file
CLIENT_SECRETS_FILE = "client_secrets.json"

#youtube configuration
SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

MISSING_CLIENT_SECRET_MESSAGE = "Secret file not found"

#Authenticate with youtube and get object to perform actions through
def get_authenticated_service(args):
	
	#Retrieve stored credentials object
	storage = Storage("%s-oauth2.json" % sys.argv[0])
	credentials = storage.get()
	
	#If necessary, flow credentials from secrets file
	if credentials is None or credentials.invalid:
		flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
			scope=SCOPE, message=MISSING_CLIENT_SECRET_MESSAGE)
		credentials = run_flow(flow, storage, args)
		
	return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, http=credentials.authorize(http2lib.Http()))
	
def saveChannelList(id):
	f = open("channel_list.csv", "w")
	f.write(id)
	f.close()
	
def fetchSubscriptions(youtube, )
{

	
	
if __name__ == "__main__":
	print "Enter channel ID:"
	newname = raw_input()
	argparser.add_argument("--channel-id", help="ID of the channel to subscribe to.",
		default=newname)
	args = argparser.parse_args()
	saveChannelList(newname)
	
youtube = get_authenticated_service(args)
try:
	channel_title = 