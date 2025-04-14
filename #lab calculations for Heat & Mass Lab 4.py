#lab calculations for Heat & Mass Lab 4

import pandas as pd
import numpy as np

# Constants
cp = 4.186  # specific heat capacity of water in kJ/kg°C
rho = 1.0   # density of water in kg/L

# Input data
data = {
    "Heat Exchanger": [
        "Shell & Tube A", "Shell & Tube B", "Shell & Tube C",
        "Brazed Plate A", "Brazed Plate B", "Brazed Plate C"
    ],
    "T_C_in": [25.5, 28.6, 30.0, 30.5, 33.2, 34.2],
    "T_H_in": [52.5, 68.9, 63.7, 58.6, 72.0, 63.3],
    "T_C_out": [30.5, 33.6, 36.0, 45.3, 44.8, 52.6],
    "T_H_out": [46.2, 54.8, 56.1, 45.2, 45.0, 51.1],
    "Q_c_gpm": [2, 3, 1, 2, 3, 1],
    "Q_h_gpm": [2, 1.5, 2, 2, 1.5, 2]
}

df = pd.DataFrame(data)

# Convert flow rates from gpm to kg/min (1 gal = 3.78541 L)
df["m_c"] = df["Q_c_gpm"] * 3.78541 * rho
df["m_h"] = df["Q_h_gpm"] * 3.78541 * rho

# Calculate q using hot side (in kJ/min)
df["q_h"] = df["m_h"] * cp * (df["T_H_in"] - df["T_H_out"])

# Temperature differences for LMTD
df["delta_T1"] = df["T_H_in"] - df["T_C_out"]
df["delta_T2"] = df["T_H_out"] - df["T_C_in"]

# Avoid division by zero and invalid logs
def lmtd(delta_T1, delta_T2):
    if delta_T1 == delta_T2:
        return delta_T1
    elif delta_T1 > 0 and delta_T2 > 0:
        return (delta_T1 - delta_T2) / np.log(delta_T1 / delta_T2)
    else:
        return np.nan

df["LMTD"] = [lmtd(d1, d2) for d1, d2 in zip(df["delta_T1"], df["delta_T2"])]

# Effectiveness
df["C_min"] = np.minimum(df["m_c"], df["m_h"]) * cp
df["epsilon"] = df["q_h"] / (df["C_min"] * (df["T_H_in"] - df["T_C_in"]))

# NTU from effectiveness (simple approximation for counterflow heat exchangers)
df["NTU_eps"] = -np.log(1 - df["epsilon"])  # valid for C_r = 0

# NTU from LMTD
df["NTU_LMTD"] = df["q_h"] / (df["C_min"] * df["LMTD"])

import ace_tools as tools; tools.display_dataframe_to_user(name="Heat Exchanger Analysis Results", dataframe=df[[
    "Heat Exchanger", "q_h", "LMTD", "epsilon", "NTU_eps", "NTU_LMTD"
]])
