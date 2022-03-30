import socket  
import isprime 
  
params = ('127.0.0.1', 8809)  
BUFFER_SIZE = 1024 # default  
  
datos = {}  
  
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Internet, TCP  
s.bind(params)  
s.listen(1) 

conn, addr = s.accept()  
print('Conexión aceptada: %s' % str(addr))  
  
while True:  
       data = conn.recv(BUFFER_SIZE)  
       if not data:  
           break  
       print('Dato recibido: %s' % data)  
       try: number = int(data)  
       except:  
           response = b'E'  
           Frase = "'%s' no es un entero" % data  
       else:  
           if isprime(number):  
               Frase = "'%s' es un número primo" % number  
               response = b'T'  
           else:  
               Frase = "'%s' no es un número primo" % number  
               response = b'F'  
       finally:   
           print(response)  
           conn.send(response)  
conn.close() 


