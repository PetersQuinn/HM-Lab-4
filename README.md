# Heat & Mass Transfer Lab 4: Heat Exchanger Performance Analysis

This repository contains Python code used to process experimental data and compute thermal performance metrics for various heat exchangers, as part of a laboratory assignment in a Heat and Mass Transfer course.

---

## Objective

To evaluate and compare the thermal performance of multiple heat exchanger types by computing:

* Heat transfer rate (`q`)
* Log Mean Temperature Difference (`LMTD`)
* Effectiveness (`ε`)
* Number of Transfer Units (NTU), both from effectiveness and from LMTD

---

## Experimental Setup

The heat exchangers tested include:

* Shell & Tube A, B, C
* Brazed Plate A, B, C

Each exchanger's inlet and outlet temperatures and flow rates (in gallons per minute) were recorded for both hot and cold fluids.

---

## Calculations Performed

1. **Mass flow rate conversion**
   Flow rates converted from GPM to kg/min.

2. **Heat transfer rate (`q_h`)**
   Computed using the hot fluid side.

3. **Log Mean Temperature Difference (LMTD)**
   Based on inlet/outlet temperatures of hot and cold streams.

4. **Effectiveness (`ε`)**
   Calculated using the minimum heat capacity rate.

5. **NTU estimation**

   * From effectiveness using the relation for counterflow with `C_r = 0`
   * From LMTD using the definition of NTU

---

## Technologies Used

* Python 3
* pandas
* NumPy

---

## How to Run

Simply execute the script:

```bash
python heat_exchanger_lab4.py
```

The output will display the computed values for each heat exchanger:

* Heat transfer rate (`q_h`)
* LMTD
* Effectiveness (`ε`)
* NTU (via effectiveness)
* NTU (via LMTD)

---

## Author

**Quinton Peters**
B.S.E. Candidate, Risk, Data, and Financial Engineering
Duke University
