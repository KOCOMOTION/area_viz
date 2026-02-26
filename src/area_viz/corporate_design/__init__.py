KOCO_COLORS = {
    "Weiß": "#f7f6f5",
    "Schwarzgrau": "#212529",
    "Grauschwarz": "#292927",
    "Dunkelgrau": "#363932",
    "Grau": "#6e6d71",
    "Hellgrau": "#dedede",
    "Blaugrau": "#97adc2",
    "Grünblau": "#5ca19f",
    "Beige": "#faeacc",
    "Gelb": "#ffe600",
    "HF_Orange": "#ff801a",
    "HF_Dunkelrot": "#a13036",
    "HF_Flieder": "#c05b88",
    "HF_Lila": "#7b4f87",
    "HF_Blaugrün": "#55ca9b",
    "HF_Hellgrün": "#b1be13",
    "HF_Hellblau": "#5b9fc0",
    "HF_Blaugrau": "#87bbcf",
    "HF_Dunkelgrau": "#171914",
}


AREA_MAPPING_COLOR_MAPPING = {
    "Ost": KOCO_COLORS.get("HF_Blaugrün"),  # Grün-Gelb
    "West": KOCO_COLORS.get("HF_Orange"),       # Orange
    "BW": KOCO_COLORS.get("HF_Hellgrün"),        # Grün
    "Bayern": KOCO_COLORS.get("HF_Hellblau"),    # Rot
    "Unknown": KOCO_COLORS.get("Blaugrau")    # Grau für unbekannte Gebiete
}
    