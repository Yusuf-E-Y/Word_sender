#  Vocabulary Email Sender

This project automatically sends **English and Turkish words** with their **pronunciations** to a selected email address every **1 hour**, in **random order**.

The data is scraped from a website and processed using the following Python libraries:

- `requests` – for handling HTTP requests  
- `BeautifulSoup (bs4)` – for parsing HTML content  
- `smtplib` – for sending emails via SMTP

##  Features
- Random word selection
- Dual language (English–Turkish) support
- Automatic email delivery every hour
- Simple and lightweight codebase

##  Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`

Install dependencies with:

```bash
pip install requests beautifulsoup4
````
smtplib
````bash
pip install smtplib
````
