from pandas import DataFrame

# Must always be imported, otherwise App is not found
from shiny.express import ui
from shinyecharts import Chart, ChartRenderer, InitOptions

init_options = InitOptions(width=600, height=400, renderer="canvas")

data = DataFrame(
    [[0, 1, 2, 3], [1, 4, 5, 6], [2, -2, 4, 9]],
    columns=["a", "b", "c", "d"],
)


@ChartRenderer
def render_dataset():
    return (
        Chart(data, init_options)
        .encode("a", "b")
        .encode("a", "c")
        .encode("a", "d")
        .attr(legend=dict(), tooltip=dict(trigger="axis"))
    )
