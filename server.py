#! /usr/bin/env python3
# _*_ coding:utf-8 _*_ 
#########################################################################
# File Name: server.py
# Author: FU Zhenqiu
# mail: fuzhenqiu0810@gmail.com
# Created Time: 2021年01月09日 星期六 14时51分46秒
#########################################################################

from socket import *
from time import ctime

host = ''
port = 11000
ADDR = (host, port)
BUFSIZ = 1024

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(ADDR)
#set the max number of tcp connection
tcpSocket.listen(5)

while True:
    print('waiting for connection...')
    clientSocket, clientAddr = tcpSocket.accept()
    print('conneted form: %s' %clientAddr[0])

    body_1_x=31.1111
    body_1_y=121.1234
    body_1_z=25.1111

    body_2_x=32.2111
    body_2_y=124.1234
    body_2_z=22.1111

    relative_x=11.2111
    relative_y=14.1234
    relative_z=2.1111   

    while True:
        try:
            data = clientSocket.recv(BUFSIZ)
            print('socket:  %s' %data.decode('utf-8'))
        except IOError as e:
            print(e)
            clientSocket.close()
            break
        if not data:
            break
        returnData = ctime()+data.decode('utf-8')


        # loop data
        # body 1
        if body_1_x<40.0:
        	body_1_x=body_1_x+0.0001
        else:
        	body_1_x=body_1_x-10

        if body_1_y<130.0:
        	body_1_y=body_1_x+0.0001
        else:
        	body_1_y=body_1_x-10

        if body_1_z<35.0:
        	body_1_z=body_1_x+0.0001
        else:
        	body_1_z=body_1_x-10

        # body 2
        if body_2_x<42.2:
        	body_2_x=body_1_x+0.0001
        else:
        	body_2_x=body_1_x-10

        if body_2_y<133.1:
        	body_2_y=body_1_x+0.0001
        else:
        	body_2_y=body_1_x-10

        if body_2_z<33.56:
        	body_2_z=body_1_x+0.0001
        else:
        	body_2_z=body_1_x-10

        # relative
        if relative_x<20.0:
        	relative_x+=0.0001
        else:
        	relative_x-=10

        if relative_y<22.5:
        	relative_y+=0.0001
        else:
        	relative_y-=5

        if relative_z<10.0:
        	relative_z+=0.0001
        else:
        	relative_z-=8


        senddata="$SKLOESUB,"+str(body_1_x)+","+str(body_1_y) +","+str(body_1_z)+","\
                  +str(body_2_x)+","+str(body_2_y)+","+str(body_2_z)+","+str(relative_x)\
                  +","+str(relative_y)+","+str(relative_z)+","+"*"

        # senddata="$SKLOESUB,1234.1234,2345.1234,1234.1234,1234.1234,1234.1234,1234.1234,1234.1234,1234.1234,1234.1234,*"
        senddata2="$SKLOESUB,27.556687,-0.591480,188.437654,-2.644942,11.087367,225.230000,30.201629,11.678847,36.792346,*"
        clientSocket.send(senddata.encode('utf-8'))
    clientSocket.close()
tcpSocket.close()