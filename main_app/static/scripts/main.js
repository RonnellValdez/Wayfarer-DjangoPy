console.log("connected");
// import bulmaCarousel from '~bulma-carousel/dist/js/bulma-carousel.min.js';

// // Initialize all elements with carousel class.
// const carousels = bulmaCarousel.attach('.carousel', options);

// // To access to bulmaCarousel instance of an element
// const element = document.querySelector('#my-element');
// if (element && element.bulmaCarousel) {
// 	// bulmaCarousel instance is available as element.bulmaCarousel
// };

console.log("working");
// To activate the hamburger menu in the navabar
$(".navbar-burger").click(function () {
	// Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
	$(".navbar-burger").toggleClass("is-active");
	$(".navbar-menu").toggleClass("is-active");
});


$(".modal-button").click(function() {
	let target = $(this).data("target");
	$("html").addClass("is-clipped");
	$(target).addClass("is-active");
});

$(".modal-close").click(function() {
	$("html").removeClass("is-clipped");
	$(this).parent().removeClass("is-active");
});

let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}


// Thumbnail image controls
function currentSlide(n) {
	showSlides(slideIndex = n);
}
