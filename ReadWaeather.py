import urllib.request, json, time, sys

file = open("weather.csv", "a", 1)
line = "{0}\t{1}\t{2}\n"
file.write(line.format('time', 'temperature [°C]', 'humidity [%]'))


while True:
    try:
        url = urllib.request.urlopen("http://192.168.178.39/weather")
        data = json.loads(url.read().decode())
        file.write(line.format(time.asctime( time.localtime(time.time()) ), data["temperature"], data["humidity"]))
    
        time.sleep(180)
    except Exception as e:
        errorfile = open("error.txt", "w")
        errorfile.write(str(e))
        errorfile.close()
        file.close()
        sys.exit(1)