from email.message import EmailMessage
import ssl
import smtplib

email_sender='hasnain.ashraf796@gmail.com'
email_password='sxqj tgei reqg ftxx'

#visit temp.mail.org to get a temporary email 
email_receiver='mahej43105@searpen.com'

subject='Email 2'

body="This is second mail. \nI am practicing this mini project again to improve. How am I doin?"

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())