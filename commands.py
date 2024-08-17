def generate_proof_commands(circuit_name):
    commands = []

    # Step 2: Compile the Circuit
    compile_command = f"circom {circuit_name}.circom --r1cs --wasm --sym -o ."
    commands.append(compile_command)

    # Step 3: Generate the Powers of Tau (Trusted Setup)
    powersoftau_commands = [
        "snarkjs powersoftau new bn128 12 powersOfTau28_hez_final.ptau -v",
        "snarkjs powersoftau contribute powersOfTau28_hez_final.ptau powersOfTau28_hez_final.ptau --name=\"First contribution\" -v",
        "snarkjs powersoftau prepare phase2 powersOfTau28_hez_final.ptau powersOfTau28_hez_final.ptau -v"
    ]
    commands.extend(powersoftau_commands)

    # Step 4: Generate the Witness
    witness_command = f"node {circuit_name}_js/generate_witness.js {circuit_name}_js/{circuit_name}.wasm input.json witness.wtns"
    commands.append(witness_command)

    # Step 5: Setup the zk-SNARK (PLONK)
    setup_command = f"snarkjs plonk setup {circuit_name}.r1cs powersOfTau28_hez_final.ptau {circuit_name}_plonk.zkey"
    commands.append(setup_command)

    # Step 6: Export the Verification Key
    export_vk_command = f"snarkjs zkey export verificationkey {circuit_name}_plonk.zkey verification_key.json"
    commands.append(export_vk_command)

    # Step 7: Generate the Proof
    generate_proof_command = f"snarkjs plonk prove {circuit_name}_plonk.zkey witness.wtns proof.json public.json"
    commands.append(generate_proof_command)

    # Step 8: Verify the Proof
    verify_proof_command = f"snarkjs plonk verify verification_key.json public.json proof.json"
    commands.append(verify_proof_command)

    # # Step 9: Optional: Create a Solidity Verifier
    # solidity_verifier_command = f"snarkjs zkey export solidityverifier {circuit_name}_plonk.zkey verifier.sol"
    # commands.append(solidity_verifier_command)

    return commands

# Get circuit name from user input
circuit_name = input("Enter the circuit name (without .circom): ")

commands = generate_proof_commands(circuit_name)

# Print all commands
for command in commands:
    print(command)
