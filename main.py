from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import random
import asyncio
import dotenv
import os

dotenv.load_dotenv()
api_key = os.getenv("API_KEY")

# Función para manejar el comando /hola
async def hola(update: Update, context: CallbackContext):
    await update.message.reply_text('¡Hola Mundo!')

# Función para manejar el comando /numero
async def numero(update: Update, context: CallbackContext):
    random_number = random.randint(1, 100)  # Número aleatorio entre 1 y 100
    await update.message.reply_text(f'El número aleatorio es: {random_number}')

# Función principal que arranca el bot
def main():
    
    # Crear la instancia de Application (más reciente y asíncrona)
    application = Application.builder().token(api_key).build()
    
    # Agregar manejadores para los comandos /hola y /numero
    application.add_handler(CommandHandler("hola", hola))
    application.add_handler(CommandHandler("numero", numero))
    
    # Iniciar el bot (asíncrono)
    application.run_polling()

# Ejecutar el bot sin asyncio.run en entornos donde el loop ya está corriendo
if __name__ == '__main__':
    # Verificar si asyncio está en ejecución
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except RuntimeError as e:
        if 'This event loop is already running' in str(e):
            asyncio.get_event_loop().create_task(main())  # Si ya está corriendo, lo ejecutamos como tarea
