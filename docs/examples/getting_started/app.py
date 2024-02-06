from echarts4py.chart import Chart
from echarts4py.renderer import ChartRenderer
from shiny.express import ui

# from echarts4py.ui import output_chart

ui.div("echarts4py")


@ChartRenderer
def render_chart():
    return Chart()
