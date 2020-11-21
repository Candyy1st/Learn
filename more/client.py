import tkinter
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

"""
CONSTANTS
"""
BUFFERSIZE = 1024
FORMAT = 'utf8'

def receive():
    while True:
        try:
            # Get the message from the server
            message = user_socket.recv(BUFFERSIZE).decode(FORMAT)

            # Add it to the message list
            message_list.insert(tkinter.END, message)
        except OSError:
            # PR
            break

def send(event=None):
    # Handling send message
    # Ambil message
    message = my_message.get()
    # Clear input setelah sent
    my_message.set('')
    # send message ke server untuk di broadcast ke user lain
    user_socket.send(bytes(message, FORMAT))
    # Handling ketika quit {quit}
    if message == '{quit}':
        user_socket.close()
        root.destroy()


def on_closing(event=None):
    # Helper function user exit chat
    print('bye bye!')



root = tkinter.Tk()
root.title('Chat me!')

message_frame = tkinter.Frame(root)
message_frame.pack()

scrollbar = tkinter.Scrollbar(message_frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# Message list
message_list = tkinter.Listbox(message_frame, height=15, width=50, yscrollcommand=scrollbar.set)
message_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
message_list.pack()

# Handle X (exit) Button
root.protocol('WM_DELETE_WINDOW', on_closing)

# input field
my_message = tkinter.StringVar()
my_message.set('Ketik disini!')

input_field = tkinter.Entry(root, textvariable=my_message)
input_field.bind('<Return>', send)
input_field.pack()

send_button = tkinter.Button(root, text='Kirim', command=send)
send_button.pack()

# Add Socket for client
HOST = input('Enter host: ') # Testing use 127.0.0.1
PORT = input('Enter Port: ') # Testing use 33000

# Error handling port
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

ADDR = (HOST, PORT)
user_socket = socket(AF_INET, SOCK_STREAM) # Socket for combo of host and port
user_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

tkinter.mainloop() #mulai GUI Execution