from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

# Create your views here.

api_key = os.getenv("OPENAI_KEY", None)
openai.api_key = api_key

def chatbot(request):
    chatbot_response = None
    if api_key is not None and request.method == "POST":
        user_input = request.POST.get("user_input")
        #prompt = user_input
        #prompt = f"eres un asistente muy util especializado en matemática para adolescentes. tus respuestas siempre incluyen el paso a paso."
        prompt = f"eres un asistente muy util especializado en matemática. tus respuestas siempre incluyen el paso a paso: {user_input}"
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = prompt, 
            max_tokens=256,
            #stop = "."
            temperature=0.5
        )
    
        print(response)
        chatbot_response = response["choices"][0]["text"]

    return render(request, "chat/main.html", {"response": chatbot_response})