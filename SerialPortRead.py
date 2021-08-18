import serial
import time
import os


# Comfuguracao da porta Serial

s = serial.Serial()
s.port = 'COM4'          # Porta serial que sera utilizada.
s.baudrate = 115200
s.bytesize = 8
s.parity = 'N'
s.stopbits = 1
s.write_timeout = 1000
s.open()

print ("Start Reading...:")
dados_serial = s.readline()
print (dados_serial)

arquivo = open('dados.txt','w')
print ("dados salvos em arquivo...:")



