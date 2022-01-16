# Solving Gauss's Law 

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

Recall from our discussion of spherical geometries $(r,\,\theta,\, \phi)$, the area normal $\vn$ vector for this 
{\bf Gaussian Sphere} will point in the $\hat{\vr}$ direction, radially outwards, as shown in Figure #.
    \begin{figure}[h!]
        \centering
        \includegraphics[scale=0.5]{figures/sphereareanormal.png}
        \caption{Area normal vector $\vn = \hat{\vr}$ for a sphere.}
        \label{fig:sphereareanormal}
    \end{figure}

To find the electric field distribution using Gauss's law, lets break up the space into three different regimes of interest:

```{math} 
r > a,\,\, &\,\, r = a,\,\, &\,\, r < a 
``` 
 
1. $r > a$
First here the charge enclosed by the radius $r>a$ is the entire charge $+Q$ carried by the sphere, thus $Q_{enclosed} = Q$.  
```{math}
E_r\,(4 \pi r^2) = \frac{Q}{\epsilon_0} \Rightarrow E_r &=& \frac{Q}{4 \pi \epsilon_0 r^2} 
``` 
The electric field $\vE$ only has a radial term and no angular dependence, therefore the full vector expression is:
```{math}
\vE &=& \frac{Q}{4 \pi \epsilon_0 r^2}\hat{\vr}
```
We notice that this result looks like that of a point charge $Q$, which for $r > a$ means we could consider the 
<em> centre of charge </em> as a point at the centre of the sphere, akin to <em> centre of mass </em> for a large rigid object.
    

2. $r = a$ 

Since at $r=a$ the whole charge is (just) entirely contained, this result matches the condition at $r > a$, but evaluated at $r = a$
```{math}
{\bf E} &=& \frac{Q}{4 \pi \epsilon_0 a^2}\hat{{\bf r}}
```
This result should match that of the inner and outer electric field - continuity of the field is important so 
that we are not creating or destroying potential energy.
    
3.  $r < a$

Here we need to find the $Q_{enclosed}$ at the radius $r$, this can be found by first finding the uniform charge 
density within the sphere:
```{math}
\rho = \frac{Q}{\frac{4}{3}\,\pi\, a^3} = \frac{3 Q}{4\,\pi\, a^3} 
```
and then multiplying this by the smaller volume of sphere up to radius $r$:
```{math}
Q_{enclosed} &=&\, \frac{3Q}{4\,\pi\, a^3}\left(\frac{4}{3}\,\pi \,r^3\right) = Q \,\left(\frac{r}{a}\right)^3 \\ 
\iint \vE \cdot \cald \vA &=&\, E_r\,(4 \pi r^2) = \frac{Q}{\epsilon_0} \,\left(\frac{r}{a}\right)^3  \\ 
\vE &=&\, \frac{Q}{4 \pi \epsilon_0}\frac{r}{a^3}\hat{{\bf r}}
```
	
We plot the interior and exterior electric fields for the uniform charge insulating sphere in Figure \ref{fig:electricfieldsphere}.  We see that continuity of field is present at the boundary, although very different radial dependencies $E(r)$ are present inside and outside of the sphere.
    \begin{figure}[h!]
        \centering
        \includegraphics[scale=0.8]{figures/electricfieldsphere1.png}
        \caption{Graph of electric field for uniform insulating sphere interior and exterior.}
        \label{fig:electricfieldsphere}
    \end{figure}
	
We can also calculate the total electrostatic energy of this charged sphere, $U_E(r)$ on a charge $Q_S(r)$ exterior 
to the sphere, which itself carries a charge $Q$:
```{math}
U_E(r) = -\frac{Q_S}{4\pi\,\epsilon_0} \int_{\infty}^{r}\frac{Q}{(r')^2}\,\cald r' =  \frac{1}{4\pi\,\epsilon_0}\frac{Q_s\,Q}{r}
```

## Cylindrical Geometries

### Sheets of Charge
We can consider a uniform infinite sheet of charge, carrying a total charge $Q$ over an area $A_{tot}$, with a uniform 
charge for unit area $\sigma = \frac{Q}{A_{tot}}$.  Here we want to find a Gauss's law surface to find the flux crossing, 
for a sheet like this we can pick a cylinder, as we see in Figure \ref{fig:sheetofcharge}.  
\begin{figure}[h!]
    \centering
\includegraphics[scale=0.5]{figures/sheetofcharge.png}
    \caption{Sheet of charge using a cylinder as our Gaussian surface.}
    \label{fig:sheetofcharge}
\end{figure}
The cylinder has three areas here, a cross sectional area $A$ on each each and a long surface cylinder of side 
$L$, $2 \pi r L$.  For the normal to the surface pointing upwards on the top of the sheet (and downwards below the sheet), 
these point in the $\text{sign}(z)\hat{{\bf z}}$ direction, depending on which side we are on, so here our Gauss's law dot product looks like
```{math}
\iint\vE \cdot \cald \vA = \oiint E_z \,\cald A_z = E_z \,A + (-E_z)(-A) = 2 E_z \,A
```
The $Q_{enclosed}$ here would just be the charge density times the cross section area of the Gaussian cylinder, 
$Q_{enclosed} = \sigma \,A$ and therefore:
```{math}
2 E_z \,A &=& \frac{\sigma\, A}{\epsilon_0} 
```
which means we can write a simplified expression here, for $z > 0 $
```{math}
 E_z = \frac{\sigma}{2 \epsilon_0} \longrightarrow \vE = \frac{\sigma}{2 \epsilon_0} \hat{{\bf z}}
```
and equally for $z < 0$
```{math}
E_z = \frac{\sigma}{2 \epsilon_0} \longrightarrow \vE = -\frac{\sigma}{2 \epsilon_0} \hat{\vz}
```
For an example of a sheet of charge system, consider a capacitor, here we can think of this system as two 
sheets of charge, one carrying a charge $+Q$ and the other with a charge $-Q$, as depicted in Figure \ref{fig:CapEfield}.  Obviously this system is idealised, because these sheets of charge are {\it finite}.  However if we ignore edge effects, the use of our expressions work fairly well!
\begin{figure}[h!]
    \centering
    \includegraphics[scale=0.75]{figures/capacitorelectricfield1.png}
    \caption{Electric field $E$ within a capacitor, two plates of area $A$, top plate at $z = d$, bottom plate at $z = 0$, carrying a charge $\pm Q$}
    \label{fig:CapEfield}
\end{figure}
For two identical plates, each carrying the same magnitude of charge (but opposite signs), 
there will be a uniform electric field between the plates:
```{math}
\vE &=& \vE_{Q+} + \vE_{Q-} \\ 
\vE &=&  -\frac{\sigma}{2\epsilon_0}\hat{{\bf z}}  + \frac{(-\sigma)}{2\epsilon_0}\hat{{\bf z}} = -\frac{\sigma}{\epsilon_0}\hat{{\bf z}}
```
The electric field outside of the plates is zero, since net charge enclosed will be $- Q + Q = 0$.  
We can also calculate the potential difference $V$ between the plates:
```{math}
V_E = -\left(\int_{r_0}^{d}\vE \cdot \cald \vell -\int_{r_0}^{0}\vE \cdot \cald \vell \right) = \frac{\sigma\,d}{\epsilon_0} 
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
depicted in Figure \ref{fig:lineofcharge}.   

\begin{figure}[h!]
    \centering
    \includegraphics[scale=0.75]{figures/InfiniteLineOfCharges.png}
    \caption{An infinite line of charges with cylinder as our Gaussian surface.}
    \label{fig:lineofcharge}
   \end{figure}
   
For a cylinder of length $L$, the area of the long side of the cylinder is $2 \pi r L$ and the charge enclosed in this area is given by $\lambda L$, so putting these facts together: 
```{math}
:label: InfiniteChargeLineEField
\iint \vE \cdot \cald \vA &=&\, \iint E_r \,\cald A_r = E_r \,(2\pi\, r\, L) = \frac{\lambda L}{\epsilon_0} \\
&=&\, \frac{\lambda}{2\pi\, \epsilon_0 \,r} \Longrightarrow \vE = \frac{\lambda}{2\pi\, \epsilon_0 \,r} \hat{{\bf r}}

    ```
### Finite Lines of Charge*}
Equation \ref{eqn:InfiniteChargeLineEField} is only true for an infinite line of charge, if we have a finite collection of charges, 
as depicted in Figure \ref{fig:finitelineofcharge}, then we loose the symmetries of the system that we needed to simplify the Gauss's 
law expression.  Now it is {\it much} harder to solve this system, but we can consider looking at it as superposition of point charges.  
\begin{figure}[h!]
    \centering
    \includegraphics[scale=0.9]{figures/FiniteLineOfCharges1.png}
    \caption{An finite line of charges with length $a + b$ aligned over the $x$ axis and an element of charge $\cald Q = \lambda \,\cald x$ indicated in red.}
    \label{fig:finitelineofcharge}
   \end{figure}
    With a line of large, of length $a + b$, aligned along the $x$ axis and considering a radial distance $r$ away.  
	The radial component of the electric field can be found by breaking up the uniform line of charge into infinitesimal chunks, 
	each by superposition contributing $\mathrm{d} Q$ charge, which we can then integrate over to find the total field:
```{math}
    \cald E_r = \frac{\cald Q}{4\pi\,\epsilon_0\,R^2}\frac{r}{R} \label{eqn:EFieldWire}
```
where the $r/R$ term is from resolving in the $E_r$ direction.  Since $\cald Q = \lambda\,\cald x$ and we can convert 
$R = \sqrt{x^2 + r^2}$,  our final result has the form:
```{math}
    E_r = \frac{\lambda\,r}{4\pi\,\epsilon_0}\int_{-a}^{b} \frac{\cald x}{(x^2 + r^2)^{3/2}}
```
Using a trigonometric substitution, $x = r \tan (\theta)$, we find:
```{math}
    E_r &=& \frac{\lambda}{4\pi\,\epsilon_0\,r}\int_{x=-a}^{x=b} \cos(\theta)\,\cald \theta = \frac{\lambda}{4\pi\,\epsilon_0\,r} \Bigg[\sin(\theta)\Bigg]_{x=-a}^{x=b} \\
    &=& \frac{\lambda}{4\pi\,\epsilon_0\,r} \left[\frac{x}{\sqrt{x^2+r^2}}\right]_{-a}^{b} = \frac{\lambda}{4\pi\,\epsilon_0\,r}\left( \frac{b}{\sqrt{b^2+r^2}} + \frac{a}{\sqrt{a^2+r^2}}\right)\\ \vE &=& \frac{\lambda}{4\pi\,\epsilon_0\,r}\left( \frac{b}{\sqrt{b^2+r^2}} + \frac{a}{\sqrt{a^2+r^2}}\right)\hat{\vr}
```
A somewhat messy result, but consider the large $a,\,b$ limit:
```{math}
    \lim_{a,\,b\rightarrow \infty}\left[\left(1+\frac{r^2}{b^2}\right)^{-1/2} + \left(1+\frac{r^2}{a^2}\right)^{-1/2}\right] = 2 
	\Rightarrow {\bf E} = \frac{\lambda}{2\pi\,\epsilon_0\,r}\hat{{\bf r}
```
which is exactly the uniform infinite line of charge result!
