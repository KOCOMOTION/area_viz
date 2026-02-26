import area_viz.area_maps as am
import area_viz.datamodel.poi as poi
import dataclasses as dc

@dc.dataclass
class CapitalCity:
    name: str
    plz: str
    coords: tuple[float, float]

def load_capital_cities(capital_cities_url: str)->list[poi.POI]:
    import pandas as pd
    df = pd.read_csv(capital_cities_url, sep=",", dtype={"PLZ": str})
    capital_cities = []
    for _, row in df.iterrows():
        plz = row["PLZ"]
        city = row["Hauptstadt"]
        coords = poi.fetch_poi_from_poi_list(am.PLZ_COORDS, plz)
        if coords:
            capital_cities.append(poi.POI(name=city, coordinates=coords.coordinates))
    return capital_cities

def main():
    pass

if __name__ == "__main__":
    main()