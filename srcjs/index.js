import * as echarts from "echarts";

class EChartsOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-echarts-output");
  }

  // TODO: Remove data, it it alread included in 'option'
  renderValue(el, { data, initOptions, option, theme }) {
    console.log(initOptions, option, theme);
    const chart = echarts.init(el, theme, initOptions);
    chart.setOption(option);
    console.log("current options", chart.getOption());
  }
}

Shiny.outputBindings.register(
  new EChartsOutputBinding(),
  "shiny-echarts-output",
);
