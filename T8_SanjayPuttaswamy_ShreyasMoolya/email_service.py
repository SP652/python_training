# email_service.py
import smtplib
from email.mime.text import MIMEText

def send_email_confirmation(name, email, flight):
    msg = MIMEText(f"""Dear {name},

Your flight has been booked successfully!

Flight Details:
- Flight ID: {flight.flight_id}
- Source: {flight.source}
- Destination: {flight.destination}
- Departure Time: {flight.departure_time}
- Arrival Time: {flight.arrival_time}
- Fare: ${flight.fare}

Thank you for booking with us!
""")
    msg['Subject'] = 'Flight Booking Confirmation'
    msg['From'] = 'sanjaypsgowda@gmail.com'  # Replace with your email
    msg['To'] = email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login('sanjaypsgowda@gmail.com', 'uooh rybg osxo saik')  # Replace with your credentials
            server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def send_cancellation_email(name, email, flight):
    msg = MIMEText(f"""Dear {name},

We regret to inform you that your flight booking has been cancelled.

Flight Details:
- Flight ID: {flight.flight_id}
- Source: {flight.source}
- Destination: {flight.destination}
- Departure Time: {flight.departure_time}
- Arrival Time: {flight.arrival_time}

We apologize for any inconvenience this may cause.

Thank you for understanding.
""")
    msg['Subject'] = 'Flight Booking Cancellation'
    msg['From'] = 'sanjaypsgowda@gmail.com'  # Replace with your email
    msg['To'] = email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login('sanjaypsgowda@gmail.com', 'uooh rybg osxo saik')  # Replace with your credentials
            server.send_message(msg)
        print("Cancellation email sent successfully.")
    except Exception as e:
        print(f"Error sending cancellation email: {e}")
