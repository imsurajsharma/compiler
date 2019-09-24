from django.shortcuts import render,redirect
from django.http import JsonResponse
import subprocess
from shell import shell
from os import system


def test(request):
    return render(request,'test.html')


def embed(request):
    return render(request,'embed.html')


def index(request):

    if request.method =='POST':
        datas= request.POST.get('compile')
        print("datas")
        user= request.POST['input']
        print(user)
        suser = user.split('\n')
        print(suser)


        with open('input.txt','w+') as file:
            for l in suser:
                file.write(l + '\n')



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

        return JsonResponse({"data":pyout})
    else:
        return render(request,'index.html')
