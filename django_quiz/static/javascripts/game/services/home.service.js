/**
 * Created by aniruddha on 20/2/17.
 */

(function(){

    angular
        .module('quiz.game.services')
        .factory('HomeServices',HomeServices);

    HomeServices.$inject = ['$resource'];

    function HomeServices($resource){
        return{
            'Info':$resource('api/v1/user/info')
        }
    }



})();