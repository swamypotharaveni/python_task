from django.shortcuts import render,redirect
from django.contrib import messages
from pyapp.forms import phoneform
from pyapp.models import MyModel,qualification


def phone1(request):
    pho = MyModel.objects.all()
    if request.method=='POST':
        form=phoneform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your course was successfully created!')
            return redirect('ph')
    else:
        form=phoneform()

    return render(request,'ph.html',{'form':form,'pho':pho})
def que(request):
    if request.method == 'POST':
        course=request.POST['course']
        university=request.POST['university']
        year=request.POST['year']
        percentage=request.POST['percentage']
        qu=qualification(course=course,university=university,year=year,percentage=percentage)
        qu.save()
        messages.success(request, f'Your course was successfully created!')
        return redirect('que')
    qualification1=qualification.objects.all()
    return render(request, 'que.html', {'qualification':qualification1})

def delete_course(request, id):
    co = qualification.objects.filter(id=id).get()
    messages.success(request, f'Your course was successfully deleted!')
    co.delete()

    return redirect("que")


