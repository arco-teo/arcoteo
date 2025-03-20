import requests
from bs4 import BeautifulSoup
import csv
import concurrent.futures

# URL base y encabezados de la solicitud HTTP
base_url = "https://www.federarco.es/raus/rfeta/detalle.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36"
}

# Función para extraer los datos de cada licencia
def obtener_datos_licencia(licencia):
    url = f"{base_url}?licencia={licencia}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Extraer el nombre del arquero
        try:
            nombre_arquero = soup.find("div", class_="col-sm-6").find("h2").text.strip()
        except AttributeError:
            nombre_arquero = "Desconocido"  # En caso de que no se encuentre el nombre

        # Buscar los registros en la tabla
        try:
            rows = soup.select("table.table tbody tr")
            data = []
            for row in rows:
                cells = row.find_all("td")

                if len(cells) >= 9:
                    # Extraer la federación desde el src de la imagen
                    img_src = cells[0].find("img")["src"]
                    federacion = img_src.split("/")[-1].replace(".jpg", "")

                    categoria = cells[1].text.strip()
                    temporada = cells[2].text.strip()
                    t1 = cells[3].text.strip()
                    t2 = cells[4].text.strip()
                    t3 = cells[5].text.strip()
                    t4 = cells[6].text.strip()
                    t5 = cells[7].text.strip()
                    media = cells[8].text.strip()

                    # Guardamos los datos en la lista
                    data.append([licencia, nombre_arquero, federacion, categoria, temporada, t1, t2, t3, t4, t5, media])
            return data
        except Exception as e:
            print(f"Error al procesar la licencia {licencia}: {e}")
            return []
    else:
        print(f"No se pudo acceder a la licencia {licencia}.")
        return []

# Función principal para gestionar la descarga de los datos
def main():
    # Crear archivo CSV y escribir encabezados
    with open("datos_multifio.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Licencia", "Nombre del Arquero", "Federación", "Categoría", "Temporada", "T1", "T2", "T3", "T4", "T5", "Media"
        ])

        # Crear un ThreadPoolExecutor para ejecutar las tareas en paralelo
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # Iterar sobre las licencias (ajustar el rango según sea necesario)
            licencias = range(0, 13000)  # Cambiar el rango según lo necesites
            # Ejecutar la función obtener_datos_licencia en paralelo
            results = executor.map(obtener_datos_licencia, licencias)

            # Escribir los resultados en el archivo CSV
            for result in results:
                for row in result:
                    writer.writerow(row)
                    print(f"Datos de la licencia {row[0]} guardados.")

    print("Proceso completo. Los datos se han guardado en 'datos_archeros.csv'.")

# Ejecutar el script
if __name__ == "__main__":
    main()
