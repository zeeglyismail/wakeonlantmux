from flask import Flask, request
from wakeonlan import send_magic_packet

app = Flask(__name__)

@app.route('/wake', methods=['GET'])
def wake():
    # Change this MAC address to your PC's MAC
    mac = "D8-5E-D3-AC-16-5D"
    send_magic_packet(mac)
    return "Magic packet sent!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
