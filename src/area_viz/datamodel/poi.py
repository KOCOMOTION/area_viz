import dataclasses as dc
import pandas as pd

@dc.dataclass
class POI:
    name: str
    coordinates: tuple[float, float]
    marker: str = 's'
    color: str = 'k'
    size: int = 10
    
def fetch_poi_from_poi_list(poi_list: list[POI], name: str) -> POI:
    for poi in poi_list:
        if poi.name == name:
            return poi
    return None 

def calc_scale_factor(df: pd.DataFrame, size_col: str, min_size: int = 10, max_size: int = 300) -> float:
    min_value = df[size_col].min()
    max_value = df[size_col].max()
    if max_value == min_value:
        return 1.0
    scale_factor = (max_size - min_size) / (max_value - min_value)
    return scale_factor

def plz_dataframe_to_poi_list(df: pd.DataFrame, plz2coord: dict[str, tuple[float, float]], data_col: str="DATA") -> list[POI]:
    poi_list = []
    scale_factor = calc_scale_factor(df, data_col)
    for _, row in df.iterrows():
        poi_item = fetch_poi_from_poi_list(plz2coord, row["PLZ"])
        if not poi_item:
            continue
        poi_item.name = row["NAME"][:3]  # Truncate name to first 3 characters
        poi_item.color = "blue"
        poi_item.marker = "o"
        poi_item.size = row[data_col] * scale_factor
        poi_list.append(poi_item)
    return poi_list


def main():
    pass    

if __name__ == "__main__":
    main()