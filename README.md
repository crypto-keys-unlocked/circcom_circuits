# Circom Circuits

## Repository Overview

This repository serves as a practice ground for various zk-SNARK circuits implemented using Circom. Each circuit is organized into its own directory within the `Circuits` folder, and each problem or circuit is placed in a separate folder named after the problem it solves.

### Structure

- **Circuits/**: This directory contains subdirectories for each circuit problem. Each subdirectory is named after the specific problem and contains the associated `.circom` file along with any input files required for proof generation.

- **commands.py**: A Python script that generates the necessary commands to compile circuits, generate proofs, and verify them. You can specify the name of the circuit as input to this script to automate the process.

- **README.md**: This file, providing an overview of the repository.

- **EXERCISES.md**: A list of exercises that are implemented or planned for future implementation in this repository.


## Background on Zero-Knowledge Proofs (ZKPs)

Zero-Knowledge Proofs (ZKPs) are cryptographic methods that allow one party to prove to another that a statement is true without revealing any additional information beyond the fact that the statement is true. This technology has profound implications for privacy, security, and trust in various applications such as authentication, blockchain, and confidential transactions.

To learn more about Zero-Knowledge Proofs, you can explore the following resources:
- [Zero-Knowledge Proofs Explained](https://blog.chain.link/zero-knowledge-proofs/)
- [An Interactive Introduction to ZKPs](https://crypto.stanford.edu/~dabo/cs255/lectures/zeroknowledge.pdf)
- [Understanding Zero-Knowledge Proofs: A Beginner’s Guide](https://medium.com/@starkware/understanding-zero-knowledge-proofs-from-the-ground-up-98c5e95f5f94)

## Background on Circom

Circom is a domain-specific language and compiler for creating zk-SNARK circuits. These circuits can be used to generate proofs that verify certain computations without revealing the inputs that led to the results. Circom is widely used in blockchain applications, particularly within the Ethereum ecosystem, for creating privacy-preserving smart contracts and other cryptographic protocols.

### How to Install Circom

To install Circom, follow these steps:

1. **Install Node.js**: Ensure that you have Node.js installed on your system. You can download it from [here](https://nodejs.org/).

2. **Install SnarkJS**: SnarkJS is a JavaScript library that interacts with Circom circuits for compiling, setting up, and generating zk-SNARK proofs.

   ```bash
   npm install -g snarkjs
   ```

3. **Install Circom**: You can install Circom using the following commands:

   ```bash
   git clone https://github.com/iden3/circom.git
   cd circom
   cargo build --release
   ```

4. **Add Circom to your PATH**:

   ```bash
   export PATH=$(pwd)/target/release:$PATH
   ```

For detailed installation instructions, you can refer to the [Circom GitHub repository](https://github.com/iden3/circom).


## How to Use the Commands

### Example Workflow for Running a Circuit

To work with an arbitrary circuit in Circom and SnarkJS, you can follow these general steps:

### 1. **Write the Circuit:**

- **Define the circuit** in a `.circom` file using the Circom language. The circuit should specify the inputs, outputs, and the constraints (arithmetic and logic operations).
  
  Example:
  ```circom
  template ExampleCircuit() {
      signal input a;
      signal input b;
      signal output c;

      c <== a + b;
  }

  component main = ExampleCircuit();
  ```

### 2. **Compile the Circuit:**

- Use the Circom compiler to compile the circuit into an R1CS file, which defines the constraints, a `.wasm` file for generating witnesses, and a `.sym` file for the symbolic representation.

  Command:
  ```bash
  circom circuit.circom --r1cs --wasm --sym -o .
  ```

### 3. **Generate the Powers of Tau (Trusted Setup):**

- Before generating a proof, you need to run a ceremony called "Powers of Tau," which is a multiparty computation protocol that provides the common reference string (CRS) for the zk-SNARK proof.

  Commands:
  ```bash
  snarkjs powersoftau new bn128 12 powersOfTau28_hez_final.ptau -v
  snarkjs powersoftau contribute powersOfTau28_hez_final.ptau powersOfTau28_hez_final.ptau --name="First contribution" -v
  snarkjs powersoftau prepare phase2 powersOfTau28_hez_final.ptau powersOfTau28_hez_final.ptau -v
  ```

### 4. **Generate the Witness:**

- Create an `input.json` file with the values for the circuit's inputs.
- Generate the witness file, which is an intermediate representation of the circuit's inputs and outputs.

  Command:
  ```bash
  node circuit_js/generate_witness.js circuit_js/circuit.wasm input.json witness.wtns
  ```

### 5. **Setup the zk-SNARK (or PLONK):**

- Generate a `.zkey` file, which is a proving key needed to create proofs. You can do this using the PLONK setup or Groth16 setup.

  Example (PLONK):
  ```bash
  snarkjs plonk setup circuit.r1cs powersOfTau28_hez_final.ptau circuit_plonk.zkey
  ```

### 6. **Export the Verification Key:**

- Export a verification key from the `.zkey` file, which will be used by the verifier to check the proof.

  Command:
  ```bash
  snarkjs zkey export verificationkey circuit_plonk.zkey verification_key.json
  ```

### 7. **Generate the Proof:**

- Create a proof using the witness and the proving key. The proof is a JSON file that can be sent to a verifier.

  Command:
  ```bash
  snarkjs plonk prove circuit_plonk.zkey witness.wtns proof.json public.json
  ```

### 8. **Verify the Proof:**

- The verifier can check the validity of the proof using the verification key and the public input/output.

  Command:
  ```bash
  snarkjs plonk verify verification_key.json public.json proof.json
  ```

  If everything is correct, SnarkJS will return `OK!`.

### 9. **Optional: Create a Solidity Verifier (if needed for blockchain deployment):**

- If you want to deploy the verifier on a blockchain, generate a Solidity contract for verification.

  Command:
  ```bash
  snarkjs zkey export solidityverifier circuit_plonk.zkey verifier.sol
  ```

These steps provide a general flow for working with arbitrary circuits in Circom and SnarkJS. Depending on your circuit and the proving scheme you choose (Groth16, PLONK, etc.), the steps might slightly vary.

## Exercises

Please refer to `EXERCISES.md` for a comprehensive list of exercises that have been implemented or are planned for this repository. Each exercise is designed to deepen your understanding of Circom and zk-SNARKs through practical implementation.

## Contributing

Contributions are welcome! If you'd like to add a new circuit or improve an existing one, please follow the repository's structure and update the relevant documentation.