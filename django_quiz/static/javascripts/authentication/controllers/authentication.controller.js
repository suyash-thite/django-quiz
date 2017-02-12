/**
 * Created by aniruddha on 11/2/17.
 */

(function() {


    angular
        .module('quiz.authentication.controllers')
        .controller('AuthenticationController', AuthenticationController);

    AuthenticationController.$inject = ['$scope','Authentication'];

    function AuthenticationController($scope,Authentication){
        console.log("in");

        // Sign Up user
        $scope.signUp = function(){

            var required_object = {
                "first_name":$scope.first_name,
                "last_name":$scope.last_name,
                "username":$scope.username,
                "email":$scope.email,
                "password":$scope.password
            };
           var user =  Authentication.Register.save(required_object);

        }


    }
})();