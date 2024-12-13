const isPalindrome = function(givenStr) {
    const str = givenStr.toLowerCase().replace(/[\W_]+/g, '');
    let e = str.length - 1 ;

    for (let s = 0; s < str.length/2; s++){
        if (str[s] !== str[e]) {
            return false;
        }
        e--;
    }

    return true;
};

