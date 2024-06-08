import numpy as np
from scipy import integrate
import time

def f(x):
    return 4 / (1 + x**2)

batas_bawah = 0
batas_atas = 1

pi = 3.14159265358979323846

Nilai_N = [10, 100, 1000, 10000]

for N in Nilai_N:
    start_time = time.time()

    x = np.linspace(batas_bawah, batas_atas, N+1)

    y = f(x)

    integral = integrate.trapz(y, x)

    end_time = time.time() 
    execution_time = end_time - start_time


    rms_error = np.sqrt(np.mean((integral - pi)**2))

    print("N =", N)
    print("Hasil integrasi trapezoid:", integral)
    print("Galat RMS:", rms_error)
    print("Waktu eksekusi:", execution_time, "detik")
    print()