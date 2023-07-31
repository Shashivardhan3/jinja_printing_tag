from django.shortcuts import render

# Create your views here.


def data_render(request):
    d={'name':'shashi','age':24}
    return render(request,'data_render.html',context=d)

def conditions(request):
    d={'a':24,'b':56,'c':148}
    return render (request,'conditions.html',context=d)


def for_loop(request):

    d={'name':'shashi','age':24,'hobbies':['cricket','football','hockey']}
    return render (request,'for_loop.html',context=d)

