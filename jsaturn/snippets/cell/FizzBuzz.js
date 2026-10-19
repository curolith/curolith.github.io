console.log(`For details about FizzBuzz see <a href="https://en.wikipedia.org/wiki/Fizz_buzz">Wikipedia</a>`);
console.log(new Array(16).keys()
    .map(x => ((x % 3 === 0 ? "Fizz" : "") + (x % 5 === 0 ? "Buzz" : "")) || x)
    .reduce((r, n) => r+", "+n));