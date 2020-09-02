//sticky navbar jscript
window.addEventListener('scroll', function(){
	var nav = document.querySelector('nav');
	var lo = document.getElementById('logo');
	var fav = document.getElementById('favicon');
	nav.classList.toggle('sticky', window.scrollY > 0);

	if (nav.classList.contains('sticky')) {
		lo.setAttribute('src','{% static "images/logos/logoa1.png" %}');
		fav.setAttribute('href','{% static "images/f2.png" %}');
	} else {
		lo.setAttribute('src','{% static "images/logos/logo1.png" %}');
		fav.setAttribute('href','{% static "images/f1.png" %}');
	}
});

//navbar jscript
const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");

//burger open animation
hamburger.addEventListener("click", () => {
	navLinks.classList.toggle("open");
	links.forEach(link => {
	link.classList.toggle("fade");
	});

	//burger animation
	hamburger.classList.toggle('toggle');
});

//scroll to top function
function topFunction() {
	document.body.scrollTop = 0;
	document.documentElement.scrollTop = 0;
}

//scroll to projects
function projectsFunction() {
	document.body.scrollTop = 500;
	document.documentElement.scrollTop = 500;
}

//iFrame javascript
function resizeIFrameToFitContent(iFrame) {
	Frame.width  = iFrame.contentWindow.document.body.scrollWidth;
	iframesFrame.height = iFrame.contentWindow.document.body.scrollHeight;
}

//resize a certain iframe:
window.addEventListener('DOMContentLoaded', function(e) {
	var iFrame = document.getElementById( 'iFrame1' );
	resizeIFrameToFitContent( iFrame );

	// or, to resize all iframes:
	var iframes = document.querySelectorAll("iframe");
	for( var i = 0; i < iframes.length; i++) {
		resizeIFrameToFitContent( iframes[i] );
	}
});

