from pandas import DataFrame
from shiny.express import ui
from shinyecharts.express import Chart, InitOptions, SeriesType
from shinyecharts.renderer import ChartRenderer

init_options = InitOptions(width=600, height=400, renderer="canvas")

data = DataFrame(dict(a=[1, 2, 3, 4], b=[2, 4, 8, 4], c=[3, -2, 3, 1]))

pie_data = DataFrame(dict(name=["A", "B", "C"], value=[10, 70, 40]))


@ChartRenderer
def render_line_chart():
    return Chart().data(data).encode("a", "b").encode("a", "c", color="pink")


@ChartRenderer
def render_pie_chart():
    return Chart().data(pie_data).series("pie")
