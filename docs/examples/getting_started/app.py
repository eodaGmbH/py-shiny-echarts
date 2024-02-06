from echarts4py.chart import Chart, InitOptions
from echarts4py.renderer import ChartRenderer
from shiny.express import ui

options = InitOptions(width=600, height=400)

bar = {
    "xAxis": {"data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},
    "yAxis": {},
    "series": [{"type": "bar", "data": [23, 24, 18, 25, 27, 28, 25]}],
}

stacked_bar = {
    "xAxis": {"data": ["A", "B", "C", "D", "E"]},
    "yAxis": {},
    "series": [
        {"data": [10, 22, 28, 43, 49], "type": "bar", "stack": "x"},
        {"data": [5, 4, 3, 5, 10], "type": "bar", "stack": "x"},
    ],
}


line = {
    "xAxis": {"type": "category", "data": ["A", "B", "C"]},
    "yAxis": {"type": "value"},
    "series": [
        {"data": [150, 200, 100], "type": "line"},
        {"data": [50, 100, 160], "type": "line"},
    ],
}


pie = {
    "series": [
        {
            "type": "pie",
            "data": [
                {"value": 335, "name": "Direct Visit"},
                {"value": 234, "name": "Union Ad"},
                {"value": 1548, "name": "Search Engine"},
            ],
        }
    ]
}

pie_ring = {
    "title": {"text": "A Case of Doughnut Chart", "left": "center", "top": "center"},
    "series": [
        {
            "type": "pie",
            "data": [
                {"value": 335, "name": "A"},
                {"value": 234, "name": "B"},
                {"value": 1548, "name": "C"},
            ],
            "radius": ["40%", "70%"],
        }
    ],
}

pie_rose = {
    "series": [
        {
            "type": "pie",
            "data": [
                {"value": 100, "name": "A"},
                {"value": 200, "name": "B"},
                {"value": 300, "name": "C"},
                {"value": 400, "name": "D"},
                {"value": 500, "name": "E"},
            ],
            "roseType": "area",
        }
    ]
}

scatter = {
    "xAxis": {},
    "yAxis": {},
    "series": [
        {"type": "scatter", "data": [[10, 5], [0, 8], [6, 10], [2, 12], [8, 9]]}
    ],
}


@ChartRenderer
def render_bar():
    return Chart(options, theme="dark").add(bar)


@ChartRenderer
def render_stacked_bar():
    return Chart(options, theme=None).add(stacked_bar)


@ChartRenderer
def render_line():
    return Chart(options).add(line)


@ChartRenderer
def render_pie():
    return Chart(options, theme=None).add(pie)


@ChartRenderer
def render_pie_ring():
    return Chart(options).add(pie_ring)


@ChartRenderer
def render_pie_rose():
    return Chart(options, theme=None).add(pie_rose)


@ChartRenderer
def render_scatter():
    return Chart(options).add(scatter)
