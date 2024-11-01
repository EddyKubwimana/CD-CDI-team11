from flask import Flask, render_template, request, jsonify
import redis
import mysql.connector

app = Flask(__name__)

# Redis for tracking page visits
r = redis.Redis(host="redis", port=6379)


@app.route("/")

def index():
    '''

    home page
    
    '''
    






@app.route("/")
def home():
    count = r.incr("hits")
    conn = db_connection("mysql", "EddyKubwimana", "password", "cloud")
    cursor = conn.cursor()

    # Create the table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS people (
        id INT AUTO_INCREMENT PRIMARY KEY,
        firstname VARCHAR(100),
        lastname VARCHAR(100),
        registration_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM people ORDER BY registration_time DESC')
    people_data = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("index.html", count=count, people=people_data)


@app.route('/submit', methods=['POST'])
def submit():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    conn = db_connection("mysql", "EddyKubwimana", "password", "cloud")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO people (firstname, lastname) VALUES (%s, %s)', (firstname, lastname))
    conn.commit()

    cursor.execute('SELECT * FROM people ORDER BY registration_time DESC')
    people_data = cursor.fetchall()
    cursor.close()
    conn.close()

   
    return jsonify({'message': 'User added successfully!', 'people': people_data, 'count': r.get("hits").decode()})


def db_connection(host, username, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )
    return connection


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
