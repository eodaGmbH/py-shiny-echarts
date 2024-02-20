from pandas import DataFrame
from shiny.express import ui
from shinyecharts.express import Chart, InitOptions, SeriesType
from shinyecharts.renderer import Chart as BaseChart
from shinyecharts.renderer import ChartRenderer

init_options = InitOptions(width=600, height=400, renderer="canvas")

data = DataFrame(dict(a=[1, 2, 3, 4], b=[2, 4, 8, 4], c=[3, -2, 3, 1], d=[3, 5, 2, 1]))

pie_data = DataFrame(dict(name=["A", "B", "C"], value=[10, 70, 40]))


@ChartRenderer
def render_line_chart():
    return (
        BaseChart(data)
        .attr(legend=dict())
        .configure(width=900, height=600, renderer="svg")
        .encode("a", "b", color="green", type="bar")
        .encode("a", "c", color="pink")
        .encode(x="a", y="d", type=SeriesType.SCATTER, color="yellow")
    )


@ChartRenderer
def render_pie_chart():
    return BaseChart(pie_data).add_series(dict(type=SeriesType.PIE))


@ChartRenderer
def render_scatter_chart():
    return (
        BaseChart(data)
        .add_series(
            dict(type=SeriesType.SCATTER, name="test", encode=dict(x="a", y="b"))
        )
        .attr(legend=dict())
    )
