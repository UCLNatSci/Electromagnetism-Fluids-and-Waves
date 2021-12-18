# Matter Waves

So far we have used the wave equation to construct the dispersion relation for travelling waves, but we can also try to 
"reverse engineer" this process to construct the wave equation from the form of the dispersion relation.  

Lets start with some basic quantum physics, for a particle moving with momentum ${\bf p}$, its magnitude $p = |{\bf p}|$ 
is related to the de Broglie wavelength $\lambda$ by:
```{math}
\lambda = \frac{h}{p} 
```
which we can rewrite in terms of wavevector $k = |{\bf k}| = \frac{2\pi}{\lambda}$
```{math}
:label: debrogliep
p = \hbar k
```
where $\hbar = \frac{h}{2\pi}$ is the reduced Planck's constant.  Likewise the Planck equation for energy $E$ and 
frequency $f$, can be rewritten using the angular frequency $\omega = 2 \pi f$:
```{math}
:label: planckE
E = hf = \hbar \omega

```
For a free particle, moving with velocity ${\bf v}$, the only contribution to the energy $E$ is the kinetic energy 
$\frac{1}{2}mv^2$ where $v^2 = {\bf v}\cdot{\bf v}$ and since ${\bf p} = m{\bf v}$, this means we can rewrite 
```{math}
E = \frac{p^2}{2m}
```
where $p^2 = {\bf p}\cdot{\bf p}$.  Substituting in the quantum equations {eq}`debrogliep`-{eq}`planckE` here gives:
```{math}
\hbar \omega = \frac{\hbar^2 k^2}{2m}
```
producing a radically different dispersion relation to those we seen up to this point. Indeed this will produce some radically 
wave behvaiour.

But can we construct a wave equation that similarly produces this? Well if we have the complex form of wave as:
```{math}
\psi(x,t) = \psi_0 \exp(i(kx-\omega t)) \nonumber
```
then we can see that in order to get a $k^2$ here we need a $\partial^2/\partial x^2$ term in the wave equation 
and for a $\omega$ term we need a $\partial/\partial t$ term in the wave equation.  

These will result in an equation of the form:
```{math}
A \frac{\partial \psi}{\partial t} = B\frac{\partial^2 \psi}{\partial x^2}
```
where $A = i \hbar$ because $\frac{\partial \psi}{\partial t} = -i\omega \psi$ and $B = -\frac{\hbar^2}{2m}$ 
because $\frac{\partial^2 \psi}{\partial x^2} = -k^2 \psi$ producing a one dimensional free particle equation of the form:
```{math}
i \hbar\frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2}
```
If we want to include a potential energy $V = V(x,t)$ in the system, then we first rewrite the energy as KE + PE:
```{math}
:label: TotalEnergy
E = \frac{p^2}{2m} + V
```
which results in a modified dispersion relation
```{math}
\hbar \omega = \frac{\hbar^2 k^2}{2m} + V
```
and a modified wave equation of the form:
```{math}
:label: TDSE
i \hbar\frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} + V\psi
```
which should look familiar as the <b>Time Dependent Schrödinger Equation (TDSE).</b>  If we consider the form of the energy
from Equation {eq}`TotalEnergy`, we can interpret the RHS of {eq}`TDSE` as an energy operator acting of the wave function $\hat{E}\psi = E\psi$, 
giving:
```{math}
:label: TISE
\left(-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V\right)\psi = E\psi
```
which should look familiar as the <b>Time Independent Schrödinger Equation (TISE).</b> 

## Relativistic Quantum Mechanics*
It turns out we can write a relativistic version of the Schrödinger equation, known as the Klein-Gordon equation, 
using the d'Alembertian, this results in:
```{math}
\left(-\frac{1}{c^2}\frac{\partial^2}{\partial t^2} + \nabla^2 \right)\psi = -\Box \psi = \frac{m_0^2\,c^2}{\hbar^2}\psi
``` 
where $m_0$ is the rest mass of some relativistic particle.  
This equation also becomes very useful when studying quantum fields.  The dispersion relation of this equation is 
related to the form of the mass-energy-momentum relation from special relativity, 
```{math} 
E^2 = p^2 c^2 + {m_0}^2 c^4
```

## Wavepackets

A wave packet, also described sometimes as a wave train is a short "burst" or "envelope" of localized wave(s) 
that travel as  one unit together. A wave packet can be considered from an infinite set of component sinusoidal 
waves of different wavenumbers, with phases and amplitudes such that they interfere constructively only over a 
small region of space, and destructively elsewhere.  We can see an example of this in {numref}`WavePacket`.

```{figure} ../figures/WavePacket.png
---
name: WavePacket
---
Schematic of a Wave Packet, with localisation near the centre of the packet.
```

Given a wave packet will be the sum of many different wave forms, we can use an integral definition:
```{math}
u(x,t) = \frac{1}{\sqrt{2\pi}} \int^{\,\infty}_{-\infty} A(k) \,\exp(i(kx-\omega(k)t))\,\mathrm{d} k
```
Just like in the usual wave case, the wave packet travels to the right for $\omega(k) = kc$ and to the left for $\omega(k) = -kc$.

If the packet is strongly <em> localized</em>, more frequencies are needed to allow the constructive superposition in the 
spatial region of localization and destructive superposition outside this region. 
 
Each component wave here is a solution of a wave equation and so the entire wave packet is.  Depending on the wave equation, 
the wave packet's profile may remain constant (no dispersion) or it may change (dispersion) while propagating. 


