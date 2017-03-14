/**
 * Created by aniruddha on 28/2/17.
 */


(function(){

    angular
        .module('quiz.game.controllers')
        .controller('MainquizController',MainquizController);

    MainquizController.$inject = ['$scope','HomeServices','$stateParams','$timeout'];

    function MainquizController($scope,HomeServices,$stateParams,$timeout){
        $scope.quizStart = false;
        var quiz_questions = [];
        var curr_question = 0;
        var id = JSON.parse($stateParams.category);
        //$scope.i=0;

        //Get Category Info
        $scope.chosen_category = HomeServices.CategoryDetail.get({'category':id});

        // Get Questions of chosen category & delete empty options
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

        // begin the quiz
        $scope.beginQuiz = function(){
            $scope.quizStart = true;
            var max_questions = quiz_questions.length;
            if (curr_question < max_questions) {
                $scope.question = quiz_questions[curr_question];
                $scope.options = [];
                angular.forEach($scope.question.options, function (v, k) {
                    $scope.options.push(v)
                });
            }
            else{
                console.log('Quiz Finished');
            }
        };


        $scope.checkanswer = function(){
          var user_answer = {
              'answer':$scope.answer
              };
          var is_correct = HomeServices.CheckAnswer.get(user_answer,{'question_id':$scope.question.id});
          curr_question += 1;
          $scope.beginQuiz();
        };


    }



})();