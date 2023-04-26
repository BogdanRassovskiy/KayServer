import os;
files=os.listdir();
a='''
removed = "0"
'''
b='''
removed = "0"
merchName = "0"
'''
for f in files:
    if "inCar_" in f or "orders_" in f:
        file=open(f,"r");
        data=file.read();
        file.close();
        data=data.replace(a,b);
        file=open(f,"w");
        file.write(data);
        file.close();
print("write complete")
