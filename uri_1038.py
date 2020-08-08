x,y = list(map(int, input().split()))

if(x==1):
    print("Total: R$ "+format(y*4.00,'.2f'))
if(x==2):
    print("Total: R$ "+format(y*4.50,'.2f'))
if(x==3):
    print("Total: R$ "+format(y*5.00,'.2f'))
if(x==4):
    print("Total: R$ "+format(y*2.00,'.2f'))
if(x==5):
    print("Total: R$ "+format(y*1.50,'.2f'))
