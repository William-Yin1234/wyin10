// Team smoothBrain -- William Yin, Jessica Yeung
// SoftDev pd1
// K27 -- canvas based JS animation
// 2021-05-07

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById("buttonCircle");// GET DOT BUTTON
var stopButton = document.getElementById("buttonStop");// GET STOP BUTTON
var dvdButton = document.getElementById("buttonDvD");

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");// YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = "red" // YOUR CODE HERE

var requestID = 0;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
    // YOUR CODE HERE
    ctx.clearRect(0, 0, c.width, c.height);
};


var radius = 0;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
    if (requestID === 0) animateCircle();
};

var animateCircle = () => {
    // YOUR CODE HERE
    stopIt();
    clear();
    ctx.beginPath();

    // arc draws the circle shape, but cannot immediatly be seen on the canvas
    ctx.arc(c.width / 2, c.height / 2, radius, 0, (2 * Math.PI));

    // stroke adds an outline to the circle shape so that it can be seen
    ctx.stroke();

    // fill fills in the circle, finishing our shape
    ctx.fill();

    if (radius >= c.width / 2) {
        growing = false
    } else if (radius <= 0) {
        growing = true;
    }
    if (growing) radius++;
    else radius--;

    requestID = window.requestAnimationFrame(animateCircle);
};

var logo = new Image();
logo.src = "logo_dvd.jpg"
var dx = 1;
var dy = 1;
var x = c.width / 2;
var y = c.height / 2;
var width;
var height;
var drawDvD = () => {
    ctx.drawImage(logo, x, y, logo.width / 5, logo.height / 5);
    width = logo.width / 5;
    height = logo.height / 5;

    if (requestID === 0) animateDvD();
};

var animateDvD = () => {
    stopIt();
    clear();

    if (x + width >= c.width || x <= 0) {
        dx = -dx;
    }
    if (y + height >= c.height || y <= 0) {
        dy = -dy;
    }

    ctx.drawImage(logo, x, y, width, height);

    x = x + dx;
    y = y + dy;

    requestID = window.requestAnimationFrame(animateDvD);
};

//var stopIt = function() {
var stopIt = () => {
    // YOUR CODE HERE
    if (requestID !== 0) {
        window.cancelAnimationFrame(requestID);
        requestID = 0;
    }
};

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", drawDvD);
stopButton.addEventListener("click", stopIt);
