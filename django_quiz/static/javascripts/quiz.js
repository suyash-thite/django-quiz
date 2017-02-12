/**
 * Created by gauravkumar on 19/12/16.
 */


angular
    .module('quiz',['ngMaterial',
                    'ngMessages',
                    'material.svgAssetsCache',
                    'ngCookies',
                    'ngResource',
                    'quiz.layout',
                    'quiz.authentication'
                    ]).config(function($resourceProvider) {
                                    $resourceProvider.defaults.stripTrailingSlashes = false;
                                    });

 angular
    .module('quiz')
    .run(run);

  run.$inject = ['$http'];


function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }