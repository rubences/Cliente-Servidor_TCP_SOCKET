import socket  
  
params = ('127.0.0.1', 8809)  
BUFFER_SIZE = 1024 # default  
  
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(params) 
cifras = [4j, 4, 5, -5, 17, 29, 2**50, 2**50-1] 

for cifra in cifras:  
   s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
   s.connect(params)  
   print("Envío de un mensaje %s" % cifra)  
   s.send(('%s\n' % cifra).encode('utf8'))  
   data = s.recv(BUFFER_SIZE)  
   if len(data) == 0:  
       print("\tSin respuesta")  
   elif data == b'E\n':  
       print("\tEl servidor detecta un error ")  
   elif data == b'T\n':  
       print("\tEl número es primo")  
   elif data == b'F\n':  
       print("\tEl número no es primo ")  
   else:  
       print("\tEl dato recibido no se entiende: %s" % data)  
   s.close() 