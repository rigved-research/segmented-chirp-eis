# Segmented-Chirp-EIS – DFN PyBaMM - ECM Fitting


**Note:**  
The datafiles required for Figure 12 in this section can be downloaded from the 
following link: https://drive.google.com/drive/folders/1ZpwoNF9GtOkIqTjLgYLsY8qNHglLrPtC?usp=sharing

This dataset contains the segmented chirp and conventional EIS data used for 
**equivalent circuit model (ECM) fitting**. The ECM fitting procedure corresponds 
to the results shown in **Figure 12** of the manuscript.

---

## Datafiles for ECM Fitting

### Figure 12 – 0.001 Hz to 10 kHz Segmented Chirp EIS for SoC=0.5, Temp = 25 degree C 
- Full_SoC_0.2.Temp_283.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.5.Temp_298.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat
- Full_SoC_0.8.Temp_313.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat

Each dataset contains:
- `f` — Chirp frequency vector  
- `F` — Conventional EIS frequency vector  
- `z_chirp` — Chirp-based impedance  
- `Z` — Conventional impedance  
- `error` — Relative absolute error  
---


## Script

### **ECM_Fit.py**
Runs ECM fitting independently for:
- Conventional EIS  
- Chirp-based EIS (interpolated to the conventional frequency grid)

Outputs include:
- ECM parameters  
- Fit quality metrics (NRSS, R², RMSE %)  
- Fitting time  
- Nyquist plot comparing measured and ECM-fitted spectra  

## Function
- **chirp_interpolator.py** — Interpolates chirp impedance onto the conventional frequency grid   
---

## Instructions for Use

## 1. Select a dataset file
Modify the line inside `ECM_Fit.py`:

```python
MAT_FILE = r"Full_SoC_0.2.Temp_283.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat"
```

Replace the filename with any dataset listed above.

---

## 2. Run the ECM fitting script

```bash
python ECM_Fit.py
```

The script will:
- Load the dataset  
- Interpolate chirp EIS  
- Clean and sort frequency–impedance pairs  
- Fit the ECM to both datasets  
- Compute fit metrics  
- Save ECM parameter files  
- Generate Nyquist plots  
---
## 3. Outputs Generated Automatically

### A. ECM Parameter Files
Saved as:

```
ECM_Fit_<filename>_conv.txt
ECM_Fit_<filename>_chirp.txt
```

Each file includes:
- Extracted ECM parameters  
- Fit-quality metrics (NRSS, R², RMSE%)  
- Number of data points  
- Fitting time  
- Circuit model used  

### B. Nyquist Plot
Saved as:

```
ECM_Fit_SOC<value>_Temp<value>.png
```

## 4. Notes

- ECM structure: **R0 + (CPE1 ‖ R1) + (CPE2 ‖ R2) + (C1 ‖ R3)**  
- Impedance is scaled to **mΩ** using `SCALE_MOHM = 1000`  
- Required Python packages:
  - numpy  
  - scipy  
  - matplotlib  
  - impedance.py  
