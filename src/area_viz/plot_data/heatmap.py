import pandas as pd
import matplotlib.pyplot as plt
import area_viz.corporate_design as ci
import area_viz.area_maps as am
import area_viz.plot_data.generic as generic

def plz2_area(
        ax: plt.Axes,
        plz2_data: pd.DataFrame,
        area: str = "Deutschland",
        show_HQ: bool = True,
        show_sales_offices: bool = True,
        show_capital_cities: bool = True,
        caption: str = None
) -> plt.Axes:
    if not ax:
        fig=plt.figure(figsize=(20, 12), dpi=600)
        ax=fig.add_subplot(1, 1, 1)
    plz2_gdf = am.PLZ2_SHAPES.copy()
    if area != "Deutschland":
        plz2_gdf = plz2_gdf[plz2_gdf["gebiet"].str.lower().str.contains(area.lower())]
    plz2_gdf["value"] = plz2_gdf["plz2"].map(plz2_data)
    plz2_gdf.plot(column="value", ax=ax, legend=True, cmap="OrRd", edgecolor=ci.KOCO_COLORS.get("Grau"), linewidth=0.3)
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    ax=am.AREA_SHAPES.boundary.plot(ax=ax, color=ci.KOCO_COLORS.get("HF_Blaugrau"), linewidth=1)
    am.AREA_SHAPES.apply(lambda x: ax.annotate(text=x["gebiet"], xy=x.geometry.centroid.coords[0], ha="center", fontweight="bold", fontsize=10, color=ci.KOCO_COLORS.get("Grau")), axis=1)
    ax.axes.set_axis_off()

    if show_HQ:
        generic.add_poi_to_map(ax, [am.HQ])
        
    if show_sales_offices:
        generic.add_poi_to_map(ax, am.SALES_OFFICES)
    
    if show_capital_cities:
        generic.add_poi_to_map(ax, am.CAPITAL_CITIES)
    if caption:
        plt.figtext(0.5, 0.01, caption, ha="center", fontsize=10)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    return ax

def plz3_area(
        ax: plt.Axes,
        plz3_data: pd.DataFrame,
        area: str = "Deutschland",
        show_HQ: bool = True,
        show_sales_offices: bool = True,
        show_capital_cities: bool = True,
        caption: str = None
) -> plt.Axes:
    if not ax:
        fig=plt.figure(figsize=(10, 15))
        ax=fig.add_subplot(1, 1, 1)
    plz3_gdf = am.PLZ3_SHAPES.copy()
    if area != "Deutschland":
        plz3_gdf = plz3_gdf[plz3_gdf["gebiet"].str.lower().str.contains(area.lower())]
    plz3_gdf["value"] = plz3_gdf["plz3"].map(plz3_data)
    # plz3_gdf["value"] = plz3_gdf["value"].fillna(0)  # Optional: Fill NaN values with 0 for better visualization
    plz3_gdf.plot(column="value", ax=ax, legend=True, cmap="Reds", edgecolor=ci.KOCO_COLORS.get("Grau"), linewidth=0.3)
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    ax=am.AREA_SHAPES.boundary.plot(ax=ax, color=ci.KOCO_COLORS.get("HF_Blaugrau"), linewidth=1)
    am.AREA_SHAPES.apply(lambda x: ax.annotate(text=x["gebiet"], xy=x.geometry.centroid.coords[0], ha="center", fontweight="bold", fontsize=10, color=ci.KOCO_COLORS.get("Grau")), axis=1)

    if show_HQ:
        generic.add_poi_to_map(ax, [am.HQ])
        
    if show_sales_offices:
        generic.add_poi_to_map(ax, am.SALES_OFFICES)
    
    if show_capital_cities:
        generic.add_poi_to_map(ax, am.CAPITAL_CITIES)


    ax.axes.set_axis_off()
    if caption:
        plt.figtext(0.5, 0.01, caption, ha="center", fontsize=10)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    return ax




def main():
    pass    

if __name__ == "__main__":
    main()