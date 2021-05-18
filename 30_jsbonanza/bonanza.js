/*
  Team YIE: Ethan Shenker / Ishita Gupta / William Yin
  SoftDev pd1
  K30 - JSorcery
  2021-05-14
*/

// model for HTML5 canvas-based animation

//access canvas and buttons via DOM
var c = document.getElementById("playground")

//prepare to interact with canvas in 2D
var ctx = c.getContext('2d')

var requestID;  //init global var for use with animation frames

//var clear = function(e) {
var clear = () => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.width, c.height)
};


// initialize images
var img = new Image();
img.src = "catSprite.png"

var draw = () => {
    clear()
    console.log("draw invoked...")
    window.cancelAnimationFrame(requestID);

    ctx.drawImage(img, x, y, 100, 50);

    requestID = window.requestAnimationFrame(draw) // call animation again
};

var setImgCat = () => {
    img.src = "catSprite.png"
    document.getElementById("message").innerHTML = "Have a Cat follow your mouse!"; // changes HTML text
}

var setImgDog = () => {
    img.src = "undertaleDog.jpeg"
    document.getElementById("message").innerHTML = "Have a Dog follow your mouse!"; // changes HTML text
}

document.getElementById("catButton").addEventListener( "click", setImgCat );
document.getElementById("dogButton").addEventListener( "click", setImgDog );


document.getElementById("playground").addEventListener("mousemove", e => {
    x = e.offsetX // distance mouse has travelled from left of canvas
    y = e.offsetY // distance mouse has travelled from top of canvas
    draw()
})