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
            'Info':$resource('api/v1/user/info'),
            'Categories':$resource('api/v1/qna/categories'),
            'Questions': $resource('api/v1/qna/questions'),
            'Quiz':$resource('api/v1/qna/quiz/category/:category',{
                category:'@category'
            })
        }
    }



})();