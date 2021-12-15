# Solving Electrostatic Systems

## Spherical Geometries

Lets consider the case of a spherical insulator (the key idea here being the charges are fixed), which carries a net charge of $+Q$.  
In the first instance we consider that the charge is uniformly distributed throughout the sphere, which has some radius $a$, as can 
be seen in Figure #. 
\begin{figure}[h!]
    \centering
    \includegraphics[scale = 0.5]{figures/sphericalinsulator.png}
    \caption{Left: Charged spherical insulator of radius $a$.  Middle: Cross section considering spheres $r \leq a$.  Right: Cross section considering spheres size $r \geq a$ }
    \label{fig:sphericalinsulator}
\end{figure}

Recall from our discussion of spherical geometries $(r,\,\theta,\, \phi)$, the area normal $\hat{{\bf n}}$ vector for this 
<b> Gaussian Sphere </b> will point in the $\hat{{\bf r}}$ direction, radially outwards, as shown in {numref}`sphereareanormal`.
```{figure} ../figures/sphereareanormal.png
---
name: sphereareanormal
---
Area normal vector $\hat{{\bf n}} = \hat{{\bf r}}$ for a sphere.
```

To find the electric field distribution using Gauss's law, lets break up the space into three different regimes of interest:
 
- <b> REGION I: $r > a$ </b>

First here the charge enclosed by the radius $r>a$ is the entire charge $+Q$ carried by the sphere, thus $Q_{enclosed} = Q$.  
```{math}
E_r\,(4 \pi r^2) = \frac{Q}{\epsilon_0} \Rightarrow E_r = \frac{Q}{4 \pi \epsilon_0 r^2} 
``` 
The electric field ${\bf E}$ only has a radial term and no angular dependence, therefore the full vector expression is:
```{math}
{\bf E} = \frac{Q}{4 \pi \epsilon_0 r^2}\hat{{\bf r} }
```
We notice that this result looks like that of a point charge $Q$, which for $r > a$ means we could consider the 
<em> centre of charge </em> as a point at the centre of the sphere, akin to <em> centre of mass </em> for a large rigid object.

- <b> REGION II: $r = a$ </b>

Since at $r=a$ the whole charge is (just) entirely contained, this result matches the condition at $r > a$, but evaluated at $r = a$
```{math}
{\bf E} = \frac{Q}{4 \pi \epsilon_0 a^2}\hat{{\bf r}}
```
This result should match that of the inner and outer electric field - continuity of the field is important so 
that we are not creating or destroying potential energy.
    
-  <b> REGION III: $r < a$ </b>

Here we need to find the $Q_{enclosed}$ at the radius $r$, this can be found by first finding the uniform charge 
density within the sphere:
```{math}
\rho = \frac{Q}{\frac{4}{3}\,\pi\, a^3} = \frac{3 Q}{4\,\pi\, a^3} 
```
and then multiplying this by the smaller volume of sphere up to radius $r$:
```{math}
Q_{enclosed} &=&\, \frac{3Q}{4\,\pi\, a^3}\left(\frac{4}{3}\,\pi \,r^3\right) = Q \,\left(\frac{r}{a}\right)^3 \\ 
\iint {\bf E} \cdot \mathrm{d} {\bf A}  &=&\, E_r\,(4 \pi r^2) = \frac{Q}{\epsilon_0} \,\left(\frac{r}{a}\right)^3  \\ 
{\bf E} &=&\, \frac{Q}{4 \pi \epsilon_0}\frac{r}{a^3}\hat{{\bf r}}
```
	
We plot the interior and exterior electric fields for the uniform charge insulating sphere in {numref}`electricfieldsphere`.  
We see that continuity of field is present at the boundary, although very different radial dependencies $E(r)$ are present 
inside and outside of the sphere.
```{figure} ../figures/electricfieldsphere1.png
---
name: electricfieldsphere
---
Graph of electric field for uniform insulating sphere interior and exterior.
```
	
We can also calculate the total electrostatic energy of this charged sphere, $U_E(r)$ on a charge $Q_S(r)$ exterior 
to the sphere, which itself carries a charge $Q$:
```{math}
U_E(r) = -\frac{Q_S}{4\pi\,\epsilon_0} \int_{\infty}^{r}\frac{Q}{(r')^2}\,\mathrm{d} r' =  \frac{1}{4\pi\,\epsilon_0}\frac{Q_s\,Q}{r}
```

## Cylindrical Geometries

### Sheets of Charge
We can consider a uniform infinite sheet of charge, carrying a total charge $Q$ over an area $A_{tot}$, with a uniform 
charge for unit area $\sigma = \frac{Q}{A_{tot}}$.  Here we want to find a Gauss's law surface to find the flux crossing, 
for a sheet like this we can pick a cylinder, as we see in Figure {eq}`sheetofcharge`.  
```{figure} ../figures/sheetofcharge.png
---
name: sheetofcharge
---
Sheet of charge using a cylinder as our Gaussian surface.
```

The cylinder has three areas here, a cross sectional area $A$ on each each and a long surface cylinder of side 
$L$, $2 \pi r L$.  For the normal to the surface pointing upwards on the top of the sheet (and downwards below the sheet), 
these point in the $\text{sign}(z)\hat{{\bf z}}$ direction, depending on which side we are on, so here our Gauss's law dot 
product looks like
```{math}
\iint{\bf E} \cdot \mathrm{d} {\bf A} = \iint E_z \,\mathrm{d} A_z = E_z \,A + (-E_z)(-A) = 2 E_z \,A
```
The $Q_{enclosed}$ here would just be the charge density times the cross section area of the Gaussian cylinder, 
$Q_{enclosed} = \sigma \,A$ and therefore:
```{math}
2 E_z \,A = \frac{\sigma\, A}{\epsilon_0} 
```
which means we can write a simplified expression here, for $z > 0 $
```{math}
 E_z = \frac{\sigma}{2 \epsilon_0} \longrightarrow {\bf E}= \frac{\sigma}{2 \epsilon_0} \hat{{\bf z}}
```
and equally for $z < 0$
```{math}
E_z = \frac{\sigma}{2 \epsilon_0} \longrightarrow {\bf E}= -\frac{\sigma}{2 \epsilon_0} \hat{{\bf z}}
```
For an example of a sheet of charge system, consider a capacitor, here we can think of this system as two 
sheets of charge, one carrying a charge $+Q$ and the other with a charge $-Q$, as depicted in {numref}`capacitorelectricfield`.  
Obviously this system is idealised, because these sheets of charge are <em> finite</em>.  However if we ignore edge 
effects, the use of our expressions work fairly well!

```{figure} .../figures/capacitorelectricfield1.png
---
name: capacitorelectricfield
---
Electric field $E$ within a capacitor, two plates of area $A$, top plate at $z = d$, bottom plate at $z = 0$, carrying a charge $\pm Q$.
```

For two identical plates, each carrying the same magnitude of charge (but opposite signs), 
there will be a uniform electric field between the plates:
```{math}
{\bf E} &=&\, {\bf E}_{Q+} + {\bf E}_{Q-} \\ 
{\bf E} &=& \, -\frac{\sigma}{2\epsilon_0}\hat{{\bf z}}  + \frac{(-\sigma)}{2\epsilon_0}\hat{{\bf z}} = -\frac{\sigma}{\epsilon_0}\hat{{\bf z}}
```
The electric field outside of the plates is zero, since net charge enclosed will be $- Q + Q = 0$.  
We can also calculate the potential difference $V$ between the plates:
```{math}
V_E = -\left(\int_{r_0}^{d}{\bf E} \cdot \mathrm{d} {\bf \ell} -\int_{r_0}^{0}{\bf E} \cdot \mathrm{d} {\bf \ell} \right) = 
\frac{\sigma\,d}{\epsilon_0} 
```
which can be used to find an expression for the capacitance:
```{math}
C = \frac{Q}{V_E} = \frac{\sigma \,A\,\epsilon_0}{\sigma\,d} = \frac{A}{d}\,\epsilon_0
```
Clearly therefore the capacitance can be increased with a larger plates area $A$ and/or smaller plate separation $d$.  
In each case the plates can therefore carry a bigger charge and therefore will result in a larger capacitance $C$.

### Infinite Lines of Charge
We can consider a uniform infinite line of charges, with charge per unit length $\lambda$.  
Here we can again consider a cylinder as our Gauss's law surface area for flux to cross, but the normal vector now 
is directed in the radial direction away from the charges and its the long side area that we are concerned with, as 
depicted in {numref}`:lineofcharge`.   
```{figure} ../figures/InfiniteLineOfCharges.png
---
name: lineofcharge
---
An infinite line of charges with a cylinder as our Gaussian surface.
```
   
For a cylinder of length $L$, the area of the long side of the cylinder is $2 \pi r L$ and the charge enclosed in this 
area is given by $\lambda L$, so putting these facts together: 
```{math}
:label: InfiniteChargeLineEField
\iint {\bf E} \cdot \mathrm{d} {\bf A} &=&\, \iint E_r \,\mathrm{d} A_r = E_r \,(2\pi\, r\, L) = \frac{\lambda L}{\epsilon_0} \\
&=&\, \frac{\lambda}{2\pi\, \epsilon_0 \,r} \Longrightarrow {\bf E} = \frac{\lambda}{2\pi\, \epsilon_0 \,r} \hat{{\bf r}}
```

## Superposition of Charge
Solving systems with Gauss's law with pen and paper methods usually requires some degree of symmetry, 

### Finite Lines of Charge*
Equation {numref}`FiniteChargeLineEField` is only true for an infinite line of charge, if we have a finite collection of charges, 
as depicted in {numref}`Finitelineofcharge`, then we loose the symmetries of the system that we needed to simplify the Gauss's 
law expression - making it harder to solve this system using Gauss's law, but we can consider iot from a superposition of point charges perspective.  

```{figure} ../figures/FiniteLineOfCharges1.png
---
name: Finitelineofcharge
---
An finite line of charges with length $a + b$ aligned over the $x$ axis and an element of charge $\mathrm{d} Q = \lambda \,\mathrm{d} x$ indicated in red.
```
With a line of large, of length $a + b$, aligned along the $x$ axis and considering a radial distance $r$ away.  The radial 
component of the electric field can be found by breaking up the uniform line of charge into infinitesimal chunks, 
each by superposition contributing $\mathrm{d} Q$ charge, which we can then integrate over to find the total field:
```{math}
:label: EFieldWire
    \mathrm{d} E_r = \frac{\mathrm{d} Q}{4\pi\,\epsilon_0\,R^2}\frac{r}{R} 
```
where the $r/R$ term is from resolving in the $E_r$ direction.  Since $\mathrm{d} Q = \lambda\,\mathrm{d} x$ and we can convert 
$R = \sqrt{x^2 + r^2}$,  our final result has the form:
```{math}
    E_r = \frac{\lambda\,r}{4\pi\,\epsilon_0}\int_{-a}^{b} \frac{\mathrm{d} x}{(x^2 + r^2)^{3/2}}
```
Using a trigonometric substitution, $x = r \tan (\theta)$, we find:
```{math}
    E_r &=&\, \frac{\lambda}{4\pi\,\epsilon_0\,r}\int_{x=-a}^{x=b} \cos(\theta)\,\mathrm{d} \theta = 
	\frac{\lambda}{4\pi\,\epsilon_0\,r} \Bigg[\sin(\theta)\Bigg]_{x=-a}^{x=b} \\
    &=&\, \frac{\lambda}{4\pi\,\epsilon_0\,r} \left[\frac{x}{\sqrt{x^2+r^2}}\right]_{-a}^{b} = 
	\frac{\lambda}{4\pi\,\epsilon_0\,r}\left( \frac{b}{\sqrt{b^2+r^2}} + \frac{a}{\sqrt{a^2+r^2}}\right)\\ 
	{\bf E} &=&\, \frac{\lambda}{4\pi\,\epsilon_0\,r}\left( \frac{b}{\sqrt{b^2+r^2}} + \frac{a}{\sqrt{a^2+r^2}}\right)\hat{{\bf r}}
```
A somewhat messy result, but consider the large $a,\,b$ limit:
```{math}
    \lim_{a,\,b\rightarrow \infty}\left[\left(1+\frac{r^2}{b^2}\right)^{-1/2} + \left(1+\frac{r^2}{a^2}\right)^{-1/2}\right] = 2 
	\Rightarrow {\bf E} = \frac{\lambda}{2\pi\,\epsilon_0\,r}\hat{{\bf r}}
```
which is exactly the uniform infinite line of charge result!
