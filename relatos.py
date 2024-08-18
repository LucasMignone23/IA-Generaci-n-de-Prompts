# Instalar las bibliotecas necesarias si es necesario
!pip install google-generativeai
!pip install openai==0.28

# Configurar las API keys para Gemini y OpenAI
import os
os.environ["GEMINI_API_KEY"] = ""
os.environ["OPENAI_API_KEY"] = ""

# Importar las bibliotecas necesarias
import google.generativeai as genai
import openai

# Configurar la API key en el entorno de Google Generative AI
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Configuración del modelo de generación de texto
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="Generar un micro relato de no más de 100 palabras.",
)

# Función para generar relatos
def generar_relatos_gemini(personajes, descripcion, genero):
    prompt = f"Escribe una breve historia {genero} con los personajes: {personajes}. Descripción: {descripcion}"

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [prompt],
            }
        ]
    )

    response = chat_session.send_message(prompt)
    return response.text.strip(), prompt

# Función para generar imágenes a partir de un prompt
def generar_imagen_desde_prompt(prompt_imagen):
    try:
        response = openai.Image.create(
            prompt=prompt_imagen,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    except openai.error.InvalidRequestError as e:
        print(f"Error en la solicitud: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

# Interacción con el usuario
personajes = input("Introduce los personajes: ")
descripcion = input("Introduce una breve descripción de la historia: ")
genero = input("Introduce el género de la historia: ")

# Generar el relato y el prompt utilizado
relato, prompt = generar_relatos_gemini(personajes, descripcion, genero)

# Mostrar el relato generado
print("\nRelato generado:\n")
print(relato)

# Generar la imagen basada en el prompt del relato
imagen_url = generar_imagen_desde_prompt(prompt)

# Mostrar la URL de la imagen generada
print("\nImagen generada:\n")
print(imagen_url)
