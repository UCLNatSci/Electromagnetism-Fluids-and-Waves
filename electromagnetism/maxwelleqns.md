# Maxwell's Equations

## Gauss's Law in Differential Form
Lets revisit what we have learnt about Gauss's law for electric charges
```{math}
\iint_A  {\bf E} \cdot\,\mathrm{d} {\bf A} = \frac{Q_{encl}}{\epsilon_0}
```
since the charge $Q_{encl}$ is enclosed within some closed surface area, that is the boundary to a volume, we can equally think about a charge density inside that volume
```{math}
\iint_A  {\bf E} \cdot\,\mathrm{d} {\bf A} = \iiint_V \frac{\rho}{\epsilon_0}\,\mathrm{d} V
```
If we recall the divergence theorem, it states that the flux of a vector field passing a closed surface area is related to the divergence of the vector field 
within the volume, so for an electric field
```{math}
\iint_A  {\bf E} \cdot\,\mathrm{d} {\bf A} = \iiint_V \nabla \cdot {\bf E}\,\mathrm{d} V
```
so we can write that, up to a boundary term
```{math}
\iiint_V \left(\nabla \cdot {\bf E} - \frac{\rho}{\epsilon_0}\right)\,\mathrm{d} V = 0
```
in order for this expression to be true for <em> any </em>  volume $V$ considered, the expression within the integrand must equal zero, meaning that:
```{math}
:label: divE
\nabla \cdot {\bf E} = \frac{\rho}{\epsilon_0} 
```
Likewise we can do the same for magnetic fields, which in the absence of magnetic monopoles will look like:
```{math}
:label: divB
\nabla \cdot {\bf B} = 0 
```


## Ampère's Law in Differential Form
We can revisit Amp\`ere's law, with the displacement current:
```{math}
\oint_{\ell}  {\bf B} \cdot\,\mathrm{d} {\bf \ell} = \mu_0 I + \mu_0\epsilon_0\iint_A \frac{\partial {\bf E}}{\partial t}\,\mathrm{d}{\bf A}
```
Given we know the Stoke's theorem tells us that the summing of a vector field around a closed loop will be related to the curl of the field, for the magnetic field:
```{math}
\oint_{\ell}  {\bf B} \cdot\,\mathrm{d} {\bf \ell} = \iint_A \left(\nabla \times {\bf B}\right)\cdot\mathrm{d}{\bf A}
```
Also we can think about the current $I$ in terms of a current density ${\bf J}$ through some conductor with surface area $A$, meaning that:
```{math}
I = \iint_A {\bf J}\cdot\mathrm{d}{\bf A}
```
which all put together gives:
```{math}
\iint_A \left( \nabla \times {\bf B} - \mu_0 {\bf J} - \mu_0\epsilon_0\frac{\partial {\bf E}}{\partial t}\right)\cdot\mathrm{d}{\bf A} = 0
```
in order for this expression to be true for <em> any </em> bounding area $A$ considered, the expression within the integrand must equal zero, meaning that:
```{math}
:label: curlB
\nabla \times {\bf B} = \mu_0 {\bf J} + \mu_0\epsilon_0\frac{\partial {\bf E}}{\partial t}
```


## Faraday's Law in Differential Form
Finally looking at Faraday's law again:
```{math}
\mathcal{E} = -\frac{\partial}{\partial t}\iint_A {\bf B}\cdot \mathrm{d} {\bf A} = -\iint_A \frac{\partial {\bf B}}{\partial t}\cdot \mathrm{d} {\bf A}
```
The EMF $\mathcal{E}$ can be thought of as a potential difference induced by the changing magnetic flux - in a circuit this potential difference pushes charges, 
causing a current to flow.  We can write $\mathcal{E}$ as a contour integral, summing up each of the infinitesimal electric field segments 
$\mathrm{d} {\bf \ell}$ in the circuit:
```{math}
\mathcal{E} = -\int_{{\bf r}_1}^{{\bf r}_2} {\bf E} \cdot \mathrm{d}{\bf \ell} = \oint_c {\bf E} \cdot \mathrm{d}{\bf \ell}
```
where the final sign on the integral is given by the convention for clockwise conventional current.  {numref}`MagnetInACoil` shows that a positive 
change in $\Phi_B$ eventually produces current in a negative direction.  We can rewrite this using Stoke's theorem:
```{math}
\oint_\ell {\bf E} \cdot \mathrm{d} \ell= \iint_A \left(\nabla \times {\bf E}\right)\cdot \mathrm{d} {\bf A} \nonumber
```
and so this can all be written as
```{math}
\iint_A \left(\nabla \times {\bf E} + \frac{\partial {\bf B}}{\partial t}\right)\cdot \mathrm{d} {\bf A} = 0
```
in order for this expression to be true for <em> any </em> bounding volume $A$ considered, the expression within the integrand must equal zero, meaning that:
```{math}
:label: curlE
\nabla \times {\bf E} = - \frac{\partial {\bf B}}{\partial t} 
```


## Maxwell's Equations
We can collect together Equations {eq}`divE`, {eq}`divB`, {eq}`curlB` and {eq}`curlE` and present as Maxwell's equations:
```{math}
:label: MaxwellsEqns
\nabla\cdot {\bf E} &=&\, \frac{\rho}{\epsilon_0}    \\
\nabla \cdot {\bf B} &=&\, 0   \\
\nabla \times {\bf E} &=&\, -\frac{\partial {\bf B}}{\partial t}   \\
\nabla \times {\bf B} &=&\, \mu_0 {\bf J} + \mu_0\epsilon_0\frac{\partial {\bf E}}{\partial t} 
```
These are <b>local</b> equations, they can be solved at points in space ${\bf r}$, rather than the integral form <b>global</b> equations, which we had to 
think about in terms of a bounding surface ${\bf A}$.  Another thing to notice is that the second / third of Maxwell's equations are <em> homogeneous</em>, 
they are sourced only by the ${\bf E},\,{\bf B}$ fields, whereas the first / fourth equations are inhomogeneous, being sourced by additional 
scalar/vector fields $\rho,\,{\bf J}$.  


## Maxwell's Equations in Matter*
Recall that Equation {eq}`MaxwellsEqns` is valid in vacuum, however we know that in matter, electromagnetic fields are better described in terms of 
${\bf E} \rightarrow {\bf D}$ and ${\bf B} \rightarrow {\bf H}$, which means we can write Maxwell's equations in matter as:
```{math}
:label: MaxwellsEqnsMatter
\nabla\cdot {\bf D} &=&\,\rho_{free}   \\
\nabla \cdot {\bf H} &=&\, 0   \\
\nabla \times {\bf E} &=&\, -\frac{\partial {\bf B}}{\partial t} \\
\nabla \times {\bf H} &=&\,  {\bf J}_{free} + \frac{\partial {\bf D}}{\partial t} 
```
where $\rho_{free}$ and ${\bf J}_{free}$ represent charges that move within matter.  

## Magnetic Monopoles*
We could add source terms to Maxwell's equations that would need to be present, if magnetic monopoles were found to exist: 
```{math}
:label: MaxwellsEqnsBMonopole
\nabla\cdot {\bf E} &=&\, \frac{1}{\epsilon_0}\,\rho  \\
\nabla \cdot {\bf B} &=&\, \mu_0 \,\rho_m  \\
\nabla \times {\bf E} &=&\, - {\bf J}_m -\frac{\partial {\bf B}}{\partial t}  \\
\nabla \times {\bf B} &=&\, \mu_0 {\bf J} + \mu_0\epsilon_0\frac{\partial {\bf E}}{\partial t}
```
where $\rho_m$ is the monopole charge density and ${\bf J}_m$ is the monopole current density.  We notice the increase degree of symmetry between the 
equations here now - all the equations are now inhomogeneous.

Additionally if there are $Q_m$ which could move under magnetic and electric fields, we would have to amend the expression from 
Equation {eq}`LorentzForce` for the Lorentz force law:
```{math}
{\bf F} = Q\left( {\bf E} + {\bf v} \times {\bf B} \right) + Q_m\left( {\bf B} - \frac{1}{c^2}{\bf v} \times {\bf E} \right)
```
where $Q_m$ is the size of the magnetic charge. No current evidence of these in nature, but symmetry breaking of GUT theories suggest they 
should have existed and ideas like cosmic inflation are proposed to explain the non-observation just as a vast 
dilution within our observable universe.  The observed quantisation of electric charge, into chunks no smaller than $\pm q_e$ can be 
explained by the presence of a <em> single</em>  magnetic monopole in our universe, as Dirac proposed in 1931.  A good paper on magnetic 
monopoles is [here](https://doi.org/10.1080/00107514.2012.685693), Dirac's paper can be found [here](https://doi.org/10.1098/rspa.1931.0130) and for more on 
cosmic inflation, check out any good lecture course on, such as these from [DMTP](http://www.damtp.cam.ac.uk/user/tong/cosmo/cosmo.pdf).