from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Mail configuration
app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # Here, we use Gmail, but you can use any other.
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'email@adress.com' # Your account's login.
app.config['MAIL_PASSWORD'] = 'password' # Your account's password.
app.config['MAIL_DEFAULT_SENDER'] = ("Sender's name", 'sender@adress.com')
app.config['MAIL_MAX_EMAILS'] = 1 # The max amount of emails to send in a single connection.
app.config['MAIL_SUPRESS_SEND'] = False # If this is set to True, the email will not be actually sent. Used for testing.
app.config['MAIL_ASCII_ATTACHMENTS'] = True

mail = Mail(app)

def sendEmail(email):
    msg = Message("Title", recipients=[email]) # The list should contain the recipients' emails.
    msg.body = "This is the message's body."
    msg.html = "<p> This is for message's HTML, for <b>pretty</b> emails. </p>"

    '''This last part is meant for sending emails with attachments. I put two examples: pdf and png.
        This way, the archives should be put in the same folder as your app. If you wish, you could pass the archives
        paths as parameters, and put them at app.open_resource.'''
    with app.open_resource("archive.pdf") as pdf_attachment:
        msg.attach("archive.pdf", "application/pdf", pdf_attachment.read())
    
    with app.open_resource("image.png") as png_attachment:
        msg.attach("image.png", "image/png", png_attachment.read())

    mail.send(msg) # Finally, the email is sent.