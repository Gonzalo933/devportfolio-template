// Nice tutorial here: https://philipwalton.com/articles/the-google-analytics-setup-i-use-on-every-site-i-build/
var dimensions = {
  TRACKING_VERSION: 'dimension1',
};

var gon_analytics = {
  TRACKING_VERSION: '1',
};

window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};
ga('create', 'UA-83860748-1', 'auto');
ga('set', 'transport', 'beacon');
ga('set', dimensions.version, gon_analytics.TRACKING_VERSION);
ga('send', 'pageview');
