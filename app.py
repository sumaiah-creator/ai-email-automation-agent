# app.py

import streamlit as st

from read_emails import read_emails

from ai_agent import (
    classify_email,
    summarize_email,
    generate_reply
)

from gmail_auth import authenticate_gmail
from send_email import send_email


# -----------------------------------
# EXTRACT EMAIL ADDRESS
# -----------------------------------

def extract_email_address(sender):

    if "<" in sender and ">" in sender:

        return sender.split("<")[1].split(">")[0]

    return sender


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Email Automation Agent",
    page_icon="📧",
    layout="wide"
)


# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

/* MAIN APP */
.stApp {
    background-color: #0B1120;
    color: white;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #1F2937;
}

/* TITLES */
h1, h2, h3 {
    color: white;
    font-weight: 700;
}

/* BUTTONS */
.stButton > button {
    background: linear-gradient(
        135deg,
        #06B6D4,
        #3B82F6
    );

    color: white;
    border: none;
    border-radius: 12px;

    padding: 12px 22px;

    font-size: 16px;
    font-weight: 600;

    transition: 0.3s;
}

.stButton > button:hover {

    transform: scale(1.03);

    box-shadow: 0 0 20px rgba(
        59,
        130,
        246,
        0.5
    );
}

/* EMAIL CARD */
.email-card {

    background: rgba(
        17,
        24,
        39,
        0.9
    );

    border: 1px solid #1F2937;

    border-radius: 18px;

    padding: 25px;

    margin-top: 20px;
    margin-bottom: 20px;

    box-shadow: 0px 4px 25px rgba(
        0,
        0,
        0,
        0.3
    );
}

/* METRIC CARDS */
[data-testid="metric-container"] {

    background-color: #111827;

    border: 1px solid #1F2937;

    padding: 20px;

    border-radius: 16px;

    box-shadow: 0 4px 20px rgba(
        0,
        0,
        0,
        0.2
    );
}

/* TEXT AREA */
textarea {

    border-radius: 12px !important;

    background-color: #111827 !important;

    color: white !important;

    border: 1px solid #374151 !important;
}

/* EXPANDER */
.streamlit-expanderHeader {

    background-color: #111827;

    border-radius: 12px;
}

/* SUCCESS BOX */
.stSuccess {

    border-radius: 12px;
}

/* WARNING BOX */
.stWarning {

    border-radius: 12px;
}

/* INFO BOX */
.stInfo {

    border-radius: 12px;
}

/* ERROR BOX */
.stError {

    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------
# TITLE
# -----------------------------------

# -----------------------------------
# DASHBOARD HEADER
# -----------------------------------

st.markdown("""
<div style="
    padding: 25px;
    border-radius: 18px;
    background: linear-gradient(
        135deg,
        #111827,
        #1E293B
    );
    margin-bottom: 25px;
    text-align: center;
">

<h1 style="
    color: white;
    margin-bottom: 10px;
">
AI Email Automation Dashboard
</h1>

<p style="
    color: #CBD5E1;
    font-size: 18px;
">

AI-powered email automation using
Gmail API and locally hosted Llama3.

</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------------
# DASHBOARD METRICS
# -----------------------------------

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric(
        "📩 Emails",
        "24",
        
    )

with metric2:
    st.metric(
        "🤖 AI Status",
        "Active"
    )

with metric3:
    st.metric(
        "⚡ Responses",
        "18"
    )

with metric4:
    st.metric(
        "📬 Gmail",
        "Connected"
    )

st.markdown("---")

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.markdown("""
# 🤖 AI Agent

### Navigation
""")

max_emails = st.sidebar.slider(
    "Number of Emails",
    min_value=1,
    max_value=20,
    value=5
)

st.sidebar.success("🟢 AI Agent Running")

st.sidebar.info("""
### Current Model
Llama3 via Ollama
""")


# -----------------------------------
# AUTHENTICATE GMAIL
# -----------------------------------

service = authenticate_gmail()


# -----------------------------------
# LOAD EMAILS
# -----------------------------------

if st.button("Load Emails"):

    progress_bar = st.progress(0)

    with st.spinner("Reading emails..."):

        emails = read_emails(max_results=max_emails)

    progress_bar.progress(25)

    if not emails:

        st.warning("No emails found.")

    else:

        # -----------------------------------
        # DASHBOARD METRICS
        # -----------------------------------

        total_emails = len(emails)

        st.success(f"{total_emails} emails loaded successfully.")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📩 Emails", total_emails)

        with col2:
            st.metric("🤖 AI Status", "Active")

        with col3:
            st.metric("📬 Gmail", "Connected")

        progress_bar.progress(50)

        # -----------------------------------
        # PROCESS EMAILS
        # -----------------------------------

        for index, email in enumerate(emails, start=1):

            sender = email["sender"]
            subject = email["subject"]
            body = email["body"]

            # -----------------------------------
            # EMAIL CARD
            # -----------------------------------

            with st.container():

                st.markdown(
                    '<div class="email-card">',
                    unsafe_allow_html=True
                )

                st.subheader(f"📨 Email {index}")

                st.write(f"👤 Sender: {sender}")

                # -----------------------------------
                # EMAIL BODY
                # -----------------------------------

                with st.expander("View Email Body"):

                    st.write(body[:2000])

                # -----------------------------------
                # CLASSIFY EMAIL
                # -----------------------------------

                with st.spinner("Classifying email..."):

                    category = classify_email(body)

                st.markdown("### 🏷 Category")

                category_clean = category.strip().lower()

                if "important" in category_clean:

                    st.error(category)

                elif "job" in category_clean:

                    st.success(category)

                elif "meeting" in category_clean:

                    st.info(category)

                elif "spam" in category_clean:

                    st.warning(category)

                else:

                    st.write(category)

                progress_bar.progress(70)

                # -----------------------------------
                # SUMMARIZE EMAIL
                # -----------------------------------

                with st.spinner("Generating summary..."):

                    summary = summarize_email(body)

                st.markdown("### Summary")

                st.write(summary)

                progress_bar.progress(85)

                # -----------------------------------
                # SPAM CHECK
                # -----------------------------------

                if "spam" in category_clean:

                    st.warning("⚠ Possible spam email detected.")

                    generate_anyway = st.checkbox(
                        f"Generate reply anyway? #{index}"
                    )

                    if not generate_anyway:

                        continue

                # -----------------------------------
                # GENERATE REPLY
                # -----------------------------------

                with st.spinner("Generating AI reply..."):

                    reply = generate_reply(body)

                st.markdown("### AI Generated Reply")

                edited_reply = st.text_area(
                    "Edit Reply Before Sending",
                    value=reply,
                    height=220,
                    key=f"reply_{index}"
                )

                # -----------------------------------
                # SEND EMAIL
                # -----------------------------------

                if st.button(f"Send Reply {index}"):

                    try:

                        recipient = extract_email_address(
                            sender
                        )

                        send_email(
                            service=service,
                            to=recipient,
                            subject=f"Re: {subject}",
                            body=edited_reply
                        )

                        st.success(
                            "Reply sent successfully!"
                        )

                    except Exception as e:

                        st.error(
                            f"Failed to send email: {str(e)}"
                        )

        progress_bar.progress(100)

        st.success("Email processing completed!")