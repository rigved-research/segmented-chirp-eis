# -*- coding: utf-8 -*-
"""
ECM fit to Conv. & Chirp EIS (separately).
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from pathlib import Path
from datetime import datetime
import time
from impedance.models.circuits import CustomCircuit
from chirp_interpolator import interp_chirp_to_conv

# ---------- CONFIG ----------
MAT_FILE = r"Full_SoC_0.2.Temp_283.15.tf_2s.amp_0.1.f0_0.01Hz.ff_10000Hz.mat"
F_MARKERS = [1e4, 1e3, 1e2, 10, 1, 1e-1, 1e-2]
SCALE_MOHM = 1000.0

# ECM: R0 + (CPE1||R1) + (CPE2||R2) + (C1||R3)
CIRCUIT_STR = 'R0-p(CPE1,R1)-p(CPE2,R2)-p(C1,R3)'
INITIAL_GUESS = [
    1E-3,             # R0   [Ohm]
    1E-2, 0.9,        # CPE1 (Q [Ohm^-1 s^a], a [-])
    1e-2,             # R1   [Ohm]
    1E2, 0.9,         # CPE2 (Q [Ohm^-1 s^a], a [-])
    4e-2,             # R2   [Ohm]
    1E-2,             # C1   [F]
    1e-2              # R3   [Ohm]
]
PARAM_NAMES = ["R0","Q1","a1","R1","Q2","a2","R2","C1","R3"]

# ----- PLOT STYLING CONFIG -----
LEGEND_POSITION = 'best' # Options: 'upper right', 'upper left', 'lower right', 'lower left', 'best', 'center', 'lower center' 
LEGEND_FONTSIZE = 12
AXIS_LABEL_FONTSIZE = 20
TICK_LABEL_FONTSIZE = 20
TITLE_FONTSIZE = 12

# ---------- helpers ----------
def clean_sort_conv_and_align_chirp(f_conv_raw, Z_conv_raw, Z_chirp_interp_raw):
    f = np.asarray(f_conv_raw, float).ravel()
    Zc = np.asarray(Z_conv_raw, complex).ravel()
    Zx = np.asarray(Z_chirp_interp_raw, complex).ravel()

    m = (np.isfinite(f) & (f > 0) &
         np.isfinite(Zc.real) & np.isfinite(Zc.imag) &
         np.isfinite(Zx.real) & np.isfinite(Zx.imag))

    n_original = len(f)
    f, Zc, Zx = f[m], Zc[m], Zx[m]
    n_valid = len(f)
    if n_valid == 0:
        raise ValueError("No valid data points after cleaning!")

    print(f"Data cleaning: {n_original} → {n_valid} valid points ({n_original-n_valid} removed)")

    idx = np.argsort(f)
    f, Zc, Zx = f[idx], Zc[idx], Zx[idx]

    return f, Zc, Zx

def fit_circuit(f, Z, circuit_str, initial_guess):
    circ = CustomCircuit(circuit_str, initial_guess=initial_guess.copy())
    t0 = time.perf_counter()
    circ.fit(f, Z)
    t = time.perf_counter() - t0
    return circ, t

def compute_metrics(f, Z, Z_fit, pcount):
    res = Z - Z_fit
    N = len(f)
    RSS = np.sum(np.abs(res)**2)
    NRSS = RSS / np.sum(np.abs(Z)**2)
    TSS = np.sum(np.abs(Z - np.mean(Z))**2)
    R2 = 1.0 - RSS / TSS
    RMSE_rel_pct = 100.0 * np.sqrt(np.mean((np.abs(res)/np.abs(Z))**2))
    return dict(N=N, p=pcount, NRSS=NRSS, R2=R2, RMSE_rel_pct=RMSE_rel_pct)

def save_results(stem, src, circuit_obj, metrics, param_names, fit_time):
    out_path = Path(MAT_FILE).with_name(f"ECM_Fit_{stem}_{src}.txt")
    vals = np.asarray(circuit_obj.parameters_, float).ravel()
    fit_params = dict(zip(param_names, vals))
    with open(out_path, "w", encoding="utf-8") as ftxt:
        ftxt.write("# Fitted EIS circuit parameters and fit-quality metrics\n")
        ftxt.write(f"# Source            : {src}\n")
        ftxt.write(f"# Circuit           : {getattr(circuit_obj, 'circuit', 'CustomCircuit')}\n")
        ftxt.write(f"# Fitting Time      : {fit_time:.4f} s\n")
        ftxt.write(f"# Generated         : {datetime.now().isoformat(timespec='seconds')}\n")
        ftxt.write("# Units: R [Ohm], C [F], CPE Q [Ohm^-1 s^a], a [-]\n\n")
        ftxt.write("[Parameters]\n")
        for k in param_names:
            ftxt.write(f"{k:>6s} = {fit_params[k]:.12g}\n")
        ftxt.write("\n[FitQuality]\n")
        ftxt.write(f"N_points          = {metrics['N']:d}\n")
        ftxt.write(f"p_parameters      = {metrics['p']:d}\n")
        ftxt.write(f"NRSS              = {metrics['NRSS']:.6e}\n")
        ftxt.write(f"R2                = {metrics['R2']:.6f}\n")
        ftxt.write(f"RMSE_rel_pct      = {metrics['RMSE_rel_pct']:.3f}\n")
    print(f"Saved: {out_path}")

def extract_soc_temp_from_filename(filename):
    import re
    soc_match = re.search(r'SoC[_\s]*([0-9.]+)', filename, re.IGNORECASE)
    soc = soc_match.group(1) if soc_match else 'unknown'
    temp_match = re.search(r'Temp[_\s]*([0-9.]+)', filename, re.IGNORECASE)
    temp = temp_match.group(1) if temp_match else 'unknown'
    return soc, temp

def save_figure(fig, base_name):
    out_path = Path(MAT_FILE).parent / f"ECM_Fit_{base_name}.png"
    fig.savefig(out_path, format='png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {out_path}")
    return [out_path]


# ---------- MAIN ----------
print("="*60)
print("Loading data...")
mat_raw = loadmat(MAT_FILE, squeeze_me=True, struct_as_record=False)
mat = {k: v for k, v in mat_raw.items() if not k.startswith("__")}

f_conv_raw  = mat['F']
f_chirp     = mat['f']
Z_conv_raw  = mat['Z']
Z_chirp_raw = mat['z_chirp']

print(f"Raw data shapes: f_conv={np.shape(f_conv_raw)}, Z_conv={np.shape(Z_conv_raw)}, f_chirp={np.shape(f_chirp)}, Z_chirp={np.shape(Z_chirp_raw)}")

print("\nInterpolating chirp data to Conv. frequency grid...")
Z_chirp_interp = interp_chirp_to_conv(f_conv_raw, Z_chirp_raw, f_chirp, extrapolate=False)

print("\nCleaning and sorting data...")
f, Z_conv, Z_chirp = clean_sort_conv_and_align_chirp(f_conv_raw, Z_conv_raw, Z_chirp_interp)

print(f"Frequency range: {f.min():.3e} to {f.max():.3e} Hz")
print(f"Conv |Z| range: {np.abs(Z_conv).min():.3e} to {np.abs(Z_conv).max():.3e} Ω")
print(f"Chirp |Z| range: {np.abs(Z_chirp).min():.3e} to {np.abs(Z_chirp).max():.3e} Ω")

# ---------- fit separately ----------
print("\n" + "="*60)
print("Fitting Conv. data...")
c_conv, t_conv = fit_circuit(f, Z_conv, CIRCUIT_STR, INITIAL_GUESS)
print(f"  Time: {t_conv:.3f}s")
print(f"  Parameters: {c_conv.parameters_}")

print("\nFitting Chirp data (on conv grid)...")
c_chirp, t_chirp = fit_circuit(f, Z_chirp, CIRCUIT_STR, INITIAL_GUESS)
print(f"  Time: {t_chirp:.3f}s")
print(f"  Parameters: {c_chirp.parameters_}")

Zfit_conv  = c_conv.predict(f)
Zfit_chirp = c_chirp.predict(f)

# ---------- metrics & save ----------
print("\n" + "="*60)
print("Computing metrics and saving results...")
stem = Path(MAT_FILE).with_suffix('').name
m_conv  = compute_metrics(f, Z_conv,  Zfit_conv,  pcount=len(c_conv.parameters_))
m_chirp = compute_metrics(f, Z_chirp, Zfit_chirp, pcount=len(c_chirp.parameters_))

save_results(stem, "conv",  c_conv,  m_conv,  PARAM_NAMES, t_conv)
save_results(stem, "chirp", c_chirp, m_chirp, PARAM_NAMES, t_chirp)

print("\nFit Quality Summary:")
print(f"  Conv:  R²={m_conv['R2']:.4f}, RMSE%={m_conv['RMSE_rel_pct']:.2f}%")
print(f"  Chirp: R²={m_chirp['R2']:.4f}, RMSE%={m_chirp['RMSE_rel_pct']:.2f}%")

# =====================  FIGURE 1: EIS (Nyquist) ONLY  ======================
print("\n" + "="*60)
print("Creating plots...")
plt.close('all')

# Colors
COLOR_CONV_DATA = '#003F5C'
COLOR_CONV_FIT = '#00677F'
COLOR_CHIRP_DATA = '#2DB88B'
COLOR_CHIRP_FIT = '#94DC7B'

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['CMU Serif', 'Computer Modern', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'cm'

figN, axN = plt.subplots(figsize=(6.0, 5.0), dpi=100)

# Conv. measured
axN.plot(np.real(Z_conv)*SCALE_MOHM,  -np.imag(Z_conv)*SCALE_MOHM,
         linestyle='None', marker='o', markersize=5,
         markerfacecolor=COLOR_CONV_DATA, markeredgecolor=COLOR_CONV_DATA,
         label="Conv. $Z_{meas}$", zorder=3)

# Conv. ECM fit
axN.plot(np.real(Zfit_conv)*SCALE_MOHM,  -np.imag(Zfit_conv)*SCALE_MOHM,
         '--', marker='o', markersize=4, lw=2.0, color=COLOR_CONV_FIT,
         markerfacecolor=COLOR_CONV_FIT, markeredgecolor=COLOR_CONV_FIT,
         markevery=5, label="Conv. $Z_{ECM}$", zorder=2)

# Chirp measured
axN.plot(np.real(Z_chirp)*SCALE_MOHM, -np.imag(Z_chirp)*SCALE_MOHM,
         linestyle='None', marker='^', markersize=6,
         markerfacecolor=COLOR_CHIRP_DATA, markeredgecolor=COLOR_CHIRP_DATA,
         label="Chirp $Z_{meas}$", zorder=3)

# Chirp ECM fit
axN.plot(np.real(Zfit_chirp)*SCALE_MOHM, -np.imag(Zfit_chirp)*SCALE_MOHM,
         '-', marker='^', markersize=5, lw=2.0, color=COLOR_CHIRP_FIT,
         markerfacecolor=COLOR_CHIRP_FIT, markeredgecolor=COLOR_CHIRP_FIT,
         markevery=5, label="Chirp $Z_{ECM}$", zorder=2)

axN.set_xlabel(r'$Z_r(f)$ [m$\Omega$]', fontsize=AXIS_LABEL_FONTSIZE)
axN.set_ylabel(r'$-Z_j(f)$ [m$\Omega$]', fontsize=AXIS_LABEL_FONTSIZE)
axN.tick_params(axis='both', which='major', labelsize=TICK_LABEL_FONTSIZE)
axN.grid(True, which='both', ls=':')

# ----- axis limits -----
xr = np.r_[np.real(Z_conv),  np.real(Z_chirp),
           np.real(Zfit_conv),  np.real(Zfit_chirp)] * SCALE_MOHM
xi = np.r_[np.imag(Z_conv),  np.imag(Z_chirp),
           np.imag(Zfit_conv),  np.imag(Zfit_chirp)] * -SCALE_MOHM

xmax = xr.max()
ymax = xi.max()
x_range = xmax
y_range = ymax
x_pad = 0.1 * x_range
y_pad = 0.1 * y_range

# keep origin common and keep full box
axN.set_xlim(left=0, right=np.ceil(xmax + x_pad))
axN.set_ylim(bottom=0, top=np.ceil(ymax + y_pad))

from matplotlib.ticker import MaxNLocator
axN.xaxis.set_major_locator(MaxNLocator(nbins=5, integer=False))
axN.yaxis.set_major_locator(MaxNLocator(nbins=5, integer=False))

axN.legend(loc=LEGEND_POSITION, fontsize=LEGEND_FONTSIZE,
           framealpha=1.0, edgecolor='black', fancybox=False, shadow=False)

figN.tight_layout(pad=0.5)

soc, temp = extract_soc_temp_from_filename(MAT_FILE)
nyquist_basename = f"NewFit_EIC_SOC{soc}_Temp{temp}"
print(f"\nSaving Nyquist plot as: {nyquist_basename}.[png/jpg/pdf/svg]")
save_figure(figN, nyquist_basename)



print("Done! Displaying plots...")
plt.show()
