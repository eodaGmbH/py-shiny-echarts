from echarts4py._core import Bar, Line, Scatter
from echarts4py.options import Pie
from pandas import DataFrame


def test_bar():
    # Act
    chart_option = Bar(x="a", y="b", legend={})

    # Assert
    print("bar option", chart_option.to_dict())
    # print(sorted(list(chart_option.to_dict().keys())))
    assert sorted(list(chart_option.to_dict().keys())) == sorted(
        ["xAxis", "yAxis", "legend", "series"]
    )


def test_line():
    # Act
    chart_option = Line(x="a", y="b")

    # Assert
    print("line option", chart_option.to_dict())
    assert list(chart_option.to_dict().keys()) == ["xAxis", "yAxis", "series"]


def test_scatter():
    # Act
    chart_option = Scatter(x="a", y="b")

    # Assert
    print("scatter option", chart_option.to_dict())
    assert list(chart_option.to_dict().keys()) == ["xAxis", "yAxis", "series"]


def test_pie():
    # Prepare
    data = DataFrame([["A", 10], ["B", 20], ["C", 40]], columns=["Category", "Value"])

    # Act
    chart_option = Pie(data=data, name="Category", value="Value")

    # Assert
    # print(chart_option.series)
    print("pie option", chart_option.to_dict())
