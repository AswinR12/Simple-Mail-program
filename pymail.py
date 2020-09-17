from email.message import EmailMessage
import mimetypes
import smtplib

msg = EmailMessage()
sender = input("From:")
receiver = input("To:(for multiple receivers, separate each by comma): ")
receiver = receiver.split(",")  
msg['From'] = sender
msg['To'] = receiver
body = input("Enter body:")
msg.set_content(body)

x = input("Add attachment?(y/n): ")
x.lower()
while x != "n":
    if x != "y":
        print("Please enter y or n.")
        x = lower(input("Add attachment?(y/n):"))
        x.lower()
        continue
    attachment = input("Enter attachment path: ")
    mime_type,_ = mimetypes.guess_type(attachment)
    print(mime_type)
    mtype,msubtype = mime_type.split('/',1)
    with open(attachment,'rb') as ap:
        msg.add_attachment(ap.read(), maintype = mtype, subtype = msubtype, filename = attachment)
    x = input("Add attachment?(y/n): ")
    x.lower()

#connect to mail server
#search SMTP settings for the service (gmail) if conn. is being refused.
#May have to change some settings and permissions based on which service is being used.
mail_server = smtplib.SMTP_SSL("smtp.gmail.com")

#mail_server.set_debuglevel(1) #to see the behind the scenes SMTP messages.

#To make sure that the password isn't visible.
#not necessary 
import getpass
mail_pass = getpass.getpass("Password? ") #enter sender's password


#login to server
mail_server.login(sender,mail_pass)
mail_server.send_message(msg)

mail_server.quit()
