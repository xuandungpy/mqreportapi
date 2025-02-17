from flask import Flask, jsonify
import cx_Oracle

app = Flask(__name__)

@app.route('/get-data', methods=['GET'])
def get_data():
    dsn_tns = cx_Oracle.makedsn('mqsoft.ddns.net', '1521', service_name='mqsoft')
    connection = cx_Oracle.connect(user='system', password='Mqsoft0989777722', dsn=dsn_tns, encoding='UTF-8', nencoding='UTF-8')
    
    cursor = connection.cursor()
    cursor.execute('SELECT id, ma, ten, dang FROM mqsoftbvnhabe_test.d_dmbd')
       
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    
    data = [dict(zip(columns, row)) for row in rows]
    
    cursor.close()
    connection.close()
    
    response = jsonify(data)
    response.headers.add('Content-Type', 'application/json; charset=utf-8')
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
