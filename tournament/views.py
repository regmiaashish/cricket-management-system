from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from tournament.middlewares import auth, guest, staff
from tournament.models import Player, Coach
from tournament.forms import PlayerForm, CoachForm


# Create your views here.
@guest
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("homepage")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "tournament/register.html", {"form": form})
    else:
        initial_data = {"username": "", "password1": "", "password2": ""}
        form = UserCreationForm(initial=initial_data)
    return render(request, "tournament/register.html", {"form": form})


@guest
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("homepage")
        else:

            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, "tournament/login.html", {"form": form})


@auth
def homepage(request):
    return render(request, "tournament/base.html")


def logout_view(request):
    logout(request)
    return redirect("login")


# To test the extends for the base.html
def newview(request):
    return render(request, "tournament/testview.html")


# to list the players
@auth
def playerlist(request):
    content = {"data": Player.objects.all}
    return render(request, "tournament/playerlist.html", content)


@auth
def manage_player(request):
    content = {"data": Player.objects.all}
    return render(request, "tournament/manageplayer.html", content)


# View  individual player in  details
@auth
def view_player(request, id):
    reader = Player.objects.get(id=id)
    if reader.balls_faced > 0:
        strike_rate = round((100 * reader.total_runs) / reader.balls_faced, 2)
    else:
        strike_rate = 0

    if reader.outs > 0:
        average = round(reader.total_runs / reader.outs, 2)
    else:
        average = 0

    if reader.overs_bowled > 0:
        economy = round(reader.runs_conceded / reader.overs_bowled, 2)
    else:
        economy = 0

    if reader.new_run > 0 or reader.new_ball_played > 0:
        reader.match_played += 1

    if reader.new_run > 49 and reader.new_run < 100:
        reader.fifties += 1

    if reader.new_run > 100:
        reader.hundreds += 1

    reader.total_runs += reader.new_run

    if reader.new_run > reader.highest_score:
        reader.highest_score = reader.new_run

    if reader.new_ball_played > 0:
        reader.balls_faced += reader.new_ball_played

    reader.new_run = 0
    reader.new_ball_played = 0
    reader.save()

    context = {
        "data": reader,
        "strike_rate": strike_rate,
        "average": average,
        "economy": economy,
    }
    return render(request, "tournament/eachplayer.html", context)


@auth
@staff
def add_player(request):
    form = PlayerForm()
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("playerlist")
        else:
            return form.errors

    info = {"data": "Form FillUp", "form": form}
    return render(request, "tournament/createplayer.html", info)


@auth
@staff
def edit_player(request, id):
    player = Player.objects.get(id=id)
    form = PlayerForm(instance=player)
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES or None, instance=player)
        if form.is_valid():
            form.save()
            return redirect("manageplayer")
        else:
            return form.errors

    context = {"data": player, "form": form}
    return render(request, "tournament/edit_player.html", context)


def delete_player(request, id):
    Player.objects.get(id=id).delete()
    return redirect("manageplayer")


# For the gallery
@auth
def gallery1(request):
    return render(request, "tournament/gallery/gallery.html")


@auth
def gallery2(request):
    return render(request, "tournament/gallery/gallery1.html")


# For the Coach
@auth
def coachview(request):
    data = Coach.objects.all()
    content = {"data": data}
    return render(request, "tournament/coach/managecoach.html", content)


@auth
def coachlist(request):
    content = {"data": Coach.objects.all}
    return render(request, "tournament/coach/coachlist.html", content)


@auth
@staff
def add_coach(request):
    form = CoachForm()
    if request.method == "POST":
        form = CoachForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("coachlist")
        else:
            return form.errors

    info = {"data": "Form FillUp", "form": form}
    return render(request, "tournament/coach/createcoach.html", info)


@auth
@staff
def edit_coach(request, id):
    player = Coach.objects.get(id=id)
    form = CoachForm(instance=player)
    if request.method == "POST":
        form = CoachForm(request.POST, request.FILES or None, instance=player)
        if form.is_valid():
            form.save()
            return redirect("coachlist")
        else:
            return form.errors

    context = {"data": player, "form": form}
    return render(request, "tournament/coach/edit_coach.html", context)


def delete_coach(request, id):
    Coach.objects.get(id=id).delete()
    return redirect("coachlist")


@auth
def view_coach(request, id):
    reader = Coach.objects.get(id=id)
    context = {
        "data": reader,
    }
    return render(request, "tournament/coach/eachcoach.html", context)


# for contact US
@auth
def reachus(request):
    return render(request, "tournament/contact.html")
