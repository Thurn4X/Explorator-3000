#!/usr/bin/env python3

import socket
import struct

"""
    Magic headers:
        'INPT' : Key inputs
            - Key char (1 byte)
        'DATA' : Lidar data
            - Data size (4 bytes)
            - Data (size)
        ...
"""

class Server:
    def __init__(self, ip, port):

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((ip, port))

        self.keymap = "zqsde123"

    def connect(self):

        self.server.listen()
        self.conn, _ = self.server.accept()


    def send_input(self, key):

        if key not in self.keymap:
            print("[x] Unrecognized key!")
            return
        
        self.conn.send(b"INPT")
        self.conn.send(key.encode("utf-8"))

    def close_conn(self):
        self.conn.close()

    def rnp(self):
        hdr = self.conn.recv(4)
        if hdr == b"DATA":
            mat_points = []
            data_size = int.from_bytes(self.conn.recv(4), 'little')

            data = b""
            while len(data) != data_size:
                recvd = self.conn.recv(4)
                if recvd == b"": break
                data += recvd

            assert(len(data) == data_size)

            for i in range(0, len(data), 4):
                float_bytes = data[i:i+4]
                float_value, = struct.unpack('f', float_bytes)
                mat_points.append(float_value)
                

            return mat_points


            
if __name__ == "__main__":
    print("[x] This code is a module!")
    exit(-1)