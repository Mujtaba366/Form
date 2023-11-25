import streamlit as st
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yagmail
from email.message import EmailMessage
# import ssl
# import smtplib

st.set_page_config(page_title="Making website form", page_icon="😀")

def send_gmail(contact_gmail, purpose_of_the_website, programming_languages, tabs, gmail, website_color, websit_look, money, name):
    gmail_sender = "godofwar9999991@gmail.com"
    gmail_password = "saht ndfx banu xfzo"
    gmail_resever = "mosavimujtaba366@gmail.com"
    subject = f"{name} want you to make a website for him/her"
    body = f"""
<html>
    <body>
      <h1>{name} want you to make a websit for him/her<h1>
      <p>name: {name}  
      contact gmail: {contact_gmail}   
      purpos of the website: {purpose_of_the_website}   
      programming languages to use: {programming_languages}   
      pages: {tabs}    
      account for web: {gmail}     
      website pages color info: {website_color}
      website should look like: {websit_look}
      money will give: {money}
      </p>
    </body>
</html>
"""
    yag=yagmail.SMTP(gmail_sender,gmail_password)
    contents=[body]
    yag.send(
        to=gmail_resever,
        subject=subject,
        contents=contents
    )
def main():
    st.title("Making website form")
    st.subheader("Your name: ")
    name = st.text_input(label="")
    st.subheader("Contact gmail: ")
    contact_gmail = st.text_input(label="", key="")
    st.subheader("Purpose of the website:")
    purpose_of_the_website = st.text_area(label="")
    st.subheader("Programming languages: ")
    programming_languages_list = ["Pyhton", "Html", "CSS", "SQL", "CSV", "Java script", "C#", "C++", "R"]
    programming_languages = st.multiselect(options=["Pyhton", "Html", "CSS", "SQL", "CSV", "Java script", "C#", "C++", "R"], label=" ")
    st.subheader("tabs:")
    st.write("Like what pages in your website like login, sign in and...")
    taps = st.text_area(label="", key="your mom")
    st.subheader("Gmail account and password:")
    st.write("write your gmail name and password that you will use for this website or write make a new after you write a new gmail and password.")
    gmail = st.text_area(label="", key="Your mom")
    st.subheader("Website page background color: ")
    st.write("like what should be the page login background color be or any other page.")
    website_color = st.text_area(label="", key="Your mom again")
    st.subheader("Give info how your website should look like including url or link?")
    websit_look = st.text_area(label="", key="your mom again")
    st.header("Money will you pay me: ")
    money = st.number_input(label="")

    if st.button("Send:"):
        send_gmail(name=name,gmail=gmail, money=money, websit_look=websit_look, website_color=website_color, tabs=taps, programming_languages=programming_languages, contact_gmail=contact_gmail, purpose_of_the_website=purpose_of_the_website)

if __name__ == "__main__":
    main()
