#! /usr/bin/env python3
# _*_ coding:utf-8 _*_ 
#########################################################################
# File Name: gui2.py
# Author: FU Zhenqiu
# mail: fuzhenqiu0810@gmail.com
# Created Time: 2021年01月08日 星期五 22时26分11秒
#########################################################################

import tkinter
import time
import _thread
from socket import *

# socket varible
serverName = '127.0.0.1'
serverPort = 11000
BUFSIZ = 1024
ADDR = (serverName,serverPort)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADDR)

lock = _thread.allocate()

# # # $SKLOESUB,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,*
# # $SKLOESUB, XXXX.XXXX一号船x坐标, XXXX.XXXX一号船y坐标 ，XXXX.XXXX一号船首向角, 
# # XXXX.XXXX二号船x坐标, XXXX.XXXX二号船y坐标, XXXX, XXXX二号船首向角, XXXX, 
# # XXXX两条船x上的位移差值,XXXX, XXXX两条船y方向的位移差值,XXXX, XXXX两条船之间的夹角,*
# rscv_str="$SKLOESUB,1234.1234,2345.1234,1234.1234,1234.1234,1234.1234,1234.1234,1234.1234,1234.1234,1234.1234,*"

# global handle
global rscv_str
rscv_str="$SKLOESUB,9999.999999,9999.999999,9999.999999,9999.999999,9999.999999,9999.999999,9999.999999,9999.999999,9999.999999,*"
global root

global lb_body_1_x_value
global lb_body_1_y_value
global lb_body_1_phi_value

global lb_body_2_x_value
global lb_body_2_y_value
global lb_body_2_phi_value

global lb_relative_x_value
global lb_relative_y_value
global lb_relative_phi_value

global lb_raw_data

global lb

# callback function for updating the GUI showe
def getallvarible():
	# global handle
	global rscv_str
	# rscv_str = "$SKLOESUB,27.556687,-0.591480,188.437654,-2.644942,11.087367,225.230000,30.201629,11.678847,36.792346,*"
	
	global lb_body_1_x_value
	global lb_body_1_y_value
	global lb_body_1_phi_value

	global lb_body_2_x_value
	global lb_body_2_y_value
	global lb_body_2_phi_value

	global lb_relative_x_value
	global lb_relative_y_value
	global lb_relative_phi_value 

	global lb_raw_data

	global lb

	# updata data

	
	# lock
	lock.acquire()
	
	# time
	timestr = time.strftime("%Y-%m-%d %H:%M:%S") # 获取当前的时间并转化为字符串
	timestep="当前时间：　"+timestr
	lb.configure(text = timestep)

	# body 1 x
	body_1_x="{:.4f}".format(float(rscv_str.split(',')[1]))
	body_1_x=body_1_x.rjust(9,'0')
	lb_body_1_x_value.configure(text = body_1_x)

	# body 1 y
	body_1_y="{:.4f}".format(float(rscv_str.split(',')[2]))
	body_1_y=body_1_y.rjust(9,'0')
	lb_body_1_y_value.configure(text = body_1_y)

	# body 1 z
	body_1_phi="{:.4f}".format(float(rscv_str.split(',')[3]))
	body_1_phi=body_1_phi.rjust(9,'0')
	lb_body_1_phi_value.configure(text = body_1_phi)
	
	# body 2 x
	body_2_x="{:.4f}".format(float(rscv_str.split(',')[4]))
	body_2_x=body_2_x.rjust(9,'0')
	lb_body_2_x_value.configure(text = body_2_x)

	# body 2 y
	body_2_y="{:.4f}".format(float(rscv_str.split(',')[5]))
	body_2_y=body_2_y.rjust(9,'0')
	lb_body_2_y_value.configure(text = body_2_y)

	# body 2 z
	body_2_phi="{:.4f}".format(float(rscv_str.split(',')[6]))
	body_2_phi=body_2_phi.rjust(9,'0')
	lb_body_2_phi_value.configure(text = body_2_phi)

	# relative_x
	relative_x="{:.4f}".format(float(rscv_str.split(',')[7]))
	relative_x=relative_x.rjust(9,'0')
	lb_relative_x_value.configure(text = relative_x)	

	# relative_y
	relative_y="{:.4f}".format(float(rscv_str.split(',')[8]))
	relative_y=relative_y.rjust(9,'0')
	lb_relative_y_value.configure(text = relative_y)

	# relative_phi
	relative_phi="{:.4f}".format(float(rscv_str.split(',')[9]))
	relative_phi=relative_phi.rjust(9,'0')
	lb_relative_phi_value.configure(text = relative_phi)

	lb_raw_data.delete(0.0,tkinter.END)
	lb_raw_data.insert(tkinter.INSERT,str(rscv_str))
	lb_raw_data.update()

	# run update
	root.after(100, getallvarible) 

	# lock
	lock.release()

# thread function for socket to the server
def communication():
	global rscv_str
	while True:
		data = "OK"
		if not data:
			break
		clientSocket.send(data.encode('utf-8'))
		returnData = clientSocket.recv(BUFSIZ)
		if not returnData:
			break
		lock.acquire()
		rscv_str=str(returnData)
		lock.release()
	clientSocket.close()

# thread function for GUI layout and show
def gui():
	print("gui")
	global root
	global text1
	global text2
	global lb

	global lb_body_1_x_value
	global lb_body_1_y_value
	global lb_body_1_phi_value

	global lb_body_2_x_value
	global lb_body_2_y_value
	global lb_body_2_phi_value

	global lb_relative_x_value
	global lb_relative_phi_value
	global lb_relative_y_value

	global lb_raw_data

	root = tkinter.Tk()
	root.title("多船多目标")
	# root.geometry('1920x1080')
	root.geometry('1220x980')

	# title
	lb_name=tkinter.Label(root, text="SJTU多船多目标运动捕捉临时调试界面", borderwidth=5, relief="groove",fg='black',font=("微软雅黑",40))
	lb_name.grid(row=0,column=0,columnspan=7,pady=15)

	## body-1
	# body-1
	lb_body_1 = tkinter.Label(root, text="BODY-1", bg="orange",fg='black', font=("微软雅黑",45))
	lb_body_1.grid(row=1,column=0,padx=20,pady=10,ipadx=40)

	lb_body_1_x = tkinter.Label(root, text="X", fg="black", font=("微软雅黑",45))
	lb_body_1_x.grid(row=1,column=1,padx=20,pady=10)


	lb_body_1_x_value = tkinter.Label(root, text='', borderwidth=5, relief="groove", bg="red", fg='black', font=("微软雅黑",45))
	lb_body_1_x_value.grid(row=1,column=2,padx=20,pady=10)

	lb_body_1_y = tkinter.Label(root, text="Y",fg='black', font=("微软雅黑",45))
	lb_body_1_y.grid(row=1,column=3,padx=20,pady=10)

	lb_body_1_y_value = tkinter.Label(root, text='', borderwidth=5, relief="groove", bg="red",fg='black', font=("微软雅黑",45))
	lb_body_1_y_value.grid(row=1,column=4,padx=20,pady=10)

	lb_body_1_phi = tkinter.Label(root, text="YAW", fg='black', font=("微软雅黑",45))
	lb_body_1_phi.grid(row=1,column=5,padx=20,pady=10)

	lb_body_1_phi_value = tkinter.Label(root, text='', borderwidth=5, relief="groove",  bg="red",fg='black', font=("微软雅黑",45))
	lb_body_1_phi_value.grid(row=1,column=6,padx=20,pady=10)

	## body-2
	lb_body_2 = tkinter.Label(root, text="BODY-2", bg="orange",fg='black', font=("微软雅黑",45))
	lb_body_2.grid(row=2,column=0,padx=20,pady=10,ipadx=40)

	lb_body_2_x = tkinter.Label(root, text="X", fg='black', font=("微软雅黑",45))
	lb_body_2_x.grid(row=2,column=1,padx=20,pady=10)

	lb_body_2_x_value = tkinter.Label(root, text='', borderwidth=5, relief="groove", bg="red", fg='black', font=("微软雅黑",45))
	lb_body_2_x_value.grid(row=2,column=2,padx=20,pady=10)

	lb_body_2_y = tkinter.Label(root, text="Y",fg='black', font=("微软雅黑",45))
	lb_body_2_y.grid(row=2,column=3)

	lb_body_2_y_value = tkinter.Label(root, text='', borderwidth=5, relief="groove", bg="red",fg='black', font=("微软雅黑",45))
	lb_body_2_y_value.grid(row=2,column=4,padx=20,pady=10)

	lb_body_2_phi = tkinter.Label(root, text="YAW", fg='black', font=("微软雅黑",45))
	lb_body_2_phi.grid(row=2,column=5,padx=20,pady=10)

	lb_body_2_phi_value = tkinter.Label(root, text='', borderwidth=5, relief="groove", bg="red",fg='black', font=("微软雅黑",45))
	lb_body_2_phi_value.grid(row=2,column=6,padx=20,pady=10)

	## relative
	lb_relative = tkinter.Label(root, text="RELATIVE", bg="orange",fg='black', font=("微软雅黑",45))
	lb_relative.grid(row=3,column=0,padx=20,pady=10,ipadx=10)

	lb_relative_x = tkinter.Label(root, text="X", fg='black', font=("微软雅黑",45))
	lb_relative_x.grid(row=3,column=1,padx=20,pady=10)

	lb_relative_x_value = tkinter.Label(root, text='', borderwidth=5, relief="groove", bg="red", fg='black', font=("微软雅黑",45))
	lb_relative_x_value.grid(row=3,column=2,padx=20,pady=10)

	#
	lb_relative_y = tkinter.Label(root, text="Y",fg='black', font=("微软雅黑",45))
	lb_relative_y.grid(row=3,column=3,padx=20,pady=10)

	lb_relative_y_value = tkinter.Label(root, text='', borderwidth=5, relief="groove", bg="red",fg='black', font=("微软雅黑",45))
	lb_relative_y_value.grid(row=3,column=4,padx=20,pady=10)

	#
	lb_relative_phi = tkinter.Label(root, text="YAW", fg='black', font=("微软雅黑",45))
	lb_relative_phi.grid(row=3,column=5,padx=20,pady=10)

	lb_relative_phi_value = tkinter.Label(root, text='', borderwidth=5, relief="groove", bg="red",fg='black', font=("微软雅黑",45))
	lb_relative_phi_value.grid(row=3,column=6,padx=20,pady=10)
	
	# raw data
	lb_raw_data = tkinter.Text(root,width=200,height=5)
	lb_raw_data.grid(row=7,column=0,columnspan=7)


	# # update time
	lb = tkinter.Label(root, text='', fg='blue', font=("黑体", 20),justify="left")
	lb.grid(row=4,column=0,columnspan=2,padx=20,pady=10)
	root.after(100,getallvarible)
	# root.after(1000,gettime)
	
	root.mainloop()

if __name__ == '__main__':
# 创建两个线程
	try:
		_thread.start_new_thread( communication, () )
		_thread.start_new_thread( gui, () )
	except:
		print ("Error: 无法启动线程")

	while 1:
		pass

