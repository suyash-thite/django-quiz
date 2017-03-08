/**
 * Created by aniruddha on 28/2/17.
 */


(function(){

    angular
        .module('quiz.game.controllers')
        .controller('MainquizController',MainquizController);

    MainquizController.$inject = ['$scope','HomeServices','$stateParams'];

    function MainquizController($scope,HomeServices,$stateParams){
        $scope.quizStart = false;
        var quiz_questions = [];
        var curr_question = 0;
        //$scope.i=0;

        // Get Questions of chosen category & delete empty options
        var id = JSON.parse($stateParams.category);
        var questions = HomeServices.Quiz.get({'category':id});
        questions.$promise.then(questionSuccessFn);
        function questionSuccessFn(res){
            angular.forEach(res.data.Quiz,function(question){
                for (var key in question.options){
                    if (key == "number_of_options") {
                        delete question.options[key];
                    }
                }
                quiz_questions.push(question);
            });
        }


        $scope.beginQuiz = function(){
            $scope.quizStart = true;
            $scope.question = quiz_questions[curr_question];
            $scope.options = [];
            angular.forEach($scope.question.options,function(v,k){
               $scope.options.push(v)
            });
        }


    }



})();