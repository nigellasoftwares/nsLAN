import requests
from flask import Flask, render_template

app = Flask(__name__)

SERVER_URL = 'http://192.168.29.41:5000'  # Replace 'server_ip' with the IP address of the server

def check_connection():
    try:
        response = requests.get(SERVER_URL)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

@app.route('/')
def client_status():
    connected = check_connection()
    return render_template('client_status.html', connected=connected)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
