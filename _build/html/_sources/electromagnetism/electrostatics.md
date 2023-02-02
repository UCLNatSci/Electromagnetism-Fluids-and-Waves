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
where $\hat{\bf r}_{12}$ is a normalised vector that points from $Q_1({\bf r}_1) \rightarrow Q_2({\bf r}_2)$.  This force is related 
directly to the size of the charges and to the inverse square of the distance between them.  We can define the <b>Electric Field </b>
as the force per unit charge, in this case we can find the electric field due to the charge $Q_1$ measured at ${\bf r}_2$ as:
```{math}
:label: EFieldCharge
{\bf E} = \frac{{\bf F}_c}{Q_2} = \frac{Q_1}{4\,\pi\,\epsilon_0}\frac{1}{|{\bf r}_1-{\bf r}_2|^2}\,\hat{{\bf r}}_{12}
```
This expression has $Q_1$ taking the role of a <b>Source Charge</b>.  If we have a point charge, we can draw the electric field around it, 
as shown in {numref}`PositiveChargeEField`.
```{figure} ../figures/PositiveChargeEField.png
---
name: PositiveChargeEField
---
Electric fields lines from a positive charge
```

Our field lines radiate outwards radially, depending only on the distance from a point to the charge (here we are just assuming a point charge) 
and in the direction a positive charge would follow (here outwards as like charges repel).  

These are all very sound ideas that we have no doubt learnt before, the question is whilst Coulombs law is a very effective tool to empirically 
describe electric fields from point charges, where does is arrive from? Will it work in more complicated situations?  


## Superposition of charges

## Infinitesimal Coulombs law
Lets start with a simpler problem first though, a semicircular arc of charge, as depicted in {numref}`SemiCircularArcofCharge`
```{figure} ../figures/SemiCircularArcofCharge.png
---
name: SemiCircularArcofCharge
---
An finite line of charges, with charge density $\lambda$, arranged in a semicircular arc of length $L$ and centered on the origin.
```
What are the symmetries of this semicircular system? Well if we consider a section of the arc, it will carry a charge $\mathrm{d} Q$ which we can rewrite as 
$\mathrm{d} Q = \lambda \mathrm{d} \ell$.  Given that for a circular arc $\ell = r \theta$ and since $L = \pi r$, therefore 
```{math}
\mathrm{d} Q = \frac{\lambda\,L}{\pi} \mathrm{d} \theta
```
where $\theta$ is an angle that moves round the arc, as we define in {numref}`AngularArcofCharge`.
```{figure} ../figures/SemiCircularArcofCharge2.png
---
name: AngularArcofCharge
---
Semicircular arc of charges, centered on the origin, with charge element $\mathrm{d} Q$, length $L$, radius $r$ and angle $\theta$.
```
Clearly now we want to integrate over all the charges $\mathrm{d}Q$ which will involve integrating over all angles $\mathrm{d} \theta$.  Since we are treating 
these infitesimal charge elements as point charges, the magnitude of the electric field has the form:
```{math}
\mathrm{d} E = \frac{\mathrm{d}Q}{4 \pi\,\epsilon_0\,r^2} = \frac{\pi \,\mathrm{d}Q}{4\,\epsilon_0\,L^2}
```
The direction of the field components however will change depending on whereabouts along the ring we are, clearly are $\theta = 0$, the field is directed along the $x$-axis only:
```{math}
\mathrm{d}{\bf E}_{\theta = 0} = \frac{\pi \,\mathrm{d}Q}{4\,\epsilon_0\,L^2} \,\hat{\bf i} + 0 \,\hat{\bf j}
```
Whilst if we examine the field at $\theta = -\pi/2$ and $\theta = \pi/2$, we notice that the electric field will be aligned in the positive and negative $y$-axis directions (respectively):
```{math}
\mathrm{d}{\bf E}_{\theta = -\pi/2} &=&\, 0 \,\hat{\bf i} + \frac{\pi \,\mathrm{d}Q}{4\,\epsilon_0\,L^2} \,\hat{\bf j} \\
\mathrm{d}{\bf E}_{\theta =\pi/2} &=&\, 0 \,\hat{\bf i} - \frac{\pi \,\mathrm{d}Q}{4\,\epsilon_0\,L^2} \,\hat{\bf j} 
```
In fact we see that there will always be a cancellation of the $y$ components of the electric field from the arc, we can always pair up the components over 
$-\pi/2 \leq \theta \leq \pi/2$, this leaves just the $x$ components:
```{math}
\mathrm{d}{\bf E}_{\theta} &=&\, \frac{\pi \,\mathrm{d}Q}{4\,\epsilon_0\,L^2} \Big[ \cos(\theta) \,\hat{\bf i} + \sin(\theta) \,\hat{\bf j} \Big] \\
\int_0^{\bf E} \mathrm{d}{\bf E}_{\theta} &=&\,  \frac{\pi}{4\,\epsilon_0\,L^2} \frac{\lambda\,L}{\pi} \int_{-\pi/2}^{\pi/2} \Big(\cos(\theta)\,\hat{\bf i} + 
\sin(\theta)\,\hat{\bf j} \Big)\,\mathrm{d} \theta\\
{\bf E} &=&\,  \frac{\lambda}{4\,\epsilon_0\,L}  \Big[\sin(\theta)\,\hat{\bf i} - \cos(\theta)\,\hat{\bf j}\Big]_{-\pi/2}^{\pi/2} = \frac{\lambda}{2\,\epsilon_0\,L} \,\hat{\bf i} + 0\,\hat{\bf j}
```
### Rectilinear Rod
Lets return to the rod in {numref}`Finitelineofcharge`, we can set this system up in {numref}`Finitelineofcharge2`, trying to make the rod as symmetric as possible:

```{figure} ../figures/FiniteLineOfCharges3.png
---
name: Finitelineofcharge2
---
An finite line of charges, with charge density $\lambda$, with length $L$, symmetrically aligned over the $x$ axis. We pick out an element of charge indicated 
in red, so here $\mathrm{d} Q = \lambda \,\mathrm{d} x$.
```
With a line of charge, of length $L$, aligned along the $x$ axis, we can look at a point at a distance $R$ away, aligned halfway along the rod.  Once again we can break up this 
line of charge into infinitesimal chunks, each contributing $\mathrm{d} Q$ charge and then the overall electric field will be found by superposition.  The magnitude of the electric 
field at a distance $R$ from the rod appears to be given by:
```{math}
\mathrm{d} E = \frac{\mathrm{d}Q}{4\pi \,\epsilon_0\,r^2}
```
where the length $r$ can take values between $R \leq r \leq \sqrt{R^2 + L^2 / 4}$. 

In this system, we find that at $x = 0$, the electric field is only aligned in the $y$ direction:
```{math}
\mathrm{d} {\bf E}_{x = L/2} = 0\,\hat{\bf i} + \frac{\mathrm{d}Q}{4\pi \,\epsilon_0\,R^2}\,\hat{\bf j}
```
whereas the $x$ components of the electric field for all the lengths at $-L/2 \leq x < 0$ and $0 > x \leq L/2$ will pair up, to cancel out, leaving only the $y$ components:
```{math}
\mathrm{d} {\bf E} &=&\, \frac{\mathrm{d}Q}{4\pi \,\epsilon_0\,r^2} \Big (\sin(\theta)\,\hat{\bf i} + \cos(\theta)\,\hat{\bf j}\Big)\\
\int_0^{\bf E} \mathrm{d} {\bf E}' &=&\, \frac{\lambda }{4\pi \,\epsilon_0} \int_{-L/2}^{L/2}\Big (\frac{x}{r^3}\,\hat{\bf i} + \frac{R}{r^3}\,\hat{\bf j}\Big)\,\mathrm{d} x\\
{\bf E} &=&\, \frac{\lambda}{4\pi \,\epsilon_0} \int_{-L/2}^{L/2}\Bigg(\frac{x}{(x^2 + R^2)^{3/2}}\,\hat{\bf i} + \frac{R}{(x^2 + R^2)^{3/2}}\,\hat{\bf j}\Bigg)\,\mathrm{d} x 
```
Where we have used the substitutions $\sin(\theta) = x/r = x / \sqrt{x^2 + R^2},\, \cos(\theta) = R / r = R / \sqrt{x^2 + R^2}$.  We can also use the substitution 
$x = R\,\tan(\theta) \Rightarrow \mathrm{d}x = R\,\sec^2(\theta)$ to find:
```{math}
{\bf E} &=&\, \frac{\lambda}{4\pi \,\epsilon_0} \int_{x = -L/2}^{x = L/2}\Big (\frac{R \,\tan(\theta)}{R^3\,\sec^3(\theta)}\,\hat{\bf i} + 
\frac{R}{R^3\,\sec^3(\theta)}\,\hat{\bf j}\Big) R\,\sec^2(\theta)\,\mathrm{d} \theta \\
 &=&\,\frac{\lambda}{4\pi \,\epsilon_0\,R} \int_{x = -L/2}^{x = L/2}\Bigg(\sin(\theta)\,\hat{\bf i} + \cos(\theta)\,\hat{\bf j}\Bigg)\,\mathrm{d} \theta \\
 &=&\,\frac{\lambda}{4\pi \,\epsilon_0\,R} \Big[ -\cos(\theta)\,\hat{\bf i} + \sin(\theta)\,\hat{\bf j}\Big]_{x = -L/2}^{x = L/2} \\
 &=&\,\frac{\lambda}{4\pi \,\epsilon_0\,R} \Big[ -\frac{R}{(x^2 + R^2)^{1/2}}\,\hat{\bf i} + \frac{x}{(x^2 + R^2)^{1/2}}\,\hat{\bf j}\Big]_{-L/2}^{L/2} \\
 &=&\,\frac{\lambda}{4\pi \,\epsilon_0\,R} \Big( 0 \,\hat{\bf i} + \frac{L}{(L^2/4 + R^2)^{1/2}}\,\hat{\bf j}\Big) 
```
Which results in:
```{math}
{\bf E} = \frac{\lambda\,L }{4\pi \,\epsilon_0\,R\,\sqrt{L^2/4 + R^2}}\,\hat{\bf j}
```
Notice that in the limit of $L \gg 1$, this would look like:
```{math}
{\bf E} \rightarrow \frac{\lambda}{2\pi \,\epsilon_0\,R}\,\hat{\bf j}
```
which is essentially the result for the infinite line of charge in Equation {eq}`InfiniteChargeLineEField`.

We note therefore that the relevant expression for the magnitude of the electric field at a distance $R$ from the rod is found from just the $y$ component:
```{math}
:label: EFieldWire
\mathrm{d} E &=&\, \frac{\mathrm{d}Q}{4\pi \,\epsilon_0\,r^2}\,\cos(\theta) = \frac{\mathrm{d}Q\,R}{4\pi \,\epsilon_0\,r^3}\\
\Rightarrow E &=&\,  \frac{\lambda}{4\pi \,\epsilon_0}\int_{rod} \frac{R}{r^3}\,\mathrm{d}x = \frac{\lambda}{4\pi \,\epsilon_0\,R} \Bigg[\frac{x}{\sqrt{x^2+R^2}}\Bigg]_{rod}
```

## Gauss's law
Lets now look at electric fields from the point of view of an a containing surface and flux crossing the surface boundary.  Starting with a charge 
$Q$, we can surround this in three dimensions by a sphere, as seen in Figure {numref}`EFieldFlux`.
```{figure} ../figures/EFieldFlux2.png
---
name: EFieldFlux
---
Flux of the electric field from a point charge $+q$ passing through a spherical surface.
```

Now we have field lines perpendicular to the surface, here a sphere, so a similar situation to hose pipe and the water.  But now we have 
to think about <em>how close</em> the field lines get over the spheres surface - they should really be thought of as infinitesimally small, so we use 
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
where we decomposed the electric field $\bf E$ in to components:
```{math}
{\bf E} = E_r \hat{{\bf r}} + E_\theta \hat{{\bf \theta}} + E_\phi \hat{{\bf \phi}}
```
By symmetry therefore the electric field does not have an angular $(\theta,\, \phi)$ dependence - this makes sense physically because 
whether a charge is on our left or right hand side does not charge the force felt if it is at the same fixed distance.  

Calculating $\iint {\bf E}\cdot \mathrm{d} {\bf A}$ is straightforward on a sphere:
```{math}
\iint E_r\, \mathrm{d} A_r = \iint E_r \,r^2 \,\sin \theta\, \mathrm{d} \theta \,\mathrm{d} \phi
```
Since $E_r$ only has $r$ dependence, we can factorise this out of the integral:
```{math}
E_r \iint  \,r^2 \,\sin \theta\, \mathrm{d} \theta \,\mathrm{d} \phi = E_r(4 \pi\,r^2) &=&\, kQ \\
\Rightarrow E_r &=&\, \frac{kQ}{4\pi\,r^2}
```
Finally we can write this in vector form:
```{math}
{\bf E} = \,E_r \,\hat{{\bf r}} = \frac{k Q}{4\pi\,r^2} \,\hat{{\bf r}}
```
Comparing this result with Coulomb's law in Equation {eq}`CoulombsLaw`, we find we can fix $k = 1/\epsilon_0$ (which also has the required units, check 
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
One of the grand goals of physics is to understand nature through the same equations but on different scales - so called <b>universality</b>.  We
find that the equations in electrostatics can be used to discuss Newton's law of gravitation.  We notice that the equations are essentially just a 
redefinition of fields and constants:
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
