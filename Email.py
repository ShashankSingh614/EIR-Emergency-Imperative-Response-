import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.message import EmailMessage
from email import encoders
import os.path



def send_email(email_recipient,
               email_subject,
               email_message,
               attachment_location = 'Video_Output.mp4'):

    email_sender = 'eirprimeconsole@outlook.com'

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_message+'\n', 'plain'))

    with open('GPS_Location.txt','r') as f:
        file_data = f.read()
        msg.attach(MIMEText(file_data, 'plain'))

    if attachment_location != '':
        filename = os.path.basename(attachment_location)
        attachment = open(attachment_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= %s" % filename)
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.ehlo()
        server.starttls()
        server.login("eirprimeconsole@outlook.com", 'code_open')
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        print('email sent')
        server.quit()
    except:
        print("SMPT server connection error")
    return True

send_email('eirprimeconsole@gmail.com',
           'SOS EMERGENCY',
           'there has been a accident help reqired \nI am attaching you the GPS location and a 15 seconds Video file.\nResopnd ASAP!' 
           )