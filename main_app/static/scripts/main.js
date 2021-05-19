
// To activate the hamburger menu in the navabar
$(".navbar-burger").click(function () {
	// Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
	$(".navbar-burger").toggleClass("is-active");
	$(".navbar-menu").toggleClass("is-active");
});



// document.querySelector('.close').addEventListener('click', function() {
// 	document.querySelector('.bg-modal').style.display = "none";
// });

// $(".modal-button").click(function() {
// 	let target = $(this).data("target");
// 	$("html").addClass("is-clipped");
// 	$(target).addClass("is-active");
// });

// $(".modal-close").click(function() {
// 	$("html").removeClass("is-clipped");
// 	$(this).parent().removeClass("is-active");
// });


var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  
}


// // Login
// document.getElementById('log-in-tag').addEventListener('click', function() {
// 	document.querySelector('.bg-modal').style.display = "flex";
// });