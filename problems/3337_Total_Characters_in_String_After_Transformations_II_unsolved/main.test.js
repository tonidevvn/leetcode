const { lengthAfterTransformations } = require("./main");

test('test 1', () => {
	expect(
    lengthAfterTransformations(
      "abcyy",
      2,
      [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 2,
      ]
    )
  ).toBe(7);
});

test("test 2", () => {
  expect(
    lengthAfterTransformations(
      "azbk",
      1,
      [
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2,
      ]
    )
  ).toBe(8);
});