# Energy in an Electric Field
We can see that if we have charges that are free to move in space and some are at rest, the presence of a moving 
charge or uniform electric field will cause a force to act on these free charges to move, pick up kinetic energy 
and have non-zero momentum.  Therefore an electric field carries <b> Electric Potential Energy</b>.  The work done 
$\mathrm{d} W$ on a charge $Q$ in the presence of an electric field ${\bf E}$ moving a distance $\mathrm{d} {\bf r}$ 
in the field would be given by:
```{math}
\mathrm{d} W = Q\,{\bf E}\,\cdot \mathrm{d} {\bf r}
```
and therefore the change in electric potential energy $\mathrm{d} U_E$ is found to be:
```{math}
:label: elecpotenergy
\mathrm{d} U_E = - Q\,{\bf E}\,\cdot \mathrm{d} {\bf r} \Rightarrow U_E = -\int_{\mathcal{C}} Q\,{\bf E}\,\cdot \mathrm{d} {\bf r} 
```
For a point charge $Q_s$ producing the electric field, then for a charge moving in from $r \rightarrow \infty$ 
up to a distance $r$, the potential energy required is:
```{math}
U_E = -\,\frac{Q\,Q_s}{4\pi\,\epsilon_0}\int_{\infty}^r \frac{\hat{{\bf r}}'}{(r')^2}\,\cdot \mathrm{d} {\bf r}' = 
\frac{Q\,Q_s}{4\pi\,\epsilon_0}\frac{1}{r}
```
This gives rise to the idea of <b> Electric Potential </b> $V_E$,
```{math}
:label: EFieldpotential
V_E({\bf r}) = -\int_c {\bf E} \cdot \mathrm{d}{\bf \ell}
```
Here $V_E$ is amount of energy per unit charge given to $Q$ when moving on some path $C$ through an electric field from a 
point with zero potential to position ${\bf r}$.  By the Helmholtz decomposition theorem, the field ${\bf E}$ will (in general) 
have divergence and curl components, however if ${\bf E}$ is curl free, then we can write:
```{math}
:label: Efieldgradpotential
{\bf E} = -\nabla V_E 
```
We can also see that $V_E$ is related to the potential energy $U_E$, 
```{math}
U_E = Q\,V_E
``` 
For a point charge $Q_S$ producing an electric field, the electrical potential is given by:
```{math}
V_E = -\frac{Q_S}{4\pi\,\epsilon_0}\int_{\infty}^{r}\frac{\hat{\bf r}'}{(r')^2}\cdot\mathrm{d}{\bf r}' 
= -\frac{Q_S}{4\pi\,\epsilon_0}\int_{\infty}^{r}\frac{\mathrm{d} r'}{(r')^2} = \frac{Q_S}{4\pi\,\epsilon_0}\frac{1}{r}
```
The term <b> Potential Difference </b> is given to the difference between the electric potentials $\Delta V_E$ between 
two points $({\bf r}_1,\,{\bf r}_2)$ in an electrostatic system:
```{math}
\Delta V_E = {V_E}_2 - {V_E}_1 &=&\, -\int_{{\bf r}_0}^{{\bf r}_2} {\bf E} \cdot \mathrm{d}{\bf \ell} - 
\left (- \int_{{\bf r}_0}^{{\bf r}_1} {\bf E} \cdot \mathrm{d}{\bf \ell}\right) 
= \int_{{\bf r}_2}^{{\bf r}_0} {\bf E} \cdot \mathrm{d}{\bf \ell} + \int_{{\bf r}_0}^{{\bf r}_1} {\bf E} \cdot \mathrm{d}{\bf \ell} \\ 
&=&\,  \int_{{\bf r}_2}^{{\bf r}_1} {\bf E} \cdot \mathrm{d}{\bf \ell} = -\int_{{\bf r}_1}^{{\bf r}_2} {\bf E} \cdot \mathrm{d}{\bf \ell}
```
Suppose we have a system of two charges, how does $U_E$ change?  $Q_1({\bf r}_1)$ and $Q_2({\bf r}_1)$ will each produce an 
electrostatic field which a test charge $Q$ coming in from $r \rightarrow \infty$ will feel and therefore $U_E$ has the form:
```{math}
U_E = \frac{Q}{4 \pi\,\epsilon_0}\left(\frac{Q_1}{r_1} + \frac{Q_2}{r_2}\right)
```
which we can generalise for $N$ point charges $Q_1({\bf r}_1), \,Q_2({\bf r}_2), \,\dots,\, Q_N({\bf r}_N)$:
```{math}
U_E = \frac{Q}{4 \pi\,\epsilon_0}\left(\frac{Q_1}{r_1} + \frac{Q_2}{r_2} + \dots + \frac{Q_N}{r_N}\right) = 
\frac{Q}{4 \pi\,\epsilon_0}\,\sum_{i=1}^N \frac{Q_i}{r_i}
```
We should notice however that this is the potential energy that is a result of a charge $Q$ being introduced into the system, 
but clearly if there two or more charges already in the system, they too possess electric potential energies because there are 
also pairs of charges mutually interacting:
```{math}
U_E = \frac{1}{4\pi\,\epsilon_0}\frac{Q_1\,Q_2}{|r_1-r_2|}
```
We can also think about this in terms of potentials, e.g. $V_E({\bf r}_1)$ is as a result of charge $Q_1({\bf r}_1)$, therefore here:
```{math} 
U_E = \frac{1}{2}\bigg[Q_2\,{V_E}_1({\bf r}_2) + Q_1\,{V_E}_2({\bf r}_1)\bigg] 
```
where the $1/2$ factor is to avoid the over counting of the interaction field $Q_1 \rightarrow Q_2$ and $Q_2 \rightarrow Q_1$.  These 
expressions can be generalised for $N$ point charges:
```{math}
:label: intrinsicelecpotenergy
U_E &=& \,\frac{1}{2}\sum_{i=1}^N Q_i\,{V_E}({\bf r}_i)  \\ 
&=&  \,\frac{1}{2}\left(\frac{1}{4\pi\,\epsilon_0}\right)\sum_{i=1}^N Q_i\, \sum_{j=1}^{N(j \neq i)} \frac{Q_j}{|r_i-r_j|}
```
