/**
 * Created by aniruddha on 18/2/17.
 */


(function(){

    angular
    .module('quiz.game.controllers')
    .controller('HomeController', HomeController);

    HomeController.$inject = ['$scope','$cookies','$rootScope','Authentication','HomeServices','$rootScope'];

    function HomeController($scope,$cookies,$rootScope,Authentication,HomeServices){

        // redirect to login page if not logged in.
        if($cookies.get('Atkn')){
            var is_authenticated =  Authentication.Authenticate.get();
            is_authenticated.$promise.then(isAuthenticatedSuccess);
            function isAuthenticatedSuccess(res){
                if (res.status == 'Error') {
                    $cookies.remove('Atkn');
                    $rootScope.logged_in = false;
                    window.location = '#/login';
                }
                else{
                    $rootScope.logged_in = true;
                    window.location = '#/'
                }
            }
        }
        else{
            $rootScope.logged_in = false;
            window.location = '#/login';
        }


        //Get Info about logged in user
        var user_info = HomeServices.Info.get();
        user_info.$promise.then(UserSuccessFn);
        function UserSuccessFn(res){
            var data = res.data.User;
            $rootScope.user = {
                'first_name': data.first_name,
                'last_name': data.last_name,
                'email': data.email,
                'user_id': data.id
            }
        }

        // Get Categories
        var categories = HomeServices.Categories.get();
        categories.$promise.then(CategorySuccessFn);
        function CategorySuccessFn(res){
             $scope.category1 = (res.data.Categories)[0];
             $scope.category2 = (res.data.Categories)[1];
             $scope.category3 = (res.data.Categories)[2];
        }





    }

})();