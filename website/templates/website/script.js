//using a polyfill for safary to have smooth scroling behavior. for more info: https://github.com/iamdustan/smoothscroll
// using jQuery

var activeImage = 0;
var allimages = $(".img");
var allImagesPossitionLefts = [];

calcScrollPositionsForWindowScroll();

$(document).ready(function () {
  $("#container").on("scroll", function () { // on scroll check active image
    CheckForNewActiveImageBasedOnScroll();
  });
  $(window).on("resize", function () { // on resize recalculate scroll possitions
    calcScrollPositionsForWindowScroll();
  });
});

function calcScrollPositionsForWindowScroll() {
  allImagesPossitionLefts = [];
  $(".img").each(function () {
    var scrollPossition =
      $(this).position().left - ($(window).width() - $(this).width()) / 2;
    if (scrollPossition < 0) {
      scrollPossition = 0;
    } else if (scrollPossition > $("#wrapper").width()) {
      scrollPossition = $("#wrapper").width() - 100;
    }
    allImagesPossitionLefts.push(scrollPossition);
  });
  // console.log(allImagesPossitionLefts);
}

// --- 3 exemples of valid function calls to move carousel ---
// activateImage(8);
// activateImage(undefined, true);
// activateImage(undefined, false, true);

function activateImage(imgNbr, next, previous) {
  var scrollTime = 400; // time it takes to mae the scroll
  if (next) { 
    activeImage++; // acrtivate the next img

    if (activeImage > allImagesPossitionLefts.length - 1) { //if the next img is after the last one
      activeImage = 0; // select first image
    }

    $("#container").animate(
      { scrollLeft: allImagesPossitionLefts[activeImage], behavior: "smooth" },
      scrollTime
    );
  } else if (previous) {
    activeImage--;

    if (activeImage < 0) {
      activeImage = allImagesPossitionLefts.length - 1;
    }

    $("#container").animate(
      { scrollLeft: allImagesPossitionLefts[activeImage], behavior: "smooth" },
      scrollTime
    );
  } else {
    activeImage = imgNbr;

    if (activeImage > allImagesPossitionLefts.length - 1) {
      activeImage = 0;
    } else if (activeImage < 0) {
      activeImage = allImagesPossitionLefts.length - 1;
    }

    $("#container").animate(
      { scrollLeft: allImagesPossitionLefts[activeImage], behavior: "smooth" },
      scrollTime
    );
  }
}

function CheckForNewActiveImageBasedOnScroll() {
  // determin new active image based on scroll position
  var scrollPosition = $("#container").scrollLeft();
  for (i in allImagesPossitionLefts) {
    // see for all images if it is within range of being active
    if (
      // if scroll postiono of window is within 25 of scroll position of img
      allImagesPossitionLefts[i] < scrollPosition + 25 &&
      allImagesPossitionLefts[i] > scrollPosition - 25
    ) {
      activeImage = i; // if true activate that image
      console.log("New active image: " + i);
    }
  }
  if (
    scrollPosition >
    allImagesPossitionLefts[allImagesPossitionLefts.length - 2] + 200 // compage scrolle to befor last possition plus some room for error, 200 here
  ) {
    activeImage = allImagesPossitionLefts.length - 1; // activate last
    console.log("New active image: " + i);
  }
}