"use strict";

var i = [0];
var images = [];
var time = 3000;
images[1] = "./assets/images/hero1.jpg";
images[2] = "./assets/images/hero2.jpg";
images[3] = "./assets/images/hero3.jpg";
images[4] = "./assets/images/sky.jpg";

function changeImg() {
  if (i < images.length) {
    document.slide.src = images[i];
    i++;
  } else {
    i = 0;
  }

  setTimeout("changeImg()", time);
}

window.onload = changeImg;
$(document).ready(function () {
  $('.logo').click(function () {
    window.location.href = '/';
  });
  $('.login').click(function () {
    window.location.href = '/login';
  });
  $('.signup').click(function () {
    window.location.href = '/signup';
  });
  $('.abt').click(function () {
    window.location.href = '/about';
  });
  $('.tour').click(function () {
    window.location.href = '/tours';
  });
  $('.fb').click(function () {
    window.location.href = 'facebook.com/erekereng';
  });
  $('.ig').click(function () {
    window.location.href = 'instagram.com/erekereng';
  });
  $('.twi').click(function () {
    window.location.href = 'twitter.com/erekereng';
  });
  $('.tour').click(function () {
    window.location.href = '/tours';
  });
});
//# sourceMappingURL=script.dev.js.map
