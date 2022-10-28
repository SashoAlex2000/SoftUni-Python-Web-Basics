from django.shortcuts import render, redirect

from games_play_app.web.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from games_play_app.web.models import Profile, Game


# Create your views here.

def get_average_rating():
    total_score = 0
    games = Game.objects.all()
    game_count = Game.objects.count()

    if game_count == 0:
        return 0

    for game in games:
        total_score += game.rating

    result = total_score / game_count
    return result


def index(request):
    has_user_registered = Profile.objects.count() == 1

    context = {
        'registration': has_user_registered,
    }

    return render(request, 'home-page.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.all()[0]
    games_count = Game.objects.count()
    average_rating = get_average_rating()

    context = {
        'profile': profile,
        'count': games_count,
        'average': average_rating,
    }

    return render(request,
                  'profile/details-profile.html',
                  context)


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
                  context)


def profile_delete(request):
    profile = Profile.objects.all()[0]

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)


def game_create(request):
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request,
                  'game/create-game.html',
                  context)


def game_details(request, pk):
    game = Game.objects.filter(pk=pk).get()

    context = {
        'game': game,
    }
    print(game.game_title)
    return render(request, 'game/details-game.html', context)


def game_edit(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'game/edit-game.html', context)


def game_delete(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save(commit=True)
            print(f'Deleting {game.game_title}')
            return redirect('index')

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'game/delete-game.html', context)


def dashboard(request):
    games = Game.objects.all()
    game_count = len(games)

    context = {
        'games': games,
        'count': game_count,
    }
    # print(games)
    # print(game_count)
    return render(request,
                  'dashboard.html',
                  context
                  )
