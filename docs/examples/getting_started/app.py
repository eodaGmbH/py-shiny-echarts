from echarts4py.chart import Chart, InitOptions
from echarts4py.renderer import ChartRenderer
from shiny.express import ui

options = InitOptions(width=800, height=600)

bar = {
    "xAxis": {"data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},
    "yAxis": {},
    "series": [{"type": "bar", "data": [23, 24, 18, 25, 27, 28, 25]}],
}

ui.div("echarts4py")


@ChartRenderer
def render_chart():
    return Chart(options, theme="dark").add(bar)
