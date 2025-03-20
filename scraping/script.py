import requests
from bs4 import BeautifulSoup
import csv

# URL base y encabezados de la solicitud HTTP
base_url = "https://www.federarco.es/raus/rfeta/detalle.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36"
}

# Crear archivo CSV y escribir encabezados
with open("datos_archeros.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Licencia", "Nombre del Arquero", "Federación", "Categoría", "Temporada", "T1", "T2", "T3", "T4", "T5", "Media"
    ])  # Escribimos los encabezados de las columnas

    # Iterar sobre las licencias (ajustar el rango según sea necesario)
    for licencia in range(10000,15000):  # Cambiar el rango según lo necesites
        url = f"{base_url}?licencia={licencia}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            # Extraer el nombre del arquero desde la etiqueta <h2> dentro de <div class="col-sm-6">
            try:
                nombre_arquero = soup.find("div", class_="col-sm-6").find("h2").text.strip()
            except AttributeError:
                nombre_arquero = "Desconocido"  # En caso de que no se encuentre el nombre

            # Buscar los registros en la tabla
            try:
                # Buscar la tabla de resultados
                rows = soup.select("table.table tbody tr")
                for row in rows:
                    # Extraemos cada celda de la fila
                    cells = row.find_all("td")

                    if len(cells) >= 9:  # Verificamos que haya suficientes celdas (incluyendo los valores T1 a T5)
                        # Extraer la federación desde el src de la imagen
                        img_src = cells[0].find("img")["src"]  # Obtener el atributo src de la imagen
                        federacion = img_src.split("/")[-1].replace(".jpg", "")  # Extraer el nombre del archivo y eliminar ".jpg"

                        # Extraer los demás datos de la tabla
                        categoria = cells[1].text.strip()  # Categoría
                        temporada = cells[2].text.strip()  # Temporada
                        t1 = cells[3].text.strip()  # T1
                        t2 = cells[4].text.strip()  # T2
                        t3 = cells[5].text.strip()  # T3
                        t4 = cells[6].text.strip()  # T4
                        t5 = cells[7].text.strip()  # T5
                        media = cells[8].text.strip()  # Media

                        # Escribir los datos extraídos en el archivo CSV
                        writer.writerow([licencia, nombre_arquero, federacion, categoria, temporada, t1, t2, t3, t4, t5, media])
                        print(f"Datos de la licencia {licencia} guardados.")
            except Exception as e:
                print(f"Error al procesar la licencia {licencia}: {e}")
        else:
            print(f"No se pudo acceder a la licencia {licencia}.")

print("Proceso completo. Los datos se han guardado en 'datos_archeros.csv'.")
