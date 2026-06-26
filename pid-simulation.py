# ============================================
# PID Controller Simulation
# Author: Meerat Dave
# Date: 26th June 2026
# Description: Simulates PID motor speed
# control and compares P, PD, PID responses
# ============================================

import matplotlib.pyplot as plt

# ── Single PID simulation ──────────────────
setpoint = 100   # target motor speed (RPM)
dt = 0.1         # time step (seconds)
steps = 200      # total steps = 20 seconds

kp = 1.2         # proportional gain
ki = 0.5         # integral gain
kd = 0.3         # derivative gain

output = 0
integral = 0
prev_error = 0
outputs = []

for i in range(steps):
    error = setpoint - output
    integral = integral + error * dt
    derivative = (error - prev_error) / dt
    control = kp*error + ki*integral + kd*derivative
    output = output + control * dt * 0.8
    prev_error = error
    outputs.append(output)

time = [i * dt for i in range(steps)]

plt.figure(figsize=(10, 5))
plt.plot(time, outputs, color='blue',
         linewidth=2, label='System output')
plt.axhline(setpoint, color='red',
            linestyle='--', linewidth=1.5,
            label='Setpoint (100)')
plt.xlabel('Time (seconds)')
plt.ylabel('Output (RPM)')
plt.title('PID Controller Simulation')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('pid_response.png')
plt.show()

# ── P vs PD vs PID Comparison ─────────────
def simulate(kp, ki, kd,
             setpoint=100, steps=200, dt=0.1):
    output = 0
    integral = 0
    prev_error = 0
    results = []
    for i in range(steps):
        error = setpoint - output
        integral = integral + error * dt
        derivative = (error - prev_error) / dt
        control = (kp*error +
                   ki*integral +
                   kd*derivative)
        output = output + control * dt * 0.8
        prev_error = error
        results.append(output)
    return results

p_only = simulate(kp=1.2, ki=0,   kd=0)
pd     = simulate(kp=1.2, ki=0,   kd=0.3)
pid    = simulate(kp=1.2, ki=0.5, kd=0.3)

plt.figure(figsize=(10, 5))
plt.plot(time, p_only, linestyle='--',
         linewidth=2, label='P only')
plt.plot(time, pd,     linestyle='-.',
         linewidth=2, label='PD')
plt.plot(time, pid,    linewidth=2.5,
         label='PID (best)')
plt.axhline(setpoint, color='red',
            linestyle=':', linewidth=1.5,
            label='Setpoint (100)')
plt.xlabel('Time (seconds)')
plt.ylabel('Output (RPM)')
plt.title('P vs PD vs PID — Step Response Comparison')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('pid_comparison.png')
plt.show()
