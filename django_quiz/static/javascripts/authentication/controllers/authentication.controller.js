/**
 * Created by aniruddha on 11/2/17.
 */

(function() {


    angular
        .module('quiz.authentication.controllers')
        .controller('AuthenticationController', AuthenticationController);

    AuthenticationController.$inject = ['$scope','Authentication','$cookies','$rootScope'];

    function AuthenticationController($scope,Authentication,$cookies,$rootScope) {

        // redirect to homepage if logged in.
        if($cookies.get('Atkn')){
             $rootScope.logged_in = true;
             window.location ='#/';
        }


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
                $cookies.put('Atkn',res.data.User.token);
                $rootScope.logged_in = true;
                window.location ='#/';
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
              $cookies.put("Atkn",res.data.User.token);
              $rootScope.logged_in = true;
              window.location ='#/';
          }

          function loginErrorFn(){
              console.log(res);
          }


        }
    }
})();