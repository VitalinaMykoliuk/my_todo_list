from django.contrib import admin
from django.urls import path
from dashboard.views import UserNotesView, UserAddNotesView, UserSaveNotesView, UserLogoutView, NoteDeleteView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'notes'


urlpatterns = [
    path('notes_user/', UserNotesView.as_view(), name='note'),
    path('notes_add/', UserAddNotesView.as_view(), name='add'),
    path('save_note/', UserSaveNotesView.as_view(), name='keep'),
    path('logout_user/', UserLogoutView.as_view(), name='logout'),
    path('notes_delete/', NoteDeleteView.as_view(), name='delete'),

]


