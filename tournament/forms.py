from django import forms
from tournament.models import Player, Coach, Match

class PlayerForm(forms.ModelForm):
  class Meta:
    model=Player
    fields='__all__'



class CoachForm(forms.ModelForm):
  class Meta:
    model=Coach
    fields='__all__'
    
    
class MatchForm(forms.ModelForm):
  class Meta:
    model = Match
    fields = '__all__'
    
