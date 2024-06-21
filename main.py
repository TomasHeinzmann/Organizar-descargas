from os import scandir
from shutil import move
from time import sleep

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

direccionDescargas = r"C:\Users\Juli\Downloads"


extensiones_imagenes = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico', '.eps']
extensiones_videos = ['.mp4', '.avi', '.mov', '.wmv', '.mkv', '.flv', '.webm', '.mpeg', '.3gp', '.rm']
extensiones_documentos = ['.txt', '.doc', '.docx', '.pdf', '.rtf', '.odt', '.tex', '.wpd', '.md', '.html']
extensiones_audio = ['.mp3', '.wav', '.aac', '.wma', '.ogg', '.flac', '.m4a', '.aiff', '.mid', '.amr']
extensiones_comprimidos = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.z', '.tgz', '.pkg']
extensiones_ejecutables = ['.exe', '.msi', '.app', '.bat', '.sh', '.jar', '.deb', '.dmg', '.apk', '.rpm']
extensiones_codigo = ['.py', '.cpp', '.c', '.java', '.js', '.html', '.css', '.php', '.rb', '.swift']
extensiones_bases_datos = ['.db', '.sql', '.mdb', '.accdb', '.sqlite', '.dbf', '.csv', '.dat', '.xml', '.json']

direccionImagenes = r'C:\Users\Juli\Desktop\Imagenes'
direccionVideos = r'C:\\Users\\Juli\\Desktop\\Videos'
direccionDocumentos = r'C:\Users\Juli\Desktop\Documentos'
direccionAudios = r'C:\Users\Juli\Desktop\Audios'
direccionComprimidos = r'C:\Users\Juli\Desktop\Comprimidos'
direccionEjecutables = r'C:\Users\Juli\Desktop\Ejecutables'
direccionCodigos = r'C:\Users\Juli\Desktop\Codigos'
direccionBasesdedatos = r'C:\Users\Juli\Desktop\Basesdedatos'
direccionVarios = r'C:\Users\Juli\Desktop\Varios'


class CambiaDirecciones(FileSystemEventHandler):
    def on_modified(self, evento):
        with scandir(direccionDescargas) as archivos:
            for archivo in archivos:
                nombre = archivo.name
                self.checkearImagen(archivo, nombre)
                self.checkearVideo(archivo, nombre)
                self.checkearDocumento(archivo, nombre)
                self.checkearAudio(archivo, nombre)
                self.checkearComprimido(archivo, nombre)
                self.checkearEjecutables(archivo, nombre)
                self.checkearCodigo(archivo, nombre)
                self.checkearBaseDeDatos(archivo, nombre)

    def checkearImagen(self, archivo, nombre):
        for extencion in extensiones_imagenes:
            if nombre.endswith(extencion) or nombre.endswith(extencion.upper()):
                move(archivo, direccionImagenes)
                logging.info(f"Moviendo imagen a {direccionImagenes}")

    def checkearVideo(self, archivo, nombre):
        for extencion in extensiones_videos:
            if nombre.endswith(extencion) or nombre.endswith(extencion.upper()):
                move(archivo, direccionVideos)
                logging.info(f"Moviendo video a {direccionVideos}")

    def checkearDocumento(self, archivo, nombre):
        for extencion in extensiones_documentos:
            if nombre.endswith(extencion) or nombre.endswith(extencion.upper()):
                move(archivo, direccionDocumentos)
                logging.info(f"Moviendo documento a {direccionDocumentos}")

    def checkearAudio(self, archivo, nombre):
        for extencion in extensiones_audio:
            if nombre.endswith(extencion) or nombre.endswith(extencion.upper()):
                move(archivo, direccionAudios)
                logging.info(f"Moviendo audio a {direccionAudios}")

    def checkearComprimido(self, archivo, nombre):
        for extencion in extensiones_comprimidos:
            if nombre.endswith(extencion) or nombre.endswith(extencion.upper()):
                move(archivo, direccionComprimidos)
                logging.info(f"Moviendo audio a {direccionComprimidos}")

    def checkearEjecutables(self, archivo, nombre):
        for extencion in extensiones_ejecutables:
            if nombre.endswith(extencion) or nombre.endswith(extencion.upper()):
                move(archivo, direccionEjecutables)
                logging.info(f"Moviendo audio a {direccionEjecutables}")

    def checkearCodigo(self, archivo, nombre):
        for extencion in extensiones_codigo:
            if nombre.endswith(extencion) or nombre.endswith(extencion.upper()):
                move(archivo, direccionCodigos)
                logging.info(f"Moviendo audio a {direccionCodigos}")

    def checkearBaseDeDatos(self, archivo, nombre):
        for extencion in extensiones_bases_datos:
            if nombre.endswith(extencion) or nombre.endswith(extencion.upper()):
                move(archivo, direccionBasesdedatos)
                logging.info(f"Moviendo audio a {direccionBasesdedatos}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = direccionDescargas
    event_handler = CambiaDirecciones()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
