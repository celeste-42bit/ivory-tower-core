from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import functions
import time


app = Flask(__name__)


#------------------
# Pages
#------------------

@app.route("/")  # index
def index():
    return render_template("index.html")


@app.route("/functions/wol/<device_name>", methods=["GET"])
def wol(device_name):
    status = functions.wol(device_name)

    if status != 0:
        return render_template("error.html", message=status)
    
    return render_template("wol.html", device_name=device_name)



#------------------
# getters
#------------------
def get_rdp_status(device_name, host, timeout=60):  # this is called by the JS code in wol.html
    """Waits until the RDP port (3389) is open and sends a WebSocket event."""
    print(f"Waiting for {device_name} to become available on port 3389...")
    start = time.time()

    while time.time() - start < timeout:
        if functions.is_port_open(host, 3389):  # Only check port 3389
            print(f"{device_name} is now ready for RDP!")
            SocketIO.emit("device_online", {"device_name": device_name})
            return
        time.sleep(2)

    print(f"{device_name} did not open port 3389 within the timeout.")

#------------------
# run
#------------------

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)