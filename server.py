import mysql.connector
import os
import json
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/rates')
def test_route():
	db_conn = mysql.connector.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USER'],
    passwd=os.environ['DB_PASS'],
    database=os.environ['DB_DATABASE']
  )

	cursor = db_conn.cursor()
	query = 'SELECT id, del_cu_rate, eur_to_usd_ex_rate, camden_cu_rate, date_added FROM rates;'
	cursor.execute(query)
	results = cursor.fetchall()
	fields = [x[0] for x in cursor.description]
	json_data = []

	for row in results:
		json_data.append(dict(zip(fields, row)))

	return jsonify(json_data)


if __name__ == '__main__':
	app.run()