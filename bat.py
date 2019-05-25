import subprocess

znow = float(open('/sys/class/power_supply/BAT0/energy_now', 'r').read())
onow = float(open('/sys/class/power_supply/BAT1/energy_now', 'r').read())
zfull = float(open('/sys/class/power_supply/BAT0/energy_full', 'r').read())
ofull = float(open('/sys/class/power_supply/BAT1/energy_full', 'r').read())

charging = open('/sys/class/power_supply/BAT0/status', 'r').read()

now = znow + onow
full = zfull + ofull

percent = round(((now / full) * 100), 1)

if percent <= 15 and charging != 'Charging\n':
	subprocess.Popen(['notify-send', 'Low battery!'])

print(str(percent) + '%')
