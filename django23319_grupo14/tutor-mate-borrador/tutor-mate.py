# < ^ >  { }  [ ] ' ' [' '] / \
"""
TERMINAL_CHATGPT 
Description: asistente académico en matemáticas nivel escuela secundaria técnica
@author: pabloalustiza
date: 03/2023
version: 1.0.0
"""

# Módulos
import openai
import environ
import sys

env = environ.Env()
environ.Env.read_env()

def main():
    # OpenAI Api_key Config
    openai.api_key = env('CLAVE_OPENAI')

    # Useful Elements
    separador_asteriscos = "*"*60

    # Welcome
    print("")
    print(separador_asteriscos)
    print("MATE.ai")
    print("Asistente de Matemáticas para Adolescentes en Argentina")
    print(separador_asteriscos)
    print("")

    print("new /// Crear nueva conversación")
    print("exit /// Salir del asistente")

    # Sysyem Context
    context = {"role":"system","content":"eres un asistente muy util especializado en matemática para adolescentes. tus respuestas siempre incluyen el paso a paso"}
    messages = [context]

    # Loop User Prompts
    while True:
        print("")
        print(separador_asteriscos)
        content = __prompt()
        print("")

        if content == "new":
            messages = [context]
            print("Nueva conversación iniciada...")
            content = __prompt()
            print("")

        messages.append({"role":"user", "content": content})

        if content == "exit":
            print("🤟 Hasta luego!")
            sys.exit()

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role":"assistant", "content": response_content})

        print("")
        print("Respuesta:")
        print("")
        
        print("💬 ",response_content)

    
def __prompt() -> str:
    prompt = input("¿Sobre qué quieres aprender? 👉")

    return prompt


if __name__ == "__main__":
    main()
