# Dispersion Relations and Wave Speed

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
Therefore if we use {eq}`waveform` with the proviso that $\omega = \omega(k) = \pm c\, k$, this describes the travelling wave solutions
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

## Group and Phase Velocity

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
through space.  

We can extend this to two and higher dimensions using the gradient operator
```{math}
\bf{v_p} &=& \,\frac{\bf \hat{k} }{|\bf{k}|}\omega \\
\bf{v_g} &=& \,\nabla_k \omega 
```
Usually these vectors point in the same direction, but there are examples in nature, for instance 
the anisotropic structure within a crystal, where the two vectors are not parallel. 


