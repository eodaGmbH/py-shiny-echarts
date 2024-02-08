from echarts4py.express import Bar, Line, Pie
from pandas import DataFrame


def test_bar():
    chart_option = Bar(x="a", y="b", legend={})

    print(chart_option.to_option())

    print(chart_option.to_dict())


def test_line():
    chart_option = Line(x="a", y="b")

    print(chart_option.to_dict())


def test_pie():
    data = DataFrame([["A", 10], ["B", 20], ["C", 40]], columns=["Category", "Value"])

    chart_option = Pie(data=data, name="Category", value="Value")

    print(chart_option.series)
    print(chart_option.to_dict())
