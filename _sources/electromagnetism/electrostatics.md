# Electrostatics

## Coulombs Law

Lets start with the basics, Coulombs law in Equation {eq}`CoulombsLaw`, tells us that a repulsive force between two 
charges $Q_i$, $Q_1$ at the origin and $Q_2$ at distance $r$:
```{math}
:label: CoulombsLaw
F_c = \frac{Q_1\,Q_2}{4\,\pi\,\epsilon_0}\frac{1}{r^2}
```
Obviously we can shift the charges, so that in general  $(Q_1({\bf r}_1), \, Q_2({\bf r}_2))$.  Also ${\bf F}_c$ is a vector quantity, 
so we can write the force acting on $Q_2({\bf r}_2)$ due to $Q_1({\bf r}_1)$ as:
```{math}
{\bf F}_{12} = \frac{Q_1\,Q_2}{4\,\pi\,\epsilon_0}\frac{1}{|{\bf r}_1 - {\bf r}_2|^2}\,\hat{{\bf r}}_{12}
``` 
where $\hat{{\bf{r}}_{12}$ is a normalised vector that points from $Q_1({\bf r}_1) \rightarrow Q_2({\bf r}_2)$.  This force is related 
directly to the size of the charges and to the inverse square of the distance between them.  We can define the <b>Electric Field </b>
as the force per unit charge, in this case we can find the electric field due to the charge $Q_1$ measured at ${\bf r}_2$ as:
```{math}
:label: EFieldCharge
{\bf E} = \frac{{\bf F}_c}{Q_2} = \frac{Q_1}{4\,\pi\,\epsilon_0}\frac{1}{|{\bf r}_1-{\bf r}_2|^2}\,\hat{{\bf r}}_{12}
```
This expression has $Q_1$ taking the role of a <b> Source Charge </b>.  If we have a point charge, we can draw the electric field around it, 
as shown in {numref}`PositiveChargeEField`.
```{figure} ../figures/PositiveChargeEField.png
---
name: PositiveChargeEField
---
Electric fields lines from a positive charge
```

Our field lines radiate outwards radially, depending only on the distance from a point to the charge (here we are just assuming a point charge) 
and in the direction a positive charge would follow (here outwards as like charges repel).  These are all very sound ideas that we have no doubt 
learnt before, the question is whilst Coulombs law is a very effective tool to empirically describe electric fields from point charges, where 
does is arrive from? Will it work in more complicated situations?  

## Gauss's Law
Lets now look at electric fields from the point of view of an a containing surface and flux crossing the surface boundary.  Starting with a charge 
$Q$, we can surround this in three dimensions by a sphere, as seen in Figure {nameref}`EFieldFlux`.
```{figure} ../figures/EFieldFlux2.png
---
name: EFieldFlux
---
Flux of the electric field from a point charge $+q$ passing through a spherical surface.
```

Now we have field lines perpendicular to the surface, here a sphere, so a similar situation to hose pipe and the water.  But now we have 
to think about "how close" the field lines get over the spheres surface - they should really be thought of as infinitesimally small, so we use 
an area integral summing up the flux crossing the bounding surface area $A$:  
```{math}
\Phi_E = \iint_A {\bf E}\cdot \mathrm{d}{\bf A}
```
What will this flux we related to? Well imagine us increasing the size of the charge at the centre of the sphere, clearly the size of the Coulombic 
force between this and another charge will increase and so the magnitude of the electric field will increase.  As the flux is counting however much 
of the electric field is crossing the spherical boundary here, clearly the flux will increased, so we can make the statement:
```{math}
\iint {\bf E}\cdot \mathrm{d} {\bf A} \propto Q
```
This makes sense because both flux and charge are scalar quantities and because the flux only seems to change with the charge linearly 
(we saw this in Equation {eq}`EFieldCharge`).  Lets just assign a constant $k$ to make this an equation
```{math}
\iint {\bf E}\cdot \mathrm{d} {\bf A} = k\,Q
```
and we will aim to find the value of $k$ later.  One thing we can find straightforwardly is what units $k$ should have
```{math}
[\textrm{k}] = [\rho][{\bf v}][\textrm{Q}]^{-2} = \textrm{kg}\,\textrm{m}^{-3}\,\textrm{m}\,\textrm{s}^{-1}\,\textrm{C}^{-2} 
= \textrm{kg}\,\textrm{m}^{-2}\,\textrm{s}^{-1}\,\textrm{C}^{-2}
```
We can aim to use this flux law to get to Coulombs law, as the two results must agree, so starting with the spherical surface area $A$ 
around the charge $Q$ we find that the area normal vector is ${\bf A} = A_r\,\hat{{\bf r}}$.  The surface integral term therefore reduces to:
```{math}
\iint {\bf E}\cdot \mathrm{d} {\bf A} = \iint E_r \,\mathrm{d} A_r
``` 
where we decomposed $\bf E$ in to components:
```{math}
{\bf E} = E_r \hat{{\bf r}} +E_\theta \hat{{\bf \theta}} + E_\phi \hat{{\bf \phi}}
```
By symmetry therefore the electric field does not have an angular $(\theta,\, \phi)$ dependence - this makes sense physically because 
whether a charge is on our left or right hand side does not charge the force felt if it is at the same fixed distance.  Calculating 
$\iint {\bf E}\cdot \mathrm{d} {\bf A}$ is straightforward on a sphere:
```{math}
\iint E_r\, \mathrm{d} A_r = \iint E_r \,r^2 \,\sin \theta\, \mathrm{d} \theta \,\mathrm{d} \phi &=& \,E_r \,(4 \pi r^2) = k Q\\
\Rightarrow {\bf E} &=& \,E_r \,\hat{{\bf r}} = \frac{k Q}{4 \,\pi\,r^2} \,\hat{{\bf r}}
```
Comparing this result with Coulomb's law in Equation {eq}`CoulombsLaw`, we fix $k = 1/\epsilon_0$ (which also has the required units, check 
this for yourself!).  So our final expression, which is known as <b>Gauss's Law</b>, can be written as:
```{math}
:label: GaussLaw
\iint_A {\bf E} \cdot \mathrm{d} {\bf A} = \frac{Q}{\epsilon_0} 
```
The charge $Q$ here should be carefully explained, central to the discussion of the flux were the field lines from the 
charge cutting the bounding surface area $A$, so we really mean to write the $Q$ as one enclosed by the area $A$ and so 
we should really write Gauss's law as:
```{math}
\iint_A {\bf E} \cdot \mathrm{d} {\bf A} = \frac{Q_{enclosed}}{\epsilon_0}
```

## Gravitational Analogue
One aspect of the equations of electrostatics to notice is that the original consideration of Coulomb's law could be extended over 
to discuss Newton's law of gravitation.  We notice that the equations are essentially just a redefinition of fields and constants:
```{math}
F_C = \frac{1}{4\pi \epsilon_0}\frac{Q_1\,Q_2}{r^2} \Longleftrightarrow F_G = -G\frac{\,M_1\,M_2}{r^2}
```
where $F_G$ is negative as it is only an attractive force, these suggest that by analogy:  
```{math}
\frac{1}{\epsilon_0} \Longleftrightarrow -4\pi\, G, \quad \quad Q_i \Longleftrightarrow M_i
```
Our electric field here ${\bf E}$ has a direct analogue in the gravitational field ${\bf g}$:
```{math}
{\bf E} = \frac{{\bf F}_E}{Q} \Longleftrightarrow {\bf g} = \frac{{\bf F}_N}{M}
```
and therefore we could examine Gauss's law for gravitational fields:
```{math}
:label: gravfieldGauss
\iint {\bf g} \cdot \mathrm{d} {\bf A} = -4\pi\,G\,M_{enclosed}
```
An application of this is understanding the interior gravitational field of a large uniform astrophysical body (e.g. the Earth), 
which we find results in the analogue of {numref}`electricfieldsphere`.  
