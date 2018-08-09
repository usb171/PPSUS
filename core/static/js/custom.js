
function simpleSlider(type){
	var sliderActive = $("#slider .sliderActive");
		if(type == 'prev') {
			var sliderPrev   = sliderActive.prev().length ? sliderActive.prev() : $("#slider li:last");
              sliderPrev.addClass('sliderActive').fadeIn();
		} else {
              var sliderNext   = sliderActive.next().length ? sliderActive.next() : $("#slider li:first");
              sliderNext.addClass('sliderActive').fadeIn();
          }
          sliderActive.removeClass('sliderActive').fadeOut();
}

$(document).ready(function(){

  $('.scrollspy').scrollSpy({
    scrollOffset: 265
  });

  $('.slider').slider({
    indicators: false,
    interval: 2000,
    height: 600
  });

  $(".button-collapse").sideNav();
  $('.carousel').carousel();
  $('.collapsible').collapsible();
  $('.modal').modal();
  $('.tooltipped').tooltip({delay: 50});
  $('select').material_select();


  $('.datepicker').pickadate({
	 monthsFull: [ 'Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro' ],
	 selectMonths: true,
	 selectYears: true,
   selectMonths: true, // Creates a dropdown to control month
   selectYears: 30, // Creates a dropdown of 15 years to control year,
	 clear: false,
	 format: 'dd/mm/yyyy',
	 today: "Hoje",
	 close: "Ok",
   closeOnSelect: true // Close upon selecting a date,
  });

  $('.timepicker').pickatime({
    default: 'now',
    twelvehour: false, // change to 12 hour AM/PM clock from 24 hour
    donetext: 'OK',
    autoclose: false,
    vibrate: true // vibrate the device when dragging clock hand
    });
});
