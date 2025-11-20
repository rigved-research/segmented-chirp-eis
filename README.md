# Segmented-Chirp-EIS: Scripts and Instructions

This repository contains all the **MATLAB and Python scripts**, helper functions, and folder-level documentation required to reproduce the results presented in the manuscript:

**“Accelerated and Broadband Electrochemical Impedance Spectroscopy of Lithium-ion Batteries using Segmented Chirp Signals.”**

Due to the large size of `.mat` datafiles (≈4 GB), only the **code** is hosted on GitHub.  
All corresponding **datafiles are provided separately via Google Drive** and can be downloaded using the links below.

---

## 🔗 Download Datafiles (Google Drive)

### 1. Reaction Mechanisms (Figures 4–8)
Datafiles for the three nonlinear electrochemical mechanisms:  
👉 **Download:**  
https://drive.google.com/drive/folders/1J-2GV99jn5CFh7NhR-Fz-34wdC53-82I?usp=sharing

---

### 2. DFN PyBaMM EIS (Figures 9–11)
Segmented-chirp and conventional EIS data generated using the DFN model across SoC and temperature conditions:  
👉 **Download:**  
https://drive.google.com/drive/folders/1qP_ItZE9ZMHxyiDmv_j5SqhSs5BICrKY?usp=sharing

---

### 3. DFN PyBaMM – ECM Fitting (Figure 12)
Datafiles used for ECM fitting (segmented-chirp vs conventional EIS):  
👉 **Download:**  
https://drive.google.com/drive/folders/1ZpwoNF9GtOkIqTjLgYLsY8qNHglLrPtC?usp=sharing

---

## 📁 Repository Contents

The GitHub repository includes:

- MATLAB scripts for generating Nyquist, Bode, and error plots  
- Python scripts for ECM fitting   
- Folder-level `README.md` files with detailed instructions   

No datafiles are included here due to size constraints.

---

## 📘 How to Use This Repository

1. **Download the required datafiles** from the Google Drive links above.  
2. **Clone or download this GitHub repository** to access the scripts.  
3. Navigate to the corresponding folder (e.g., `Reaction_Mechanism/`, `DFN_PyBaMM/`, `ECM_Fitting/`).  
4. **Open the `README.md` file inside each folder** for detailed instructions on:
   - Loading `.mat` data  
   - Reproducing manuscript figures  
   - Running MATLAB or Python scripts  
   - Modifying filenames and parameters  
5. Follow the step-by-step instructions to generate all plots and results presented in the paper.

---

## 📝 Notes

- All folder-level `README.md` files contain **detailed reproduction instructions** for the plots corresponding to their figure numbers.
- Make sure to download required python packages before running ECM fitting scripts 
- Data files must be downloaded separately and placed in the correct folders before running scripts.

---

