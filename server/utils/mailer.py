import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

sender_email = os.getenv("EMAIL_USER")
sender_password = os.getenv("EMAIL_PASS")

def send_email(to_email, product_name, current_price, product_url):
    subject = f"🔔 Price Drop Alert: {product_name}"
    body = f"""
    <h3>Good news!</h3>
    <p>The price for <b>{product_name}</b> dropped to ₹{current_price}.</p>
    <p><a href="{product_url}">Check it on Flipkart</a></p>
    <br>
    <p>– TrendTicker 📦</p>
    """ 
    
    
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")