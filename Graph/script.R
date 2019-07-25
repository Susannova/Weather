weather <- read.delim("../weather.csv")
weather_filtered <- weather[weather$temperature..Â.C.>-900, ]


pdf("Temp.pdf",width=7,height=5)
plot(weather_filtered$time, weather_filtered$temperature..Â.C., xlab = "time", ylab = "temperature [°C]")

plot(weather_filtered$time, weather_filtered$humidity...., xlab = "time", ylab = "humidity [%]")

dev.off()

