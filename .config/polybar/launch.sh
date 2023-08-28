#!usr/bin/sh

# DEBUG=1 to debug fails
DEBUG=0

# Termina todas las instancias de polybar
killall -q polybar

# Inicia la unica barra de estado 'bar'
polybar bar 2>&1 | tee -a /tmp/polybar_bar.log & disown
# Si hay segunda pantalla iniciar barra con la segunda pantalla
if [[ $(xrandr -q | grep 'HDMI2 connected') ]]; then
   polybar barHDMI | tee -a /tmp/polybar_barHDMI.log & disown
fi
