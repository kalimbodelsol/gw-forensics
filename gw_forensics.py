# ==============================================================================
# GW-FORENSICS: TOROIDAL PHASE & ASYMMETRY DETECTOR
# Version: 1.1 (Density Ladder Release)
# Hypothesis: Matter-to-Waveform Phase Transition (Toroidal Decomposition)
# ==============================================================================

import sys
try:
    import gwpy
except ImportError:
    print("Error: 'gwpy' not found. Install via: pip install gwpy")
    sys.exit()

from gwpy.timeseries import TimeSeries
import numpy as np

# --- CONFIGURATION: THE DENSITY LADDER ---
# Events sorted by mass/density to demonstrate the "U-Curve" scaling law.
TARGETS = [
    # ZONE 1: MATTER FRAGMENTATION (Neutron Stars & Hybrids)
    {'name': 'GW170817', 'gps': 1187008882.4, 'type': '1. BNS (Matter Breakup)'},
    {'name': 'GW200115', 'gps': 1263090623.6, 'type': '1. NSBH (Vortex Clash)'},
    
    # ZONE 2: VACUUM VALLEY (Standard Black Holes)
    {'name': 'GW150914', 'gps': 1126259462.4, 'type': '2. BBH (Symmetric Vacuum)'},
    {'name': 'GW151226', 'gps': 1135136350.6, 'type': '2. BBH (Symmetric Vacuum)'},

    # ZONE 3: CRITICAL DENSITY (Super-Massive / Toroidal Phase)
    {'name': 'GW190521', 'gps': 1242442967.4, 'type': '3. IMBH (Toroidal Vector)'},
    {'name': 'GW190412', 'gps': 1239082262.2, 'type': '3. BBH (Recoil/Kick)'}
]

def analyze_topology(series):
    """
    Calculates the Topological Asymmetry Factor (A).
    A > 2.0 indicates a Unipolar Transient (Vector Pulse).
    """
    try:
        val = series.value
        # Filter extreme electronic glitches (>8 sigma)
        val = val[np.abs(val) < 8 * np.std(val)]
        
        max_v = np.max(val)
        min_v = np.min(val)
        
        if abs(min_v) == 0: min_v = 1e-15
        
        # Calculate Asymmetry Ratio
        ratio = abs(max_v / min_v)
        
        # Normalize (always >= 1.0)
        if ratio < 1.0: ratio = 1.0 / ratio
        
        return ratio
    except:
        return -1.0

def run_audit():
    print(f"{'EVENT':<15} | {'TYPE':<28} | {'H1':<5} | {'L1':<5} | {'V1':<5} | {'VERDICT'}")
    print("-" * 85)

    for evt in TARGETS:
        gps = evt['gps']
        name = evt['name']
        etype = evt['type']
        
        scores = {'H1': -1.0, 'L1': -1.0, 'V1': -1.0}
        
        for det in ['H1', 'L1', 'V1']:
            try:
                # Fetch 1s around merger, Bandpass 20-300Hz (Astrophysical Range)
                data = TimeSeries.fetch_open_data(det, gps-0.5, gps+0.5, verbose=False)
                data = data.bandpass(20, 300)
                scores[det] = analyze_topology(data)
            except:
                pass # Detector offline

        # Format Scores
        s_h1 = f"{scores['H1']:.2f}" if scores['H1'] != -1 else "-"
        s_l1 = f"{scores['L1']:.2f}" if scores['L1'] != -1 else "-"
        s_v1 = f"{scores['V1']:.2f}" if scores['V1'] != -1 else "-"
        
        # Classification Logic
        kicks = sum(1 for s in scores.values() if s > 2.0)
        valid = sum(1 for s in scores.values() if s != -1)
        
        verdict = "SYMMETRIC"
        if kicks >= 1: verdict = "VECTOR PULSE" 
        if kicks > 1 and valid > 1: verdict = "GLOBAL SHOCK"
        if "Vacuum" in etype and kicks == 0: verdict = "CLEAN WAVE" # Confirmation for Zone 2

        print(f"{name:<15} | {etype:<28} | {s_h1:<5} | {s_l1:<5} | {s_v1:<5} | {verdict}")

if __name__ == "__main__":
    print("--- GW-FORENSICS v1.1: STARTING AUDIT ---")
    run_audit()
    
