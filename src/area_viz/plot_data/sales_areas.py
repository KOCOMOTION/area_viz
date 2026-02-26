import matplotlib.pyplot as plt
import area_viz.corporate_design as ci
import area_viz.plot_data.generic as generic
import area_viz.area_maps as am

def basic_map(
        ax: plt.Axes|None, 
        show_plz2: bool = True, 
        show_area_shape: bool = True,
        show_HQ: bool = True,
        show_sales_offices: bool = True, 
        show_capital_cities: bool = True
    )->plt.Axes:
    if show_plz2:
        ax=am.PLZ2_SHAPES.plot(ax=ax, legend=False, figsize=(10, 10), edgecolor=ci.KOCO_COLORS.get("Grau"), linewidth=0.3, color=am.PLZ2_SHAPES['color'], alpha=0.3)
        am.PLZ2_SHAPES.apply(lambda x: ax.annotate(text=x["plz2"], xy=x.geometry.centroid.coords[0], ha="center", fontsize=5, color=ci.KOCO_COLORS.get("Grau")), axis=1)

    if show_area_shape:
        ax=am.AREA_SHAPES.boundary.plot(ax=ax, color=ci.KOCO_COLORS.get("HF_Blaugrau"), linewidth=1)
        am.AREA_SHAPES.apply(lambda x: ax.annotate(text=x["gebiet"], xy=x.geometry.centroid.coords[0], ha="center", fontweight="bold", fontsize=10, color=ci.KOCO_COLORS.get("Grau")), axis=1)
    ax.axes.set_axis_off()
    if ax is None:
        return None

    if show_HQ:
        generic.add_poi_to_map(ax, [am.HQ])
        
    if show_sales_offices:
        generic.add_poi_to_map(ax, am.SALES_OFFICES)
    
    if show_capital_cities:
        generic.add_poi_to_map(ax, am.CAPITAL_CITIES)
    return ax

def basic_map_area(
        ax: plt.Axes|None,
        area_name: str, 
        show_plz2: bool = True, 
        show_area_shape: bool = True,
        show_HQ: bool = True,
        show_sales_offices: bool = True, 
        show_capital_cities: bool = True
    )->plt.Axes:
    if show_plz2:
        plz2_area = am.PLZ2_SHAPES.where(am.PLZ2_SHAPES["gebiet"] == area_name).dropna(subset=["geometry"])
        ax=plz2_area.plot(ax=ax, legend=False, figsize=(10, 10), edgecolor=ci.KOCO_COLORS.get("Grau"), linewidth=0.3, color=plz2_area['color'], alpha=0.3)
        plz2_area.apply(lambda x: ax.annotate(text=x["plz2"], xy=x.geometry.centroid.coords[0], ha="center", fontsize=5, color=ci.KOCO_COLORS.get("Grau")), axis=1)

    if show_area_shape:
        area_shape = am.AREA_SHAPES.where(am.AREA_SHAPES["gebiet"] == area_name).dropna(subset=["geometry"])
        ax=area_shape.boundary.plot(ax=ax, color=ci.KOCO_COLORS.get("HF_Blaugrau"), linewidth=1)
        area_shape.apply(lambda x: ax.annotate(text=x["gebiet"], xy=x.geometry.centroid.coords[0], ha="center", fontweight="bold", fontsize=10, color=ci.KOCO_COLORS.get("Grau")), axis=1)
    ax.axes.set_axis_off()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    if ax is None:
        return None

    if show_HQ:

        generic.add_poi_to_map(ax, [am.HQ])
        
    if show_sales_offices:
        generic.add_poi_to_map(ax, am.SALES_OFFICES)
    
    if show_capital_cities:
        generic.add_poi_to_map(ax, am.CAPITAL_CITIES)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    return ax

def germany_sales_areas() -> plt.axes:
    fig = plt.figure(figsize=(10, 15))
    ax = fig.add_subplot(1, 1, 1)

    ax=basic_map(
        ax=ax, 
        show_plz2=True, 
        show_area_shape=True, 
        show_HQ=True, 
        show_sales_offices=True, 
        show_capital_cities=True
    )
    return ax


def germany_sales_area(area_name: str) -> plt.axes:
    fig = plt.figure(figsize=(10, 15))
    ax = fig.add_subplot(1, 1, 1)

    ax=basic_map_area(
        ax=ax, 
        area_name=area_name, 
        show_plz2=True, 
        show_area_shape=True, 
        show_HQ=True, 
        show_sales_offices=True, 
        show_capital_cities=True
    )
    return ax



def main():
    pass

if __name__ == "__main__":
    main()