import numpy as np
import matplotlib.pyplot as plt

def angular_velocity(t, alpha):
    return -120 * alpha * np.exp(-np.cosh(alpha * t)**2 - np.sinh(alpha * t)**2) * (np.cosh(alpha * t) * np.sinh(alpha * t))

t_values = np.linspace(-2, 2, 400)
alpha_1 = 1
alpha_2 = 2
omega_1 = angular_velocity(t_values, alpha_1)
omega_2 = angular_velocity(t_values, alpha_2)

plt.figure(figsize=(8, 6))
plt.plot(t_values, omega_1, label='alpha = 1')
plt.plot(t_values, omega_2, label='alpha = 2')
plt.xlabel('Time (t)')
plt.ylabel('Angular Velocity (dTheta/dt)')
plt.title('Angular Velocity vs Time for Different Alpha Values')
plt.legend()  # You were missing the parentheses to call the legend function
plt.grid()    # You were missing the parentheses to call the grid function
plt.show()




