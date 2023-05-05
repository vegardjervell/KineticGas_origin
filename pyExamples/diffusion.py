from pykingas.HardSphere import HardSphere
from pykingas.MieKinGas import MieKinGas

hs = HardSphere('KR') # Initialize hard-sphere model for pure krypton
# State point
T, Vm = 300, 1e-3 # State point
# Mole fractions must still be supplied for two components because
# pure fluids are treated as binary mixtures of identical particles
# x = [0.5, 0.5] is good for numerical stability
x = [0.5, 0.5]
N = 1 # Enskog approximation order (must be >= 1 for diffusion)
D_self = hs.interdiffusion(T, Vm, x, N=N)
print('Self diffusion coefficient of Krypton')
print('At T =', T, 'K', 'Vm =', Vm, 'm3 / mol')
print('is', D_self)
print()

hs = HardSphere('AR,KR', N=1) # Initialize for a fluid mixture, specify default Enskog approximation order
T, Vm = 300, 1e-3 # State point
x = [0.1, 0.9]
D_12 = hs.interdiffusion(T, Vm, x) # Fickean interdiffusion coefficient int the Centre of moles Frame of Reference
print('Fickean interdiffusion coefficient for Argon/Krypton mixture with mole fractions', x)
print('At T =', T, 'K', 'Vm =', Vm, 'm3 / mol')
print('is', D_12, 'in the centre of moles frame of reference')

# Fickean interdiffusion coefficients in the centre-of-mass frame of reference
D_12m = hs.interdiffusion(T, Vm, x, frame_of_reference='CoM')
print()
print('In the centre of mass frame of reference :')
print(D_12m)

# Interdiffusion coefficients in the solvent FoR, identifying Argon (component 1) as the solvent
D_12sAr = hs.interdiffusion(T, Vm, x, frame_of_reference='solvent', solvent_idx=0)
print()
print('In the solvent frame of reference (with component 1 as the solvent) :')
print(D_12sAr)

# Interdiffusion coefficients in the solvent FoR, identifying Krypton (component 2) as the solvent
D_12sKr = hs.interdiffusion(T, Vm, x, frame_of_reference='solvent', solvent_idx=1)
print()
print('In the solvent frame of reference (with component 2 as the solvent) :')
print(D_12sKr)
print()

hs = HardSphere('AR,NE,H2') # Initialize hard sphere model for ternary mixture
T, Vm = 300, 1e-3 # State point
x = [0.1, 0.7, 0.2]

# D[i, j] is the response of flux i to a gradient in the concentration of component j.
# Note: This matrix is not invertible
D = hs.interdiffusion(T, Vm, x, N=1) # 3x3 matrix of diffusion coefficients
print('Generalized multicomponent diffusion coefficients of Ar/Ne/H2 mixture')
print('with mole fractions', x)
print('At T =', T, 'K', 'Vm =', Vm, 'm3 / mol')
print('are', D, 'in the centre of moles frame of reference')