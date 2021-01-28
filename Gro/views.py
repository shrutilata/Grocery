from django.shortcuts import render
from .models import list1
from django.http import HttpResponse,JsonResponse


def index(request):
    context={
        'lists' : list1.objects.all()
    }
    return render(request,'Gro/index.html', context)

def add_item(request):
    return render(request,'Gro/add_item.html')

def update_item(request):
    return render(request,'Gro/update_item.html')



def add_submit(request):
    obj=list1()
    obj.iname = request.GET['iname']
    obj.quant = request.GET['quant']
    obj.status = request.GET['status']
    obj.date=request.GET['date']
    obj.save()
    context = {
        "lists" :list1.objects.all()
    }
    print(list1.objects.all())
    return render(request,'Gro/add_item.html',context)

# def edit(request,id):
#     obj = list.objects.get(id=id)
#     context = {
#         "iname" : obj.iname,
#         "quant" : obj.quant,
#         "status" : obj.status,
#         "date" : obj.date,
#         "id" : obj.id
#     }
#     mydictionary = {
#         "title" : obj.title,
#         "description" : obj.description,
#         "priority" : obj.priority,
#         "id" : obj.id
#     }
#     return render(request,'edit.html',context)

# def update(request,id):
#     obj = Todo(id=id)
#     obj.title = request.GET['title']
#     obj.description = request.GET['description']
#     obj.priority = request.GET['priority']
#     import datetime
#     updated_at = datetime.datetime.now()
#     obj.created_at = updated_at
#     obj.save()
#     mydictionary = {
#         "alltodos" : Todo.objects.all()
#     }
#     return render(request,'list.html',context=mydictionary)

# def edit(request,id):
#     obj = Todo.objects.get(id=id)
#     mydictionary = {
#         "title" : obj.title,
#         "description" : obj.description,
#         "priority" : obj.priority,
#         "id" : obj.id
#     }
#     return render(request,'edit.html',context=mydictionary)

def update_submit(request):
        obj=list1.objects.get(iname=request.GET['iname'])
        # obj=list1(id=zname)
        # obj =  list1(iname=request.GET['iname'])
        print(obj)
        # obj.iname=request.GET['iname']
        obj.quant = request.GET['quant']
        obj.status = request.GET['status']
        import datetime
        updated_at = datetime.datetime.now()
        obj.date=updated_at
        obj.save()
        context = {
            "lists" :list1.objects.all()
        }
        return render(request,'Gro/update_item.html',context)