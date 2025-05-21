import smtplib
from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

app_pass = os.getenv('GOOGLE_APP_PASS')

email = "mridularaul72@gmail.com"
receiver_email = input("Receiver Email : ")

subject = "html message"
html_message = '''
    <html>
        <body>
            <h3>Hello</h3>
            <hr>
            <p>This is a message that I wrote using Python and HTML.</p>
        </body>
    </html>
'''

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(html_message, 'html'))

try:
    print('Sending email...')
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, app_pass)
    server.sendmail(email, receiver_email, msg.as_string())
    print("Email sent successfully!")
    server.quit()
except Exception as e:
    print("Error:", e)