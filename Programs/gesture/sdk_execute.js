var localhost = 'http://localhost:8080' + properties.path;

ajax({
  url: localhost,
  type: 'get',
  timeout: 5000,
  success: function(contents) {
    log(contents);

    callbackSuccess({
      resultType: 'continue',
    });
  },
  error: function(request, errorMessage) {
    log('ERROR: ' + errorMessage);

    callbackSuccess({
      resultType: 'continue',
    });
  }
});

return {
  resultType: 'pause'
};
