
//it's used to change the background color of a navigation bar based on the scrolling position of the window.
var navbar = document.getElementById('web-navbar');
window.onscroll = function () {
    if (window.pageYOffset > 300) {
        navbar.style.background = "#555555";
    } else {
        navbar.style.background = "transparent";
    }
}
