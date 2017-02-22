/**
 * Created by aniruddha on 18/2/17.
 */

(function(){

    angular
        .module('quiz.layout.services')
        .factory('Unauthenticate',Unauthenticate);

    Unauthenticate.$inject = ['$resource'];

    function Unauthenticate($resource){
        return {
         Logout:$resource('api/v1/user/logout/')
        }
    }


})();