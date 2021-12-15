# Deriving the Wave Equation

## Mathematical Preliminaries

Since waves involve changes in both space and time $u(x,\,t)$, the definitions of first and second partial derivatives in terms of limits
are useful here:

```{math}
\frac{\partial u(x,t)}{\partial x} &=& \lim_{\Delta x \rightarrow 0} \frac{u(x + \Delta x,t) - u(x,t)}{\Delta x} \\
\frac{\partial^2 u(x,t)}{\partial x^2} &=& \frac{\partial}{\partial x}\left(\frac{\partial u(x,t)}{\partial x}\right) \\
&=& \lim_{\Delta x \rightarrow 0} \frac{1}{\Delta x}\left[\frac{\partial u(x+\Delta x,t)}{\partial x} - \frac{\partial u(x,t)}{\partial x} \right] \\
&=& \lim_{\Delta x \rightarrow 0} \frac{1}{\Delta x}\left[\frac{u(x + 2\Delta x,t) - u(x+ \Delta x,t)}{\Delta x} - \frac{u(x + \Delta x,t) - u(x,t)}{\Delta x} \right] \\
```
Which means we can write a second partial derivative using a limit definition as:
```{math}
:label: partialderiv
\frac{\partial^2 u(x,t)}{\partial x^2} = \lim_{\Delta x \rightarrow 0} \frac{u(x+2\Delta x,t) - 2u(x+\Delta x,t) + u(x,t)}{{\Delta x}^2} 
```

## Longitudinal Waves
Lets start with the classic derivation of waves propagating, with a collection of $N$ masses $m$ connected together on springs (with spring constant $k$), each with equilibrium separation $h$, as shown in Figure 1. We can measure the horizontal displacement $u(x,t)$ from the equilibrium positions.

| ![massspringarray.png](../figures/massspringarray.png) |
|:--:|
| <b>Figure 3 - </b> Identical masses connected by identical springs.|

If the springs follow Hooke's law, then $F_{H} = k\,u(x,t) $ and equally all the masses will follow Newton's second law $F_{N} = m \,a(x,t)$.  We can analyse the dynamics of the middle mass, where the Hooke's law forces will from both the spring $x+h \rightarrow x+2h$ as well as the spring $x \rightarrow x+h$
```{math}
F_N &=& m \frac{\partial^2}{\partial t^2}u(x+h,t)\\
F_H &=& k[u(x+2h,t) - u(x+h,t)] - k[u(x+h,t) - u(x,t)] \\
&=& k[u(x+2h,t) - 2u(x+h,t) + u(x,t)]
```

Since these two sets of forces must equal, then by rearrangement
```{math}
:label: masschainforces
\frac{\partial^2}{\partial t^2}u(x+h,t) = \frac{k}{m}[u(x+2h,t) - 2u(x+h,t) + u(x,t)] 
```
Lets also consider a chain of springs  in series, as shown in Figure 4.  

| ![massspringarray.png](../figures/springsinseries.png) |
|:--:|
| <b>Figure 4 - </b> Two springs in series with a mass|

We can consider the total displacement of the mass $m$, as well as as the individual springs displacements 
```{math}
F_{tot} &=& k_{tot}\,x_{tot}\\
F_1 &=& k_1\,x_1\\
F_2 &=& k_2\,x_2
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
\frac{1}{k_{tot}} = \frac{N}{k} \Rightarrow k_{tot} = \frac{k}{N}
```
We can substitute this into Equation {eq}`masschainforces`:
```{math}
\frac{\partial^2 u}{\partial t^2} = \frac{N\,k_{tot}}{m} [u(x+2h,t) - 2u(x+h,t) + u(x,t)]
```
Now if we want to consider the whole chain of masses and springs, then with $N$ masses and total mass on the chain is $m_{tot} = Nm$, which results in
```{math}
\frac{\partial^2 u}{\partial t^2} = \frac{N^2\,k_{tot}}{m_{tot}} [u(x+2h,t) - 2u(x+h,t) + u(x,t)]
```
and if the the total chain length is $L = Nh$, then:
```{math}
:label: almostwaveqn
\Rightarrow \frac{\partial^2 u}{\partial t^2} = \frac{L^2\,k_{tot}}{m_{tot}} \frac{u(x+2h,t) - 2u(x+h,t) + u(x,t)}{h^2} 
```
By taking the limit $N \rightarrow \infty$ and therefore $h \rightarrow 0$ for a finite chain length $L$, this has exactly 
the form of the partial derivative in Equation {eq}`partialderiv`. So Equation {eq}`almostwaveqn` has the form:
```{math}
\frac{\partial^2 u}{\partial t^2} = \frac{L^2\,k_{tot}}{m_{tot}} \frac{\partial^2 u}{\partial x^2} 
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
where $c$ is the wave speed of some form (more on this later).  We can extend this to higher dimensions, packaging the spatial derivatives up into the Laplacian 
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


## Transverse Waves*

Our derivation so far has been done for a <b> longitudinal waves </b> - where the direction of oscillation of 
the wave is parallel to the direction of propagation of the wave.  We could however derive the wave equation 
for a string, as seen in Figure 5, stretched out by a tension $\bf{T}$ and solving the equations of motion.  
This results in a wave that where the direction of oscillation is perpendicular to the direction of 
propagation - this is known as a <b> transverse wave </b>.
| ![TransverseWaveOnString.png](../figures/TransverseWaveOnString.png) |
|:--:|
| <b>Figure 5 - </b> Section of a string oscillating under tension $\bf{T}$, 
a wave equation can be derived considering infinitesimal deviations in the $\bf{x}$ direction.}

Figure 5 depicts oscillations in the $y$ direction for a smaller cross section $\Delta m$ of 
oscillating (non-stiff) wire, whilst the wave itself is travelling in the $x$ direction.  
We will consider a small section of the wire, with $\Delta x,\,\Delta y,\, \Delta m \rightarrow 0$ 
and therefore $\theta \ll 1$.  To begin we resolve forces in the $y$ direction, which will be 
unbalanced and therefore have an acceleration term appearing:
```{math}
:label: TransverseNewtons2ndLaw
T(x + \Delta x,\,t)\,\sin(\theta(x + \Delta x,\,t)) - T(x,\,t)\,\sin(\theta(x,\,t)) 
= \Delta m\,\frac{\partial^2 y(x,\,t)}{\partial t^2} 
```
The cross section of wire $\Delta m$ can be reduced down to a mass density $\rho_L$ of the wire 
(with units kg m$^{-1}$) and a length $\Delta s$ 
```{math}
\Delta m = \rho_L \,\Delta s = \rho_L \,\sqrt{\Delta x^2 + \Delta  y^2} = \rho_L \,\Delta x\, \sqrt{1 + \left(\frac{\Delta y}{\Delta x}\right)^2}
```
Looking at Figure 5 we see that 
```{math}
\tan(\theta(x,t)) = \frac{\Delta y}{\Delta x}
```
and therefore we can reduce $\Delta m$ down to:
```{math}
\Delta m = \rho_L \,\Delta x \,\sqrt{1 + \left(\frac{\Delta y}{\Delta x}\right)^2} = \rho_L \,\Delta x \,\sqrt{1 + \tan^2(\theta(x,t))} = \rho_L \,\Delta x\,\sec(\theta)
```
Rearranging Equation {eq}`TransverseNewtons2ndLaw`, we find:
```{math}
\frac{\rho_L}{\cos(\theta)}\,\frac{\partial^2 y}{\partial t^2} = \frac{T(x + \Delta x,t)\,\sin(\theta(x + \Delta x,\,t)) - T(x,t)\,\sin(\theta(x,\,t))}{\Delta x}
```
and taking the limit of $\Delta x \rightarrow 0$, we see this is just a partial derivative:
```{math}
\frac{\rho_L}{\cos(\theta)}\,\frac{\partial^2 y}{\partial t^2} = \frac{\partial}{\partial x}\left(T(x,t)\,\sin(\theta(x,t))\right)
```
```{math}
:label: Transversewaveyeqn
\Rightarrow \frac{\rho_L}{\cos(\theta)}\,\frac{\partial^2 y}{\partial t^2} = \frac{\partial T}{\partial x}\,\sin(\theta) + T\,\cos(\theta)\,\frac{\partial \theta}{\partial x} 
```
If we examine the forces in the $x$ direction, we see these are balanced:
```{math}
T(x + \Delta x,\,t)\,\cos(\theta(x + \Delta x,\,t)) - T(x,\,t)\,\cos(\theta(x,\,t)) = 0
```
dividing through by $\Delta x$ and again taking the limit $\Delta x \rightarrow 0$, we find:
```{math}
\frac{\partial}{\partial x}\left(T(x,t)\,\cos(\theta(x,t)) \right) &=& 0 \\ 
\frac{\partial T}{\partial x}\, \cos(\theta) - T \,\sin(\theta) \,\frac{\partial \theta}{\partial x} &=& 0\\
\Rightarrow \frac{\partial T}{\partial x} &=& T\,\tan(\theta)\,\frac{\partial \theta}{\partial x}
```
Substituting this result into Equation {eq}`Transversewaveyeqn` and rearranging gives:
```{math}
\rho_L\,\frac{\partial^2 y}{\partial t^2} &=&\, \cos(\theta)\left( T\,\tan(\theta)\,\sin(\theta)\,\frac{\partial \theta}{\partial x} + T\,\cos(\theta)\,\frac{\partial \theta}{\partial x} \right) \\ 
&=& \,T \,\frac{\partial \theta}{\partial x}
```
In the limit of $\Delta x \rightarrow 0$:
```{math}
\tan(\theta(x,t)) = \frac{\partial y}{\partial x} \\
\Rightarrow \sec^2(\theta)\frac{\partial \theta}{\partial x} = \frac{\partial^2 y}{\partial x^2}
```
and therefore we find:
```{math}
\frac{\partial^2 y}{\partial t^2} =  \frac{T}{\rho_L} \,\cos^2(\theta)\,\frac{\partial^2 y}{\partial x^2}
```
in the limit of $\theta \ll 1$, with $c = \sqrt{T/\rho_L}$. This reduces to the wave equation:
```{math}
\frac{\partial^2 y}{\partial t^2} =  c^2\,\frac{\partial^2 y}{\partial x^2}
```
We can check the units of $c$, 
```{math}
[T] &=& \text{ N} = \text{kg}\,\text{m}\,\text{s}^{-2}\\
[\rho_L] &=& \text{ kg}\,\text{m}^{-1}\\
\Rightarrow \sqrt{[T] / [\rho_L]} &=&  \sqrt{\text{m}^2\,\text{s}^{-2}} = \text{m}\,\text{s}^{-1}
```


