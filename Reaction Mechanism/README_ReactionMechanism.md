# Segmented-Chirp-EIS – Reaction Mechanism

**Note:**  
The datafiles required for all figures in this section (Figures 4–8) can be downloaded from the following link:  
https://drive.google.com/drive/folders/1J-2GV99jn5CFh7NhR-Fz-34wdC53-82I?usp=sharing


This dataset contains chirp-based impedance simulations for three nonlinear electrochemical mechanisms (Mech1, Mech2, Mech3). The files correspond to the results presented in Figures 4–8 of the manuscript.

---

## Datafiles

## Figure 4 – Three-Segments Chirp EIS
- Mech2_Vac0_0.001.Rs_10.Vdc_0.3.b1_5.f0_1000Hz.ff_10000Hz.tf_2s.Idx_1.mat
- Mech2_Vac0_0.001.Rs_10.Vdc_0.3.b1_5.f0_1Hz.ff_1000Hz.tf_50s.Idx_1.mat
- Mech2_Vac0_0.001.Rs_10.Vdc_0.3.b1_5.f0_0.001Hz.ff_1Hz.tf_5400s.Idx_5.mat

---

## Figure 5 – Full Frequency Range (Combined) Segmented Chirp EIS
- Full_Mech1_Vac0_0.001.Rs_10.Vdc_0.3.b1_5.mat
- Full_Mech2_Vac0_0.001.Rs_10.Vdc_0.3.b1_5.mat
- Full_Mech3_Vac0_0.001.Rs_10.Vdc_0.3.b1_5.mat

---

## Figure 6 – Effect of Chirp Amplitude (b₁ = 10, 20, 30)

**Mech1**
- Full_Mech1_Vac0_0.001.Rs_10.Vdc_0.3.b1_10.mat
- Full_Mech1_Vac0_0.001.Rs_10.Vdc_0.3.b1_20.mat
- Full_Mech1_Vac0_0.001.Rs_10.Vdc_0.3.b1_30.mat

**Mech2**
- Full_Mech2_Vac0_0.001.Rs_10.Vdc_0.3.b1_10.mat
- Full_Mech2_Vac0_0.001.Rs_10.Vdc_0.3.b1_20.mat
- Full_Mech2_Vac0_0.001.Rs_10.Vdc_0.3.b1_30.mat

**Mech3**
- Full_Mech3_Vac0_0.001.Rs_10.Vdc_0.3.b1_10.mat
- Full_Mech3_Vac0_0.001.Rs_10.Vdc_0.3.b1_20.mat
- Full_Mech3_Vac0_0.001.Rs_10.Vdc_0.3.b1_30.mat

---

## Figure 7 – Effect of DC Bias (Vdc = 0.1, 0.3, 0.5, 0.7)

**Mech1**
- Full_Mech1_Vac0_0.001.Rs_10.Vdc_0.1.b1_5.mat
- Full_Mech1_Vac0_0.001.Rs_10.Vdc_0.3.b1_5.mat
- Full_Mech1_Vac0_0.001.Rs_10.Vdc_0.5.b1_5.mat
- Full_Mech1_Vac0_0.001.Rs_10.Vdc_0.7.b1_5.mat

**Mech2**
- Full_Mech2_Vac0_0.001.Rs_10.Vdc_0.1.b1_5.mat
- Full_Mech2_Vac0_0.001.Rs_10.Vdc_0.3.b1_5.mat
- Full_Mech2_Vac0_0.001.Rs_10.Vdc_0.5.b1_5.mat
- Full_Mech2_Vac0_0.001.Rs_10.Vdc_0.7.b1_5.mat

**Mech3**
- Full_Mech3_Vac0_0.001.Rs_10.Vdc_0.1.b1_5.mat
- Full_Mech3_Vac0_0.001.Rs_10.Vdc_0.3.b1_5.mat
- Full_Mech3_Vac0_0.001.Rs_10.Vdc_0.5.b1_5.mat
- Full_Mech3_Vac0_0.001.Rs_10.Vdc_0.7.b1_5.mat

---

## Figure 8
Contains all files listed in Figures 6 and 7.

---

## Scripts

- Plot_EIS_Bode_Error.m — Generates Nyquist (EIS), Bode, and error plots for Figure 4.
- Plot_EIS.m — Produces Nyquist (EIS) plots for Figures 5, 6, and 7.
- Error_plot_combined.m — Produces error plots for Figures 5(d) and 8.

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
- `Plot_EIS_Bode_Error.m` → Figure 4
- `Plot_EIS.m` → Figures 5(a,b,c), 6, 7
- `Error_plot_combined.m` → Figures 5(d) and 8

### 4. Error computation
- Error values are precomputed and stored in each `.mat` file.
- The formula is included as comments inside the scripts.

---

