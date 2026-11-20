// Watch a function climb JSC's tiers, then fall back on a broken guess.
function add(a, b) {
    return a + b;
}

noInline(add);                          // keep `add` separate to watch it alone

let sum = 0;

for (let i = 0; i < 200000; i++) {      // hot loop, integers only
    sum = add(sum, 1) | 0;
}

print("[+] after the 'int' loop: DFG compiles =", numberOfDFGCompiles(add));

add("web", "kit");                      // a string: the int guess fails, OSR exit

for (let i = 0; i < 200000; i++) {      // recompile with the new types
    add("a", i);
}

print("[+] after the mixed types: DFG compiles =", numberOfDFGCompiles(add));

// EOF
