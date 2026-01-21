# GW-Forensics v1.1: Toroidal Asymmetry & Vector Recoil Detector

### Abstract
**GW-Forensics** is an audit pipeline designed to analyze high-frequency gravitational wave data for **non-oscillatory topological defects** and **vector asymmetry**.

While standard matched-filtering searches for symmetric wavelets (oscillating strain), this tool screens for unipolar transients ("Kicks") associated with the **Matter-to-Waveform Phase Transition**.

### Theoretical Framework (v1.1 Update)
Based on data mining of O1-O3 runs, we propose a density-dependent scaling law for gravitational wave generation. The model moves beyond thermodynamic annihilation, proposing a **Toroidal Decomposition**:
1.  **Infalling Matter** is decomposed into coherent waveforms.
2.  At critical density (IMBH/Super-Massive), these summate into a **Toroidal Super-Structure** (macroscopic quantum object).
3.  The formation of this ring generates a **Unipolar Vector Pulse** (Asymmetry > 2.0) rather than isotropic thermal noise.

### The "U-Curve" Evidence
Our population study reveals a specific Asymmetry signature based on density:
* **Zone 1: Matter Fragmentation (Neutron Stars)**
    * High Asymmetry ($\mathcal{A} \approx 1.8 - 2.2$) due to physical crust/fluid breakup. (e.g., GW170817).
* **Zone 2: The Vacuum Valley (Standard BBH)**
    * Low Asymmetry ($\mathcal{A} \approx 1.0 - 1.3$). Clean, symmetric spacetime coalescence. (e.g., GW150914).
* **Zone 3: Critical Density (Super-Massive / IMBH)**
    * High, Directional Asymmetry ($\mathcal{A} > 2.5$). Consistent with the **Toroidal Phase Transition**. (e.g., GW190521).

### Methodology
The core algorithm calculates the **Topological Asymmetry Factor ($\mathcal{A}$)** on band-passed strain data (20-300Hz):

$$\mathcal{A} = \left| \frac{\text{max}(h(t))}{\text{min}(h(t))} \right|$$

-   **$\mathcal{A} \approx 1.0$**: Symmetric Wave.
-   **$\mathcal{A} > 2.0$**: Vector Recoil / Toroidal Pulse.

### Usage
Run `gw_forensics.py` to fetch open data from LOSC and perform the topological audit.


