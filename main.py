import area_viz.plot_data.sales_areas as pd_sales_areas
import area_viz.area_maps as area_maps
import matplotlib.pyplot as plt

def main():
    print(area_maps.ENFORCE_NEW_CREATION)
    pd_sales_areas.germany_sales_areas()
    plt.show()

if __name__ == "__main__":
    main()