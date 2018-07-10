# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
app = Flask(__name__)

SECRET_KEY = 'a secret key'
app.config.from_object(__name__)

sid = "XXX"
auth = "XXX"
client = Client(sid, auth)

#avaliable cryptos
ava = ["bitcoin", "ethereum"]
@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    counter = session.get('counter', 0)
    counter += 1
    session['counter'] = counter
    ##hardcode...
    if counter == 1:
        
        resp = MessagingResponse()
        resp.message("Thank you for using crypto collect, what type of crypto currency would you like to buy?")
        return str(resp)
    
    
    if counter == 2:

        resp = MessagingResponse()
        resp.message("How much of Bitcoin would you like")
        return str(resp)
    
    if counter == 3:
        resp = MessagingResponse()
        resp.message("you order is 3 Bitcoin, Total price is USD 19701, enter CON to confirm")
        return str(resp)
    
    if counter == 4:
        resp = MessagingResponse()
        resp.message("You order has been recieved")
        counter = 0
        session['counter'] = counter
        return str(resp)


if __name__ == "__main__":
    app.run(debug=True)