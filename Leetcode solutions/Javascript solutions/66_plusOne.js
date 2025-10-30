/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let len = digits.length - 1;
    let carry = 1; // Start with a carry of 1 since we are adding one
    
    while (len >= 0 && carry) {
        let total = digits[len] + carry;
        digits[len] = total % 10;
        carry = Math.floor(total / 10); // Update carry for the next iteration
        len--;
    }
    
    // If there's a carry after processing all digits, insert it at the beginning
    if (carry) {
        digits.unshift(carry);
    }
    
    return digits;
};