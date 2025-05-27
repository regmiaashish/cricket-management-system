from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from tournament.middlewares import auth, guest, staff
from tournament.models import Player, Coach, Match, MatchVote, Team, HeadToHeadRecord
from tournament.forms import PlayerForm, CoachForm, MatchForm
from django.http import JsonResponse


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

@auth
def aboutus(request):
    return render(request, "tournament/about/about.html")


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



####################### For the match sections ########################


def upcoming_matches_view(request):
    upcoming_matches = Match.objects.filter(date__gt=timezone.now()).order_by('date')
    return render(request, 'tournament/matches/match.html', {'matches': upcoming_matches})

def add_match(request):
    form = MatchForm()
    if request.method == "POST":
        form = MatchForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("match_centre")
        else:
            return form.errors

    info = {"data": "Form FillUp", "form": form}
    return render(request, "tournament/matches/addmatch.html", info)





def match_centre(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    team1 = match.team1
    team2 = match.team2

    # Vote statistics
    votes = MatchVote.objects.filter(match=match)
    team1_votes = votes.filter(voted_team=team1).count()
    team2_votes = votes.filter(voted_team=team2).count()
    total_votes = team1_votes + team2_votes or 1  # Avoid division by zero

    # Head-to-head record
    h2h, _ = HeadToHeadRecord.objects.get_or_create(team1=team1, team2=team2)
    team1_wins = h2h.team1_wins
    team2_wins = h2h.total_matches - team1_wins
    
    


    context = {
        'match': match,
        'team1': team1,
        'team2': team2,
        'team1_votes': team1_votes,
        'team2_votes': team2_votes,
        'team1_percent': round((team1_votes / total_votes) * 100, 2),
        'team2_percent': round((team2_votes / total_votes) * 100, 2),
        'h2h_labels': [team1.name, team2.name],
        'h2h_data': [team1_wins, team2_wins],
        
    }
    import json


    return render(request, 'tournament/matches/match_centre.html', context)

@auth
def vote_ajax(request, match_id):
    if request.method == "POST":
        team_id = request.POST.get("team_id")
        match = get_object_or_404(Match, id=match_id)

        # Prevent multiple votes
        if MatchVote.objects.filter(match=match, user=request.user).exists():
            return JsonResponse({'error': 'Already voted'}, status=400)

        try:
            team = Team.objects.get(id=team_id)
            MatchVote.objects.create(match=match, user=request.user, voted_team=team)
        except Team.DoesNotExist:
            return JsonResponse({'error': 'Invalid team'}, status=400)

        # Updated vote stats
        votes = MatchVote.objects.filter(match=match)
        team1_votes = votes.filter(voted_team=match.team1).count()
        team2_votes = votes.filter(voted_team=match.team2).count()
        total = team1_votes + team2_votes or 1

        return JsonResponse({
            'team1_percent': round((team1_votes / total) * 100, 2),
            'team2_percent': round((team2_votes / total) * 100, 2),
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
