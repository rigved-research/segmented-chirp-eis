# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 20:42:07 2025

@author: Rigved
"""

import numpy as np
from scipy.interpolate import PchipInterpolator

def interp_chirp_to_conv(f_conv, Z_chirp, f_chirp, *, extrapolate=False):
    """
    Interpolate complex chirp-spectrum Z_chirp (measured at f_chirp) 
    onto the conventional grid f_conv using PCHIP (real & imag separately).

    Parameters
    ----------
    f_conv : array-like
        Target frequency grid (e.g., F_new).
    Z_chirp : array-like (complex)
        Complex impedance samples at f_chirp.
    f_chirp : array-like
        Frequencies corresponding to Z_chirp.
    extrapolate : bool, optional (default False)
        If False, out-of-range points become NaN. If True, PCHIP extrapolates.

    Returns
    -------
    z_chirp_interpolated : np.ndarray (complex)
        Z_chirp interpolated onto f_conv.
    """
    f_conv = np.asarray(f_conv, float).ravel()
    f = np.asarray(f_chirp, float).ravel()
    Z = np.asarray(Z_chirp, complex).ravel()

    # Clean & sort
    m = np.isfinite(f) & np.isfinite(Z.real) & np.isfinite(Z.imag)
    f, Z = f[m], Z[m]
    if f.size == 0:
        raise ValueError("No finite data in f_chirp/Z_chirp.")
    idx = np.argsort(f)
    f, Z = f[idx], Z[idx]

    # Deduplicate frequencies by averaging Z at ties
    u, inv = np.unique(f, return_inverse=True)
    if u.size < 2:
        raise ValueError("Need at least two unique frequency points for PCHIP.")
    Zr_avg = np.bincount(inv, weights=Z.real) / np.bincount(inv)
    Zi_avg = np.bincount(inv, weights=Z.imag) / np.bincount(inv)

    # Build PCHIP on real & imag parts
    p_r = PchipInterpolator(u, Zr_avg, extrapolate=extrapolate)
    p_i = PchipInterpolator(u, Zi_avg, extrapolate=extrapolate)

    # Interpolate and return complex array (same shape as f_conv input)
    Z_interp = p_r(f_conv) + 1j * p_i(f_conv)
    return Z_interp
