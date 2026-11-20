// Objects built the same way share one Structure (hidden class).
let a = { x: 1, y: 2 };
let b = { x: 3, y: 4 };
let c = { y: 5, x: 6 };         // other order: a different Structure

print(describe(a));
print(describe(b));
print(describe(c));

// EOF
