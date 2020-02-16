''' dung buffer de doc ghi file nhanh nhu java'''

BUFFERSIZE=100
rFile=open("data/writeFile.txt","r")
wFile=open("data/toFile.txt","w")

buffer=rFile.read(BUFFERSIZE)

i=0
while len(buffer):
    i = i+1
    wFile.write(buffer)
    print(i,"{} byte".format(len(buffer)))
    buffer=rFile.read(BUFFERSIZE)
print("Done")