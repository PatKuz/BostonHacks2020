import yaml
from twilio.rest import Client
from pyngrok import ngrok
import http.server
import socketserver
import threading


PORT = 8000

def start_server():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

def send_message(messageToSend, toNum=None, image=None):
    creds = yaml.safe_load(open("creds.yaml", "r"))
    account_sid = creds['ACCOUNT_SID']
    auth_token = creds['AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    toNum = creds['to']
    fromNum = creds['from']

    if toNum == None:
        toNum = toNum
    else:
        toNum = toNum
    if image:
        target = threading.Thread(target=start_server)
        target.start()
        tunnels = ngrok.get_tunnels()
        for tunnel in tunnels:
            ngrok.disconnect(tunnel.public_url)
        url = ngrok.connect(PORT)
        imageUrl = url.public_url + '//' + image
        print("ImageURL")
        print(imageUrl)
        message = client.messages.create(
                        body=messageToSend,
                        from_=fromNum,
                        to=toNum,
                        media_url=[imageUrl]
                    )
    else:
        message = client.messages.create(
            body=messageToSend,
            from_=fromNum,
            to=toNum,
        )
    print(message)

    
