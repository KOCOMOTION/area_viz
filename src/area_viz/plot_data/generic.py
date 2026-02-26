import matplotlib.pyplot as plt
import area_viz.datamodel.poi as dm_poi

def add_poi_to_map(ax: plt.Axes, poi_list: list[dm_poi.POI], kwargs_scatter: dict = {}, kwargs_annotate: dict = {}) -> plt.Axes:
    for poi in poi_list:
        ax.scatter(poi.coordinates[0], poi.coordinates[1], color=poi.color, label=poi.name, marker=poi.marker, s=poi.size, **kwargs_scatter)
        ax.annotate(text=poi.name, xy=(poi.coordinates[0], poi.coordinates[1]), xytext=(3, 3), textcoords="offset points", fontsize=8, color=poi.color, **kwargs_annotate)
    return ax


def main():
    pass

if __name__ == "__main__":
    main()