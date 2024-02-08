from echarts4py.express import Bar


def test_bar():
    chart_option = Bar(x="a", y="b", legend={})

    print(chart_option.to_option())

    print(chart_option.to_dict())
