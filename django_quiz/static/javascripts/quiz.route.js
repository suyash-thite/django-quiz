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
                templateUrl: '/static/templates/authentication/register.html',
                controller: 'AuthenticationController'
            }).state('login',{
                url:'/login',
                templateUrl:'/static/templates/authentication/login.html',
                controller: 'AuthenticationController'
            }).state('home',{
                url:'/',
                templateUrl: '/static/templates/home/home.html',
                controller: 'HomeController'
            }).state('profile',{
                url:'/myProfile',
                templateUrl: '/static/templates/home/profile.html',
                controller: 'ProfileController'
            }).state('game',{
                url:'/game/:category',
                templateUrl: '/static/templates/home/game.html',
                controller: 'MainquizController'
            });
        $locationProvider.hashPrefix("");

    }

})();