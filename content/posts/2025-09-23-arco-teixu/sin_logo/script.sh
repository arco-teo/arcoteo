#!/bin/bash

# Directorio onde están as imaxes orixinais
input_directory="./"

# Directorio de saída para as imaxes con logo
output_directory="./imaxenes-logo"

# Crear o directorio de saída se non existe
mkdir -p "$output_directory"

# Ruta do logotipo
logo="logo.png"

# Tamaño do logotipo
logo_width=300
logo_height=300

# Recorrer todas as imaxes no directorio
for image in "$input_directory"/*.{jpg,jpeg,png}; do
    # Verifica se o arquivo existe
    if [ -f "$image" ]; then
        filename=$(basename "$image")
        output_image="$output_directory/${filename%.*}_logo.${filename##*.}"

        # Engadir o logotipo á imaxe
        convert "$image" "$logo" -gravity southeast -geometry "${logo_width}x${logo_height}+10+10" -composite "$output_image"

        echo "Logotipo engadido con éxito: $output_image"
    fi
done
