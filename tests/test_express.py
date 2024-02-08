from echarts4py.express import Bar, Line


def test_bar():
    chart_option = Bar(x="a", y="b", legend={})

    print(chart_option.to_option())

    print(chart_option.to_dict())


def test_line():
    chart_option = Line(x="a", y="b")

    print(chart_option.to_dict())
