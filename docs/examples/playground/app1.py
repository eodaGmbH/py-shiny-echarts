from pandas import DataFrame
from shiny.express import ui
from shinyecharts.express import Chart, InitOptions
from shinyecharts.renderer import ChartRenderer

init_options = InitOptions(width=600, height=400, renderer="canvas")

data = DataFrame(
    [[0, 1, 2, 3], [1, 4, 5, 6], [2, -2, 4, 9]],
    columns=["a", "b", "c", "d"],
)


@ChartRenderer
def render_lines():
    return Chart().data(data).encode("a", "b").encode("a", "c", color="pink")


@ChartRenderer
def render_scatter():
    return Chart().data(data).encode("a", "b", type="scatter")


@ChartRenderer
def render_bar():
    return Chart().data(data).encode("a", "b", type="bar").encode("a", "c", type="bar")
