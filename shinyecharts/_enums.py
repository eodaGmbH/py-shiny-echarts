from enum import Enum


class SeriesType(str, Enum):
    LINE = "line"
    BAR = "bar"
    PIE = "pie"
    SCATTER = "scatter"
    EFFECT_SCATTER = "effectScatter"
    RADAR = "radar"
    TREE = "tree"
    TREEMAP = "treemap"
    SUNBURST = "sunburst"
    BOXPLOT = "boxplot"
