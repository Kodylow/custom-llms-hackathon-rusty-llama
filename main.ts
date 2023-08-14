type MaybeNumber = number | string;

function add(a: MaybeNumber, b: MaybeNumber): MaybeNumber {
  return a + b; // This could be string concatenation or number addition. Who knows?
}
