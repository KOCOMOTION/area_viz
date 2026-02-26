import geopandas as gpd
import datamodel.poi as poi
import corporate_design as ci
import dataclasses as dc
import json
import os

def create_coords_file(output_file: str, plz_shape_file: str)->None:
    print("Creating PLZ coordinates file...")
    plz_data = gpd.read_file(plz_shape_file)
    plz_data["coords"] = plz_data.geometry.centroid.apply(lambda point: (point.x, point.y))
    plz_coords = [poi.POI(name=row["plz"], coordinates=row["coords"], color=ci.KOCO_COLORS.get("Schwarzgrau")) for _, row in plz_data.iterrows()]
    with open(output_file, "w") as f:
        json.dump([dc.asdict(p) for p in plz_coords], f)
    

def load_coords_file(output_file: str, plz_shape_file: str, enforce_new_creation: bool = False) -> list[poi.POI]:
    if enforce_new_creation or not os.path.exists(output_file):
        create_coords_file(output_file, plz_shape_file)
    with open(output_file, "r") as f:
        plz_coords = json.load(f)
    return [poi.POI(**p) for p in plz_coords]

def main():
    pass


if __name__ == "__main__":
    main()