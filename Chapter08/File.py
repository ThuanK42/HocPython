''' Bai nay chi don gian la doc File theo cach cua Pyython '''

# open('duong dan den file','che do') trong do che do gom read (r),write(w)
#fp.close: dong file

fp = open("data/list.txt", "r")
for line in fp:
    print(line, end="")
fp.close()

#fp.write("chuoi can ghi vao"): ghi file
fp2=open("data/writeFile.txt","w")
fp2.write("1")
fp2.write("\n")
fp2.write("2")
fp2.write("\n")
fp2.write("3")
fp2.write("\n")
fp2.write("4")
fp2.write("\n")
fp2.write("5")
fp2.write("\n")
fp2.write("6")
fp2.write("\n")
fp2.write("7")
fp2.write("\n")
fp2.write("8")
fp2.write("\n")
fp2.write("9")
print("Done")

''' copy file '''
fp3=open("data/copyFile.txt","r")
fp4=open("data/toFile.txt","w")
for line in fp3:
    print(line,file=fp4,end="")
print("done 2")


