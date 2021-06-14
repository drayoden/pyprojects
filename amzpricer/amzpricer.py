import requests
from bs4 import BeautifulSoup
import smtplib, os


# DC POWER SUPPLY:
URL = 'https://www.amazon.com/dp/B085S34NNW/?coliid=I17DAAJI135MYC&colid=17SKM49OPEZA2&psc=1&ref_=lv_ov_lig_dp_it'
notifyPrice = 92.34


# Google 'my user agent'
headers = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    # soup = BeautifulSoup(page.content, features='lxml')
    title = soup.find(id='productTitle').get_text().strip()
    price = float(soup.find(id="priceblock_ourprice").get_text()[1:6])
    print(f'Item: {title}')
    print (f'Current Price: {price}')
    print(f'Notify Price: {notifyPrice}')
        
    if (price < notifyPrice):
        print(f'\tsending email...')
        send_email(title)


def send_email(title):

    subject = 'Hazah! A amazon price has reduced...'
    body = f'Your amazon list item: {title} has a reduced price!\n\nCheck this link: {URL}'
    msg = f'subject: {subject}\n\n{body}'
    gappPw = os.getenv('GAPPPW')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('daryn.oden@gmail.com',gappPw)

    # list: from, to, msg
    server.sendmail(
        'daryn.oden@gmail.com',
        'daryn.oden@gmail.com',
        msg
    )
    server.quit()
    print('\temail sent...')

check_price()
