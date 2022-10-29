from django.shortcuts import render, redirect

from notes_app_third.web.forms import ProfileRegisterForm, NoteAddForm, NoteEditForm, NoteDeleteForm
from notes_app_third.web.models import Profile, Note


# Create your views here.


def index(request):
    is_there_a_profile = len(Profile.objects.all()) == 1

    if not is_there_a_profile:

        if request.method == 'GET':
            form = ProfileRegisterForm()
        else:
            form = ProfileRegisterForm(request.POST)

            if form.is_valid():
                form.save()

                return redirect('index')

        context = {
            'form': form,
        }

        return render(request,
                      'home-no-profile.html',
                      context,
                      )
    else:

        notes = Note.objects.all()
        note_count = len(notes)

        context = {
            'notes': notes,
            'count': note_count,
        }

        return render(request,
                      'home-with-profile.html',
                      context
                      )


def add_note(request):
    if request.method == 'GET':
        form = NoteAddForm()
    else:
        form = NoteAddForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form,
    }

    return render(request,
                  'note-create.html',
                  context,
                  )


def edit_note(request, pk):
    current_note = Note.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = NoteEditForm(instance=current_note)
    else:
        form = NoteEditForm(request.POST, instance=current_note)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form,
        'note': current_note,
    }

    return render(
        request,
        'note-edit.html',
        context,
    )


def delete_note(request, pk):
    current_note = Note.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = NoteDeleteForm(instance=current_note)
    else:
        form = NoteDeleteForm(request.POST, instance=current_note)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form,
        'note': current_note,
    }

    return render(request,
                  'note-delete.html',
                  context,
                  )


def details_note(request, pk):
    current_note = Note.objects.filter(pk=pk).get()

    context = {
        'note': current_note,
    }

    return render(request,
                  'note-details.html',
                  context
                  )


def profile(request):
    try:
        profile = Profile.objects.all()[0]
    except:
        return redirect('index')

    notes_count = Note.objects.count()



    context = {
        'profile': profile,
        'count': notes_count,
    }

    return render(request,
                  'profile.html',
                  context,
                  )


def delete_profile(request):

    # if request.method == 'GET':
    #     return redirect('index')

    def delete_all():
        Note.objects.all().delete()
        Profile.objects.all().delete()

    delete_all()

    return redirect('index')

