# Solutions to Maxwell's Equations

## Electromagnetic Waves
Using Maxwell's equations, we can see that there are two scalar equations and two vector equations, in the form of coupled ODEs.  Lets rewrite these in terms of 
one field and then try to solve.  Recall the Lagrange identity for $\nabla$ with a vector ${\bf A}$: 
```{math}
\nabla \times \left(\nabla \times {\bf A}\right) = \nabla (\nabla \cdot {\bf A}) - \nabla^2 {\bf A} 
```
If we take the curl of Equation {eq}`curlE`:
```{math}
\nabla \times \left(\nabla \times {\bf E}\right) = \nabla (\nabla \cdot {\bf E}) - \nabla^2 {\bf E} = 
\nabla \times \left(  -\frac{\partial {\bf B}}{\partial t}\right)  = -\frac{\partial}{\partial t}\left(\nabla \times {\bf B} \right)
```
where we have used the fact that the order of mixed partial derivatives doesn't matter for any well behaved function in the last step.  This allows us to 
substitute in Equation {eq}`curlB` and so decouple the ${\bf B}$ field:
```{math}
\nabla (\nabla \cdot {\bf E}) - \nabla^2 {\bf E} = -\mu_0\frac{\partial\, {\bf J}}{\partial t} - \mu_0\epsilon_0 \frac{\partial^2\, {\bf E}}{\partial t^2}
```
If we then assume vacuum conditions, with no charges $\rho = 0$ or currents ${\bf J} = (0,0,0)$ present, then $\nabla \cdot {\bf E} = 0$ and this equation becomes
```{math}
:label: EMwaveeqn
\nabla^2 {\bf E} = \mu_0\epsilon_0 \frac{\partial^2\, {\bf E}}{\partial t^2} 
```
which is a wave equation!  Comparing this with Equation {eq}`WaveEqn3D` we can associate: 
```{math}
:label: SpeedOfLight
c = \frac{1}{\sqrt{\mu_0\epsilon_0}} 
```
and we can also find wave solutions for $\bf B$, with the same constant wave speed $c$.  Einstein was led (in part) to his celebrated Special Theory of Relativity by 
noticing that the speed of light $c$ is related to two vacuum parameters that are thought to be constant.

If we solve for $\bf E,\ B$ from Equation {eq}`EMwaveeqn`, these produce:
```{math}
{\bf E} &=& {\bf E_0}\,\exp(i({\bf k}\cdot {\bf x} - \omega t))\\
{\bf B} &=& {\bf B_0}\,\exp(i({\bf k}\cdot {\bf x} - \omega t))
```
where $\bf E_0,\, B_0$ are the polarization vectors of the electric and magnetic field, {numref}`EMPlaneWaves` shows some different choices of $\bf E_0,\, B_0$ for plane 
polarised and circularly polariesed waves.
```{figure} ../figures/EMWaves1.png
---
name: EMPlaneWaves
---
<b> Left Pane </b> - Depiction of electric and magnetic plane waves, 
<b> Right Pane </b> - Depiction of electric and magnetic circularly polarised waves.
```

## Polarisation of Waves
Plugging in wave solutions into Maxwell's equations in vacuum:
```{math}
:label: kEBperp
\nabla \cdot {\bf E} &=& \,0 \Longrightarrow {\bf k} \cdot {\bf E}_0 = 0 \\
\nabla \cdot {\bf B} &=& \,0 \Longrightarrow {\bf k} \cdot {\bf B}_0 = 0 \\
\nabla \times {\bf E} &=& \,-\frac{\partial {\bf B}}{\partial t} \Longrightarrow {\bf k} \times {\bf E}_0 = \omega\, {\bf B}_0 
```
These first two equations means $\bf k \perp E$ and $\bf k \perp  B$ and the third that $\bf B \perp (k,\, E)$ implying $\bf E \perp B$.  

Therefore once we pick a direction of oscillation for $\bf E$, then $\bf B$ is also set (and vice-versa).  Choosing to orientate along the $z$ axis, Equation {eq}`kEBperp` 
implies in general:
```{math}
{\bf k} = \begin{bmatrix}
 0 \\
 0 \\
 k_z
\end{bmatrix} 
\Longrightarrow {\bf E}_0 = 
\begin{bmatrix}
 E_x \\
 E_y \\
 0
\end{bmatrix}
```
For plane polarised solutions, we must pick one of $E_x,\,E_y$ to be zero, such that the oscillations are only in <em>on</em> dimension and clearly the wave propagates 
in a perpendicular $z$ dimension.  So lets pick $E_y = 0$, which results in:
```{math}
:label: PlaneWaveSolns
vE_0 = 
\begin{bmatrix}
 E_x \\
 0 \\
 0 
\end{bmatrix}
\Longrightarrow {\bf B}_0 = \frac{1}{\omega}({\bf k}\times {\bf E})= 
\begin{bmatrix}
 0 \\
 E_x \,k_z/\omega\\
 0
\end{bmatrix}  = 
\begin{bmatrix}
 0 \\
 B_y \\
 0
\end{bmatrix} 
```

## Drude Model *
In addition to solving Maxwell's for single electric charges, magnetic dipoles or in vacuum, we can also find other simple solutions.  Within a conductor, 
with an electric field ${\bf E}$ present, we can think about Ohm's law 
```{math}
V = I\,R
```
or terms of fields this is written:
```{math}
{\bf J} = \sigma {\bf E}
```
where $\sigma$ is the conductivity of the material (often written in the related form of resistivity $\rho$, where $\rho = 1 / \sigma$) and $\bf J$ is the current density. 
This is often known as the <b>Drude Model</b>.  

Substituting this model into Maxwell's equations, we can now source $\bf J$ with this relation, if we choose to ignore free charges again $\rho = 0$ and by solving for $\bf E$:
```{math}
\nabla^2 {\bf E} = \mu_0 \sigma \frac{\partial {\bf E}}{\partial t} + \mu_0\epsilon_0 \frac{\partial^2 {\bf E}}{\partial t^2}
```
Which should look familiar as a damped hoarmonic osciallator from the Waves section.  Using the wave solutions, we find a modified dispersion relation of the form: 

```{math}
k^2 = \mu_0\epsilon_0\omega^2 + i \mu_0\sigma\omega
```
which is now complex! 

We can rewrite this in the form a relative permitivity $\epsilon_r(\omega)$, for $k^2 = \omega^2 / c^2 = \omega^2 \,\mu_0 \,\epsilon(\omega)$ with 
$\epsilon = \epsilon_0\,\epsilon_r$, therefore:
```{math}
\epsilon_r(\omega) = \frac{\epsilon(\omega)}{\epsilon_0} = \underbrace{1}_{vacuum\, part} + \underbrace{i \frac{\sigma}{\epsilon_0\omega}}_{dispersion\,part} 
```
If we calculate the energy of waves travelling through this media, the dispersion part corresponds to the energy losses of the electromagnetic field.  
