import rpyc
import sys
import time

start = time.time()       

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))
server = sys.argv[1]
n = int(sys.argv[2])

array = []
for i in range(0, n):
    array.append(i)

conn = rpyc.connect(server, 18866)
print(array)
print(conn.root.soma(array))

end = time.time()
print(end-start)