
# db2-quantum-pipeline
=======
# Quantum Bloomberg DB2 Analytics Pipeline

This repository contains a complete hybrid **classical + quantum analytics pipeline** that integrates:

- **IBM Db2** for market data storage & feature engineering  
- **Python** for feature extraction and quantum data formatting  
- **Qiskit** for probabilistic regime detection  
- **Streamlit** for live dashboard visualization

---

## Repository Structure
Db2 → Feature Engineering → Python → Quantum Circuit → Regime Probabilities → Dashboard


Pipeline stages:

1. **Db2 Layer**
   - Stores structured market data
   - Computes normalized statistical features

2. **Python Layer**
   - Pulls features from Db2
   - Maps features → quantum rotation angles

3. **Quantum Layer (Qiskit)**
   - Encodes market state into qubits
   - Produces probabilistic regime distribution

4. **Visualization Layer (Streamlit)**
   - Displays trend / transition probabilities
   - Highlights market regimes

---

## Quantum Semantics

Qubit interpretation:

| Qubit | Financial Meaning |
|------|-------------------|
| q0 | Directional Bias |
| q1 | Cross-Index Coherence |
| q2 | Volatility / Instability |

Example regime states:

- `001` → Stable trend / risk-on behavior  
- `110` → Rotational / transitional regime  

---

## Repository Structure
db2-quantum-pipeline/
│
├── db2/
│ ├── 01_create_market_data.sql
│ ├── 02_insert_sample_data.sql
│ └── 03_quantum_features_view.sql
│
├── python/
│ ├── db2_pull_features.py
│ ├── quantum_circuit.py
│ └── regime_engine.py
│
├── streamlit/
│ └── dashboard.py
│
├── requirements.txt
└── README.md
---

## Running the Dashboard

Install dependencies:


pip install -r requirements.txt


bash streamlit run streamlit/dashboard.py

---

After this change your repository will look like a **very credible IBM / Quant / Quantum Finance project**.

If you want next, we can:

✅ Add regime gauges like Bloomberg  
✅ Add live probability charts  
✅ Connect Streamlit ↔ Python ↔ Db2 live  






# Quantum Bloomberg DB2 Analytics Pipeline

Hybrid Classical + Quantum Market Regime Detection

---

## Overview

This repository implements a **hybrid classical–quantum analytics pipeline** inspired by institutional market monitoring workflows.

The system combines:

- **IBM Db2** → Market data storage & feature engineering  
- **Python** → Feature extraction & quantum parameter mapping  
- **Qiskit** → Quantum probabilistic regime modeling  
- **Streamlit** → Interactive Bloomberg-style dashboard  

The objective is to demonstrate how classical financial signals can be transformed into
**quantum state representations** for regime analysis.

---

## Architecture






