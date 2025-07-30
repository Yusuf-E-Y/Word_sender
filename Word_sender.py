import time
import requests
from bs4 import BeautifulSoup
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

def send_mail():
    load_dotenv(dotenv_path="word.env")  
    sender_email = os.getenv("MAİL")
    receiver_email = os.getenv("MAİL")
    password = os.getenv("APP") 

    subject = "Today words"

    column1 = []
    column2 = []
    column3 = []

    url = "https://www.englishcentral.com/blog/adan-zye-en-cok-kullanilan-ingilizce-kelimeler-ve-anlamlari/" # <-- URL of the website to scrape

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    lines = soup.find_all("tr")

    for line in lines:
        Eng = line.find("td", class_="column-1")
        Tr = line.find("td", class_="column-2")
        read = line.find("td", class_="column-3")

        if Eng and Tr and read:
            column1.append(Eng.text.strip())
            column2.append(Tr.text.strip())
            column3.append(read.text.strip())

    word_index = random.randint(0, len(column1) - 1)
    word1 = column1[word_index]
    word2 = column2[word_index]
    word3 = column3[word_index]

    mail_content = f"Word: {word1}\nMean: {word2}\npronunciation: {word3}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(mail_content, "plain", "utf-8"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email was sent successfully.")
    except Exception as e:
        print("Bug:", e)

while True:
    send_mail()
    time.sleep(3600)
