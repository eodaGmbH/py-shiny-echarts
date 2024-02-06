import * as echarts from "echarts";

class EChartsOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-echarts-output");
  }

  renderValue(el, { data, initOptions, options, theme }) {
    console.log(data, initOptions, options, theme);
    const chart = echarts.init(el, theme, initOptions);
    options.forEach((option) => chart.setOption(option));
  }
}

Shiny.outputBindings.register(
  new EChartsOutputBinding(),
  "shiny-echarts-output",
);
