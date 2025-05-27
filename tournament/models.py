from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Player(models.Model):
    # Basic details
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.DateField(default='1990-01-01')  # Set a default date of birth
    is_captain = models.BooleanField(default=False)
    is_vicecaptain = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    # Role
    role_choices = [
        ('Batsman', 'batsman'),
        ('Bowler', 'bowler'),
        ('All Rounder', 'all_Rounder'),
        ('Wicket Keeper', 'wicket_keeper'),
    ]
    role = models.CharField(max_length=20, choices=role_choices, default='batsman') 

    # Batting details
    batting_style_choices = [
        ('Right Hand', 'right_hand'),
        ('Left Hand', 'left_hand'),
    ]
    batting_style = models.CharField(max_length=20, choices=batting_style_choices, default='Right hand')
    match_played = models.IntegerField(default=0)
    highest_score = models.IntegerField(default=0)  # Set a default value for highest score
    total_runs = models.IntegerField(default=0)  # Set a default value for total runs
    balls_faced = models.IntegerField(default=0)
    fifties = models.IntegerField(default=0)  # Set a default value for fifties
    hundreds = models.IntegerField(default=0)  # Set a default value for hundreds
    outs = models.IntegerField(default=0)  # Set a default value for outs
    description = models.TextField(default="Player")

    # Bowling details
    bowling_style_choices = [
        ('Right Arm Fast', 'right_arm_fast'),
        ('Right Arm Medium', 'right_arm_medium'),
        ('Right Arm Off-Spin', 'right_arm_off_spin'),
        ('Left Arm Fast', 'left_arm_fast'),
        ('Left Arm Medium', 'left_arm_medium'),
        ('Left Arm Orthodox Spin', 'left_arm_orthodox_spin'),
    ]
    bowling_style = models.CharField(max_length=30, choices=bowling_style_choices, default='left Arm Medium')
    new_run = models.IntegerField(default=0)
    new_ball_played= models.IntegerField(default=0)
    total_wickets = models.IntegerField(default=0)  # Set a default value for total wickets
    runs_conceded = models.IntegerField(default=0)  # Set a default value for runs conceded
    overs_bowled = models.FloatField(default=0.0) 
    image = models.ImageField(upload_to='player_images/', blank=True, null=True) 

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)  # Or use static if you're not uploading dynamically

    def __str__(self):
        return self.name
      
class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1_matches', null=True)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2_matches', null=True)
    date = models.DateTimeField()
    venue = models.CharField(max_length=200, default='Mulpani Cricket Ground') 

    def is_upcoming(self):
        return self.date > timezone.now()

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.date.date()}"


class Coach(models.Model):

    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default='1980-01-01')  
    experience_years = models.IntegerField(default=0) 
    contact_number = models.CharField(max_length=15, blank=True, null=True) 
    email = models.EmailField(max_length=100, blank=True, null=True)  
    is_head_coach = models.BooleanField(default=False) 
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='coach_images/', blank=True, null=True) 

    role_choices = [
    ('Batting Coach', 'batting_coach'),
    ('Bowling Coach', 'bowling_coach'),
    ('Fielding Coach', 'fielding_coach'),
    ('Fitness Coach', 'fitness_coach'),
    ('Assistant Coach', 'assistant_coach'),
]

    role = models.CharField(max_length=30, choices=role_choices, default='assistant_coach')  
    is_available = models.BooleanField(default=False)    
    def __str__(self):
        return f"{self.name} - {self.role}"



class MatchVote(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voted_team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('match', 'user')  # Ensures one vote per user per match

    def __str__(self):
        return f"{self.user.username} voted for {self.voted_team.name} in match {self.match.id}"
    
    
    
class HeadToHeadRecord(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1_h2h', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_h2h', on_delete=models.CASCADE)
    total_matches = models.PositiveIntegerField(default=0)
    team1_wins = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('team1', 'team2')

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} Record"