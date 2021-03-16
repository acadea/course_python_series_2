import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mailer:

    def __init__(self):

        # to send email via SSL (for security purposes)
        context = ssl.create_default_context()

        # use this if using outlook
        # self._server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        # self._server.starttls()

        # I'm using gmail, so defining host and port here
        self._server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=context)
        # self._server = smtplib.SMTP(host='smtp.gmail.com', port=465)

        # login credential to send to smtp server
        self._server.login(user="user@gmail.com", password="password")

    def send(self, to: str, subject: str, body: str):
        """
        Send email
        :param to: email address of recipient 
        :param subject: subject of email
        :param body: email body
        """
        # creating message
        # MIME is sort of like data type. For example, jpeg, mp4, png are 3 different MIME type
        # multipart MIME means message can consist of a variety of MIME
        message = MIMEMultipart()

        # we want the body to be plain text MIME
        message.attach(MIMEText(body, 'plain'))

        # Setting the subject of message.
        # Read the python doc for more information about the email module
        # https://docs.python.org/3/library/email.examples.html
        message['Subject'] = subject

        self._server.sendmail(
            from_addr='droopboxy03@gmail.com',
            to_addrs=[to],  # you can specify an array of to addresses here if you want
            msg=message.as_string())


if __name__ == "__main__":
    subject = input("Subject: ")
    message = input("Message: ")
    to = input("To who? email: ")
    mailer = Mailer()
    mailer.send(to, subject, message)
    print("Email sent....")
