# Energy in an Electromagnetic field
Whilst we are now comfortable with the idea of electric and magnetic fields (and how the two are inextricably linked), we can return 
to an idea from the waves section, namely where are all the sources of energy in this system? 

## Deriving Intrinsic Energy from Potentials*
Recall the intrinsic electrostatic potential energy $U_E$ from a system of charges from Equation {eq}`elecpotenergy`, we can 
modify this to consider a continuous charge density $\rho({\bf r})$:
```{math}
U_E = \frac{1}{2}\sum_{i=1}^N Q_i\,{V_E}({\bf r}_i) \rightarrow U_E  = \frac{1}{2}\iiint \rho({\bf r}) \,V_E({\bf r}) \, \mathrm{d} V 
```
Given Equation {eq}`divE`, we can rewrite this using Gauss's law in differential form:
```{math}
U_E  = \frac{1}{2}\,\epsilon_0\,\iiint V_E\,(\nabla\cdot {\bf E})\, \, \mathrm{d} V 
```
For some vector field ${\bf A}$ and scalar field $B$, we find the following vector identity applies:
```{math}
\nabla\cdot \left( {\bf A}\,B\right) = {\bf A}\,\cdot(\nabla\, B) + B\,\nabla\cdot {\bf A} \Longrightarrow B\,\nabla\cdot {\bf A} = 
\nabla\cdot \left( {\bf A}\,B\right) - {\bf A}\,\cdot(\nabla\, B)
``` 
and therefore the potential energy result becomes:
```{math}
U_E  = \frac{1}{2}\,\epsilon_0\,\left[\iiint \nabla\cdot (V_E\,{\bf E}) \, \mathrm{d} V - \iiint {\bf E}\cdot (\nabla\,V_E) \, \mathrm{d} V\right]
```
Using the divergence theorem on the first term and applying tne definition of $V_E$ from Equation \ref{eqn:Efieldgradpotential}, this reduces to:
```{math}
U_E &=& \,\frac{1}{2}\,\epsilon_0\,\left[\iint V_E\,{\bf E} \cdot \mathrm{d} {\bf A} - \iiint {\bf E}\cdot (-{\bf E}) \, \mathrm{d} V\right] \\
&=& \,\frac{1}{2}\,\epsilon_0\,\left[-\iint V_E\,(\nabla V_E) \cdot \mathrm{d} {\bf A} - \iiint {\bf E}\cdot (-{\bf E}) \, \mathrm{d} V\right] \\
&=& \,\frac{1}{2}\,\epsilon_0\,\left[\iiint E^2 \, \mathrm{d} V -\,\iint V_E\,(\nabla V_E) \cdot \mathrm{d} {\bf A} \right]
```
If we integrate over all space, then since $V_E(r) \rightarrow 0$ for $r \rightarrow \infty$ by definition, the second term here goes to zero.  
Then we can define the energy density $u_E$ through:
```{math}
U_E = \iiint u_E\,\mathrm{d} V= \iiint \frac{1}{2}\,\epsilon_0\,E^2 \, \mathrm{d} V \Longrightarrow u_E = \frac{1}{2}\,\epsilon_0\,E^2 
```

## Energy Flux and Poynting Vector
To find the total energy density we would need to repeat this process for ${\bf B}$ (which is fairly lengthy!), but we can consider this problem 
through analogy.  The form of the Equation {eq}`curlB` in vacuum reveals that the units of the ${\bf B}$ field related to the ${\bf E}$ field by:
```{math}
:label: E=cB
\frac{[B]}{[\textrm{Length}]} = \epsilon_0\,\mu_0\,\frac{[E]}{[\textrm{Time}]} \Rightarrow [B] = [E]\,[\textrm{Speed}]\,\epsilon_0\,\mu_0 
```
Equation {eq}`SpeedOfLight` says $c = 1/\sqrt{\epsilon_0\,\mu_0}$, hence using $c$ as the wave speed, $u_B$ has the form:
```{math}
u_B = \frac{1}{2}\,\epsilon_0\,c^2\,B^2 = \frac{1}{2\,\mu_0}\,B^2
```
Therefore the total intrinsic energy density of electromagnetic fields is given by:
```{math}
u = u_E + u_B = \frac{1}{2}\left(\epsilon_0\,E^2 + \frac{1}{\mu_0}\,B^2 \right)
```
Equations for $u$ also appear within Maxwell's equations, take Equations {eq}`curlB` and {eq}`curlE`:
```{math}
\frac{1}{\mu_0}{\bf E} \cdot \nabla \times {\bf B} &=& \,\left({\bf J} + \epsilon_0\frac{\partial {\bf E}}{\partial t} \right)\cdot {\bf E} = 
{\bf J} \cdot {\bf E} + \frac{\partial}{\partial t}\left( \frac{1}{2}\epsilon_0 E^2 \right) \label{eqn:Spart1}\\
\frac{1}{\mu_0}{\bf B} \cdot \nabla \times {\bf E} &=& \,-\frac{1}{\mu_0}\left(\frac{\partial {\bf B}}{\partial t}\right)\cdot {\bf B} = 
-\frac{\partial}{\partial t}\left( \frac{1}{2\,\mu_0}B^2 \right) \label{eqn:Spart2}
```
Tidying up these expressions we find:
```{math}
\frac{1}{\mu_0}{\bf E} \cdot \nabla \times {\bf B} - \frac{1}{\mu_0}{\bf B} \cdot \nabla \times {\bf E} = {\bf J} \cdot {\bf E} + \frac{\partial u}{\partial t}
```
Finally through $ \nabla \cdot ({\bf A} \times {\bf B}) = (\nabla \times {\bf A}) \cdot {\bf B} - {\bf A} \cdot (\nabla \times {\bf B})$, we rewrite as:
```{math}
\frac{\partial u}{\partial t} = -\nabla \cdot {\bf S} - {\bf J} \cdot {\bf E}
```
where we identify the vector ${\bf S}$ as the <b>Poynting Vector</b>:
```{math}
{\bf S} = \frac{1}{\mu_0}{\bf E} \times {\bf B}
```
which indicates the flow of electromagnetic energy within a system - recall we talked about the flow of wave energy in the waves section with 
a vector of this form.  

The form of this equation draws similarity with the <b> Continuity Equation:</b>
```{math}
\frac{\partial \rho}{\partial t} = -\nabla \cdot {\bf F} - \sigma
```
where $\rho$ is the density of quantity $X$ being investigated, ${\bf F}$ is the flux of $X$ and $\sigma$ is the rate at which $X$ is 
generated per unit volume per unit time.  Thus we can see that the Poynting vector ${\bf S}$ is the electromagnetic energy flux and 
${\bf J}\cdot {\bf E}$ relates to the energy given to free charges with current density ${\bf J}$.

## Electromagnetic Plane Waves
Recall the plane wave solutions from Equation {eq}`PlaneWaveSolns`:
```{math}
{\bf E} &=& \,\begin{bmatrix}
 E_0 \\
 0 \\
 0 
\end{bmatrix}\,\exp(i(k_z z - \omega t)) \\
{\bf B} &=&\, \begin{bmatrix}
 0 \\
 B_0 \\
 0
\end{bmatrix} \,\exp(i(k_z z  - \omega t)) 
```
If we examine the Poynting energy flux ${\bf S}= \frac{1}{\mu_0} {\bf E} \times {\bf B}$:
```{math}
{\bf S} = \begin{bmatrix}
 0 \\
 0\\
 E_0\,B_0/\mu_0
\end{bmatrix}\,\exp(2i(k_z z  - \omega t)) = \begin{bmatrix}
 0 \\
 0\\
 S_0
\end{bmatrix}\,\exp(2i(k_z z  - \omega t))
```
which suggests for wave oscillations in the $({\bf x},\,{\bf y})$ planes, the wave energy is transmitted in the ${\bf z}$ direction, 
as we see in {numref}`EMPlaneWaves` (we knew this from the Waves chapter).  Interestingly the energy flux speed is also given by 
$v_S = c = v_{E,\,B}$ but the wavelength $\lambda_S = \frac{1}{2}\lambda_{E,\,B}$ and frequency $f_S = 2\,f_{E,\,B}$ are changed.


## Characteristic Impedance*
Another way to view these results is through Equation {eq}`kEBperp`, 
```{math}
{\bf S} = \,\frac{1}{\mu_0}{\bf E}\times {\bf B} = \frac{1}{\mu_0}{\bf E}\times \left(\frac{1}{\omega} {\bf k} \times {\bf E}\right) 
= \frac{1}{\omega\,\mu_0} \bigg[ \left({\bf E}\cdot {\bf E}\right){\bf k} - \left({\bf E} \cdot {\bf k} \right){\bf E} \bigg]
```
where we have used the triple vector product expression, and given Equation {eq}`kEBperp` shows that $\bf E,\, k$ are perpendicular:
```{math}
{\bf S} = \frac{1}{\omega\,\mu_0}|{\bf E}|^2\,\,{\bf k} = \frac{k_z}{\omega\,\mu_0}|{\bf E}|^2\,\,\hat{{\bf z}}
```
Given that $\omega / k_z = c$ here, this means we can write the expression as:
```{math}
{\bf S} = \frac{1}{c\,\mu_0}\,|{\bf E}|^2\,\,\hat{{\bf z}}
```
For a plane wave this will be a time varying expression, however recall in the Waves section we discussed time averaging waves when finding 
their power. For the plane wave propograting along the $z$ axis in {eq}`PlaneWaveSolns`:
```{math}
{\bf E} = \textrm{Re}\Big[{\bf E_0}\,\exp(i({\bf k \cdot x} - \omega t))\Big] = {\bf E_0}\,\cos(k_z x - \omega t)
```
therefore we find that:
```{math}
S_{\langle T \rangle} &=&\, \frac{1}{\eta}{E_0}^2\left(\frac{1}{T}\int_0^T\,\cos^2(k_z x - \omega t)\,\mathrm{d}t\right) \\
&=&\, \frac{{E_0}^2}{2\,\eta\,T}\left(\int_0^T\,\left(\cos(2(k_z x - \omega t))+1\right)\,\mathrm{d}t\right)\\ 
&=&\, \frac{{E_0}^2}{2\,\eta\,T}\left[\frac{1}{2\omega}\sin(2(k_z x - \omega t))+t\right]_0^T\\
&=&\, \frac{1}{2 \eta}\,{E_0}^2
```
where $\eta$ is the characteristic impedance of the transmission medium, which has units of electrical resistance $\Omega$. In a vacuum, this takes the value 
$\eta \simeq 377\, \Omega$, but in matter its value will vary according to $\epsilon(\omega),\,\mu(\omega)$, as mentioned previously.

