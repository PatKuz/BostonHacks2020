
import yaml
from twilio.rest import Client

class Messager: 

    def __init__(self):
        self.creds = yaml.safe_load(open("creds.yaml", "r"))
        self.account_sid = self.creds['ACCOUNT_SID']
        self.auth_token = self.creds['AUTH_TOKEN']
        self.client = Client(self.account_sid, self.auth_token)
        self.toNum = self.creds['to']
        self.fromNum = self.creds['from']

    def send_message(self, messageToSend, toNum=None):
        if toNum == None:
            self.toNum = self.toNum
        else:
            self.toNum = toNum
        message = self.client.messages.create(
                        body=messageToSend,
                        from_=self.fromNum,
                        to=self.toNum
                    )
        
        print(message.sid)
