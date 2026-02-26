import area_maps.cities as cities
import area_maps.plz_coords as plz_coords
import area_maps.plz2_shape as plz2_shape
import area_maps.plz3_shape as plz3_shape
import area_maps.area_shape as area_shape
import datamodel.poi as poi
import corporate_design as ci

ENFORCE_NEW_CREATION = False

PLZ_SHAPE_FILE = "data/PLZ_Gebiete/OSM_PLZ.shp"
PLZ_COORDS_FILE = "data/PLZ_Gebiete/PLZ_Coords.json"
PLZ_2DIGITS_SHAPE_FILE = "data/PLZ_Gebiete/OSM_PLZ_2digits.shp"
PLZ_3DIGITS_SHAPE_FILE = "data/PLZ_Gebiete/OSM_PLZ_3digits.shp"
GEBIETE_SHAPE_FILE = "data/PLZ_Gebiete/OSM_Gebiete.shp"
CAPITAL_CITIES_URL = "data/city_data/Hauptstädte der deutschen Bundesländer (PLZ, Hauptstadt).csv"


AREA_MAPPING = {
    "Ost": [
        "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", 
        "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
        "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
        "38", "39"],
    "West": ["30", "31", "32", "33", "34", "35", "36", "37",
             "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",
             "50", "51", "52", "53", "54", "55", "56", "57", "58", "59",
             "60", "61", "62", "63", "65", "97"],
    "BW": ["64", "66", "67", "68", "69",
           "70", "71", "72", "73", "74", "75", "76", "77", "78", "79",
           "88", "89"],
    "Bayern": ["80", "81", "82", "83", "84", "85", "86", "87",
               "90", "91", "92", "93", "94", "95", "96", "98", "99"],
}


HQ_PLZ = "78083"
SALES_OFFICES_PLZ = {'BW':"71032", 'West':"65934", 'Bayern':"92224", 'Bayern_2':"90491", 'Ost':"01458"}

PLZ_COORDS = plz_coords.load_coords_file(output_file=PLZ_COORDS_FILE, plz_shape_file=PLZ_SHAPE_FILE, enforce_new_creation=ENFORCE_NEW_CREATION)
CAPITAL_CITIES = cities.load_capital_cities(capital_cities_url=CAPITAL_CITIES_URL)

HQ = poi.fetch_poi_from_poi_list(PLZ_COORDS, HQ_PLZ)
HQ.name = "HQ"
HQ.color = ci.KOCO_COLORS.get("HF_Orange")
HQ.marker = "x"

SALES_OFFICES = []
for office_plz in SALES_OFFICES_PLZ:
    office_coords = poi.fetch_poi_from_poi_list(PLZ_COORDS, SALES_OFFICES_PLZ.get(office_plz))
    if office_coords:
        office_coords.name = f"Büro {office_plz}"
        office_coords.color = ci.KOCO_COLORS.get("HF_Lila")
        office_coords.marker = "D"
        SALES_OFFICES.append(office_coords)

PLZ2_SHAPES = plz2_shape.load_shape_file(input_file=PLZ_SHAPE_FILE, output_file=PLZ_2DIGITS_SHAPE_FILE, area_mapping=AREA_MAPPING, enforce_new_creation=ENFORCE_NEW_CREATION)
PLZ3_SHAPES = plz3_shape.load_shape_file(input_file=PLZ_SHAPE_FILE, output_file=PLZ_3DIGITS_SHAPE_FILE, area_mapping=AREA_MAPPING, enforce_new_creation=ENFORCE_NEW_CREATION)   
AREA_SHAPES = area_shape.load_shape_file(file_path=GEBIETE_SHAPE_FILE, plz2_file=PLZ_2DIGITS_SHAPE_FILE, enforce_new_creation=ENFORCE_NEW_CREATION)
