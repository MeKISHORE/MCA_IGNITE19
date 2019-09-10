$(document).ready(function(){

  var w = window.innerWidth;
  var h = window.innerHeight;

  var boxAmount = 10;
  if (w > 1000) {
    boxAmount += 10
  } else if (w < 500) {
    boxAmount -= 5;
  }

  for (var i = 0; i < boxAmount; i++) {

      $('.grid').append('<div class="ani ani'+i+'">');
      num = Math.random() * h + 1;
      num2 = Math.random() * w + 1;
      $('.ani'+i+'').css('top',num).css('left',num2);
      
  }


  $('.start').on('click', function(){
    $(this).addClass('op');
    setTimeout (function(){
      $('.start').remove();
      $('.shape-contain').append('<div class="container">'
        + '<div class="p1"></div>'
        + '<div class="p2"></div>'
        + '</div>');
    },1000);
    setTimeout (function(){
      $('.container').append('<div class="p3"></div>');
    },2500);
    setTimeout (function(){
      $('.container').append('<div class="p4"></div><div class="p5"></div>');
    },3000);
    setTimeout (function(){
      $('.container').append('<div class="p4"></div><div class="p6"></div><div class="p7"></div><div class="p23"></div><div class="p32"></div>');
    },3200);
    setTimeout (function(){
      $('.container').append('<div class="p33"></div><div class="p34"></div><div class="p35"></div><div class="p8"></div><div class="p9"></div><div class="p10"></div><div class="p11"></div><div class="p12"></div><div class="p13"></div><div class="p14"></div><div class="p15"></div><div class="p16"></div><div class="p17"></div><div class="p18"></div><div class="p19"></div><div class="p20"></div><div class="p21"></div><div class="p22"></div>');
    },3700);
    setTimeout (function(){
      $('.container').append('');
    },3800);
  });

});