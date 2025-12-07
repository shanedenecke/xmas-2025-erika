

#### IMPORT LIBRARIES
import streamlit as st
import time
from dotenv import load_dotenv
import os
from IPython import get_ipython
from imapclient import IMAPClient
import pyzmail
import smtplib
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText

### LOAD ENV VARS
if get_ipython(): ### local dev
    load_dotenv()
    base_dir = "/home/deneckes/protonDrive/Social/Xmas/Xmas2025/xmas-2025-erika"
else:
    base_dir = os.path.dirname(os.path.realpath(__file__))
    


app_password = os.environ['app_password']





def forward_email(
        app_password,
        IMAP_SERVER = "imap.gmail.com",
        EMAIL = "shanedenecke@gmail.com",
        FORWARD_TO = "shane.denecke@protonmail.com",
        TARGET_SUBJECT = 'All about your LottieFiles account'
        ):

    # ---- Step 1: Connect to IMAP and fetch the email ----
    with IMAPClient(IMAP_SERVER) as client:
        client.login(EMAIL, app_password)
        client.select_folder("INBOX")

        # IMAP SUBJECT search (case-insensitive)
        message_ids = client.search(['SUBJECT', TARGET_SUBJECT])[0]

        raw_message = client.fetch([message_ids], ["RFC822"])[message_ids][b"RFC822"]
        msg = pyzmail.PyzMessage.factory(raw_message)

    # Extract content
    subject = msg.get_subject()
    from_addr = msg.get_addresses("from")[0][1]

    if msg.text_part:
        body = msg.text_part.get_payload().decode(msg.text_part.charset)
    else:
        body = "(No text content)"

    # ---- Step 2: Forward the email using SMTP ----
    forward_msg = MIMEMultipart()
    forward_msg["From"] = EMAIL
    forward_msg["To"] = FORWARD_TO
    forward_msg["Subject"] = "Fwd: " + subject

    forward_msg.attach(MIMEText(
        f"Forwarded message from {from_addr}:\n\n" + body,
        "plain"
    ))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, app_password)
        server.send_message(forward_msg)

    print("Email forwarded!")




## TITLE 
st.title("Erika's Wonderful Xmas Gift")
st.write(app_password)



### PHOTOS OF US
left_co, right_co = st.columns(2)

with left_co:
    st.image("photos/Shane_Erika_2.jpg", width=300)

with right_co:
    st.image("photos/Shane_Erika_3.jpg", width=300)



### SET STYLE FOR SELECTBOX LABEL
st.markdown("""
    <style>
        .stSelectbox > label {
            font-size: 40; /* Adjust the size as needed */
            font-weight: bold; /* Optional: make the label bold */
        }
    </style>
""", unsafe_allow_html=True)




### INITIALIZE STATES
cat_choice=None
shoot_ya_shot=None
dummyval = None
claim_prize=None


#### QUESTION NUMBER 1

date_choice = st.selectbox(label='## Where did we have our first date',
             options=['Da Club', 'The Pier behind Walmart', "Pier67", "Pier Bar", "Moss"]
             )

if date_choice=='Pier Bar':
    st.success("Correct Choice... Onto the next round")

    st.image("photos/SuccessKid.jpg", width=300)

    cat_choice = st.selectbox(label='Best Cat of all time?',
                options=['Decimus', 'Europa', "Grumpy Cat", "Cat Stevens"]
                )
 

#### QUESTION 2
if cat_choice=='Europa':
    st.success("You got it. Now you just have to sink this shot")
    time.sleep(2)
    shoot_ya_shot = st.button("Shoot your shot")



### GOLF SHOT
if shoot_ya_shot:

    st.video("photos/Golf.mp4", autoplay=True, start_time=1, end_time=25)
    time.sleep(26)

    st.success("Hole in One!")
    time.sleep(2)
    
    st.video("photos/Email Archive.mp4", loop=True, autoplay=True, width=300)
    st.success("Sending your gift via email...", width=300)
    
    forward_email(
        IMAP_SERVER = "imap.gmail.com",
        EMAIL = "shanedenecke@gmail.com",
        app_password = app_password,
        FORWARD_TO = "shane.denecke@protonmail.com",
        TARGET_SUBJECT = 'All about your LottieFiles account'
        )









#scratch


# def send_email():

#     # ---- Email sending section ----
#     sender_email = "shanedenecke@gmail.com"
#     receiver_email = "shane.denecke@protonmail.com"
    

#     msg = MIMEText("This is a test email sent after the fake animation.")
#     msg["Subject"] = "Streamlit Test Email"
#     msg["From"] = sender_email
#     msg["To"] = receiver_email

#     try:
#         # Connect to Gmail SMTP
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(sender_email, app_password)
#         server.sendmail(sender_email, receiver_email, msg.as_string())
#         server.quit()

#         st.success("Email sent successfully!")

#     except Exception as e:
#         st.error(f"Failed to send email: {e}")



#https://handandstone.zenoti.com/webstoreNew/giftcards/74e2d9c9-6800-4b31-9ae4-74d5571acac9
