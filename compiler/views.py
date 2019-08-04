from django.shortcuts import render,redirect
import subprocess
from shell import shell


def index(request):

    if request.method =='POST':
        datas= request.POST['compile']
        user= request.POST['input']
        input_list= list()


        with open('input.txt','w') as file:
            file.write(user)
        with open('input.txt','r') as file:

            for line in file.readlines():
                input_list.append(line)
        print(input_list)

        with open('script.py','w') as file:
            file.write(datas)
        with open('script.py','r+') as file:
            data = file.read()
            ot = shell("python script.py "+'> out.txt',has_input=True)
            ot.write(input_list[0])

            ott = ot.output()

        with open('out.txt','r') as file:
            o=file.read()
        return render(request,'index.html',{'dic':ott})
    else:
        return render(request,'index.html')
