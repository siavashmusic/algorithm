function binary_search(haystack, needle) {
  let low = 0;
  let high = haystack.length - 1;

  do {
    let mid = Math.floor((low + high) / 2);
    let guess = haystack[mid];
    if (guess === needle) {
      return mid;
    } else if (guess > needle) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  } while (low <= high);

  return false;
}

