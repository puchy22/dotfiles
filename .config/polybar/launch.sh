#!usr/bin/sh

# DEBUG=1 to debug fails
DEBUG=0

# Termina todas las instancias de polybar
killall -q polybar

# Si las barras tienen 'ipc' habilitado lo puedes utilizar con
# polybar-msg cmd quit

# Inicia la unica barra de estado 'bar'
if [ $DEBUG -eq 1 ]
then
	echo "---" | tee -a /tmp/polybar.log
	polybar bar 2>&1 | tee -a /tmp/polybar.log & disown
    if [[ $(xrandr -q | grep 'HDMI-2 connected') ]]; then
        polybar barHDMI 2>&1 | tee -a /tmp/polybar.log & disown
	fi
else
	polybar bar > /dev/null 2>&1 & disown
	if [[ $(xrandr -q | grep 'HDMI-2 connected') ]]; then
		polybar barHDMI > /dev/null 2>&1 & disown
	fi
fi
echo "Barra de estado iniciada..."
