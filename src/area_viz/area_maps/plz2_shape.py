import geopandas as gpd
import area_viz.corporate_design as ci
import os

def map_plz_areas(plz2: str, area_mapping: dict) -> str:
    for area, prefixes in area_mapping.items():
        if plz2 in prefixes:
            return area
    return "Unknown"    

def create_shape_file(input_file: str, output_file: str, area_mapping: dict)->None:
    plz_data = gpd.read_file(input_file)
    plz_data_2digits = plz_data.copy()
    plz_data_2digits["plz2"] = plz_data_2digits["plz"].str[:2]
    plz2 = plz_data_2digits[["plz2", "geometry"]].dissolve(by="plz2", as_index=False)
    plz2['gebiet'] = plz2['plz2'].apply(lambda x: map_plz_areas(x, area_mapping))
    plz2['color'] = plz2['gebiet'].map(ci.AREA_MAPPING_COLOR_MAPPING)
    # print(plz2[['plz2', 'gebiet', 'color']].head())
    plz2.to_file(output_file)

def load_shape_file(input_file: str, output_file: str, area_mapping: dict, enforce_new_creation: bool = False) -> gpd.GeoDataFrame:
    if enforce_new_creation or not os.path.exists(output_file):
        create_shape_file(input_file, output_file, area_mapping)
    plz2 = gpd.read_file(output_file)
    return plz2


def main():
    pass


if __name__ == "__main__":
    main()