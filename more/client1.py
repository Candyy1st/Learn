"""
Here, we will use TKInter to create the UI where users will be able to chat with one another.
It will connect to the server code that we just wrote.
GUI = graphical user interface, when a pilot controls a plane, he doesn't move the wings himself.
He has buttons, a user-friendly interface to help him control it.
"""

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

"""
CONSTANTS
"""
BUFFERSIZE = 1024  # The amount of data in KB that can be sent before the send is interrupted
FORMAT = "utf8"  # Format of the content we're sending

"""
Function to receive messages
"""


def receive():
    while True:  # Infinite loop receives messages randomly, so have to always wait and listen
        try:
            # Get the message from the socket
            message = user_socket.recv(BUFFERSIZE).decode(FORMAT)
            # Add it to a message list
            message_list.insert(tkinter.END, message)
        except OSError:  # If user left the chat
            break


"""
Function to handle sending messages
"""


def send(
        event=None):  # Parameter for event is passed by binders, implicitly passed by TKInter when send button is pressed

    # Grab the message that wants to be sent
    message = my_message.get()

    # Clears input field for next message
    my_message.set("")

    # send message to server, which will be broadcasted
    user_socket.send(bytes(message, FORMAT))

    # When user wants to quit, close and quit GUI
    if message == "{quit}":
        user_socket.close()
        root.destroy()


"""
Function to close socket connections if we close the TKInter GUI window
"""


def on_closing(event=None):
    # simulates user sending {quit} message
    my_message.set("{quit}")
    send()


"""
STEP 1: Start building the GUI
pack() function organizes widgets in blocks before placing them in parent frame
"""
root = tkinter.Tk()  # Initializes the root-level widget and set the title
root.title("Chat me!")

message_frame = tkinter.Frame(root)
message_frame.pack()

scrollbar = tkinter.Scrollbar(message_frame)  # To scroll up and see old messages
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

message_list = tkinter.Listbox(message_frame, height=15, width=50, yscrollcommand=scrollbar.set)
message_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
message_list.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)  # Binds the on_closing function with the X button

"""
STEP 2: Create textfield for users to type messages and send button
"""
my_message = tkinter.StringVar()  # variable to store user's inputted message
my_message.set("Type your messages here!")  # initiate the first message to show users where to type

entry_field = tkinter.Entry(root, textvariable=my_message)  # UI where users input messages
entry_field.bind("<Return>", send)  # Binds the enter key to the send function
entry_field.pack()

send_button = tkinter.Button(root, text="Send", command=send)
send_button.pack()

"""
STEP 3: Ask user to input in HOST and PORT and connect GUI to the server!
"""
HOST = input("Enter host: ")  # for testing, 0.0.0.0
PORT = input("Enter port: ")  # for testing, 33000

if not PORT:
    PORT = 33000  # Give default value in case they don't enter anything, HOMEWORK: create error checking!
else:
    PORT = int(PORT)

ADDR = (HOST, PORT)
user_socket = socket(AF_INET, SOCK_STREAM)
user_socket.connect(ADDR)

receive_thread = Thread(target=receive)  # Binds this thread with the receive function
receive_thread.start()  # Start the receive thread
tkinter.mainloop()  # starts GUI execution
