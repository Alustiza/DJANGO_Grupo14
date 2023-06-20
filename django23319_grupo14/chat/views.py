from django.shortcuts import render
import openai
import os
import datetime
from django.contrib.sessions.backends.db import SessionStore
from dotenv import load_dotenv

load_dotenv()

# Create your views here.

api_key = os.getenv("OPENAI_KEY", None)
openai.api_key = api_key


def chatbot(request):
    # Hora del mensaje
    current_time = datetime.datetime.now()  # Obtiene la fecha y hora actual

    # Obtiene la variable de sesión o crea una nueva si no existe
    session = SessionStore(session_key=request.session.session_key)

    # Obtiene la respuesta anterior de OpenAI de la variable de sesión
    previous_response = session.get("chatbot_response")

    # System Context
    context = {
        "role": "system",
        "content": "eres un asistente muy útil especializado en matemáticas para adolescentes. Tus respuestas siempre incluyen el paso a paso. Siempre arrancas diciendo Respuesta: "
    }
    chatbot_response = None
    user_input = previous_response

    if api_key is not None and request.method == "POST":
        user_input = request.POST.get("user_input")
        prompt = f"{context['content']}{user_input}"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=256,
            temperature=0.5
        )

        chatbot_response = response["choices"][0]["text"]

        # Guarda la respuesta actual en la variable de sesión
        session["chatbot_response"] = chatbot_response
        session.save()

    return render(request, "chat/main.html", {"timestamp": current_time, "question": user_input, "response": chatbot_response})
