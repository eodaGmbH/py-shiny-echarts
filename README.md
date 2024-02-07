# py-shiny-echarts: ECharts for Shiny for Python

[![Release](https://img.shields.io/github/v/release/eodaGmbH/py-shiny-echarts)](https://img.shields.io/github/v/release/eodaGmbH/py-shiny-echarts)
[![pypi](https://img.shields.io/pypi/v/shiny-echarts.svg)](https://pypi.python.org/pypi/shiny-echarts)
[![Build status](https://img.shields.io/github/actions/workflow/status/eodaGmbH/py-shiny-echarts/pytest.yml?branch=main)](https://img.shields.io/github/actions/workflow/status/eodaGmbH/py-shiny-echarts/pytest.yml?branch=main)
[![License](https://img.shields.io/github/license/eodaGmbH/py-shiny-echarts)](https://img.shields.io/github/license/eodaGmbH/py-shiny-echarts)

[Shiny for Python](https://shiny.posit.co/py/) bindings for [ECharts JS](https://echarts.apache.org/)

## Installation

```bash
pip install git+https://github.com/eodaGmbH/py-shiny-echarts
```

## Basic usage

```python
from echarts4py.chart import Chart, InitOptions
from echarts4py.option import ChartOption
from echarts4py.renderer import ChartRenderer
from pandas import DataFrame

# Must always be imported, otherwise App is not found
from shiny.express import ui

options = InitOptions(width=600, height=400, renderer="canvas")

data = DataFrame(
    [[0, 1, 2, 3], [1, 4, 5, 6], [2, -2, 4, 9]],
    columns=["a", "b", "c", "d"],
)


lines = ChartOption(
    tooltip={"trigger": "axis"},
    legend={},
    series=[
        {"name": "L1", "type": "line", "encode": {"x": 0, "y": 1}},
        {"name": "L2", "type": "line", "encode": {"x": 0, "y": 2}},
        {"name": "L3", "type": "line", "encode": {"x": 0, "y": 3}},
    ],
)


@ChartRenderer
def render_dataset():
    return Chart(options, data=data).set_option(lines)
```

```bash
shiny run docs/examples/getting_started/basic_usage.py --reload
```