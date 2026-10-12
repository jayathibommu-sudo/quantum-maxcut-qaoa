# Phase 1 Report — Max-Cut on Weighted Graphs Using QAOA

## Objective
Implement a reproducible six-node weighted Max-Cut problem, evaluate a p=1 QAOA circuit, and compare a logical baseline with two participant-defined processor topologies.

## Problem generation
The notebook creates an Erdős–Rényi graph using `n=6`, `p=0.5`, and seed 42. Edge weights are integers from 1 to 5 assigned with `random.Random(42)`. The classical optimum is computed by exhaustive search at notebook runtime.

## Quantum method
The notebook creates a six-qubit QAOA p=1 circuit using Hadamard initialization, weighted RZZ cost interactions, RX mixer rotations, and measurements. Four parameter pairs are evaluated with a simulator. The Processor B run uses 4096 shots and the stated fixed noise assumptions.

## Processor comparison
Processor A is a five-qubit linear chain and is infeasible for the full six-qubit workload. Processor B is a nine-qubit 3x3 grid. The notebook computes transpilation depth and CX gate counts for baseline and Processor B.

## Results
Run `main.ipynb` to calculate the exact cut values, noisy metrics, circuit depths, CX counts, and plots. The repository includes a graph visualization and CSV templates; no unverified simulation numbers are presented as measured results.

## Noise assumptions
Single-qubit depolarizing error 0.001, CX depolarizing error 0.005, and symmetric readout error 0.01. These are simulation assumptions, not measured device calibration data.

## Limitations
Depth/CX differences are routing-overhead proxies, not an exact SWAP count. The small simulation and selected parameters do not establish quantum advantage.
