import io
import os

import pymssql
from flask import Flask


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    buf = io.StringIO()
    try:
        conn = pymssql.connect(os.getenv("MSSQL_SERVER"), os.getenv("MSSQL_USERNAME"),
            os.getenv("MSSQL_PASSWORD"), "tempdb")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM persons")
        row = cursor.fetchone()
        while row:
            buf.write("ID=%d, Name=%s\n" % (row[0], row[1]))
            row = cursor.fetchone()
        conn.close()
    except:
        buf.write("Unable to connect to database!\n")
    return buf.getvalue()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
