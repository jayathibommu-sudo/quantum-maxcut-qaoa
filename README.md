# PS-O1 — Max-Cut on Weighted Graphs with QAOA

## Overview
This project studies the weighted Max-Cut problem using a p=1 Quantum Approximate Optimization Algorithm (QAOA) circuit, exhaustive classical search, constrained transpilation, and noisy simulation.

## Reproducible configuration
- Graph: `networkx.erdos_renyi_graph(n=6, p=0.5, seed=42)`
- Edge weights: integers from 1 to 5, assigned using `random.Random(42)`
- QAOA: `p=1`, `gamma=0.5`, `beta=0.25` for the main processor comparison
- Basis gates: `rz`, `sx`, `x`, `cx`
- Transpiler optimization level: 1; transpiler seed: 42
- Noisy simulation: 4096 shots, simulator seed 42
- Noise assumptions: single-qubit depolarizing error 0.001, CX depolarizing error 0.005, readout error 0.01

## Processor configurations
- **Processor A:** five-qubit linear chain. The full problem requires six logical qubits, so this processor is infeasible for the full workload. No score is fabricated for it.
- **Processor B:** nine-qubit 3x3 grid. The notebook transpiles the circuit to this coupling map and simulates it with the stated noise model.

## How to run
1. Open `main.ipynb` in Google Colab or Jupyter.
2. Run all cells from top to bottom.
3. The notebook computes the graph, classical optimum, parameter sweep, transpilation metrics, noisy result metrics, and figures.
4. The notebook saves generated CSV and PNG outputs in its working directory. Move/copy those outputs into `results/tables/` and `results/figures/` if running locally.

## Results interpretation
The notebook calculates metrics from the simulation output during execution. Do not treat previous run values as guaranteed outputs until you run this exact notebook. Circuit-depth and CX-count deltas are proxies for routing overhead, not an exact SWAP count.

## Limitations
The experiment uses a small graph and fixed QAOA parameters. Noise values are assumptions for simulation, not device calibration data. This experiment does not establish quantum advantage.
