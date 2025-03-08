from wakeonlan import send_magic_packet
import json
import os
import socket


# Wake on LAN

def wol(device_name):
    mac = get_device_mac(device_name)
    try:
        send_magic_packet(mac)
        return 0
    except Exception as e:
        return str(e)


# helper functions

def get_device_mac(device_name):
    try:
        with open("./config/devices.json", "r") as f:
            devices = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    if device_name in devices:
        # return the mac associated with the device name in the json library
        return devices[device_name]

    
def is_port_open(host, port=3389):
    """Checks if a specific port is open on a machine."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        return sock.connect_ex((host, port)) == 0