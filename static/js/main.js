"use strict";

var app = angular.module('housingApp', ['ngRoute']);

app.controller('mainController', function($scope){
	//do nothing
});

$(document).ready(function(){
	$('#to-top').click(function(){
        $('html, body').animate({scrollTop:$('#top').position().top}, 'slow');
    });
})