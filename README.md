# GW-Forensics v1.1: Toroidal Asymmetry Detector

### Abstract
**GW-Forensics** is an audit pipeline designed to analyze high-frequency gravitational wave data.
It screens for **non-oscillatory topological defects** and **vector asymmetry** ("Kicks") that standard matched-filtering often discards as noise.

### The Theory: Toroidal Phase Transition
This tool validates a specific physical model regarding the formation of Event Horizons.
We propose that during high-density mergers, matter does not simply disappear but undergoes a **Phase Transition** into a coherent **Toroidal Super-Structure**.
This structural formation generates a **Unipolar Vector Pulse** (Asymmetry) rather than isotropic thermal noise.

### Validated Evidence (The Density Scale)
Our analysis of O1-O3 data reveals a density-dependent scaling law:

* **Zone 1: Matter Fragmentation (Neutron Stars)**
    * High Asymmetry ($\mathcal{A} \approx 1.8 - 2.2$) caused by physical matter breakup.
    * *Example:* GW170817.

* **Zone 2: The Vacuum Valley (Standard Black Holes)**
    * Low Asymmetry ($\mathcal{A} \approx 1.0$). Clean, symmetric spacetime coalescence.
    * *Example:* GW150914.

* **Zone 3: Critical Density (Super-Massive / IMBH)**
    * **High Vector Asymmetry** ($\mathcal{A} > 2.5$). Consistent with the coherent Toroidal Pulse emission.
    * *Example:* GW190521 (Visible on L1 detector only, implying vector directionality).

### Methodology
The algorithm calculates the **Topological Asymmetry Factor ($\mathcal{A}$)** on band-passed strain data (20-300Hz):

$$\mathcal{A} = \left| \frac{\text{max}(h(t))}{\text{min}(h(t))} \right|$$

-   **$\mathcal{A} \approx 1.0$**: Symmetric Wave.
-   **$\mathcal{A} > 2.0$**: Vector Pulse / Recoil.

### Usage
Run `gw_forensics.py` to fetch open data from LOSC and perform the topological audit on the target list.
