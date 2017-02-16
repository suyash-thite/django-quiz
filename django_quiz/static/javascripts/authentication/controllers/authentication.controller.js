/**
 * Created by aniruddha on 11/2/17.
 */

(function() {


    angular
        .module('quiz.authentication.controllers')
        .controller('AuthenticationController', AuthenticationController);

    AuthenticationController.$inject = ['$scope','Authentication'];

    function AuthenticationController($scope,Authentication) {

        // Sign Up user
        $scope.signUp = function () {
            var required_object = {
                "first_name": $scope.first_name,
                "last_name": $scope.last_name,
                "username": $scope.username,
                "email": $scope.email,
                "password": $scope.password
            };
            var user = Authentication.Register.save(required_object);

            user.$promise.then(signUpSuccessFn,signUpErrorFn);

            function signUpSuccessFn(res){
                console.log(res);
            }

            function signUpErrorFn(res){
                console.log(res);
            }

        };

        // Log in User
        $scope.login = function () {
            var required_data = {
                "username": $scope.loginUsername,
                "password": $scope.loginPassword
            };
          var is_authenticated =  Authentication.Login.save(required_data);

          is_authenticated.$promise.then(loginSuccessFn,loginErrorFn);

          function loginSuccessFn(res){
              console.log(res);
          }

          function loginErrorFn(){
              console.log(res);
          }

        }
    }
})();