from echarts4py.chart import Chart, InitOptions
from echarts4py.option import ChartOption
from echarts4py.renderer import ChartRenderer
from pandas import DataFrame

# Must always be imported, otherwise App is not found
from shiny.express import ui

options = InitOptions(width=600, height=400, renderer="canvas")

data = DataFrame(
    [[0, 1, 2, 3], [1, 4, 5, 6], [2, -2, 4, 9]],
    columns=["a", "b", "c", "d"],
)


lines = ChartOption(
    tooltip={"trigger": "axis"},
    legend={},
    series=[
        {"name": "L1", "type": "line", "encode": {"x": "a", "y": "b"}},
        {"name": "L2", "type": "line", "encode": {"x": "a", "y": "d"}},
        {"name": "L3", "type": "line", "encode": {"x": 0, "y": "c"}},
    ],
)


@ChartRenderer
def render_dataset():
    return Chart(options, data=data).set_option(lines)
