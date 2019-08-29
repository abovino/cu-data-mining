# Copper Data Mining

Python3 web scraping app to download copper market prices, and save them to a MySQL database.  A scheduled cron job runs the script every weekday at market close.

# Installation

#### Clone the repo
```bash
git clone git@github.com:abovino/cu_data_mining.git
```

#### Create a virtual environment
```bash
py3 -m venv environment_name
```

#### Activate the virtual environment
```bash
venv\Scripts\activate
```

#### Install dependencies

```bash
py3 -m pip install -r requirements.txt
```
#### Create a .env file for MySQL
```
DB_HOST=<host address>
DB_PORT=<port>
DB_USER=<username>
DB_PASS=<password>
DB_DATABASE=cu_data_mining
```
#### Create the database
Login to MySQL

```bash
 mysql -u your_username -p
```
Run the SQL script using the absolute path

```sql
source path_to_project/mysql/scripts.sql
```
#### Run the web scraper
```bash
py3 scraper.py
```

#### Schedule the cron job
Open the crontab editor
```bash
crontab -e
```
Enter the cron job in your crontab file (Runs every weekday at 6pm)
```bash
0 18 * * 1-5 /path/to/bin/python /path/to/cu_data_mining/scraper.py
```
