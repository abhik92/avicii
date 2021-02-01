import smtplib
from email.message import EmailMessage


class VideoReplay:
    def __init__(self, email, filename):
        self.email = email
        self.filename = filename

    def send_email(self):
        with open(self.filename) as fp:
             # Create a text/plain message
            msg = EmailMessage()
            msg.set_content(fp.read())

        msg['Subject'] = f'You can decide to buy or sell now'
        msg['From'] = self.email
        msg['To'] = self.email


        # TODO connect to the gmail server
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()
