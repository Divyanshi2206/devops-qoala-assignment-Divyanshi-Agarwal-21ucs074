from flask import Flask, request
import datetime
import socket
import netifaces as ni

app = Flask(__name__)

def get_mac_address():
    for iface in ni.interfaces():
        try:
            mac = ni.ifaddresses(iface)[ni.AF_LINK][0]['addr']
            if mac:
                return mac
        except KeyError:
            continue
    return "N/A"

@app.route('/')
def user_info():
    user_ip = request.remote_addr
    username = request.headers.get('Username', 'Divyanshi - 21ucs074')
    mac_address = get_mac_address()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Adding CSS styling here
    return f"""
    <html>
    <head>
       <style>
    body {{
        font-family: Arial, sans-serif;
        margin: 40px;
        color: #333;
        background-color: #f4f7f6;
        text-align: center;
        display: flex;
        justify-content:center;
    }}

    h3 {{
        color: blue;
        font-weight: bold;
        font-size: 24px;
        margin-bottom: 10px;
    }}

    p {{
        font-size: 16px;
        line-height: 1.8;
        margin: 10px 0;
    }}

    .info {{
        border: 1px solid #ddd;
        padding: 20px;
        border-radius: 8px;
        background-color: #f9f9f9;
        max-width: 600px;
        margin: auto;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }}



    
</style>

    </head>
    <body>
        <div class="info">
            <p><b>IP Address:</b> {user_ip}</p>
            <p><b>MAC Address:</b> {mac_address}</p>
            <p><b>Username:</b> {username}</p>
            <p><b>Timestamp:</b> {timestamp}</p>
            <br>
            <h3>Assignment completed successfully!</h3>
        </div>
    </body>
    </html>
    """
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)