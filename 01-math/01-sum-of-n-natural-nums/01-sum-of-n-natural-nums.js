var ts_sum_of_n_natural_numbers = function (n) {
    var result = 0;
    for (var i = 1; i <= n; i++) {
        result += i;
    }
    return result;
};
console.log(ts_sum_of_n_natural_numbers(5));
