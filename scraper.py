from requests import get
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from datetime import datetime
import os
import mysql.connector

load_dotenv()


def get_todays_rates(url):
    res = get(url, stream=True).content
    html = BeautifulSoup(res, 'html.parser')
    del_cu_rate = html.find_all(attrs={'href': '/en/markdaten.php?action=diagram&field=DEL_high'})[1].text
    eur_to_usd_ex_rate = html.find_all(attrs={'href': '/en/markdaten.php?action=diagram&field=Euro_MTLE'})[1].text

    return {
        'del_cu_rate': del_cu_rate,
        'eur_to_usd_ex_rate': eur_to_usd_ex_rate,
        'camden_cu_rate': 3.03,  # Freeze at 3.03
    }


def insert_into_rates(rates):
    db_conn = mysql.connector.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        passwd=os.environ['DB_PASS'],
        database=os.environ['DB_DATABASE']
    )

    cursor = db_conn.cursor()
    mysql_str = f"""INSERT INTO rates (del_cu_rate, eur_to_usd_ex_rate, camden_cu_rate)
                 VALUES ({rates["del_cu_rate"]}, {rates["eur_to_usd_ex_rate"]}, {rates["camden_cu_rate"]})"""
    cursor.execute(mysql_str)
    db_conn.commit()


try:
    url = 'https://www.westmetall.de/en/markdaten.php'
    rates = get_todays_rates(url)
    insert_into_rates(rates)
    print('Success!')
except Exception as e:
    print('An error occured.  Please check the logs for more info')
    log_fail = open('logs.txt', 'a')
    log_fail.write(f'[{datetime.today()}] - The following error occured: {str(e)}\n')
