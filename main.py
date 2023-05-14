
import threading
from bot import run_bot
from api import run_api

# Inicia los subprocesos para el bot y el servidor Flask
bot_thread = threading.Thread(target=run_bot)
api_thread = threading.Thread(target=run_api)

# Inicia los subprocesos
bot_thread.start()
api_thread.start()

# Espera a que los subprocesos terminen (opcional)
bot_thread.join()
api_thread.join()
