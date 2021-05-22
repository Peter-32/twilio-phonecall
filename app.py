# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        # record=True,
                        # method='GET',
                        # status_callback='https://www.myapp.com/events',
                        # status_callback_event=['initiated', 'answered'],
                        # status_callback_method='POST',                        
                        # url='http://demo.twilio.com/docs/voice.xml',
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',                        
                        to='+16612364816',
                        from_='+18653510175'
                    )

print(call.sid)