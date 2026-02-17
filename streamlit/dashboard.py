import streamlit as st
import numpy as np

from python.regime_engine import compute_regime

st.set_page_config(
    page_title="Quantum Bloomberg Regime Monitor",
    layout="wide"
)

st.title("📈 Quantum Bloomberg Regime Monitor")

st.markdown("---")

st.sidebar.header("Model Controls")

direction = st.sidebar.slider("Directional Bias (q0)", 0.0, 1.0, 0.5)
coherence = st.sidebar.slider("Cross-Index Coherence (q1)", 0.0, 1.0, 0.5)
volatility = st.sidebar.slider("Volatility / Instability (q2)", 0.0, 1.0, 0.5)

features = {
    "q0": direction,
    "q1": coherence,
    "q2": volatility
}

probs, regime = compute_regime(features)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Trend Probability", f"{probs['001']:.3f}")

with col2:
    st.metric("Transition Probability", f"{probs['110']:.3f}")

with col3:
    st.metric("Residual / Noise", f"{probs['other']:.3f}")

st.markdown("---")

if "RISK-ON" in regime:
    color = "🟢"
elif "TRANSITION" in regime:
    color = "🟠"
else:
    color = "🔴"

st.subheader(f"Market Regime: {color} {regime}")

st.markdown("---")

st.caption("Hybrid Classical–Quantum Regime Detection Engine")
