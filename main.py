import streamlit as st
import time
import smtplib
from email.mime.text import MIMEText
import random
from dotenv import load_dotenv
import os

load_dotenv()

app_password = os.environ['app_password']



st.title("Erika's Wonderful Xmas Gift")



#https://handandstone.zenoti.com/webstoreNew/giftcards/74e2d9c9-6800-4b31-9ae4-74d5571acac9

left_co, right_co = st.columns(2)
# with left_co:
#     st.image("photos/Pi7_Shane_Erika_1.jpeg")

with left_co:
    st.image("photos/Shane_Erika_2.jpg", width=300)

with right_co:
    st.image("photos/Shane_Erika_3.jpg", width=300)



date_choice = st.selectbox(label='Where did we have our first date',
             options=['Da Club', 'The Pier behind Walmart', "Pier67", "Pier Bar", "Moss"]
             )


import streamlit as st
import streamlit.components.v1 as components



def send_email():

    # ---- Email sending section ----
    sender_email = "shanedenecke@gmail.com"
    receiver_email = "shane.denecke@protonmail.com"
    

    msg = MIMEText("This is a test email sent after the fake animation.")
    msg["Subject"] = "Streamlit Test Email"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        # Connect to Gmail SMTP
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        st.success("Email sent successfully!")

    except Exception as e:
        st.error(f"Failed to send email: {e}")


cat_choice=None
shoot_ya_shot=None
dummyval = None
claim_prize=None



# Button
if date_choice=='Pier Bar':
    st.success("Correct Choice... Onto the next round")

    st.image("photos/SuccessKid.jpg", width=300)

    # Fake animation: progress bar + status updates
    # progress = st.progress(0)
    # status_text = st.empty()

    # for i in range(1, 101):
    #     progress.progress(i)
    #     status_text.text(f"Getting thigns set up {i}/100...")
    #     time.sleep(0.03)   # slow enough to see movement

    cat_choice = st.selectbox(label='Best Cat of all time?',
                options=['Decimus', 'Europa', "Grumpy Cat", "Cat Stevens"]
                )
 
if cat_choice=='Europa':
    st.success("You got it. Now you just have to sink this shot")
    time.sleep(2)
    shoot_ya_shot = st.button("Shoot your shot")



if shoot_ya_shot:

    st.video("photos/Golf.mp4", autoplay=True, start_time=1, end_time=25)
    time.sleep(26)

    st.success("Hole in One!")
    time.sleep(2)
    
    st.video("photos/Email Archive.mp4", loop=True, autoplay=True, width=300)
    st.success("Sending your gift via email...", width=300)
    
    send_email()
