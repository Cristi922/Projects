from twilio.rest import Client

TWILIO_SID = "AC41e68ae177f91dce73a28a3756dde6b9"
TWILIO_AUTH_TOKEN = '8536ac1cace0a5a0e5b9a1b196fb5ea2'
TWILIO_VIRTUAL_NUMBER = "+14432513193"
TWILIO_VERIFIED_NUMBER = "+4012345"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
