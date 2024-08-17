pragma circom  2.0.0;

template MultiplicationCircuit() {
    signal input a;
    signal input b;

    signal output mult;
    mult <== a*b;

}

component main = MultiplicationCircuit();