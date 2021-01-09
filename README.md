# GUI4MVMO
A very simple GUI for multi vessel &amp; multi object motion capture. It is developed with Python for the MVMO system onshore test .

- **gui4mvmo.py**  includes two functions, the first one is communication with the server using custom protocol and the TCP/IP protocol, the second function is show a GUI using the **Tkinter** and the data in the GUI can be updated in real time .

- **server.py** is a very simple socket server, it can be send and receive the data, the communication protocol is showed below

  > $SKLOESUB,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,XXXX.XXXX,*

Install the Tkinter before using the program.

> sudo apt-get install python3-tk

