import socket
import sys
import ssl
import binascii


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 443
s.bind(('0.0.0.0', port))
print('Connection Established through port 443\n')
s.listen(1)
print('Hello Client.....\n')

while True:
    c, addr = s.accept()
    print('Got connection from:', addr)
    data = (c.recv(1024))
    print('\nReceived From Client:',data)
    
#Encrypting And Decrypting Using RSA Method
    print('\nBelow is the Process of ENCRYPTING AND DECRYPTING CLIENTS MESSAGE\n')
    hex_data   = binascii.hexlify(data)
    print('\n Hex Data:', hex_data)
 
    plain_text = int(hex_data, 16)
    print('\n Plain text integer:', plain_text)

    n = 9516311845790656153499716760847001433441357    # p*q = modulus
    e = 65537
    d = 5617843187844953170308463622230283376298685

    if plain_text > n:
      raise Exception('\nPlain text too large for key')
 
    encrypted_text = pow(plain_text,e, n)
    print('\n Encrypted Text Integer:', encrypted_text)
 
    decrypted_text = pow(encrypted_text, d, n)
    print('\n Decrypted Text Integer:',decrypted_text)
 
    print('\n Message:', binascii.unhexlify(hex(decrypted_text)[2:]).decode())

    message1 = 'Terminate...'
    
    c.send(message1.encode()) #send data to the client    
c.close()

