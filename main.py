import area_viz.plot_data.generic as pd_sales_gen
import area_viz.area_maps as area_maps
import area_viz.test_data.generate as gen_test_data
import area_viz.plot_data.heatmap as pd_heatmap
import matplotlib.pyplot as plt

AREA = "Deutschland"

def main():

    d=gen_test_data.plz2_area_values(area_name=AREA, min_value=0, max_value=10, scale_values=100)
    p=gen_test_data.poi_list(n_pois=100, area=AREA, marker="o", color=area_maps.ci.KOCO_COLORS.get("HF_Orange"), hide_annotations=True)
    fig = plt.figure(figsize=(20, 12), dpi=600) 
    ax = fig.add_subplot(1, 1, 1)
    ax=pd_heatmap.plz2_area(
        ax=ax, 
        plz2_data=d, 
        area=AREA, 
        show_HQ=True, 
        show_sales_offices=True, 
        show_capital_cities=True,
        caption=f"Test Heatmap PLZ2 {AREA}")
    ax=pd_sales_gen.add_poi_to_map(ax, p)
    plt.savefig(f"test_heatmap_plz2_{AREA.lower()}.png", bbox_inches='tight', dpi=600)


if __name__ == "__main__":
    main()