import os;
a="session=request.GET['session'];";
session=request.GET['session'];
if request.method=='POST':session=request.POST['session'];


file=open('views.py','r');
data=file.read();
file.close();
data=data.replace(a,b);
file=open('views.py','w');
file.write(data);
file.close();
