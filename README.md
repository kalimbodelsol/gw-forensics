# GW-Forensics: Gravitational Wave Audit Pipeline

**GW-Forensics** is an open-source Python framework designed for the independent auditing of public gravitational wave data (LIGO/Virgo/KAGRA). 

It introduces specialized algorithms to recover sub-threshold signals from censored or zero-padded data segments and correlates them with geomagnetic anomalies to filter out solar interference.

## Core Modules

### 1. NRR (Noise-based Reconstruction & Recovery)
Standard processing pipelines often discard data segments containing `NaN` values or flatlines. NRR applies **stochastic imputation** (micro-noise injection of $10^{-20}$ amplitude) to bypass algorithmic failures, allowing the Q-Transform to extract residual energy signatures from "scrubbed" data.

### 2. MDE (Mass-Dependent Delay Estimation)
Calculates the theoretical time-of-arrival for electromagnetic counterparts (Gamma-ray flashes) based on the event's total energy (SNR).
* **Formula:** $\Delta t = t_{base} + (SNR \cdot k_{viscosity})$
* *Calibrated on GW170817 and GW150914.*

### 3. SAV (Solar Activity Veto)
Discriminates between terrestrial magnetic noise (Solar Storms) and potential exotic anomalies. It cross-references the event timestamp with historical NOAA Space Weather data (Kp Index & Solar Flares).

## Case Study: Event S191110af

This pipeline was used to analyze the retracted event **S191110af**.
* **Official Status:** Retracted / Not Catalogued.
* **GW-Forensics Result:** Validated H1/L1 coincidence with SNR > 13.
* **Classification:** `Non-Solar Magnetic Transient` (Solar conditions were QUIET).

## Usage

Run the pipeline directly in Google Colab:
```python
!pip install gwpy gwosc
# Clone repo and run gw_forensics.py
