from pandas import DataFrame

# Must always be imported, otherwise App is not found
from shiny.express import ui
from shinyecharts import Chart, ChartRenderer

data = DataFrame(
    [[0, 1, 2, 3], [1, 4, 5, 6], [2, -2, 4, 9]],
    columns=["a", "b", "c", "d"],
)


@ChartRenderer
def render_line_chart():
    return (
        Chart(data)
        .configure(width=800, height=600)
        .encode("a", "b")
        .encode("a", "c")
        .encode("a", "d")
        .attr(legend=dict(), tooltip=dict(trigger="axis"))
    )
