library(ggmap)


stations <- read.csv("./stations.csv")

map_frame <- c(left = -179, bottom = -89, right = 179, top = 89)
globe <- get_stamenmap(map_frame, zoom = 1, maptype = "toner-lines")

ggmap(globe, extent = "device") + 
   geom_point(aes(x = LONGITUDE,
                  y = LATITUDE),
            alpha = 1,
            size = .5,
            data = stations )
