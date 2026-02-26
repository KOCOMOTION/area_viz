import matplotlib.pyplot as plt
import plot_data.sales_areas as sales_areas
import plot_data.generic as generic
import plot_data.heatmap as heatmap
import datamodel.poi as dm_poi

import corporate_design as ci
import area_maps as am
import pandas as pd


def top_companies_revenue(
        revenue_data: pd.DataFrame,
        max_rank: int = 100, 
        show_company_names: bool = False) -> plt.axes:
    ax = sales_areas.germany_sales_areas()
    revenue_data.sort_values(by="DATA", ascending=False, inplace=True)
    top_companies_poi = dm_poi.plz_dataframe_to_poi_list(df=revenue_data.head(max_rank), plz2coord=am.PLZ_COORDS, data_col="DATA")
    if not show_company_names:
        for poi in top_companies_poi:
            poi.name = ""
    ax = generic.add_poi_to_map(ax=ax, poi_list=top_companies_poi)
    plt.title(f"Top {max_rank} Unternehmen nach Umsatz in Deutschland")
    return ax

def top_companies_revenue_area(
        area_name: str, 
        revenue_data: pd.DataFrame,
        max_rank: int = 100, show_company_names: bool = False) -> plt.axes:
    ax = sales_areas.germany_sales_area(area_name=area_name)
    revenue_data = revenue_data.sort_values(by="DATA", ascending=False)
    top_companies_poi = dm_poi.plz_dataframe_to_poi_list(df=revenue_data.head(max_rank), plz2coord=am.PLZ_COORDS, data_col="DATA")
    if not show_company_names:
        for poi in top_companies_poi:
            poi.name = ""
    ax = generic.add_poi_to_map(ax=ax, poi_list=top_companies_poi)
    plt.title(f"Top 100 Unternehmen nach Umsatz im Vertriebsgebiet {area_name}")
    return ax


def plz2_heatmap(
        plz2_data: pd.DataFrame,
        area: str = "Deutschland",
        show_HQ: bool = True,
        show_sales_offices: bool = True,
        show_capital_cities: bool = True,
) -> plt.axes:
    heatmap_ax = heatmap.plz2_area(
        plz2_data=plz2_data,
        area=area,
        show_HQ=show_HQ,
        show_sales_offices=show_sales_offices,
        show_capital_cities=show_capital_cities,
    )
    return heatmap_ax

def plz3_heatmap(
        plz3_data: pd.DataFrame,
        area: str = "Deutschland",
        show_HQ: bool = True,
        show_sales_offices: bool = True,
        show_capital_cities: bool = True,
) -> plt.axes:
    heatmap_ax = heatmap.plz3_area(
        plz3_data=plz3_data,
        area=area,
        show_HQ=show_HQ,
        show_sales_offices=show_sales_offices,
        show_capital_cities=show_capital_cities,
    )
    return heatmap_ax   


def main():
    pass

if __name__ == "__main__":
    main()