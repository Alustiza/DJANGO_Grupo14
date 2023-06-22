from django.shortcuts import render, redirect
import os

from django.contrib import auth
from django.contrib.auth.models import User
from chatbot.models import Chat, Perfil
from chatbot.forms import ProfileForm

from django.utils import timezone

from django.http import JsonResponse

import openai
from dotenv import load_dotenv
load_dotenv()

from django.contrib.auth.decorators import login_required



api_key = os.getenv("OPENAI_KEY", None)
openai.api_key = api_key


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Datos incorrectos. Intente de nuevo'
            return render(request, 'chatbot/login.html', {'error_message': error_message})
    else:
        return render(request, 'chatbot/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Ocurrió un error al crear la cuenta'
                return render(request, 'chatbot/register.html', {'error_message': error_message})
        else:
            error_message = 'Las contraseñas no coinciden'
            return render(request, 'chatbot/register.html', {'error_message': error_message})
    return render(request, 'chatbot/register.html')




def profile(request):

     if(request.method=='POST'):
        profile_form = Perfil.objects.filter(user=request.user)
        #profile_form = ProfileForm(request.POST)
     else:
        profile_form = ProfileForm()

     context = {'profile_form': profile_form}

     return render(request, 'chatbot/profile.html',context)


def logout(request):
     auth.logout(request)
     return redirect('login')
    #  return render(request, "chatbot/logout.html")




# def ask_openai(message):
#     reponse = openai.Completion.create(
#             model = "text-davinci-003",
#             prompt = message,
#             max_tokens = 150,
#             n=1,
#             stop=None,
#             temperature=0.7,
#       )
#     print(reponse)
#     answer = reponse.choices[0].text.strip()
#     return answer

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "eres un asistente muy útil que solamente responde preguntas de matemática. las respuestas siempre incluyen el paso a paso y en un tono coloquial para adolescentes"},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer

@login_required
def chatbot(request):
    
    # chats = Chat.objects.filter(user=request.user).order_by('-created_at')[:2]
    # chats = Chat.objects.filter(user=request.user).order_by('-created_at')
    chats = Chat.objects.filter(user=request.user)
    
    if request.method=='POST':
            message = request.POST.get('message')
            response = ask_openai(message)

            chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
            chat.save()


            return JsonResponse({'message': message, 'response':response})
    
 
    
    return render(request,"chatbot/chatbot.html", {'chats': chats})

