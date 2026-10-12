# Quantum Max-Cut: A Comparative Study of QAOA and Classical Optimization

## Problem Statement
Max-Cut is a graph optimization problem that divides vertices into two groups to maximize the number of edges connecting different groups.

## Objective
Explore the Max-Cut problem and compare a classical optimization baseline with the Quantum Approximate Optimization Algorithm (QAOA).

## Technologies
- Python
- Qiskit
- Qiskit Aer
- SciPy
- NetworkX
- Matplotlib
- Google Colab

## Classical Baseline
The example graph contains 5 vertices and 7 edges.

The classical exhaustive-search baseline found a best cut value of 5.

## Quantum Approach
The project aims to implement QAOA and evaluate its performance against the classical baseline. Quantum results must be generated and verified before the comparison is complete.

## How to Run
1. Open `main.ipynb` in Google Colab.
2. Install dependencies using `requirements.txt`.
3. Run the notebook cells in order.

## Limitations
The current classical experiment uses a small graph. Simulation results alone do not demonstrate quantum advantage.
