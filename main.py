import area_viz.plot_data.sales_areas as pd_sales_areas
import area_viz.area_maps as area_maps
import area_viz.test_data.generate as gen_test_data
import area_viz.plot_data.heatmap as pd_heatmap
import matplotlib.pyplot as plt

def main():
    # pd_sales_areas.germany_sales_areas()
    # plt.show()

    d=gen_test_data.plz2_area_values(area_name="Bayern")
    ax=pd_heatmap.plz2_area(ax=None, plz2_data=d, area="Bayern", show_HQ=True, show_sales_offices=True, show_capital_cities=True)
    ax.set_title("PLZ-2 Heatmap für Bayern")
    plt.show()


if __name__ == "__main__":
    main()