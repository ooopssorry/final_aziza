from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Подключение к базе
conn = psycopg2.connect(
    host="db-aziza.c32geuygvkjg.ap-southeast-1.rds.amazonaws.com",
    dbname="postgres",
    user="postgres",
    password="postgres",
    port=5432
)

@app.route('/data')
def get_data():
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_aziza_data")
    rows = cur.fetchall()
    cur.close()
    return jsonify(rows)

@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tbl_aziza_data (area, years, revenue) VALUES (%s, %s, %s)",
            (data['area'], data['years'], data['revenue'])
        )
        conn.commit()
        cur.close()
        return jsonify({'message': 'Added'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete', methods=['POST'])
def delete_data():
    cur = conn.cursor()
    cur.execute("DELETE FROM tbl_aziza_data WHERE id = (SELECT MAX(id) FROM tbl_aziza_data)")
    conn.commit()
    cur.close()
    return jsonify({'message': 'Deleted'})

if__name == '__main__':
    app.run(host='0.0.0.0', port=5000)