from shinyecharts.chart import Chart, InitOptions
from shinyecharts.options import Pie


def test_chart():
    options = InitOptions(height=600, width=400)
    chart = Chart(init_options=options).set_option(Pie())

    # Assert
    print("chart", chart.to_dict())
