<?php


function binary_search(array $haystack, int $needle) {
    $low = 0;
    $high = count($haystack) - 1;

    while ($low <= $high) {
        $mid = intval($low + ( $high - $low) / 2);

        $guess = $haystack[$mid];
        //print($guess);
        if ($guess == $needle) {
            return $mid;
        } elseif ($guess < $needle) {
            $low = $mid + 1;
        } else {
            $high = $mid - 1;
        }
    }

    return false;
}


//
$mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17];
echo(binary_search($mylist, 7));


