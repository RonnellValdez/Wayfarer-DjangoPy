console.log("connected");
import bulmaCarousel from '~bulma-carousel/dist/js/bulma-carousel.min.js';

// Initialize all elements with carousel class.
const carousels = bulmaCarousel.attach('.carousel', options);

// To access to bulmaCarousel instance of an element
const element = document.querySelector('#my-element');
if (element && element.bulmaCarousel) {
	// bulmaCarousel instance is available as element.bulmaCarousel
}

// document.getElementById('button').addEventListener('click', function(){
// 	document.querySelector('.bg-modal').style.display = 'flex';
// });