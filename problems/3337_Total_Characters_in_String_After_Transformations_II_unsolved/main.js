/**
 * @param {string} s
 * @param {number} t
 * @param {number[]} nums
 * @return {number}
 */
var lengthAfterTransformations = function (s, t, nums) {
  const MOD = 10 ** 9 + 7;
  const SIZE = 26;
  const aCharCode = "a".charCodeAt(0);

  // 1. Initialize the initial state vector (V0)
  const initialCounts = new Array(SIZE).fill(0);
  for (const char of s) {
    initialCounts[char.charCodeAt(0) - aCharCode]++;
  }

  // 2. Construct the transformation matrix (M)
  const transformationMatrix = Array(SIZE)
    .fill(null)
    .map(() => Array(SIZE).fill(0));
  for (let i = 0; i < SIZE; i++) {
    const transformationLength = nums[i];
    for (let j = 0; j < transformationLength; j++) {
      const nextCharCode = aCharCode + ((i + 1 + j) % SIZE);
      transformationMatrix[nextCharCode - aCharCode][i] =
        (transformationMatrix[nextCharCode - aCharCode][i] + 1) % MOD;
    }
  }

  // 3. Implement matrix multiplication
  const multiplyMatrices = (mat1, mat2) => {
    const result = Array(SIZE)
      .fill(null)
      .map(() => Array(SIZE).fill(0));
    for (let i = 0; i < SIZE; i++) {
      for (let j = 0; j < SIZE; j++) {
        for (let k = 0; k < SIZE; k++) {
          result[i][j] = (result[i][j] + mat1[i][k] * mat2[k][j]) % MOD;
        }
      }
    }
    return result;
  };

  // 4. Implement matrix exponentiation
  const power = (matrix, n) => {
    let result = Array(SIZE)
      .fill(null)
      .map(() => Array(SIZE).fill(0));
    for (let i = 0; i < SIZE; i++) {
      result[i][i] = 1; // Identity matrix
    }
    while (n > 0) {
      if (n % 2 === 1) {
        result = multiplyMatrices(result, matrix);
      }
      matrix = multiplyMatrices(matrix, matrix);
      n = Math.floor(n / 2);
    }
    return result;
  };

  // 5. Multiply M^t by V0
  const finalTransformationMatrix = power(transformationMatrix, t);
  const finalCounts = new Array(SIZE).fill(0);
  for (let i = 0; i < SIZE; i++) {
    for (let j = 0; j < SIZE; j++) {
      finalCounts[i] =
        (finalCounts[i] + finalTransformationMatrix[i][j] * initialCounts[j]) %
        MOD;
    }
  }

  // 6. Calculate the final length
  let finalLength = 0;
  for (const count of finalCounts) {
    finalLength = (finalLength + count) % MOD;
  }

  return finalLength;
};
exports.lengthAfterTransformations = lengthAfterTransformations;