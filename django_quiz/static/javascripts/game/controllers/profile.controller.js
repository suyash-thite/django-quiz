/**
 * Created by aniruddha on 24/2/17.
 */

(function(){
  angular
    .module('quiz.game.controllers')
    .controller('ProfileController', ProfileController);

    ProfileController.$inject=['$scope'];

    function ProfileController($scope){
        console.log('in');
    }

})();

