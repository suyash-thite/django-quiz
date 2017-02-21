/**
 * Created by aniruddha on 21/1/17.
 */

(function(){


angular
    .module('quiz.layout.controllers')
    .controller('NavbarController', NavbarController);

    NavbarController.$inject = ['$rootScope','$cookies','$scope','Unauthenticate'];

    function NavbarController($rootScope,$cookies,$scope,Unauthenticate){

        if($cookies.get('Atkn')){
            $rootScope.logged_in = true;
        }
        else{
            $rootScope.logged_in = false;
        }

        $scope.logout = function(){
            var logout = Unauthenticate.Logout.get();

            logout.$promise.then(logoutSuccessFn);
            function logoutSuccessFn(res){
                console.log(res);
                if(res.status == "Error"){
                 alert(res.error.detail);
                }
                else {
                $cookies.remove('Atkn');
                $rootScope.logged_in = false;
                window.location = '#/login';
                }

            }
        }
    }


})();