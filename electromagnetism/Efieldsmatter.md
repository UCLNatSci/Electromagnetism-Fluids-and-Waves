# Electric Fields in Matter

## Conductors

If we have a conductor placed an electric field, the mobile charge carriers now have the possibility to move.  This system will then seek to reach an 
equilibrium and and we find that the lowest energy configuration is depicted in {numref}`conductorelectricfield`.  

```{figure} ../figures/conductorelectricfield.png
---
name: conductorelectricfield
---
The internal electric field of a conductor
```

The total electric field in the conductor interior is made up of
```{math} 
{\bf E}_{tot} = {\bf E}_{charges} + {\bf E}_{field}
``` 
Since the charges move until the system reaches a stable equilibrium, the result is 
```{math} 
{\bf E}_{interior} = - {\bf E}_{field} \quad \Rightarrow \quad {\bf E}_{tot} = (0,\,0,\,0)
``` 
meaning no more charges will move, which is a stable equilibrium.

We find it is possible to have conductors carry a net charge, say $+Q$, however electrostatic fields do not permeate far through a conductor, 
the charge is essentially carried at the surface.  If we have an oscillating electric field ${\bf E}(\omega)$, then the <b>Skin Effect</b> is observed in a 
conductor and there is a measurable <b>Skin Depth</b>, $\delta(\omega)$ of the field in the conductor.  

## ${\bf D}$ Field*
We won't spend a lot of time discussing electromagnetic fields within transmission media, however one way to investigate how electric fields 
propagate within a material that isn't an insulator (or vacuum), say a conductor (or semi-conductor), is to investigate the electric 
<b>Displacement Field</b> ${\bf D}$.   In doing so we must include the effects of frequency dependent  permittivity $\epsilon(\omega)$ in our equations, 
it is usually more useful to consider the so-called Displacement field ${\bf D}$:
```{math} 
{\bf D} = \epsilon(\omega)\,{\bf E} = \epsilon_0\, {\bf E} + {\bf P} = \epsilon_0\,\left(1 + \chi \right)\,{\bf E}
``` 
where ${\bf P}$ is the polarization density and $\chi$ is the electric susceptibility.  These expressions let us write Gauss's law as:
```{math}
\iint {\bf D}\cdot \mathrm{d} {\bf A} = Q_{free}
``` 
and also mean that the depending the nature of the material and fields in question, the relative permittivity $\epsilon_r (\omega)$ is related through: 
```{math} 
\epsilon(\omega) = \epsilon_0\,\epsilon_r(\omega)
``` 
$\epsilon(\omega)$ is responsible for effects such as refection and rainbows, producing energy dissipation effects, which we would see in the wave dispersion relation.


## Gravitational Analogue
One aspect of the equations of electrostatics to notice is that the original consideration of Coulomb's law could be extended over to discuss Newton's law of gravitation.  
We notice that the equations are essentially just a redefinition of fields and constants:
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
\iint {\bf g} \cdot \mathrm{d} {\bf A} = -4\pi\,G\,M_{enclosed}
```
Close to the Earth we know that ${\bf g} = -g \hat{{\bf x}}$ where $g = 9.81 \text{ms}^{-2}$ and so the gravitational potential energy is given by 
$U_G = -M\int_0^h (-g) \,\mathrm{d} x = mgh$.  

An application of this is understanding the interior gravitational field of a large uniform astrophysical 
body (e.g. the Earth) using the analogues of the results in {numref}`electricfieldsphere`.  

