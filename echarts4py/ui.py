from htmltools import HTMLDependency, Tag
from shiny import ui
from shiny.module import resolve_id

echarts_bindings_dep = HTMLDependency(
    "echarts-bindings",
    version="1.0.0",
    source={"package": "echarts4py", "subdir": "srcjs"},
    script={"src": "echarts-bindings.js", "type": "module"},
    all_files=False,
)


def output_chart(id: str) -> Tag:
    return ui.div(
        echarts_bindings_dep,
        # Use resolve_id so that our component will work in a module
        id=resolve_id(id),
        class_="shiny-echarts-output",
        style="width: 600px;height:400px;",
    )


"""
def output_chart(id: str):
    pass
"""
