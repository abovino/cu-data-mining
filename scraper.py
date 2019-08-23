from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

url = 'https://www.westmetall.de/en/markdaten.php'

res = get(url, stream=True).content
html = BeautifulSoup(res, 'html.parser')
del_cu_rate = html.find_all(attrs={'href': '?action=show_diagram&field=DEL_high'})[1].text
eur_to_usd_ex_rate = html.find_all(attrs={'href': '?action=show_diagram&field=Euro_MTLE'})[1].text

rates = {
  'del_cu_rate': del_cu_rate,
  'eur_to_usd_ex_rate': eur_to_usd_ex_rate,
  'camden_cu_rate': 3.03, # Freeze at 3.03
  'date_added': datetime.today()
}

def push_to_sql(rates):
  client = pymongo.MongoClient(os.environ['MONGODB_URI'])
  db = client['cu_data_mining']
  rates_collection = db['rates']
  rates_collection.insert_one(rates)

# Push to sql database ...
push_to_sql(rates)