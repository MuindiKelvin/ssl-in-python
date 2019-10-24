import socket
import ssl
import binascii

s = socket.socket()
port = 443
s.connect(('localhost',port))
print('Connection Established through port 443\n')
print('Hello Server...')
message = 'I am Kelvin Muindi'
s.sendall(message.encode())

while True:
  data = s.recv(1024).decode()
  print('The Client Decrypted the following message')
  print('Received from server:' + data)# Receive Data From Server

  #Encrypting And Decrypting Using RSA Method
  print('\nBelow is the Process of ENCRYPTING AND DECRYPTING SERVER MESSAGE\n')
  hex_data   = binascii.hexlify(data.encode())
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

  message2 = 'Terminated...'

s.close()

