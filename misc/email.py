import smtplib
from smtplib import SMTPException
from email.mime.text import MIMEText
def send_email(subject, to_address, data):
    from_address = "saketh9977.test@gmail.com"
    from_address_password = "north_korea"
    try:
        body = MIMEText(data)
        body['From'] = from_address
        body['To'] = to_address[0]
        body['Subject'] = subject
        mail_server = smtplib.SMTP('smtp.gmail.com:587')
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.login(from_address, from_address_password)
        mail_server.sendmail(from_address, to_address, body.as_string())
        mail_server.quit()
        print("Mail has been sent!!!")
    except SMTPException:
        print("SMTP Exception!!!")
        
send_email("Testing...", ["saketh9977@gmail.com"], "All is well")