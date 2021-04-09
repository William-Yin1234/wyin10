// Team sleep dep from spring break -- William Yin, Helena Williams
// SoftDev
// K21 -- Get Scripty
// 2021-04-09


let factR = (n) => {
    if (n === 1) {
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
