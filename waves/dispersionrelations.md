# Dispersion Relations and Wave Energy

Now that we have our complex wave solutions to the equation, we can see that plugging in the solutions 
to the wave equation produce their own equations.  Lets start with the simplest wave solution, a 1D right hand moving wave:
```{math}
:label: waveform
u = u_0\,\exp(i(kx-\omega t))
```
Plugging this into the wave equation:
```{math}
u_{xx} &=& \,-k^2 \,u\\ 
u_{tt} &=& \, -\omega^2 \,u \\
u_{tt} &=& \, c^2\,u_{xx} \\
-\omega^2 \,u &=& \, -c^2\,k^2\,u \Rightarrow \omega^2 &=& \,c^2 k^2 \Rightarrow \omega = \,\pm\, c k
```
Since we have two roots for $\omega$ here, we can see that these correspond to either left or right hand moving waves.  
Therefore if we usee {eq}`waveform` with the proviso that $\omega = \omega(k) = \pm c\, k$, this describes the travelling wave solutions
in {eq}`fullwaveeqnsoln`.

The function $\omega = \omega(k)$ is known as a <b>dispersion relation</b>.  In this case, $\omega(k)$ is a linear function of $k$, but in 
general it could be <em>any</em> function of $k$.  We can also rewrite this linear expression in terms of frequency and wavelegnth 
$f = \omega/2\pi, \,\lambda = 2\pi/k$:
```{math}
c = f \,\lambda
```
which is of course a familiar result! 

Looking at the combination of $\omega/k$, notice it has units of:
```{math}
\frac{[\omega]}{[k]} = \frac{s^{-1}}{m^{-1}} = m\,s^{-1} = [\textrm{speed}]
```
and so we see this is a wave speed of some sort! 

This is known as the <b> phase velocity </b> of the wave $v_p$ and describes the rate at which the phase 
of the wave propagates through space.  We can see this by considering 
```{math}
\Phi &=& \,kx - \omega t  \\
\frac{\partial \Phi}{\partial t} &=& \,-\omega, \,\,\, \frac{\partial \Phi}{\partial x} = k \\ 
v_p &=& \,\left|\frac{\partial x}{\partial t}\right| = \frac{\omega}{k}
```
There are other ways to measure the propagation of waves through space, another way that is dimensionally 
equivalent (but crucially different in the detail) would be
```{math}
v_g = \frac{\partial \omega}{\partial k}
```
this is known as the <b> group velocity </b> of the wave and describes the velocity with which the overall 
envelope shape of the wave's amplitudes (known as the modulation or envelope of the wave) propagates 
through space.  We can extend this to two and higher dimensions using the gradient operator
```{math}
\bf{v_p} &=& \,\frac{\bf{\hat{k}}}{|\bf{k}|}\omega \\
\bf{v_g} &=& \,\nabla_k \omega 
```
Usually these vectors point in the same direction, but there are examples in nature, for instance 
the anisotropic structure within a crystal, where the two vectors are not parallel. 


## Energy and Power of Travelling Waves
Lets again start with a travelling wave $u$:
```{math}
u(x,\,t) = \mathrm{Re}\Big[u_0\, \exp\left(i(kx - \omega t)\right)\Big] = u_0\,\cos\left(kx - \omega t\right)
```
the energy density will be given by:
```{math}
\epsilon &=&\, \frac{1}{2}\,\rho_L\,\left[c^2\left(\frac{\partial u}{\partial x} \right)^2 + \left(\frac{\partial u}{\partial t} \right)^2\right] \\
&=&\, \frac{1}{2}\,\rho_L\,{u_0}^2\,\sin^2\left(kx - \omega t\right)\left[c^2 k^2 + \omega^2 \right]
```
and since $\omega^2 = c^2\,k^2$, this simplifies to:
```{math}
:label: energydensitytravelwave
\epsilon = \rho_L\,{u_0}^2\,\omega^2\,\sin^2\left(kx - \omega t\right)
```
{numref}`WaveEnergy` shows the difference in phase between $u(x,\,t)$ and $\epsilon(x,\,t)$.  
```{figure} ../figures/WaveEnergy.png
---
name: WaveEnergy
---
Breakdown of a travelling wave $u(x,\,t)$ and the associated energy density $\epsilon(x,\,t)$
```

Calculating the energy carried over one wavelength:
```{math}
E_\lambda &=& \, \int_0^\lambda \rho_L\,{u_0}^2\,\omega^2\,\sin^2\left(kx - \omega t\right)\,\mathrm{d}x \\
&=& \,  \frac{1}{2}\rho_L\,{u_0}^2\,\omega^2\,\int_0^\lambda \left[1 - \cos\left(2kx - 2\omega t\right)\right]\,\mathrm{d}x
```
where the second step used a trig identity to help evaluate the integral:
```{math}
E_\lambda &=&\, \frac{1}{2}\rho_L\,{u_0}^2\,\omega^2\,\left[x - \frac{1}{2k}\sin\left(2kx - 2\omega t\right)\right]_0^\lambda \\
&=&\, \frac{1}{2}\rho_L\,{u_0}^2\,\omega^2\,\left(\lambda - \frac{1}{2k}\sin\left(4\pi - 2\omega t\right) - 0 + \frac{1}{2k}\sin\left(- 2\omega t\right)\right)
```
and we use $k\lambda = 2\pi$ and by the cyclic nature of $\sin(x)$, these terms cancel, leaving:
```{math}
:label: energywavelength
E_\lambda =\frac{1}{2}\rho_L\,{u_0}^2\,\omega^2\,\lambda = \pi \,c^2\,\rho_L\,k\,{u_0}^2
```
Which suggests $E_\lambda \propto {u_0}^2$, which is a key result.  

Also note that if we did the same analysis with a left travelling wave $u = u_0\,\exp(i(|k|x + |\omega|\,t))$, the result of Equation {eq}`energydensitytravelwave` 
would be the same, therefore for plane waves the expression for $\epsilon$ can be simplifed:
```{math}
\epsilon = \rho_L\,c^2\,\left(\frac{\partial u}{\partial x} \right)^2 = \rho_L\,\left(\frac{\partial u}{\partial t} \right)^2
```
<em> Note </em> this is not true for other types of waves!  Likewise the wave power comes out to be:
```{math}
P(x,\,t) &=& \, \int \frac{\partial \epsilon}{\partial t} \,\mathrm{d}x = 
2\rho_L\,{u_0}^2\,\omega^3\,\int\sin\left(kx - \omega t\right)\cos\left(kx - \omega t\right)\,\mathrm{d}x \\
&=& \, \frac{1}{k}\rho_L\,{u_0}^2\,\omega^3\,\sin^2\left(kx - \omega t\right) = \rho_L\,{u_0}^2\,\omega^2\,c\,\sin^2\left(kx - \omega t\right)
```
Notice that this result is related to {eq}`energydensitytravelwave` by $P = c\,\epsilon$ and so the time averaged power is:
```{math}
\langle P \rangle_T &=&\, \frac{1}{T}\int_0^T P(x,\,t) \,\mathrm{d}t = \frac{1}{T}\,\rho_L\,{u_0}^2\,\omega^2\,c\,\int_0^T \sin^2\left(kx - \omega t\right)\,\mathrm{d}t \\
&=& \,  \frac{\rho_L\,{u_0}^2\,\omega^2\,c}{2T}\,\int_0^T \left(1 - \cos\left(2kx - 2\omega t\right)\right)\,\mathrm{d}t \\
&=& \, \frac{\rho_L\,{u_0}^2\,\omega^2\,c}{2T}\,\Big[t + \frac{1}{2\omega}\sin\left(2kx - 2\omega t\right)\Big]_0^T \\
&=& \, \frac{\rho_L\,{u_0}^2\,\omega^2\,c}{2T}\,\Big(T + \frac{1}{2\omega}\sin(2kx - 4\pi) - 0 - \frac{1}{2\omega}\sin(2kx)\Big)
```
where we use $\omega T = 2\pi$ and by the cyclic nature of $\cos(x)$, these terms cancel, leaving:
```{math}
\langle P \rangle_T = \frac{1}{2}\rho_L\,\omega^2\,c\,{u_0}^2 = \frac{1}{2}\rho_L\,c^3\,k^2\,{u_0}^2
```
and here we see that $\langle P \rangle_T\propto {u_0}^2$.  

If we think back to oscilaating electrical systems, for an oscillating voltage $v = V_0\cos(\Omega t)$, the electrical power would be
$P = V^2 / R = {V_0}^2\,\cos^2(\Omega t)/R$ - suggesting the power and oscillation amplitude are related according to $P \propto {V_0}^2$, which we see is a general 
fact of travelling wave systems.