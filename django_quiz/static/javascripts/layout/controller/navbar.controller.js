/**
 * Created by aniruddha on 21/1/17.
 */

(function(){


angular
    .module('quiz.layout.controllers')
    .controller('NavbarController', NavbarController);

    NavbarController.$inject = ['$scope','$cookies'];

    function NavbarController($scope,$cookies){
        if($cookies.get('Token')){
            $scope.logged_in = true;
        }
        else{
            $scope.logged_in = false;
        }
    }


})();