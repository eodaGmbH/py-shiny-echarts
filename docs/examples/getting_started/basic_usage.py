from echarts4py.chart import Chart, InitOptions
from echarts4py.options import Line
from echarts4py.renderer import ChartRenderer
from pandas import DataFrame

# Must always be imported, otherwise App is not found
from shiny.express import ui

init_options = InitOptions(width=600, height=400, renderer="canvas")

data = DataFrame(
    [[0, 1, 2, 3], [1, 4, 5, 6], [2, -2, 4, 9]],
    columns=["a", "b", "c", "d"],
)


lines = (
    Line(x="a", y="b", tooltip=dict(trigger="axis"), legend=dict())
    .add_series("c")
    .add_series("d")
)


@ChartRenderer
def render_dataset():
    return Chart(init_options, data=data).set_option(lines)
