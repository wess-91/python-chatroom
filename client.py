import socket
import threading
import rsa

public_key, private_key = rsa.newkeys(1024)
public_partner = None

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",9990))

public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
client.send(public_key.save_pkcs1("PEM"))

def sending_messages(c):
    while True:
        message = input("")
        c.send(rsa.encrypt(message.encode(), public_partner ))
        print("You : " + message)

def receiving_messages(c):
    while True:
        print(rsa.decrypt(c.recv(1024), private_key).decode())


#Authentification Process
username_msg = client.recv(1024).decode()
username = input(username_msg)
client.send(username.encode())

password_msg = client.recv(1024).decode()
password = input(password_msg)
encrypted_password = rsa.encrypt(password.encode(), public_partner)
client.send(encrypted_password)

otp_msg = client.recv(1024).decode()
input_otp_code = input(otp_msg)
client.send(input_otp_code.encode())

login_response = client.recv(1024).decode()
print(login_response)

if "successful" in login_response:
    threading.Thread(target=sending_messages, args=(client,)).start()
    threading.Thread(target=receiving_messages, args=(client,)).start()
else : 
    print("Authentification failed. Closing connection.")
    client.close()
