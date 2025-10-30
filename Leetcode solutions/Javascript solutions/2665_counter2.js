/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    newVal = init
    return {
        increment : () => {
            newVal = newVal + 1
            return newVal
        },
        decrement : () => {
            newVal = newVal - 1;
            return newVal
        },
        reset : () => {
            newVal = init
            return newVal
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */