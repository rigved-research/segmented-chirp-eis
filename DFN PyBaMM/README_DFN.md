# Segmented-Chirp-EIS – DFN PyBaMM

**Note:**  
The datafiles required for all figures in this section (Figures 9-11) can be downloaded from the 
following link: https://drive.google.com/drive/folders/1qP_ItZE9ZMHxyiDmv_j5SqhSs5BICrKY?usp=sharing

This folder contains dataset of chirp-based impedance datase for DFN model simulation
of LGM50 battery using PyBaMM and segmented chirp algorithm. 
The files correspond to the results presented in Figures 9-11 of the manuscript.

---

## Datafiles

### Figure 9 – 0.001 Hz to 10 kHz Segmented Chirp EIS for SoC=0.5, Temp = 25 degree C 
- Full_SoC_0.5.Temp_298.15.tf_2s.amp_0.1.f0_0.001Hz.ff_10000Hz.mat
---

## Figure 10, 11 – 0.01 Hz to 10 kHz Segmented Chirp EIS for SoC=(0.2,0.5,0.8); Temp = (-10,10,25,40) degree C
- Full_SoC_0.2.Temp_263.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.2.Temp_283.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.2.Temp_298.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.2.Temp_313.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.5.Temp_263.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.5.Temp_283.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.5.Temp_298.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.5.Temp_313.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.8.Temp_263.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.8.Temp_283.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.8.Temp_298.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.8.Temp_313.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat

---

## Scripts

- Plot_EIS.m — Produces Nyquist (EIS) plots for Figures 9(a), and 10.
- Error_plot_combined.m — Produces error plots for Figures 9(b) and 10.

---

## Instructions for Use

### 1. Load a dataset in MATLAB
```matlab
load('filename.mat')
```
(Or double-click the file in MATLAB.)

### 2. Each `.mat` file loads the following variables
- `f` — Frequency vector (chirp simulation)
- `F` — Frequency vector (conventional simulation)
- `z_chirp` — Impedance from chirp excitation
- `Z` — Reference/conventional impedance
- `error` — Relative absolute error

### 3. Run scripts to reproduce the figures
- `Plot_EIS.m` → Figures 9(a), 10.
- `Error_plot_combined.m` → Figures 9(b) and 11.

### 4. Error computation
- Error values are precomputed and stored in each `.mat` file.
- The formula is included as comments inside the scripts.

---

