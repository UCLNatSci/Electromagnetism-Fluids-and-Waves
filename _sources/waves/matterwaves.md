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
where $A = i \hbar$ because $\partial \psi/\partial t = -i\omega \psi$ and $B = -\hbar^2/2m$ 
because $\partial^2 \psi/\partial x^2 = -k^2 \psi$ producing a one dimensional free particle equation of the form:
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

## Relativistic Quantum Mechanics
Unsurprisingly quantum mechanics is not the only relevant physical theory, as bodies get larger and move at relativistic speeds, we need to add in
special relativity, given the mass-energy-momentum relation from special relativity, 
```{math} 
E^2 = p^2 c^2 + {m_0}^2 c^4
```
we can alter the dispersion relation of the wave equation to write a relativistic version of the Schrödinger equation, known as the <b>Klein-Gordon</b> equation.
We find this now includes the d'Alembertian operator:
```{math}
\left(-\frac{1}{c^2}\frac{\partial^2}{\partial t^2} + \nabla^2 \right)\psi = -\Box \psi = \frac{m_0^2\,c^2}{\hbar^2}\psi
``` 
where $m_0$ is the rest mass of some relativistic particle.  

This equation also becomes very useful when studying quantum fields and forms the basis of the <b>Dirac</b> equation.

## Wavepackets
Our simplest form of dispersion relation for travelling waves suggested $\omega = \pm ck$, which we can write as:
```{math}
u(x,\, t) &=&\, \sum_{n=1}^2 u_n \exp(i(kx-\omega_n t))\\
\omega_n &=&\, (-1)^n\,ck 
```
where $u_n$ is a each waves amplitude.  We can generalise this by letting $u_n = u_n(k)$ and using a continuous spectrum of $k$ values with a general
dispersion relation, therefore:

```{math}
u(x,\, t) = \int^{\infty}_{-\infty} A(k) \,\exp(i(kx-\omega(k)t))\,\mathrm{d} k
```

We call these <b>wave packets</b>, also known sometimes as wave trains or bursts - we can picture them as a larger wave envelope, with smaller localized waves 
that travel as one unit together, as shown in {numref}`WavePacket`.  This infinite set of oscillating waves have different wavelengths, with phases 
and amplitudes that constructively and destructively interfereonly over different regions of space.

```{figure} ../figures/WavePacket.png
---
name: WavePacket
---
Schematic of a Wave Packet, with localisation near the centre of the packet.
```
Each component wave here is a solution of a wave equation and so the entire wave packet is.  Depending on the wave equation, 
the wave packet's profile may remain constant (no dispersion) or change (dispersion) while propagating. 




