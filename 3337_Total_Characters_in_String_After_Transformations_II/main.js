/**
 * @param {string} s
 * @param {number} t
 * @param {number[]} nums
 * @return {number}
 */
var lengthAfterTransformations = function (s, t, nums) {
  const MOD = 10 ** 9 + 7;
  const aCharCode = "a".charCodeAt(0);
  const zCharCode = "z".charCodeAt(0);
  const charMap = new Map();
  let currentString = s;

  for (let k = 0; k < t; k++) {
    let nextString = "";

    for (let i = 0; i < currentString.length; i++) {
      const charCode = currentString.charCodeAt(i);
      let newChars = charMap.get(charCode);
      if (!newChars) {
        let transformationLength = nums[charCode - aCharCode];
        let nextCharCode = charCode;
        newChars = "";
        for (let j = 0; j < transformationLength; j++) {
          nextCharCode =
            nextCharCode + 1 > zCharCode ? aCharCode : nextCharCode + 1;
          newChars += String.fromCharCode(nextCharCode);
        }
        charMap.set(charCode, newChars);
      }
      nextString += newChars;
    }
    currentString = nextString;
  }

  return currentString.length % MOD;
};

exports.lengthAfterTransformations = lengthAfterTransformations;