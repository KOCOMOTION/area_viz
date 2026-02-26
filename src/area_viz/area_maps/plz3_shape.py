import geopandas as gpd
import area_viz.corporate_design as ci
import os

def map_plz_areas(plz3: str, area_mapping: dict) -> str:
    for area, prefixes in area_mapping.items():
        if plz3 in prefixes:
            return area
    return "Unknown"    

def create_shape_file(input_file: str, output_file: str, area_mapping: dict)->None:
    plz_data = gpd.read_file(input_file)
    plz_data_3digits = plz_data.copy()
    plz_data_3digits["plz2"] = plz_data_3digits["plz"].str[:2]
    plz_data_3digits["plz3"] = plz_data_3digits["plz"].str[:3]
    plz3 = plz_data_3digits[["plz2","plz3", "geometry"]].dissolve(by="plz3", as_index=False)
    plz3['gebiet'] = plz3['plz2'].apply(lambda x: map_plz_areas(x, area_mapping))
    plz3['color'] = plz3['gebiet'].map(ci.AREA_MAPPING_COLOR_MAPPING)
    plz3.to_file(output_file)

def load_shape_file(input_file: str, output_file: str, area_mapping: dict, enforce_new_creation: bool = False) -> gpd.GeoDataFrame:
    if enforce_new_creation or not os.path.exists(output_file):
        create_shape_file(input_file, output_file, area_mapping)
    plz3 = gpd.read_file(output_file)
    return plz3


def main():
    pass


if __name__ == "__main__":
    main()