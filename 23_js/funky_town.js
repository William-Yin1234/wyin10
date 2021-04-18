// Team haha -- William Yin, Alvin Wu
// SoftDev
// K23 -- JS Functionality
// 2021-04-15
// --------------------------------------------------

//CARRY OVER YOUR BEST JS fxns here
let factR = (n) => {
    if (n <= 1) {
        return 1;
    }

    return n * factR(n - 1);
};

let factI = (n) => {
    let start = n;
    let fact = 1;
    while (start >= 1) {
        fact *= start;
        start--;
    }

    return fact;
};


let fibR = (n) => {
    if (n === 1) {
        return 1;
    } else if (n === 0) {
        return 0;
    }

    return fibR(n - 1) + fibR(n - 2);
};

let fibI = (n) => {
    let counter = 2;
    let n_1 = 1;
    let n_2 = 0;
    let fib_num = n_1 + n_2;
    while (counter < n) {
        n_2 = n_1;
        n_1 = fib_num;
        fib_num = n_1 + n_2;
        counter++;
    }
    return fib_num;
};


// ~~~ NEXT STEPS  ~~~
// as a duo...
// pair programming style


//Develop, then implement gcd(a,b), which returns the greatest common divisor of a and b.
let gcd = (a, b) => {
    let smaller = (a < b) ? a : b;
    while (smaller > 1) {
        if (b % smaller == 0 && a % smaller == 0) {
            return smaller;
        }
        smaller--;
    }
    return smaller;
};

//Develop, then implement randomStudent(), which returns a randomly selected name from a list.
let randomStudent = (students) => {
    return students[Math.floor(Math.random() * students.length)];
};

//You may want to create helper functions or external list variables here.
let students = ["Alvin Wu", "William Yin", "John Doe", "Jane Doe", "Theodore Roosevelt", "Abraham Lincoln", "George Washington"];

//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
