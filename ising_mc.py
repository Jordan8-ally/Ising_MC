import numpy as np
import matplotlib.pyplot as plt
    
def lattice(L, h, J, T, num_iterations):
    spins = np.random.choice([1,-1], size=(L,L))
    
    energy = 0
    for i in range(L):
        for j in range(L):
            energy += -J*spins[i, j]*(spins[(i+1)%L, j] + spins[i, (j+1)%L]) - h*spins[i,j]
    energies = []
    magnetizations = []      
    for _ in range(num_iterations):
        i, j = np.random.randint(0, L, size=2)
        delta_energy = 2*J*spins[i, j]*(spins[(i+1)%L, j] + spins[i, (j+1)%L]) - 2*h*spins[i, j]
        
        if(delta_energy <= 0 or np.random.rand() < np.exp(-delta_energy/T)):
            spins *= -1
            energy += delta_energy
            magnetization = np.mean(spins)
            energies.append(energy)
            magnetizations.append(magnetization)
           
    ave_energy = np.mean(energies)/L**2
    ave_magnetization = np.mean(magnetizations)
    return ave_energy, ave_magnetization

# calculation parameters
L = 10
h = 1
J = 1
num_iterations = 100000
temperature = np.linspace(100, 300, 10)

energies = []
magnetizations = []
for T in temperature:
    energy,magnetization = lattice(L, h, J, T, num_iterations)
    energies.append(energy)
    magnetizations.append(magnetization)
    
plt.figure(figsize=(4,3))
plt.xlabel('Temperature')
plt.ylabel('Energy')
plt.title('Plot between T & E')
plt.plot(temperature, energies, color='b', marker='o')
plt.show()

plt.figure(figsize=(4,3))
plt.xlabel('Temperture')
plt.ylabel('Magnetization')
plt.title('Plot between T & M')
plt.plot(temperature, magnetizations, color='b', marker='o')
plt.show()