/*
No javascript has been added to this file.
Instead, code has been changed in these two files in the standard Sphinx extension:
Python37/Lib/site-packages/sphinx_copybutton/static/copybutton.js
Python37/Lib/site-packages/sphinx_copybutton/static/copybutton.css
*/

theTopButton = document.getElementById("topButton");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    theTopButton.style.display = "block";
  } else {
    theTopButton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
function overlayOn() {
  document.getElementById("overlay").style.display = "block";
}

function overlayOff() {
  document.getElementById("overlay").style.display = "none";
}