c = 4
f = 8

# °F = (°C × 1.8) + 32
# °C = (°F - 32) / 1.8
f_a_c = (f - 32) / 1.8
c_a_f = (c * 1.8) + 32

print("Celsius y Fahrenheit")
print(c, " grados celsius son ", round(c_a_f, 3), " fahrenheit ")
print(f, " grados fahrenheit son ", round(f_a_c, 3), " celsius ")
