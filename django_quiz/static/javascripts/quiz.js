/**
 * Created by gauravkumar on 19/12/16.
 */


angular
    .module('quiz',['ngMaterial',
        'ngMessages',
        'ngCookies',
        'ngResource',
        'quiz.routes',
        'quiz.layout',
        'quiz.authentication',
        'quiz.game'
    ]).factory('httpRequestInterceptor',['$cookies', function ($cookies) {
        return {
            request: function (config) {
                var token = $cookies.get('Atkn');
                if(token) {
                    config.headers['Authorization'] =" "+"Token"+" "+ token;
                }
                return config;
            }
        };
    }]).config(function($resourceProvider,$httpProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;
        $httpProvider.interceptors.push('httpRequestInterceptor');
    });


angular
    .module('quiz.routes',['ui.router']);

 angular
    .module('quiz')
    .run(run);

  run.$inject = ['$http'];


function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }