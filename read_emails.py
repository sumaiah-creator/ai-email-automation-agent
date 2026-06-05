# read_emails.py

import base64
from gmail_auth import authenticate_gmail


# -----------------------------------
# EXTRACT EMAIL BODY
# -----------------------------------

def extract_email_body(payload):

    body = ""

    # SIMPLE EMAIL
    if 'parts' not in payload:

        data = payload['body'].get('data')

        if data:
            body = base64.urlsafe_b64decode(
                data
            ).decode('utf-8')

    # MULTIPART EMAIL
    else:

        for part in payload['parts']:

            mime_type = part.get('mimeType')

            data = part['body'].get('data')

            if mime_type == 'text/plain' and data:

                body = base64.urlsafe_b64decode(
                    data
                ).decode('utf-8')

                break

    return body


# -----------------------------------
# READ EMAILS FUNCTION
# -----------------------------------

def read_emails(max_results=5):

    service = authenticate_gmail()

    email_data = []

    try:

        results = service.users().messages().list(
            userId='me',
            maxResults=max_results
        ).execute()

        messages = results.get('messages', [])

        if not messages:
            print("No messages found.")
            return []

        for msg in messages:

            txt = service.users().messages().get(
                userId='me',
                id=msg['id']
            ).execute()

            payload = txt['payload']
            headers = payload['headers']

            subject = ""
            sender = ""

            # EXTRACT SUBJECT & SENDER
            for header in headers:

                name = header['name']

                if name == 'Subject':
                    subject = header['value']

                if name == 'From':
                    sender = header['value']

            # EXTRACT BODY
            body = extract_email_body(payload)

            email_info = {
                "id": msg['id'],
                "sender": sender,
                "subject": subject,
                "body": body
            }

            email_data.append(email_info)

        return email_data

    except Exception as e:

        print(f"Error reading emails: {str(e)}")

        return []


# -----------------------------------
# TESTING
# -----------------------------------

if __name__ == "__main__":

    emails = read_emails()

    for email in emails:

        print("\n========================")
        print("FROM:", email['sender'])
        print("SUBJECT:", email['subject'])
        print("BODY:")
        print(email['body'][:500])