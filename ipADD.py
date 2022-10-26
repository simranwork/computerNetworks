
import string

ipADD = str(input('Enter IP address:\n'))
cl = 0                                     #initializing class
for i in range (5):
    a = 'ABCDE'
    if ipADD[i] =='0':
        cl = i+1
        print(f'class {a[i]}')
        break

ip = ''
for i in range(4):
    octet = ipADD[8*i:8*(i+1)]
    sumI = 0
    for i in range(8):
        sumI = sumI + int(octet[7-i])*(2**i)
    ip = ip + str(sumI)+ '.'
ip = ip[:-1]
if cl<4:
    ip = ip + '/' + str((cl) *8)
print (ip)