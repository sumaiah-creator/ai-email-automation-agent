# main.py

from read_emails import read_emails

from ai_agent import (
    classify_email,
    generate_reply,
    summarize_email
)

from gmail_auth import authenticate_gmail
from send_email import send_email


# -----------------------------------
# MAIN EMAIL AGENT WORKFLOW
# -----------------------------------

def run_email_agent():

    print("\n======================================")
    print("   AI EMAIL AUTOMATION AGENT")
    print("======================================\n")

    # AUTHENTICATE GMAIL
    service = authenticate_gmail()

    # READ EMAILS
    emails = read_emails(max_results=5)

    if not emails:

        print("No emails found.")
        return

    # PROCESS EMAILS
    for index, email in enumerate(emails, start=1):

        print("\n======================================")
        print(f" EMAIL #{index}")
        print("======================================\n")

        sender = email["sender"]
        subject = email["subject"]
        body = email["body"]

        # -----------------------------------
        # DISPLAY EMAIL DETAILS
        # -----------------------------------

        print(f"FROM    : {sender}")
        print(f"SUBJECT : {subject}")

        print("\n--------------------------------------")
        print(" EMAIL BODY ")
        print("--------------------------------------")

        print(body[:1000])

        # -----------------------------------
        # CLASSIFY EMAIL
        # -----------------------------------

        print("\n--------------------------------------")
        print(" CLASSIFYING EMAIL...")
        print("--------------------------------------")

        category = classify_email(body)

        print(f"Category : {category}")

        # -----------------------------------
        # SUMMARIZE EMAIL
        # -----------------------------------

        print("\n--------------------------------------")
        print(" EMAIL SUMMARY ")
        print("--------------------------------------")

        summary = summarize_email(body)

        print(summary)

        # -----------------------------------
        # SKIP SPAM EMAILS
        # -----------------------------------

        if category.lower() == "spam":

            print("\n⚠ Spam email detected.")
            print("Reply generation skipped.")

            continue

        # -----------------------------------
        # GENERATE AI REPLY
        # -----------------------------------

        print("\n--------------------------------------")
        print(" GENERATING AI REPLY...")
        print("--------------------------------------")

        reply = generate_reply(body)

        print("\nAI GENERATED REPLY:\n")
        print(reply)

        # -----------------------------------
        # HUMAN APPROVAL
        # -----------------------------------

        print("\n--------------------------------------")

        approval = input(
            "Do you want to send this reply? (yes/no): "
        ).lower()

        # -----------------------------------
        # SEND EMAIL
        # -----------------------------------

        if approval == "yes":

            try:

                send_email(
                    service=service,
                    to=extract_email_address(sender),
                    subject=f"Re: {subject}",
                    body=reply
                )

                print("✅ Reply sent successfully.")

            except Exception as e:

                print(f"❌ Failed to send reply: {str(e)}")

        else:

            print("Reply skipped.")

    print("\n======================================")
    print(" EMAIL PROCESSING COMPLETED ")
    print("======================================\n")


# -----------------------------------
# EXTRACT EMAIL ADDRESS
# -----------------------------------

def extract_email_address(sender):

    """
    Example:
    'John Doe <john@gmail.com>'
    -> john@gmail.com
    """

    if "<" in sender and ">" in sender:

        return sender.split("<")[1].split(">")[0]

    return sender


# -----------------------------------
# RUN APPLICATION
# -----------------------------------

if __name__ == "__main__":

    run_email_agent()