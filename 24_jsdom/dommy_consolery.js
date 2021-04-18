// Team haha -- William Yin, Alvin Wu
// SoftDev
// K24 -- Settling in to your DOMicile
// 2021-04-15


//send diagnostic output to console
//(Ctrl-Shift-J in Chromium & Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
// Similar to dictionaries from python.
var o = { 'name' : 'Thluffy',
        // Key will automatically become a string when object is created.
          age : 15,
          items : [10, 20, 30, 40],
          // Can use another object as one of the values in an object.
          morestuff : {a : 1, b : 'ayo'},
          // Can use a function as one of the values.
          func : function(x) {
            return x+30;
          }
        };


//(define fact (lambda (n) ...)
var fact = function(n) {
  var prod=1;
  for ( ; n > 1 ; n--){
    prod = prod * n;
  }
  return prod;
};


//(define fact (lambda (n) ...)
var factR = function(n) {
  if ( n<=1 ) {
    return 1;
  }
  else {
    return n * factR(n-1);
  }
};


// Gets the element with id "thelist" and creates an li element that is a child to thelist.
// Sets the text of the child element to be what is passed in.
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


// Removes the nth li element.
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


// Adds the class "red" to each li element.
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


// Adds either the class "red" or "blue" to each li element depending on if its index is even or odd respectively.
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};


// Prints the string representation of the event that is created when the button is pressed.
var buttonCallback = function(e) {
  console.log("\n\nhere comes e...");
  console.log(e);
  console.log("\n\nhere comes 'this'...");
  console.log(this);
}


// Tells the button to run the buttonCallback function when it is clicked.
var b = document.getElementById('b');
// Click event is automatically passed into buttonCallback as e when the button is clicked.
b.addEventListener('click', buttonCallback);


// This function is assigned to an element and adds the class "red" to its assigned element when it is called.
var redCallback = function(e) {
  console.log("\n\n---redCallback invoked---")
  console.log(this);
  this.classList.add('red');
}


// Assigns functions to elements and the events that must be performed on those elements to trigger those functions.
var thelist = document.getElementById("thelist");
var litems = thelist.children;
for(var i = 0; i < litems.length; i++) {
  litems[i].addEventListener('click', redCallback);
  litems[i].addEventListener('mouseover', function(e){
    console.log("user has moved into this:" + this);
    this.classList.toggle('green');
  });
  litems[i].addEventListener('mouseout', function(e){
    console.log("user has moved out of this:" + this);
    this.classList.toggle('blue');
  });
}
