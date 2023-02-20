import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd
import numpy as np

# 读取数据
df = pd.read_excel("Data2.xlsx", engine='openpyxl')

data = np.array(df)
data_list = data.tolist()

(
    Line()
    .add_xaxis(xaxis_data=[item[0] for item in data_list])
    .add_yaxis(
        series_name="Total",
        y_axis=[item[1] for item in data_list],
        yaxis_index=0,
        is_smooth=True,
        is_symbol_show=False,
    )
    .add_yaxis(
        series_name="Hard Mode",
        y_axis=[item[2] for item in data_list],
        yaxis_index=0,
        is_smooth=True,
        is_symbol_show=True,
        linestyle_opts=opts.LineStyleOpts(type_='dotted')
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        visualmap_opts=opts.VisualMapOpts(
            pos_top="80",
            pos_right="130",
            is_piecewise=True,
            pieces=[
                {"gt": 0, "lte": 50000, "color": "#096"},
                {"gt": 50000, "lte": 100000, "color": "#ffde33"},
                {"gt": 100000, "lte": 150000, "color": "#ff9933"},
                {"gt": 150000, "lte": 200000, "color": "#cc0033"},
                {"gt": 200000, "lte": 300000, "color": "#660099"},
                {"gt": 300000, "color": "#7e0023"},
            ],
            out_of_range={"color": "#999"},
#            series_index={"0"},
        ),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name_location="start",
            min_=0,
            max_=400000,
            is_scale=True,
            axistick_opts=opts.AxisTickOpts(is_inside=False),
        ),
        legend_opts=opts.LegendOpts(pos_top='10')
    )
    .set_series_opts(
        markline_opts=opts.MarkLineOpts(
            data=[
                {"yAxis": 50000},
                {"yAxis": 100000},
                {"yAxis": 150000},
                {"yAxis": 200000},
                {"yAxis": 300000},
            ],
            label_opts=opts.LabelOpts(position="end"),
        )
    )

    .render("daily_results.html")
)
