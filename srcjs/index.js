import * as echarts from "echarts";

class EChartsOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-echarts-output");
  }

  renderValue(el, { data, initOptions, option, theme }) {
    console.log(data, initOptions, option, theme);
    const chart = echarts.init(el, theme, initOptions);
    chart.setOption(option);
  }
}

Shiny.outputBindings.register(
  new EChartsOutputBinding(),
  "shiny-echarts-output",
);
