from flask import Flask, request, render_template_string
import psycopg2
import pymysql
import os

app = Flask(__name__)

# Database connections
def get_pg():
    return psycopg2.connect(
        host="postgres",
        database="vulnapp",
        user="postgres",
        password="insecure"
    )

def get_mysql():
    return pymysql.connect(
        host="mysql",
        user="root",
        password="insecure",
        database="vulnapp"
    )

# CVE-2019-9193 - PostgreSQL RCE
@app.route('/cve-2019-9193')
def pg_rce():
    query = request.args.get('query', '')
    conn = get_pg()
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM products WHERE name LIKE '%{query}%'")
        return f"Results: {cur.fetchall()}"
    except Exception as e:
        return f"Error: {str(e)}"

# CVE-2020-7471 - Django StringAgg
@app.route('/cve-2020-7471')
def django_stringagg():
    delim = request.args.get('delim', ',')
    conn = get_pg()
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT string_agg(name, '{delim}') FROM products")
        return f"Aggregated: {cur.fetchone()[0]}"
    except Exception as e:
        return f"Error: {str(e)}"

# CVE-2018-15133 - Laravel unserialize
@app.route('/cve-2018-15133', methods=['POST'])
def laravel_unserialize():
    from pickle import loads
    try:
        data = loads(request.get_data())
        return f"Unserialized: {str(data)}"
    except:
        return "Invalid data"

# CVE-2020-35476 - Drupal JSON:API
@app.route('/cve-2020-35476')
def drupal_jsonapi():
    filter = request.args.get('filter', '')
    conn = get_pg()
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM nodes WHERE {filter}")
        return f"Results: {cur.fetchall()}"
    except Exception as e:
        return f"Error: {str(e)}"

# CVE-2020-14750 - WebLogic
@app.route('/cve-2020-14750')
def weblogic():
    id = request.args.get('id', '1')
    conn = get_mysql()
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM users WHERE id = {id}")
        return f"User: {cur.fetchone()}"
    except Exception as e:
        return f"Error: {str(e)}"

# CVE-2020-5405 - Spring Data JPA
@app.route('/cve-2020-5405')
def spring_jpa():
    name = request.args.get('name', 'admin')
    conn = get_mysql()
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM users WHERE name = '{name}'")
        return f"User: {cur.fetchone()}"
    except Exception as e:
        return f"Error: {str(e)}"

# CVE-2020-1956 - Apache Kylin
@app.route('/cve-2020-1956')
def apache_kylin():
    project = request.args.get('project', 'test')
    conn = get_mysql()
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM projects WHERE project='{project}'")
        return f"Results: {cur.fetchall()}"
    except Exception as e:
        return f"Error: {str(e)}"

# CVE-2020-5515 - SuiteCRM
@app.route('/cve-2020-5515')
def suitecrm():
    id = request.args.get('id', '1')
    conn = get_mysql()
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM contacts WHERE id = {id}")
        return f"Contact: {cur.fetchone()}"
    except Exception as e:
        return f"Error: {str(e)}"

# CVE-2019-19879 - Dolibarr
@app.route('/cve-2019-19879', methods=['POST'])
def dolibarr():
    login = request.form.get('login', 'admin')
    conn = get_mysql()
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM users WHERE login='{login}'")
        return f"User: {cur.fetchone()}"
    except Exception as e:
        return f"Error: {str(e)}"

# CVE-2021-27852 - PrestaShop
@app.route('/cve-2021-27852')
def prestashop():
    id = request.args.get('id', '1')
    conn = get_mysql()
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM products WHERE id_product = {id}")
        return f"Product: {cur.fetchone()}"
    except Exception as e:
        return f"Error: {str(e)}"

# Homepage with all CVEs
@app.route('/')
def index():
    return '''
    <h1>Advanced SQL Injection Lab</h1>
    <ul>
        <li><a href="/cve-2019-9193">CVE-2019-9193 - PostgreSQL RCE</a></li>
        <li><a href="/cve-2020-7471">CVE-2020-7471 - Django StringAgg</a></li>
        <li><a href="/cve-2018-15133">CVE-2018-15133 - Laravel unserialize</a></li>
        <li><a href="/cve-2020-35476">CVE-2020-35476 - Drupal JSON:API</a></li>
        <li><a href="/cve-2020-14750">CVE-2020-14750 - WebLogic</a></li>
        <li><a href="/cve-2020-5405">CVE-2020-5405 - Spring Data JPA</a></li>
        <li><a href="/cve-2020-1956">CVE-2020-1956 - Apache Kylin</a></li>
        <li><a href="/cve-2020-5515">CVE-2020-5515 - SuiteCRM</a></li>
        <li><a href="/cve-2019-19879">CVE-2019-19879 - Dolibarr</a></li>
        <li><a href="/cve-2021-27852">CVE-2021-27852 - PrestaShop</a></li>
    </ul>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
