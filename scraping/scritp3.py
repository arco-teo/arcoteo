import requests
from bs4 import BeautifulSoup
import csv
import concurrent.futures

# URL base e encabezados de solicitude HTTP
base_url = "https://www.federarco.es/raus/rfeta/detalle.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36"
}

# Función para extraer os datos de cada licencia
def obtener_datos_licencia(licencia):
    url = f"{base_url}?licencia={licencia}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Extraer o nome do arquero
        try:
            nombre_arquero = soup.find("div", class_="col-sm-6").find("h2").text.strip()
        except AttributeError:
            nombre_arquero = "Desconocido"  # En caso de que non se atope o nome

        # Buscar os rexistros na táboa
        try:
            rows = soup.select("table.table tbody tr")
            data = []
            for row in rows:
                cells = row.find_all("td")

                if len(cells) >= 9:
                    # Extraer a federación desde o src da imaxe
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

                    # Gardamos os datos na lista
                    data.append([licencia, nombre_arquero, federacion, categoria, temporada, t1, t2, t3, t4, t5, media])
            return data
        except Exception as e:
            print(f"Erro ao procesar a licencia {licencia}: {e}")
            return []  # Retornamos lista vacía en caso de erro
    else:
        print(f"No se puido acceder á licencia {licencia}.")
        return []  # Retornamos lista vacía se a solicitude falla

# Función principal para xestionar a descarga dos datos
def main():
    # Crear arquivo CSV e escribir encabezados
    with open("datos_script3.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Licencia", "Nome do Arquero", "Federación", "Categoría", "Temporada", "T1", "T2", "T3", "T4", "T5", "Media"
        ])

        # Crear un ThreadPoolExecutor para executar as tarefas en paralelo
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # Iterar sobre as licenzas (axustar o rango segundo sexa necesario)
            licencias = range(0, 13000)  # Cambiar o rango segundo sexa necesario
            futures = [executor.submit(obtener_datos_licencia, licencia) for licencia in licencias]

            # Escribir os resultados no arquivo CSV
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                for row in result:
                    writer.writerow(row)
                    print(f"Datos da licencia {row[0]} gardados.")

    print("Proceso completo. Os datos gardáronse en 'datos_archeros.csv'.")

# Executar o script
if __name__ == "__main__":
    main()
