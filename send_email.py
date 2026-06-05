# send_email.py

from email.mime.text import MIMEText
import base64


# -----------------------------------
# SEND EMAIL FUNCTION
# -----------------------------------

def send_email(service, to, subject, body):

    try:

        # CREATE EMAIL MESSAGE
        message = MIMEText(body, "plain")

        message["to"] = to
        message["subject"] = subject

        # ENCODE MESSAGE
        raw_message = base64.urlsafe_b64encode(
            message.as_bytes()
        ).decode()

        message_body = {
            "raw": raw_message
        }

        # SEND EMAIL
        sent_message = service.users().messages().send(
            userId="me",
            body=message_body
        ).execute()

        print("\n✅ Email sent successfully!")
        print(f"Message ID: {sent_message['id']}")

        return sent_message

    except Exception as e:

        print("\n❌ Failed to send email.")
        print(f"Error: {str(e)}")

        return None


# -----------------------------------
# HTML EMAIL SUPPORT
# -----------------------------------

def send_html_email(service, to, subject, html_body):

    try:

        message = MIMEText(html_body, "html")

        message["to"] = to
        message["subject"] = subject

        raw_message = base64.urlsafe_b64encode(
            message.as_bytes()
        ).decode()

        message_body = {
            "raw": raw_message
        }

        sent_message = service.users().messages().send(
            userId="me",
            body=message_body
        ).execute()

        print("\n✅ HTML Email sent successfully!")
        print(f"Message ID: {sent_message['id']}")

        return sent_message

    except Exception as e:

        print("\n❌ Failed to send HTML email.")
        print(f"Error: {str(e)}")

        return None