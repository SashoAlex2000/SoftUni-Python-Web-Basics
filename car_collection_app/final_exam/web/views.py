from django.shortcuts import render, redirect

from final_exam.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from final_exam.web.models import Profile, Car


# Create your views here.


def index(request):
    profile_count = Profile.objects.count()

    context = {
        'count': profile_count,
    }

    return render(request,
                  'index.html',
                  context,
                  )


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request,
                  'profile-create.html',
                  context,
                  )


def profile_edit(request):
    current_profile = Profile.objects.all()[0]

    if request.method == 'GET':
        form = ProfileEditForm(instance=current_profile)
    else:
        form = ProfileEditForm(request.POST, instance=current_profile)

        if form.is_valid():
            form.save()

            return redirect('profile details')

    context = {
        'form': form,
        'profile': current_profile,
    }

    return render(
        request,
        'profile-edit.html',
        context,
    )


def profile_delete(request):

    profile = Profile.objects.all()[0]

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'profile-delete.html',
        context,
    )


def profile_details(request):
    profile = Profile.objects.all()[0]
    cars = Car.objects.all()

    total_price = 0

    for car in cars:
        total_price += car.car_price

    context = {
        'profile': profile,
        'total': total_price,
    }

    return render(
        request,
        'profile-details.html',
        context,
    )


def catalogue(request):
    cars = Car.objects.all()
    car_count = len(cars)

    context = {
        'cars': cars,
        'count': car_count,
    }

    return render(request,
                  'catalogue.html',
                  context,
                  )


def car_create(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request,
                  'car-create.html',
                  context,
                  )


def car_details(request, pk):
    current_car = Car.objects.filter(pk=pk).get()

    context = {
        'car': current_car,
    }

    return render(request,
                  'car-details.html',
                  context
                  )


def car_delete(request, pk):
    current_car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarDeleteForm(instance=current_car)
    else:
        form = CarDeleteForm(request.POST, instance=current_car)

        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': current_car,
    }

    return render(
        request,
        'car-delete.html',
        context,
    )


def car_edit(request, pk):
    current_car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarEditForm(instance=current_car)

    else:
        form = CarEditForm(request.POST, instance=current_car)

        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': current_car,
    }

    return render(request,
                  'car-edit.html',
                  context
                  )
