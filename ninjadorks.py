from dotenv import load_dotenv, set_key
import os
from search import GoogleSearch
import argparse
import sys

def banner():
    print("""  
 _   _  _       _       _____             _        
 | \ | (_)     (_)     |  __ \           | |       
 |  \| |_ _ __  _  __ _| |  | | ___  _ __| | _____ 
 | . ` | | '_ \| |/ _` | |  | |/ _ \| '__| |/ / __|
 | |\  | | | | | | (_| | |__| | (_) | |  |   <\__ \\
 |_| \_|_|_| |_| |\__,_|_____/ \___/|_|  |_|\_\___/
              _/ |                                 
             |__/                                  
""")


def env_config():
    """Configura el archivo .env con los valores proporcionados."""
    api_key=input("Introduce tu API_KEY de Google: ")
    engine_id = input("Introduce el ID del buscador personalizado de Google: ")
    set_key(".env","API_KEY_GOOGLE",api_key)
    set_key(".env","SEARCH_ENGINE_ID",engine_id)
    print("Archivo .env configurado satisfactoriamente.")


def main(query,configure_env=None,start_page=1,pages=1,lang="lang_es"):
    """Realiza una búsqueda en Google utilizando una API KEY y un SEARCH ENGINE ID almacenados en un archivo .env.
    
    Args:
        query (str): Consulta de búsqueda que se realizará en Google.
        configure_env (bool, optional): Si es True, se solicita configurar el .env. Defaults to None.
        start_page (int, optional): Página inicial de los resultados de búsqueda. Defaults to 1.
        pages (int, optional): Número de páginas de resultados a retornar. Defaults to 1.
        lang (str, optional): Código de idioma para los resultados de búsqueda. Defaults to 'lang_es'."""
    

    if configure_env or not os.path.exists(".env"):
       env_config()
       sys.exit(1)
    
    
    # Cargar las variables de entorno desde el archivo .env para garantizar la seguridad y configurabilidad.
    load_dotenv()


    # Obtener las claves de configuración desde las variables de entorno.
    API_KEY = os.getenv("API_KEY_GOOGLE")
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

    if not API_KEY or not SEARCH_ENGINE_ID:
        print("Error: Falta la API_KEY o el SEARCH_ENGINE_ID: Por favor ejecula la opción --configure para configurar el archivo .env")
        sys.exit(1)


    if not query:
        print("Indica una consulta con el comando -q. Utiliza el comando -h para mostrar la ayuda")
        sys.exit(1)

    gsearch = GoogleSearch(API_KEY,SEARCH_ENGINE_ID)
    resultados = gsearch.search(query,pages=pages,start_page=start_page,lang=lang)
    print(resultados)

if __name__ == "__main__":
    banner()
    #Configuracion de los  argumentos del programa
    parser = argparse.ArgumentParser(description="Esta herramienta permite realizar Hacking con buscadores de manera automática")
    parser.add_argument("-q","--query", type=str, help="Especifica el dork que desea buscar.\nEjemplo: -q 'filetype:sql \"MySQL dump\"(pass|password|passwd|pwd)'")
    parser.add_argument("-c","--configure",action="store_true",help="Incia el proceso de configuracion del archivo .env \nUtiliza esta opcion sin otros argumentos para configurar las claves.")
    parser.add_argument("--start-page",type=int,default=1,help="Define la pagina de incio del buscador para obtener los resultados")
    parser.add_argument("--pages",type=int,default=1, help="Numero de paginas de resultados de busqueda")
    parser.add_argument("--lang",type=str,default="lang_es",help="Codigo de idioma para los resultados de busqueda. Por defecto es 'lang_es' (español)")
    args = parser.parse_args()
    
    main(query=args.query,
         configure_env=args.configure,
         pages=args.pages,
         start_page=args.start_page,
         lang=args.lang)