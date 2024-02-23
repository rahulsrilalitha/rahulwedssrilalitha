from django.shortcuts import render, redirect
from .models import Engagement
from .forms import EngagementForm
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from django.http import HttpResponse


# Create your views here.

def invitation(request):
    # if request.method == "POST":
    #    print(request.POST.get('name'))
    #    return redirect('send_invite')
    images = Engagement.objects.all()
    context = {
        'engageTime': 'HH:MM',
        'engageDayDate': 'Day, Date',
        'engageMonthYear': 'Month, Year',
        'engagelocation': 'Convention Hall, Street, City, State, Country. Pincode. ',

        'marriageTime': 'HH:MM',
        'marriageDayDate': 'Day, Date',
        'marriageMonthYear': 'Month, Year',
        'marriagelocation': 'Convention Hall, Street, City, State, Country. Pincode. ',

        'receptionFromTime': 'HH:MM',
        'receptionToTime': 'HH:MM',
        'receptionDayDate': 'Day, Date',
        'receptionMonthYear': 'Month, Year',
        'receptionlocation': 'Convention Hall, Street, City, State, Country. Pincode. ',
        'images' : images,

    }
    return render(request, 'index.html', context)





def engagementpics(request):
    images = Engagement.objects.all()
    paginator = Paginator(images, 9)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'engageTime': 'HH:MM',
        'engageDayDate': 'Day, Date',
        'engageMonthYear': 'Month, Year',
        'engagelocation': 'Convention Hall, Street, City, State, Country. Pincode. ',
        'page': page,

    }
    return render(request, 'engagementpics.html', context)

def engagementpics_upload(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = EngagementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'gallery/engagementpics_upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = EngagementForm()
        return render(request, 'gallery/engagementpics_upload.html', {'form': form})


