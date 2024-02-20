from pandas import DataFrame
from shiny.express import ui

# from shinyecharts.express import Chart, InitOptions, SeriesType
from shinyecharts import Chart, InitOptions, SeriesType
from shinyecharts.renderer import ChartRenderer

init_options = InitOptions(width=600, height=400, renderer="canvas")

data = DataFrame(
    [[0, 1, 2, 3], [1, 4, 5, 6], [2, -2, 4, 9]],
    columns=["a", "b", "c", "d"],
)

pie_data = DataFrame([["A", 10], ["B", 20], ["C", 30]], columns=["name", "value"])


@ChartRenderer
def render_line_chart():
    return Chart(data).encode("a", "b").encode("a", "c", color="pink")


@ChartRenderer
def render_line_chart2():
    return Chart(data, theme="dark").add_series(
        dict(type=SeriesType.LINE, encode=dict(x="a", y="b"), name="b", color="green")
    )


@ChartRenderer
def render_scatter_chart():
    return Chart(data).encode("a", "b", type="scatter")


@ChartRenderer
def render_bar():
    return (
        Chart(data, theme="dark")
        .encode("a", "b", type="bar")
        .encode("a", "c", type="bar")
        .attr(tooltip=dict(trigger="axis"), legend=dict())
    )


@ChartRenderer
def render_pie_chart():
    return Chart(pie_data).add_series(dict(type=SeriesType.PIE))
