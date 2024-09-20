import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Alert:
    def __init__(self, message):
        self.message = message

    def save_to_db(self):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alerts (message, timestamp) VALUES (?, datetime('now'))", (self.message,))
        conn.commit()
        conn.close()

    @staticmethod
    def display_alerts():
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alerts")
        alerts = cursor.fetchall()
        conn.close()

        print("\n--- Alert Details ---")
        for alert in alerts:
            print(f"ID: {alert[0]}, Message: {alert[1]}, Timestamp: {alert[2]}")
        print("------------------------")

    def send_email_alert(self, to_email):
        from_email = "KingfisherAirlines@gmail.com"  # Replace with your email
        password = "YouSUCK_SBI"         # Replace with your email password

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = "Airline Management System Alert"
        body = f"Alert Message: {self.message}"
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:  # For Gmail
                server.starttls()
                server.login(from_email, password)
                server.send_message(msg)
            print("Email alert sent successfully.")
        except Exception as e:
            print(f"Failed to send email alert: {e}")
