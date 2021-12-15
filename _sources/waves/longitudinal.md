# Longitudinal Waves

## Derivation from masses and springs
Lets start with the classic derivation of waves propagating, with a collection of $N$ masses $m$ connected together on springs (with spring constant $k$), 
each with equilibrium separation $h$, as shown in {numref}`massspringarray`. We can measure the horizontal displacement $u(x,t)$ from the equilibrium positions.

```{figure} ../figures/massspringarray.png
---
name: massspringarray
---
Identical masses connected by identical springs.
```

If the springs follow Hooke's law, then $F_{H} = k\,u(x,t) $ and equally all the masses will follow Newton's second law $F_{N} = m \,a(x,t)$.  
We can analyse the dynamics of the middle mass, where the Hooke's law forces will from both the spring $x+h \rightarrow x+2h$ as well as the spring $x \rightarrow x+h$
```{math}
F_N &=& \,m \frac{\partial^2}{\partial t^2}u(x+h,t)\\
F_H &=& \,k[u(x+2h,t) - u(x+h,t)] - k[u(x+h,t) - u(x,t)] \\
&=& \,k[u(x+2h,t) - 2u(x+h,t) + u(x,t)]
```
Since these defintions are equal, then by rearrangement:
```{math}
:label: masschainforces
\frac{\partial^2}{\partial t^2}u(x+h,t) = \frac{k}{m}[u(x+2h,t) - 2u(x+h,t) + u(x,t)] 
```
Lets also consider a chain of springs  in series, as shown in {numref}`springsinseries`  

```{figure} ../figures/springsinseries.png
---
name: springsinseries
---
Two springs in series with a mass
```

We can consider the total displacement of the mass $m$, as well as as the individual springs displacements 
```{math}
F_{tot} &=& \,k_{tot}\,x_{tot}\\
F_1 &=& \,k_1\,x_1\\
F_2 &=& \,k_2\,x_2
```
If $x_{tot}$ can be broken up into the individual springs displacements $x_{tot} = x_1 + x_2$ then we simplify to
```{math}
F_{tot} = k_{tot}(x_1 + x_2)
```
by rearrangement this reduces to
```{math}
\frac{F_{tot}}{k_{tot}} = \left(\frac{F_1}{k_1} + \frac{F_2}{k_2}\right)
```
Since the springs propagate the force applied through them, all the forces are the same $F_{tot} = F_1 = F_2$, so we are finally left with
```{math}
\frac{1}{k_{tot}} = \frac{1}{k_1} + \frac{1}{k_2}
```
and therefore for two springs, the effective spring constant is 
```{math}
k_{tot} = \left(\frac{1}{k_1} + \frac{1}{k_2}\right)^{-1}
```
If there are $N$ springs in series, then this result takes the form
```{math}
\frac{1}{k_{tot}} = \frac{1}{k_1} + \frac{1}{k_2} + \dots + \frac{1}{k_N}
``` 
and if the springs are identical, $k_1 = k_2 = \dots = k_N = k$ this result reduces to
```{math}
:label: totalspringconstant
\frac{1}{k_{tot}} = \frac{N}{k} \Rightarrow k_{tot} = \frac{k}{N}
```
We can substitute {eq}`totalspringconstant` into Equation {eq}`masschainforces`:
```{math}
\frac{\partial^2}{\partial t^2}u(x+h,t) = \frac{N\,k_{tot}}{m} [u(x+2h,t) - 2u(x+h,t) + u(x,t)]
```
Now if we want to consider the whole chain of masses and springs, then with $N$ masses and total mass on the chain is $m_{tot} = Nm$, which results in
```{math}
\frac{\partial^2}{\partial t^2}u(x+h,t) = \frac{N^2\,k_{tot}}{m_{tot}} [u(x+2h,t) - 2u(x+h,t) + u(x,t)]
```
and if the the total chain length is $L = Nh$, then:
```{math}
:label: almostwaveqn
\Rightarrow \frac{\partial^2}{\partial t^2}u(x+h,t) = \frac{L^2\,k_{tot}}{m_{tot}} \frac{u(x+2h,t) - 2u(x+h,t) + u(x,t)}{h^2} 
```
By taking the limit $N \rightarrow \infty$ and therefore $h \rightarrow 0$ for a finite chain length $L$, this has exactly 
the form of the partial derivative in Equation {eq}`2ndpartialderiv`.  Hence Equation {eq}`almostwaveqn` has the form:
```{math}
\frac{\partial^2}{\partial t^2}u(x+h,t) = \frac{L^2\,k_{tot}}{m_{tot}} \frac{\partial^2}{\partial x^2} u(x+h,t)
```
If we examine the units of the constants here:
```{math}
\frac{[L]^2\,[k]}{[m]} = \frac{m^2\,N\,m^{-1}}{kg} = \frac{m\,kg\,m\,s^{-2}}{kg} = m^2\,s^{-2} = [speed]^2
```
This results in the well known form of the wave equation in one dimension:
```{math}
:label: WaveEqn1D
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2} 
``` 
where $c$ is the wave speed of some form (more on this later).  

## Wave Equation in higher dimensions

We can extend this to higher dimensions, packaging the spatial derivatives up into the Laplacian 
$\nabla^2$ (sometimes written $\Delta$)
```{math}
:label: WaveEqn3D
\nabla^2 u = \frac{1}{c^2} \frac{\partial^2 u}{\partial t^2} 
```
where in cartesian coordinates 
```{math}
\nabla &=& \left(\frac{\partial}{\partial x},\,\frac{\partial}{\partial y},\, \frac{\partial}{\partial z}\right) \\
\nabla^2 &=& \nabla\cdot \nabla
```
These derivatives are sometimes repackaged up with the d'Alembertian $\Box$
```{math}
\Box \,u = \frac{1}{c^2} \frac{\partial^2 u}{\partial t^2} - \nabla^2 u 
```
and therefore the wave equation here has the form:
```{math} 
\Box \,u = 0
```
We notice that this equation is homogeneous - we could also add a source term on the RHS, although 
then it would admit both wave like solutions AND inhomogeous solutions.

## Energy and Power of a Wave
Given that waves are a method of propogating energy, it is an important question to ask how much and what parameters does a waves energy depend on!

Lets look at the total energy $E$:
```{math}
E = KE + PE
```
where $KE$ is the total kinetic energy and $PE$ the total potential energy. 

Lets go back to the masses and springs model, the potential energy of each mass shown in Figure 3 would be given by:
```{math}
PE = \dots + \frac{1}{2}k\Big[u(x+h,t) - u(x,t)\Big]^2 + \frac{1}{2}k\Big[u(x+2h,t) - u(x+h,t)\Big]^2 + \dots
```
where each of the springs in the chain will contribute to the PE of two masses, depending on their orientation.  Notice that we don't in this model
have any terms like $PE \sim \frac{1}{2}k u^2(x,t)$, this is because we haven't considered the effects at either end of the chain - although these
<em> edge effects </em> are really important in real world systems, we will omit them here.  

Using the springs in series result from {eq}`totalspringconstant`, we can rewrite the PE in the form:
```{math}
PE = \frac{1}{2}\,N\,k_{tot} \left(\dots + \Big[u(x+h,t) - u(x,t)\Big]^2 + \Big[u(x+2h,t) - u(x+h,t)\Big]^2 + \dots \right)
```
and likewise if we introduce the size of the mass $m$ and then consider the total chain mass:
```{math}
PE &=& \, \frac{1}{2}\frac{N\,k_{tot}\,m}{m}\left(\dots + \Big[u(x+h,t) - u(x,t)\Big]^2 + \Big[u(x+2h,t) - u(x+h,t)\Big]^2 + \dots \right) \\
 &=& \,\frac{1}{2}\,m\frac{N^2\,k_{tot}}{m_{tot}}\left(\dots + \Big[u(x+h,t) - u(x,t)\Big]^2 + \Big[u(x+2h,t) - u(x+h,t)\Big]^2 + \dots \right)
```
and then looking at the total chain length $L = N\,h$:
```{math}
PE = \frac{1}{2}\,m\,\frac{L^2\,k_{tot}}{m_{tot} h^2}\left(\dots + \Big[u(x+h,t) - u(x,t)\Big]^2 + \Big[u(x+2h,t) - u(x+h,t)\Big]^2 + \dots \right)
```
We recongise the term $c^2 = L^2\,k_{tot}/m_{tot}$ and as before by taking the limit of $N \rightarrow \infty \Rightarrow h \rightarrow 0$:
```{math}
PE = \frac{1}{2}\,m\,c^2\,\lim_{h \rightarrow 0}\left(\dots + \Big[\frac{u(x+h,t) - u(x,t)}{h}\Big]^2 + \Big[\frac{u(x+2h,t) - u(x+h,t)}{h}\Big]^2 + \dots \right)
```
and {eq}`partialderiv` tells us that each of these limits corresponds to a partial derivative, thus:
```{math}
PE = \frac{1}{2}\,m\,c^2\,\left(\dots + \Big[\frac{\partial}{\partial x}u(x+h,t)\Big]^2 + \Big[\frac{\partial}{\partial x}u(x+2h,t)\Big]^2 + \dots \right)
```

Likewise the kinetic energy has the form:
```{math}
KE = \dots + \frac{1}{2}m\Big[\frac{\partial}{\partial t}u(x,t)\Big]^2 + \frac{1}{2}m\Big[\frac{\partial}{\partial t}u(x+h,t)\Big]^2 + 
\frac{1}{2}m\Big[\frac{\partial}{\partial t}u(x+2h,t)\Big]^2 + \dots
```

and so the total energy has the form:
```{math}
E = \frac{1}{2}\,m\,\left(\dots + c^2\Big[\frac{\partial}{\partial x}u(x+h,t)\Big]^2 + \Big[\frac{\partial}{\partial t}u(x+2h,t)\Big]^2 +\dots \right)
```

We can think of this system as a coupled harmonic oscillator, with each mass having oscillating KE and PE but the result from {eq}`SHMenergy` tell us
that the total amount of energy for each mass is fixed, so by symmetry over the whole chain we can simplify this to:
```{math}
E = \frac{1}{2}\,m\,N\,\left[c^2\left(\frac{\partial u}{\partial x} \right)^2 + \left(\frac{\partial u}{\partial t} \right)^2\right] 
= \frac{1}{2}\,m_{tot}\,\left[c^2\left(\frac{\partial u}{\partial x} \right)^2 + \left(\frac{\partial u}{\partial t} \right)^2\right]
```
sometimes this is more usefully presented in terms of the energy per unit length or energy density $\epsilon(x,\,t)$:
```{math}
\epsilon = \frac{E}{L} &=& \,\frac{1}{2}\,\frac{m_{tot}}{L}\,\left[c^2\left(\frac{\partial u}{\partial x} \right)^2 + \left(\frac{\partial u}{\partial t} \right)^2\right]\\
&=& \, \frac{1}{2}\,\rho_L\,\left[c^2\left(\frac{\partial u}{\partial x} \right)^2 + \left(\frac{\partial u}{\partial t} \right)^2\right]
```
where $\rho_L$ is the mass per unit length or <b> mass density </b> of the mass and spring chain.  We can use this expression to find the total energy 
transferred over a wavelength:
```{math}
:label: waveenergy
E_\lambda = \int_0^\lambda \epsilon(x,\,t) \,\mathrm{d}x 
```
Likewise to find the power or rate of energy flow over a wave, we can use the definition of power:
```{math}
P = \frac{\partial E}{\partial t}
```
In order to get a sensible physical quantity, we can find the time varying power:
```{math}
P(x,\,t) = \frac{\partial}{\partial t}\left(\int \epsilon(x,\,t) \,\mathrm{d}x\right) = \int \frac{\partial \epsilon}{\partial t} \,\mathrm{d}x 
```
and then average the power over the time period $T$, using the definition for the average value of a function:
```{math}
:label: wavepower
\langle P \rangle_T = \frac{1}{T}\int_0^T P(x,\,t) \,\mathrm{d}t 
```