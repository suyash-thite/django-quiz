/**
 * Created by aniruddha on 28/2/17.
 */


(function(){

    angular
        .module('quiz.game.controllers')
        .controller('MainquizController',MainquizController);

    MainquizController.$inject = ['$scope','HomeServices','$stateParams'];

    function MainquizController($scope,HomeServices,$stateParams){
        var my_questions = [];

        // Get Questions of chosen category
        var category = JSON.parse($stateParams.category);
        $scope.category_name = category.category_name;
        var questions = HomeServices.Quiz.get({'category':category.id});
           questions.$promise.then(questionSuccessFn);
           function questionSuccessFn(res){
               angular.forEach(res.data.Quiz,function(question){
                   console.log(question);
                   my_questions.push(question);
               });
           }


    }



})();