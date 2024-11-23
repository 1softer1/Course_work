import numpy as np
import matplotlib.pyplot as plt
import cmath

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
F = 20.0           # Гц

j = (-1)**0.5
omega = 2 * np.pi * F
num_points = 1000
T = 1 / F
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

B1 = I1.real
B2 = I2.real
B3 = I3.real
B4 = I4.real
B5 = I5.real
B6 = I6.real

A1 = I1.imag
A2 = I2.imag
A3 = I3.imag
A4 = I4.imag
A5 = I5.imag
A6 = I6.imag

ARG_I1 = (cmath.atan(A1/B1) * 180/cmath.acos(-1)).real
ARG_I2 = (cmath.atan(A2/B2) * 180/cmath.acos(-1)).real
ARG_I3 = (cmath.atan(A3/B3) * 180/cmath.acos(-1)).real
ARG_I4 = (-cmath.acos(-1)* 180/cmath.acos(-1) + cmath.atan(A4/B4) * 180/cmath.acos(-1)).real
ARG_I5 = (cmath.atan(A5/B5) * 180/cmath.acos(-1)).real
ARG_I6 = (cmath.atan(A6/B6) * 180/cmath.acos(-1)).real

B11 = U1.real
B22 = U2.real
B33 = U3.real
B44 = U4.real
B55 = U5.real
B66 = U6.real

A11 = U1.imag
A22 = U2.imag
A33 = U3.imag
A44 = U4.imag
A55 = U5.imag
A66 = U6.imag

ARG_U1 = (cmath.atan(A11/B11) * 180/cmath.acos(-1)).real
ARG_U2 = (cmath.acos(-1)* 180/cmath.acos(-1) + cmath.atan(A22/B22) * 180/cmath.acos(-1)).real
ARG_U3 = (cmath.atan(A33/B33) * 180/cmath.acos(-1)).real
ARG_U4 = (cmath.acos(-1)* 180/cmath.acos(-1) + cmath.atan(A44/B44) * 180/cmath.acos(-1)).real
ARG_U5 = (cmath.atan(A55/B55) * 180/cmath.acos(-1)).real
ARG_U6 = (cmath.atan(A66/B66) * 180/cmath.acos(-1)).real

t = np.linspace(0, T, num_points)

i1 = I11 * np.sin(2 * cmath.acos(-1) * F * t + ARG_I1 - cmath.acos(-1)/1.5)
i2 = I22 * np.sin(2 * cmath.acos(-1) * F * t + ARG_I2 - cmath.acos(-1)/1.5)
i3 = -(I33 * np.sin(2 * cmath.acos(-1) * F * t + ARG_I3 - cmath.acos(-1)/1.5))
i4 = I44 * np.sin(2 * cmath.acos(-1) * F * t + ARG_I4 - cmath.acos(-1)/1.5)
i5 = I55 * np.sin(2 * cmath.acos(-1) * F * t + ARG_I5 - cmath.acos(-1)/1.5)
i6 = I66 * np.sin(2 * cmath.acos(-1) * F * t + ARG_I6 - cmath.acos(-1)/1.5)

u1 = (U11 * np.sin(2 * cmath.acos(-1) * F * t + ARG_U1))
u2 = U22 * np.sin(2 * cmath.acos(-1) * F * t + ARG_U2)
u3 = U33 * np.sin(2 * cmath.acos(-1) * F * t + ARG_U3)
u4 = U44 * np.sin(2 * cmath.acos(-1) * F * t + ARG_U4)
u5 = -(U55 * np.sin(2 * cmath.acos(-1) * F * t + ARG_U5))
u6 = U66 * np.sin(2 * cmath.acos(-1) * F * t + ARG_U6)

plt.figure(figsize=(10, 6))
plt.plot(t, i1, label='i1')
plt.plot(t, i2, label='i2')
plt.plot(t, i3, label='i3')
plt.plot(t, i4, label='i4')
plt.plot(t, i5, label='i5')
plt.title('Изменение мгновенных значений тока в ветвях схемы')
plt.xlabel('Время (с)')
plt.ylabel('Ток (A)')
plt.legend()
plt.grid()
plt.show(block = True)
plt.interactive(False)

plt.figure(figsize=(10, 6))
plt.plot(t, u1, label='u1')
plt.plot(t, u4, label='u4')
plt.plot(t, u5, label='u5')
plt.plot(t, u6, label='u6')
plt.title('Изменение мгновенных значений напряжений в ветвях схемы')
plt.xlabel('Время (с)')
plt.ylabel('Напряжение (В)')
plt.legend()
plt.grid()
plt.show(block = True)
plt.interactive(False)

print("токи:", I1, I2, I3, I4, I5, I6,)
print("напряжения:" ,U1, U2, U3, U4, U5, U6,)
print("аргументы токов:" ,ARG_I1, ARG_I2, ARG_I3, ARG_I4, ARG_I5, ARG_I6)
print("аргументы напряжений:" ,ARG_U1, ARG_U2, ARG_U3, ARG_U4, ARG_U5, ARG_U6)