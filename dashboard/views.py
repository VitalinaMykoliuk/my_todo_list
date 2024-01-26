from django.contrib.auth import login
from django.urls import reverse
from django.views import View
from dashboard.forms import AddNoteForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from dashboard.models import Note
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse


class UserNotesView(View):
    template_name = 'dashboard/notes.html'

    def get(self, request):

        return render(request, self.template_name)


class UserAddNotesView(View):
    template_name = 'dashboard/add_note.html'

    def get(self, request, *args, **kwargs):
        form = AddNoteForm()
        return render(request, self.template_name, {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = AddNoteForm(request.POST)
    #     if form.is_valid():
    #         note = form.save(commit=False)
    #         note.user = request.user
    #         note.save()
    #         return HttpResponseRedirect(reverse('notes:note'))
    #     else:
    #         return render(request, 'add_note.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = AddNoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            note = Note.objects.create(title=title, content=content, user=request.user)
            return HttpResponseRedirect(reverse('notes:keep'))
        else:
            return render(request, 'add_note.html', {'form': form})


class UserSaveNotesView(View):
    template_name = 'dashboard/save_notes.html'

    def get(self, request):
        notes = Note.objects.filter(user=request.user)
        return render(request, self.template_name, {'result_notes_get': notes})


class UserLogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('users:log'))


class NoteDeleteView(View):

    def post(self, request):
        note_id = request.POST.get('note_id') #получаем через post запрос при нажатии на кнопку id
        notes = get_object_or_404(Note, id=note_id) #теперь с помощью этого id мы получаем обьект информации в этой модели Note
        user = request.user #получаем текущего юзера
        if notes.user == user: #сравниваем что эта запись пренадлежит этому юзеру
            notes.delete() #если это так тогда удаляем запись

        return HttpResponseRedirect(reverse('notes:keep'))



