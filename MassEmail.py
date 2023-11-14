import csv
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import os
# Email content
sender_email = 'eliteyouthrealestate@gmail.com'
password = 'Subzero29@'
subject = 'Interest In Selling Your House'
message = '''
Dear Homeowner,

I hope this message finds you well. My name is Hakop Zarikyan, and I am attempting to by houses in the area for remodelling. I came across your address and felt compelled to reach out to see if you might be considering selling your home.

As someone who appreciates the unique character of our community, I am particularly interested in homes that contribute to its charm and vibrancy. If you have ever thought about selling, or are open to discussing the possibility, it would be great if I could talk to you about that.

I understand that selling a home is a significant decision, and I assure you that my intention is to make the process as smooth and beneficial for you as possible, should you decide to explore this option.

If this is something you are interested in or would like to discuss further, please feel free to reach out to me at eliteyouthrealestate@gmail.com or 8184528375. I am flexible and can arrange a conversation at a time that is most convenient for you.

Thank you for considering. I wish you all the best and hope you have a wonderful day.

Warm regards,
Hakop Zarikyan
8184528375
eliteyouthrealestate@gmail.com

'''

path = Path(__file__).parent / "recipients.csv"

recipients = []
with path.open() as file:
    reader = csv.reader(file)
    
    for row in reader:
        recipients.append(row[0])  # Assuming the email addresses are in the first column


# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))


# Authenticate with OAuth2 flow

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, 'snus nabo roko ennt')  # Use your app password here

    # Send the email to each recipient
    for r in recipients:
        server.sendmail(sender_email, r, msg.as_string())