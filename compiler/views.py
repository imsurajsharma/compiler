from django.shortcuts import render,redirect
import subprocess
from shell import shell
from os import system



def index(request):

    if request.method =='POST':
        datas= request.POST['compile']
        user= request.POST['input']
        suser = user.split('\n')
        print(suser)


        with open('input.txt','w+') as file:
            for l in suser:
                file.writelines(l)



        with open('script.py','w') as file:
            file.write(datas)
        # with open('script.py','r+') as file:
        #     data = file.read()
        #     ot = shell("python script.py ")
        #
        #
        #     ott = ot.output()
        system('python script.py < input.txt > out.txt')
        with open('out.txt','r') as file:
            pyout = file.readlines()
            
        return render(request,'index.html',{'dic':pyout})
    else:
        return render(request,'index.html')
