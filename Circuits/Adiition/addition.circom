pragma circom 2.0.0;

template AdditionCircuit() {
    // Define the input signals
    signal input a;
    signal input b;

    // Define the output signal
    signal output sum;

    // The sum is the addition of a and b
    sum <== a + b;
}

// Instantiate the template to be used as the main circuit
component main = AdditionCircuit();
