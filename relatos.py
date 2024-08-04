# Instalar la biblioteca necesaria
!pip install google-generativeai

# Configurar la API key directamente
import os
os.environ["GEMINI_API_KEY"] = "AIzaSyAdo0sYdDurZo-kD5njvhbE8a1IkaLegxU"

# Importar las bibliotecas necesarias
import google.generativeai as genai

# Configurar la API key en el entorno de Google Generative AI
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Configuración del modelo
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
    return response.text.strip()

# Interacción con el usuario
personajes = input("Introduce los personajes: ")
descripcion = input("Introduce una breve descripción de la historia: ")
genero = input("Introduce el género de la historia: ")

# Generar y mostrar el relato
relato = generar_relatos_gemini(personajes, descripcion, genero)
print("\nRelato generado:\n")
print(relato)
