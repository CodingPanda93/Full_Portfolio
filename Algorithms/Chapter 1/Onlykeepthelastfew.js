
function keepLastFew(arr, num) {
    arr = arr.slice(arr.length - num, arr.length);
    return arr;
}
