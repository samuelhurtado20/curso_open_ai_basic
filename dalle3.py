import openai

# Configuración del cliente de OpenAI
openai.api_key = 'tu_clave_api'

response = openai.Image.create(
    model="dall-e-3",           # Especifica el modelo
    prompt="un atardecer en la ciudad",
    quality="standard",         # O "hd" para mayor resolución
    n=1                         # Número de imágenes a generar
)

# Extrae la URL de la primera imagen generada
image_url = response['data'][0]['url']
print(image_url)
