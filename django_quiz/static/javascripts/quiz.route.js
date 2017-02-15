/**
 * Created by gauravkumar on 19/12/16.
 */


(function () {
    angular
    .module('quiz.routes')
    .config(config);

    function config($locationProvider,$stateProvider){

        $stateProvider
            .state('register',{
                url:'',
                templateUrl: '/static/templates/register.html',
                controller: 'AuthenticationController'
            }).state('login',{
                url:'/',
                templateUrl:'/static/templates/login.html',
                controller: 'AuthenticationController'
            });
        $locationProvider.hashPrefix("");

    }

})();