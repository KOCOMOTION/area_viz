import area_viz.plot_data.sales_areas as pd_sales_areas
import area_viz.area_maps as area_maps
import area_viz.test_data.generate as gen_test_data
import area_viz.plot_data.heatmap as pd_heatmap
import matplotlib.pyplot as plt

def main():
    # pd_sales_areas.germany_sales_areas()
    # plt.show()

    d=gen_test_data.plz2_area_values(area_name="Bayern")
    fig = plt.figure(figsize=(10, 5), dpi=300) 
    ax = fig.add_subplot(1, 1, 1)
    ax=pd_heatmap.plz2_area(
        ax=ax, 
        plz2_data=d, 
        area="Bayern", 
        show_HQ=True, 
        show_sales_offices=True, 
        show_capital_cities=True,
        caption="Test Heatmap PLZ2 Bayern")
    plt.savefig("test_heatmap_plz2_bayern.png", bbox_inches='tight', dpi=300)


if __name__ == "__main__":
    main()