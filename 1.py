import numpy as np
import matplotlib.pyplot as plt

R1 = 10.0          # ОМ
R3 = 20.0          # ОМ
R4 = 20.0          # ОМ
R5 = 100.0         # ОМ
C1 = 0.001         # Ф
C3 = 0.0023        # Ф
C4 = 0.00025       # Ф
L1 = 0.001         # Гн
L3 = 0.011         # Гн
U = 110.0          # Вольт
f = 20.0           # Гц

j = (-1)**0.5
omega = 2 * np.pi * f
num_points = 1000
T = 1 / f
dt = T / num_points

X_l1 = omega * L1
X_l3 = omega * L3

X_c1 = 1 / (omega * C1)
X_c3 = 1 / (omega * C3)
X_c4 = 1 / (omega * C4)

Z1 = R1
Z2 = j * X_l1
Z3 = R3 - j * X_c3
Z4 = -j * X_c1
Z5 = R4 - j * X_c4
Z6 = R5 + j * X_l3

Z35 = (Z3 * Z5)/(Z3+Z5)
Z24 = (Z2 * Z4)/(Z2+Z4)
ZO = Z24 + Z35 + Z1 + Z6

I = U/ZO

U1 = I * Z1
U2 = I * Z24
U3 = I * Z35
U4 = U2
U5 = I * Z6
U6 = U
U23 = U
U145 = U

I1 = I
I2 = U2/Z2
I3 = U3/Z3
I4 = U2/Z4
I5 = U3/Z5
I6 = U5/Z6

I11 = abs(I1)
I22 = abs(I2)
I33 = abs(I3)
I44 = abs(I4)
I55 = abs(I5)
I66 = abs(I6)

U11 = abs(U1)
U22 = abs(U2)
U33 = abs(U3)
U44 = abs(U4)
U55 = abs(U5)
U66 = abs(U6)


