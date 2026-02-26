import pandas as pd

def from_excel(file_path: str) -> pd.DataFrame:
    df = pd.read_excel(file_path, sheet_name="FIRMENLISTE", skiprows=3)
    return df

def main():
    pass

if __name__ == "__main__":
    main()