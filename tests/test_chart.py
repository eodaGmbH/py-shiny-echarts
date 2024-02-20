from shinyecharts.chart import Chart, InitOptions
from shinyecharts.options import Pie


def test_chart():
    options = InitOptions(height=600, width=400)
    chart = Chart(init_options=options).set_option(Pie())

    # Assert
    print("chart", chart.to_dict())


def test_chart_attr():
    chart = Chart().attr(x_axis=dict(), y_axis=dict())

    print(chart.to_dict())
    print("chart option", chart.get_option())
