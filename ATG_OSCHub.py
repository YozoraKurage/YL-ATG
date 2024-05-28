import argparse
import json
import math
import threading

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc.udp_client import SimpleUDPClient

RED = '\033[31m'
BLUE = '\033[34m'
END = '\033[0m'

with open("ports.json") as f:
    portsChash = json.load(f)

SendIP = portsChash["SendIP"]
SendPorts = portsChash["SendPorts"]
listenIP = portsChash["listenIP"]
listenPort = portsChash["listenPort"]

clients = [SimpleUDPClient(SendIP, port) for port in SendPorts]  # Create clients

def loopback(path, data):
    for client in clients:
        client.send_message(path, data)  # Send float message

def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")
    loopback(address, args)

def printer(address, data):
    print(f"{BLUE}[address]:{END}{address}{RED} [Data]:{END}{data}")
    loopback(address, data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default=listenIP, help="The ip to listen on")
    parser.add_argument("--port",
                        type=int, default=listenPort, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/avatar/parameters/ATG/*", printer)

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    
    print("Serving on {}".format(server.server_address))

    server.serve_forever()

# Future Things
# ATG_and_PS_over_TailScaleはデフォルトでポート9010を使います
# ATG_and_PS_over_TailScaleで受信するポートは、TailScaleでの自分のIPアドレスを使います
# 127.0.0.1だとダメです