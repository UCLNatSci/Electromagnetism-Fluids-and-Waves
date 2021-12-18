# Energy and Power of a Wave
A natural question now is to ask how much energy can a wave transmit?  At what rate could this be trasmitted 
- i.e. what is the power of a wave?  Lets look at the change total energy $E$:
```{math}
\Delta E = \Delta K + \Delta U
```
where $K$ is the total kinetic energy and $U$ the total potential energy. 

Expressions for each of these components of energy are given by:
```{math}
\Delta K &=& \frac{1}{2}\,\Delta m\,v^2 = \frac{1}{2}\,\rho_L\,\Delta x\,
\left(\sqrt{1 + \left(\frac{\partial y}{\partial x}\right)^2}\right)\left(\frac{\partial y}{\partial t}\right)^2 \\
\Delta U &=& T(\Delta s - \Delta x) = T\,\Delta x\,\left(\sqrt{1 + \left(\frac{\partial y}{\partial x}\right)^2} - 1\right)
```
Recall for transverse waves $\cos(\theta) \simeq 1$, so to find $\cos(\theta)-1$ we use a binomial expansion, 
given $\frac{\partial y}{\partial x} \ll 1$:
```{math}
\Delta K &\simeq& \frac{1}{2}\,\rho_L\,\Delta x\,\left(\frac{\partial y}{\partial t}\right)^2 + \dots,\quad \quad 
\Delta U \simeq T\,\Delta x\,\left(\frac{1}{2}\right)\left(\frac{\partial y}{\partial x}\right)^2 + \dots
\\ \Rightarrow \Delta E &=& \frac{1}{2} x\,\rho_L\,\left(\left(\frac{\partial y}{\partial t}\right)^2 + 
\frac{T}{\rho_L}\left(\frac{\partial y}{\partial x}\right)^2\right)
```
Equations {eq}`vPDE` and {eq}`uhPDE` suggest that wave solutions $y_\pm = y(x \pm ct)$ will satisfy:
```{math}
\frac{\partial y_\pm}{\partial t} = \pm c\frac{\partial y_\pm}{\partial x}
\Longrightarrow \left(\frac{\partial y}{\partial t}\right)^2 = c^2\left(\frac{\partial y}{\partial x}\right)^2
```
given that  $T / \rho_L = c^2$, we can simplify to find:
```{math}
\Delta E = \frac{1}{2}\Delta x\,\rho_L\,\left[\left(\frac{\partial y}{\partial t}\right)^2 + 
\left(\frac{\partial y}{\partial t}\right)^2\right] = \Delta x\,\rho_L\,\left(\frac{\partial y}{\partial t}\right)^2 
```
If we take the limit $\Delta x \rightarrow 0$, then we can integrate up to find:
```{math}
\int_0^E \textrm{d}E' = E = \int_0^\lambda \epsilon(x,t) \,\textrm{d}x 
```
```{math}
\epsilon(x,t) = \rho_L\,\left(\frac{\partial y}{\partial t}\right)^2 = \rho_L\,c^2\,\left(\frac{\partial y}{\partial x}\right)^2 
```
The term $\epsilon(x,t)$ is known as the {\bf energy density} of the wave.  For a travelling wave, 
$y(x,\,t) = A\,\cos(kx-\omega t)$, the energy density and energy has the form:
```{math}
\epsilon(x,\,t) &=& \rho_L\,\omega^2\,A^2\,\sin^2(kx-\omega t) = \rho_L\,k^2\,c^2\,A^2\,\sin^2(kx-\omega t)\\
E &=& \frac{1}{2}\,\rho_L\,\omega^2\,A^2\,\lambda = \frac{1}{2}\,\rho_L\,k^2\,c^2\,A^2\,\lambda
```
We notice the phase shift in $y(x,\,t)$ and $\epsilon(x,\,t)$, as depicted in Figure 6.
| ![/WaveEnergy.png](../figures/WaveEnergy.png) |
|:--:|
| <b>Figure 6 - </b> Breakdown of a travelling wave $y(x,\,t)$ and energy density $\epsilon(x,\,t)$|}

 We can also find the power of a wave $P$, which is the rate of flow of energy:
```{math}
P = \frac{\Delta E}{\Delta t} = \rho_L \frac{\Delta x}{\Delta t}\left(\frac{\partial y}{\partial t}\right)^2
``` 
and therefore in the limit of $\Delta t \rightarrow 0$:
```{math}
P = \rho_L\,c\,\left(\frac{\partial y}{\partial t}\right)^2 = c\,\epsilon
``` 
where $c$ is the wave phase velocity.  For a travelling wave, $y(x,\,t) = A\,\cos(kx-\omega t)$, it is often easier 
to think about the time averaged power $P_{<T>}$ of a wave, which evaluates the power over one time period $T$:
```{math}
P_{<T>} = \frac{1}{T}\int_0^T c\,\epsilon\,\mathrm{d} t = \frac{1}{2}\,\rho_L\,\omega^2\,A^2\,c = \frac{1}{2}\,\rho_L\,k^2\,A^2\,c^3
```
We can likewise find expressions for $E,\,P$ for longitudinal waves, where we can identify 
$c^2 = T / \rho_L = (k_{tot} L)/(m_{tot} / L) = L^2\,k_{tot}/m_{tot}$ from the derivation presented in Section 1.3.1.