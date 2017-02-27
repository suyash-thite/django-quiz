/**
 * Created by aniruddha on 19/2/17.
 */



(function(){

 angular
    .module('quiz.game.services')
    .factory('HomeFactory',HomeFactory);

    HomeFactory.$inject=['$resource'];

    function HomeFactory($resource){
        return{
            Info:$resource('api/v1/user/info/')
        }

    }


})();
