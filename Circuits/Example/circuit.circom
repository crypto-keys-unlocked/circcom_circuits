template ExampleCircuit() {
    signal input a;
    signal input b;
    signal output c;

    c <== a + b;
}

component main = ExampleCircuit();
