from pandas import DataFrame
from shinyecharts.express import Chart


def test_chart():
    # Prepare
    data = DataFrame([[1, 2], [2, 4]], columns=["x", "y"])

    # Act
    chart = Chart().dark().data(data).encode("x", "y")
    print(chart._option)
    print(chart.to_dict())

    chart_dict = chart.to_dict()

    # Assert
    assert chart_dict["theme"] == "dark"
