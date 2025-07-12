#!/bin/bash

# Directorio onde están as imaxes
input_directory="./"

# Ruta do logotipo
#logo="/home/belay/Documentos/arcoteo/assets/img/about_transparent.png"
logo="logo.png"

# Tamaño do logotipo (axusta segundo as túas necesidades)
logo_width=300
logo_height=300

# Recorrer todas as imaxes no directorio
for image in "$input_directory"/*.{jpg,jpeg,png}; do
    # Verifica se o arquivo existe
    if [ -f "$image" ]; then
        output_image="${image%.*}_logo.${image##*.}"

        # Engadir o logotipo á imaxe
        convert "$image" "$logo" -gravity southeast -geometry "${logo_width}x${logo_height}+10+10" -composite "$output_image"

        echo "Logotipo engadido con éxito: $output_image"
    fi
done