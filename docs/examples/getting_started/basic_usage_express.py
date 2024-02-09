from pandas import DataFrame

# Must always be imported, otherwise App is not found
from shiny.express import ui
from shinyecharts.chart import Chart, InitOptions
from shinyecharts.options import Bar, ChartOption, Line, Pie, Scatter
from shinyecharts.renderer import ChartRenderer

# General options
options = InitOptions(width=600, height=400, renderer="canvas")

# Line chart
line_data = DataFrame(
    [
        [0, 1, 2, 3],
        [0.7, 2, 3, 4],
        [1, 0.4, 5, 6],
        [1.4, 2, 3, 4],
        [2, -2, 4, 9],
        [3, 1, 6, 7],
    ],
    columns=["a", "b", "c", "d"],
)
lines = (
    Line(
        x="a", y="b", legend={}, tooltip={"trigger": "axis"}, xAxis={"type": "category"}
    )
    .add_series("c", series_options={"type": "bar"})
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
            [27, 11, 9, 27, 29, 18, 45],
        )
    ),
    columns=["month", "2023", "2024", "2035"],
)

bars = (
    Bar(x="month", y="2023", legend={})
    .add_series("2024")
    .add_series("2025", series_options={"type": "line"})
)


@ChartRenderer
def render_bars():
    return Chart(options, data=bar_data).set_option(bars)


# Scatter chart
scatter_data = DataFrame(
    [[10, 5, 4], [0, 8, 3], [6, 10, 12], [2, 12, 6], [8, 9, 7]], columns=["x", "y", "z"]
)

scatter = Scatter("x", "y", legend={}, data=scatter_data).add_series(
    "z", series_options={"type": "bar"}
)


@ChartRenderer
def render_scatter():
    return Chart(options).set_option(scatter)


# Pie chart
pie_data = DataFrame([["A", 10], ["B", 20], ["C", 40]], columns=["name", "value"])
# pie_data = [dict(name=x, value=y) for x, y in zip(["A", "B", "C", "D"], [10, 40, 5, 9])]

pie = Pie(
    # data=pie_data
    series_options=dict(roseType="area"),
    legend=dict(),
    tooltip=dict(trigger="item"),
    title={"text": "Awesome", "x": "right"},
)


@ChartRenderer
def render_pie():
    return Chart(options, data=pie_data).set_option(pie)
