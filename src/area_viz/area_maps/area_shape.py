import geopandas as gpd
import os


def create_shape_file(output_file_path: str, plz2_file: str) -> None:
    plz2 = gpd.read_file(plz2_file)
    gebiete = plz2.copy()
    gebiete = gebiete[['gebiet','geometry','color']].dissolve(by='gebiet', as_index=False)
    # print(gebiete[['gebiet']].head())
    gebiete.to_file(output_file_path)

def load_shape_file(file_path: str, plz2_file: str, enforce_new_creation: bool = False) -> gpd.GeoDataFrame:
    if enforce_new_creation or not os.path.exists(file_path):
        create_shape_file(file_path, plz2_file)
    gebiete = gpd.read_file(file_path)
    return gebiete

def main():
    pass

if __name__ == "__main__":
    main()