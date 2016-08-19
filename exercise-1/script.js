/* You will save your code during today's demos and exercises here. */
$('.frame').fadeOut(4000,'swing');
$('.frame').fadeIn(7000,'swing');
$('h5').addClass("newColor");

function sayHi(){alert('hey whats up');}
$('img').on('click', sayHi);

function fadeMe(){
  $(this).fadeOut(1000);
}
$('.frame').on('click',fadeMe);
$(.string)
