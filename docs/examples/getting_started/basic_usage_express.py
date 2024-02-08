from echarts4py.chart import Chart, InitOptions
from echarts4py.express import Bar, Line, Pie, Scatter
from echarts4py.option import ChartOption
from echarts4py.renderer import ChartRenderer
from pandas import DataFrame

# Must always be imported, otherwise App is not found
from shiny.express import ui

# General options
options = InitOptions(width=600, height=400, renderer="canvas")

# Line chart
line_data = DataFrame(
    [[0, 1, 2, 3], [1, 4, 5, 6], [2, -2, 4, 9]],
    columns=["a", "b", "c", "d"],
)
lines = (
    Line(x="a", y="b", legend={}, tooltip={"trigger": "axis"})
    .add_series("c")
    .add_series("d")
)


@ChartRenderer
def render_lines():
    return Chart(options, data=line_data).set_option(lines)


# Bar chart
bar_data = DataFrame(
    list(
        zip(
            ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            [23, 24, 18, 25, 27, 28, 25],
            [27, 14, 8, 29, 29, 18, 45],
        )
    ),
    columns=["month", "2023", "2024"],
)

bars = Bar(x="month", y="2023", legend={}).add_series("2024")


@ChartRenderer
def render_bars():
    return Chart(options, data=bar_data).set_option(bars)


# Scatter chart
scatter_data = DataFrame(
    [[10, 5, 4], [0, 8, 3], [6, 10, 12], [2, 12, 6], [8, 9, 7]], columns=["x", "y", "z"]
)

scatter = Scatter("x", "y", legend={}).add_series("z")


@ChartRenderer
def render_scatter():
    return Chart(options, data=scatter_data).set_option(scatter)


# Pie chart
pie_data = DataFrame([["A", 10], ["B", 20], ["C", 40]], columns=["Category", "Value"])

pie = Pie(
    name="Category",
    value="Value",
    data=pie_data,
    legend={},
    tooltip={"trigger": "item"},
)


@ChartRenderer
def render_pie():
    return Chart(options).set_option(pie)
