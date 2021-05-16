console.log("connected");
import bulmaCarousel from '~bulma-carousel/dist/js/bulma-carousel.min.js';

// Initialize all elements with carousel class.
const carousels = bulmaCarousel.attach('.carousel', options);

// To access to bulmaCarousel instance of an element
const element = document.querySelector('#my-element');
if (element && element.bulmaCarousel) {
	// bulmaCarousel instance is available as element.bulmaCarousel
}

<<<<<<< HEAD
// document.getElementById('button').addEventListener('click', function(){
// 	document.querySelector('.bg-modal').style.display = 'flex';
// });
=======

// To activate the hamburger menu in the navabar
$(".navbar-burger").click(function () {
	// Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
	$(".navbar-burger").toggleClass("is-active");
	$(".navbar-menu").toggleClass("is-active");
  });
>>>>>>> submaster
