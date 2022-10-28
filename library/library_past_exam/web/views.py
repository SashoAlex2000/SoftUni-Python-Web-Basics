from django.shortcuts import render, redirect

from library_past_exam.web.forms import ProfileCreateForm, BookAddForm, BookEditForm, ProfileEditForm, ProfileDeleteForm
from library_past_exam.web.models import Profile, Book


# Create your views here.


def index(request):
    # determining whether the user is registered
    profile_exists = Profile.objects.count() == 1

    # if they are registered - show the front page with dashboard and nav-bar
    if profile_exists:

        books = Book.objects.all()
        number_of_books = len(books)

        book_matrix = []

        if number_of_books > 3:
            counter = 0
            curr = []
            for book in books:
                counter += 1
                curr.append(book)
                if counter == 3:
                    counter = 0
                    book_matrix.append(curr)
                    curr = []
            if curr:
                book_matrix.append(curr)

        else:
            curr = [x for x in books]
            book_matrix.append(curr)

        print(book_matrix)
        context = {
            'books': book_matrix,
            'count': number_of_books,

        }

        return render(request,
                      'home-with-profile.html',
                      context)

    # if they are not registered -> show the register form
    else:

        if request.method == 'GET':
            form = ProfileCreateForm()
        else:
            form = ProfileCreateForm(request.POST)

            if form.is_valid():
                form.save()

                return redirect('index')

        context = {
            'form': form,
        }

        return render(request,
                      'home-no-profile.html',
                      context)


def add_book(request):
    if request.method == 'GET':
        form = BookAddForm()
    else:
        form = BookAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request,
                  'book/add-book.html',
                  context)


def edit_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'book': book,
    }

    return render(request,
                  'book/edit-book.html',
                  context
                  )


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).all()
    book.delete()

    return redirect('index')


def details_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    context = {
        'book': book,
    }

    return render(request,
                  'book/book-details.html',
                  context)


def profile_page(request):
    profile = Profile.objects.all()[0]
    name = f'{profile.first_name} {profile.last_name}'

    context = {
        'profile': profile,
        'name': name,
    }

    return render(request,
                  'profile/profile.html',
                  context
                  )


def profile_edit(request):
    profile = Profile.objects.all()[0]

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)

    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form,
    }

    return render(request,
                  'profile/edit-profile.html',
                  context
                  )


def profile_delete(request):
    profile = Profile.objects.all()[0]

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            Book.objects.all().delete()
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)
