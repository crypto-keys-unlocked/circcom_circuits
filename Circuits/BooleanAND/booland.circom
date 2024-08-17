pragma circom 2.0.0;

template isValidBoolean() {
    signal input in; 
    signal output isValid;

    // Check if the input is either 0 or 1
    isValid <== 1 - (in * (in - 1));
}

template BooleanAndCircuit() {
    signal input a;
    signal input b;

    signal output and;
    signal output isValidA;
    signal output isValidB;

    component validA = isValidBoolean();
    component validB = isValidBoolean();

    validA.in <== a;  
    validB.in <== b;    

    isValidA <== validA.isValid;
    isValidB <== validB.isValid;

    and <== a * b;
}

component main = BooleanAndCircuit();
