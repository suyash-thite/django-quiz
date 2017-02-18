/**
 * Created by aniruddha on 18/2/17.
 */


(function(){

    angular
    .module('quiz.game.controllers')
    .controller('HomeController', HomeController);

    HomeController.$inject = ['$scope','$cookies','$rootScope'];

    function HomeController($scope,$cookies,$rootScope){

        // redirect to login page if not logged in.
        if(!$cookies.get('Atkn')){
             $rootScope.logged_in = false;
             window.location = '#/login';
        }


    }

})();