/**
 * Created by aniruddha on 28/2/17.
 */


(function(){

    angular
        .module('quiz.game.controllers')
        .controller('MainquizController',MainquizController);

    MainquizController.$inject = ['$scope','HomeServices','$stateParams'];

    function MainquizController($scope,HomeServices,$stateParams){

        // Get Questions of chosen category
        var category = JSON.parse($stateParams.category);
        var questions = HomeServices.Questions.get({'category':category.id,'is_play':false});
           questions.$promise.then(questionSuccessFn);
           function questionSuccessFn(res){
               console.log(res);
           }
    }



})();