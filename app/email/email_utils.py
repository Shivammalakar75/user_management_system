# app/email/email_utils

# import smtplib
# from email.message import EmailMessage

# def send_welcome_email(to_email: str, username: str):
#     msg = EmailMessage()
#     msg["Subject"] = "Welcome!"
#     msg["From"] = "your_email@gmail.com"
#     msg["To"] = to_email
#     msg.set_content(f"Hello {username}, Welcome!")

#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login("your_email@gmail.com", "app_password")
#         server.send_message(msg)