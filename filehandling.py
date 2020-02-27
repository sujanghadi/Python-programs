test=open("test.txt",'r')
test2=open("test2.txt",'w')
a=(test.read())
lis=list(a.split('\n'))
print(lis)
lis = [x.strip('"') for x in lis]
while ('' in lis):
    lis.remove('')
print(lis)

def convert24(str1): 
    if str1[:2] == "12": 
        return "00" + str1[2:] +' PM'    
    else: 
        return str('%02d' % (int(str1[0:2]) - 12)) + str1[2:] +' PM'

for i in range(len(lis)):
    a1= (lis[i]) 
    print(convert24(a1))     
    x=(convert24(a1))
    test2.write(x+"\n")