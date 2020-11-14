# Download the helper library from https://www.twilio.com/docs/python/install

import yaml

creds = yaml.safe_load(open("creds.yaml", "r"))

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure



account_sid = creds['ACCOUNT_SID']
auth_token = creds['AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = "This is a test"
toNum = creds['to']
fromNum = creds['from'] 

message = client.messages \
                .create(
                     body=message,
                     from_=fromNum,
                     to=toNum
                 )

print(message.sid)
