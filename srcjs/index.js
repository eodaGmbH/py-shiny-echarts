class EChartsOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-echarts-output");
  }

  renderValue(el, payload) {
    console.log(payload);
  }
}

Shiny.outputBindings.register(
  new EChartsOutputBinding(),
  "shiny-echarts-output",
);
