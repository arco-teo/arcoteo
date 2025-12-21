#!/bin/bash

# --- CONFIGURACIÓN ---
EXTENSION="jpeg"            # Extensión das imaxes
FPS="0.5"                  # 0.5 = Unha foto cada 2 segundos
NOME_VIDEO="video_nadal_final.mp4"
AUDIO_FILE="audio.mp3"
FADE_DURATION="3"          # Segundos que tarda en baixar a música ao final
# ---------------------

echo "--- Iniciando proceso ---"

# 1. Comprobar ficheiros
count=$(ls -1 *.$EXTENSION 2>/dev/null | wc -l)
if [ "$count" == "0" ]; then
    echo "Erro: Non atopo imaxes .$EXTENSION"
    exit 1
fi

if [ ! -f "$AUDIO_FILE" ]; then
    echo "Erro: Non atopo o audio $AUDIO_FILE"
    exit 1
fi

# 2. Calcular a duración total do vídeo
# Usamos 'awk' porque Bash non manexa ben os decimais
duracion_total=$(awk "BEGIN {print $count / $FPS}")
inicio_fade=$(awk "BEGIN {print $duracion_total - $FADE_DURATION}")

echo "Atopadas $count imaxes."
echo "Duración estimada: $duracion_total segundos."
echo "O son baixará a partir do segundo: $inicio_fade."

# 3. Executar FFmpeg
# -stream_loop -1: Repite a canción se é máis curta que as fotos
# -af "afade...": Aplica o filtro de audio para baixar o volume
# -shortest: Corta o vídeo cando rematan as imaxes

ffmpeg -y -framerate $FPS -pattern_type glob -i "*.$EXTENSION" \
-stream_loop -1 -i "$AUDIO_FILE" \
-c:v libx264 -r 30 -pix_fmt yuv420p \
-c:a aac -b:a 192k \
-af "afade=t=out:st=$inicio_fade:d=$FADE_DURATION" \
-shortest \
"$NOME_VIDEO"

echo "---------------------------------------"
echo "Feito! Vídeo gardado como: $NOME_VIDEO"