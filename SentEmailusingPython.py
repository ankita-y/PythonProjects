import ssl,smtplib

port = 465
email = input("Enter your email: ")
password = input("Enter your password: ")

recipient = input("Enter recipient email address: ")
subject = input("Enter Subject of the mail: ")
text = input("Type your email here: ")

message = "Subject: {}\n\n{}".format(subject,text)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as servers:
    servers.login(email,password)
    servers.sendmail(email,recipient,message)

"""
"""