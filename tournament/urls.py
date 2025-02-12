from django.urls import path
from tournament.views import register_view, logout_view, login_view, newview, playerlist, add_player, view_player, edit_player, manage_player,delete_player, coachview, coachlist, gallery1, gallery2, add_coach, edit_coach, delete_coach, view_coach, reachus, aboutus, match

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('test/', newview, name='testview'),
    #For Gallery
    path('gallery/', gallery1, name='gallery'),
    path('gallery2/', gallery2, name='gallery1'),
    
    
    #Crud for the players
     path('player/', playerlist, name='playerlist'),
     path("player/manage/", manage_player, name="manageplayer"),
     path('player/add/', add_player, name='add_player'), #C
     path('player/view/<id>', view_player, name='view_player'), #R
     path("player/edit/<id>", edit_player, name="editplayer"), #U
     path("player/delete/<id>", delete_player, name="deleteplayer"), #D
     
     #for inquiry and contact
     path('contact/', reachus, name='contact'),
     
     #For about us
     path('aboutus/', aboutus, name='about'),
     

     #crud for coach   
     path('coach/', coachview, name='coachlist'),
     path('coachview/', coachlist, name='coach'),
     path('coach/add/', add_coach, name='add_coach'),#C
     path('coach/view/<id>', view_coach, name='view_coach'),#R
     path('coach/edit/<id>', edit_coach, name='edit_coach'),#U
     path('coach/delete/<id>', delete_coach, name='delete_coach'),#D
     
     ## for match
     path('matches/', match, name='viewmatch')
]