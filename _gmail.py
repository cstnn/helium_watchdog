import smtplib, ssl
from datetime import datetime

#### EMAIL 
def send_email(subject, email_text, email_to):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    PORT = 465  # For SSL
    HOST = "smtp.gmail.com"
    FROM = "costin.nadolu@gmail.com"  # Enter your address
    PASSWORD = "dgubzcqbhxxasxtv"

    # TO = ['costin.nadolu@gmail.com', 'razvan.ciocoiu19@yahoo.com'] #'andreea_nadolu@yahoo.com',
    TO = email_to
    SUBJECT = subject
        
    EMAIL_text = email_text
    context = ssl.create_default_context()

    MESSAGE = 'Subject: {}\n\n{}'.format(SUBJECT, EMAIL_text)


    with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
        server.login(FROM, PASSWORD)
        server.sendmail(FROM, TO, MESSAGE)

if __name__ == "__main__":
    send_email("subject", "email_text", "costin.nadolu@gmail.com")
