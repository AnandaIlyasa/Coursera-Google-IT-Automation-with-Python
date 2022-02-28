from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

    
def send_email(message, smtp_server):
    try:
        mail_server = smtplib.SMTP(smtp_server)
        mail_server.send_message(message)
        mail_server.quit()
    except Exception as e:
        print("failed to send email : {}".format(e))

def generate_email(sender, recipient, subject, body, smtp_server, attachment=""):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    if attachment != "":
        attachment_filename = os.path.basename(attachment)
        mime, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime.split('/')

        with open(attachment, 'rb') as ap:
            message.add_attachment(
                ap.read(),
                maintype=mime_type,
                subtype=mime_subtype,
                filename=attachment_filename
            )
            ap.close()

    send_email(message=message, smtp_server=smtp_server)