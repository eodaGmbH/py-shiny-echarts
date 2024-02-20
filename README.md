# py-shiny-echarts: ECharts for Shiny for Python

[![Release](https://img.shields.io/github/v/release/eodaGmbH/py-shiny-echarts)](https://img.shields.io/github/v/release/eodaGmbH/py-shiny-echarts)
[![pypi](https://img.shields.io/pypi/v/shinyecharts.svg)](https://pypi.python.org/pypi/shinyecharts)
[![Build status](https://img.shields.io/github/actions/workflow/status/eodaGmbH/py-shiny-echarts/pytest.yml?branch=main)](https://img.shields.io/github/actions/workflow/status/eodaGmbH/py-shiny-echarts/pytest.yml?branch=main)
[![License](https://img.shields.io/github/license/eodaGmbH/py-shiny-echarts)](https://img.shields.io/github/license/eodaGmbH/py-shiny-echarts)

[Shiny for Python](https://shiny.posit.co/py/) bindings for [ECharts JS](https://echarts.apache.org/)

## Note

This package is still in an early state.

## Installation

```bash
# Stable
pip install shinyecharts

# Dev
pip install git+https://github.com/eodaGmbH/py-shiny-echarts
```

## Basic usage

```python
from pandas import DataFrame

# Must always be imported, otherwise App is not found
from shiny.express import ui
from shinyecharts import Chart, ChartRenderer, InitOptions

init_options = InitOptions(width=600, height=400)

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
```

```bash
shiny run docs/examples/getting_started/basic_usage.py --reload
```
