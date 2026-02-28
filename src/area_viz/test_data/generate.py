import area_viz.datamodel.poi as dm_poi
import area_viz.area_maps as am
import pandas as pd
import random

def fetch_rand_coordinates(area: str = "Deutschland") -> tuple[float, float]:
    if area == "Deutschland":
        return random.choice(am.PLZ_COORDS).coordinates
    elif area in am.AREA_MAPPING:
        plz_prefixes = am.AREA_MAPPING[area]
        filtered_coords = [coord for coord in am.PLZ_COORDS if any(coord.name.startswith(prefix) for prefix in plz_prefixes)]
        if filtered_coords:
            return random.choice(filtered_coords).coordinates
    return (0.0, 0.0)  # Default fallback coordinates

def poi_list(
        n_pois: int = 10, 
        min_value: float = 0, 
        max_value: float = 100, 
        scale_values: float = 1,
        marker: str = 'o', 
        color: str = 'blue',
        hide_annotations: bool = False,
        area: str = "Deutschland"
        ) -> list[dm_poi.POI]:
    poi_list = []
    for i in range(n_pois):
        rand_coords = fetch_rand_coordinates(area=area)
        poi = dm_poi.POI(
            name=f"POI {i+1}",
            coordinates=rand_coords,
            marker=marker,
            color=color,
            size=random.uniform(min_value, max_value) * scale_values
        )
        if hide_annotations:
            poi.name = ""
        poi_list.append(poi)
    return poi_list

def plz2_area_values(
        area_name: str,
        min_value: float = 0,
        max_value: float = 100,
        scale_values: float = 1
) -> pd.DataFrame:
    if area_name == "Deutschland":
        df = am.PLZ2_SHAPES[["plz2"]].copy()
    else:
        df = am.PLZ2_SHAPES[am.PLZ2_SHAPES["gebiet"] == area_name][["plz2"]].copy()
    df["value"] = df["plz2"].apply(lambda x: random.uniform(min_value, max_value) * scale_values)
    df.rename(columns={"plz2": "PLZ"}, inplace=True)
    df.set_index("PLZ", inplace=True)
    df = df.groupby(df.index)["value"].sum()  # Sum values for duplicate PLZ-2 areas
    return df

def plz3_area_values(
        area_name: str,
        min_value: float = 0,
        max_value: float = 100,
        scale_values: float = 1
) -> pd.DataFrame:
    if area_name == "Deutschland":
        df = am.PLZ3_SHAPES[["plz3"]].copy()
    else:
        df = am.PLZ3_SHAPES[am.PLZ3_SHAPES["gebiet"] == area_name][["plz3"]].copy()
    df["value"] = df["plz3"].apply(lambda x: random.uniform(min_value, max_value) * scale_values)
    df.rename(columns={"plz3": "PLZ"}, inplace=True)
    df.set_index("PLZ", inplace=True)
    df = df.groupby(df.index)["value"].sum()  # Sum values for duplicate PLZ-2 areas
    return df



def main():
    pass

if __name__ == "__main__":
    main()