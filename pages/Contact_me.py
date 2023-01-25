import streamlit as st
from send_email import send_email

page_title = "Contact me"

st.title(page_title)

with st.form(key='email_form'):
    email = st.text_input("Your email:")
    print(email)
    msg = st.text_area("Your message:")
    print(msg)
    submit_button = st.form_submit_button('Send')
    if submit_button:
        send_email(email_user=email, raw_message=msg)
