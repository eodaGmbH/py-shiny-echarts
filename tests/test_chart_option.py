from echarts4py.options import ChartOption


def test_chart_options():
    options = ChartOption(legend={})
    print(options.to_dict())

    assert list(options.to_dict().keys()) == ["legend", "xAxis", "yAxis", "series"]
