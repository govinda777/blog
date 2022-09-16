# Como desenhar um poligono em um mapa, dentro do Github README.md

Como_desenhar_um_poligono_em_um_mapa_dentro_do_Github_README_2.jpeg

## 

Como desenhar um poligono em um mapa, dentro do Github README.md?

## Exemplo

```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 1,
      "properties": {
        "ID": 0
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
              [-90,35],
              [-90,30],
              [-85,30],
              [-85,35],
              [-90,35]
          ]
        ]
      }
    }
  ]
}
```

## Exemplo Code

type: geojson

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 1,
      "properties": {
        "ID": 0
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
              [-90,35],
              [-90,30],
              [-85,30],
              [-85,35],
              [-90,35]
          ]
        ]
      }
    }
  ]
}
```

#Geo #Poligono #Spatial #Geopandas #GIS #GIS_GUIs #polygon #GeoJSON


https://github.com/govinda777/blog/blob/main/README-Components.md#mapas-geofraficos-mapas-do-geojson-e-topojson