import sqlite3 
import hashlib
import socket
import threading
import rsa
import pyotp

public_key, private_key = rsa.newkeys(1024)
clients = []  # Liste pour garder les clients connectés et leurs clés publiques

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9990))
server.listen()

print("Server is listening on 127.0.0.1:9990. . . ")

def broadcast(message, sender_client, sender_username):
    for client, pub_key in clients:
        if client != sender_client:  
            
            try:
                full_message =f"{sender_username}: {message}"
                client.send(rsa.encrypt(full_message.encode(), pub_key))
            except:
                clients.remove((client, pub_key))

def receiving_messages(c, pub_key, username):
    while True:
        try:
            message = rsa.decrypt(c.recv(1024), private_key).decode()
            print(f"Received message from {username}: {message}")
            broadcast(message, c, username)
        except:
            print("An error occurred. Closing connection.")
            clients.remove((c, pub_key))
            c.close()
            break

def handle_connection(c):
    global clients

    c.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(c.recv(1024))

    c.send("Username: ".encode())
    username = c.recv(1024).decode()

    c.send("Password: ".encode())
    encrypted_password = c.recv(1024)
    password = rsa.decrypt(encrypted_password, private_key).decode()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?",(username, hashed_password))

    if cur.fetchone():
        key = pyotp.random_base32()
        totp = pyotp.TOTP(key)
        print("TOTP: " + totp.now())
        c.send("Enter the two-factor authentication code: ".encode())
        input_otp_code = c.recv(1024).decode()

        if totp.verify(input_otp_code):
            c.send("Login successful!".encode())
            print(f"User {username} authenticated successfully.")
            clients.append((c, public_partner)) 

            threading.Thread(target=receiving_messages, args=(c, public_partner, username)).start()
        else:
            c.send("Login failed!".encode())
            print(f"Failed login attempt for user {username}.")
            c.close()
    else:
        c.send("Login failed!".encode())
        print(f"Failed login attempt for user {username}.")
        c.close()

while True:
    client, addr = server.accept()
    print(f"Connection established with {addr}.")
    threading.Thread(target=handle_connection, args=(client,)).start()
