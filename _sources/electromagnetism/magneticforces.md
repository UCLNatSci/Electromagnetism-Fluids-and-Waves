# Magnetic Forces

## Lorentz Force
Given current carrying wires can produce magnetic fields, neighbouring current carrying wires can therefore feel mutual magnetic fields.  We find that this 
combination of currents and fields causes a force, as depicted in {numref}`AmpereForceLaw`.  
```{figure} ../figures/AmpereForceLaw.png
---
name: AmpereForceLaw
---
Depiction of magnetic forces, 
<b> Left Pane </b> - parallel wires magnetic fields and force $F_{12}$ - there will also be an equal and opposite $F_{21}$ due to the field from $I_2$ 
that we have not depicted here.  
<b> Right Pane </b> - face on magnetic fields of each wire, showing opposing magnetic field directions and hence a mutual attractive force.
```

The neighbouring wires magnetic fields are in opposite directions and therefore the force is attractive.  We can motivate the form of the force on wire 2 $F_{12}$, 
due to wire 1's current $I_1$ by thinking about the effect of currents and magnetic fields:

```{math}
\begin{matrix}
\textrm{Current} & \rightarrow & \textrm{Charge velocity} & \rightarrow & \textrm{Magnetic field at radial distance} & \rightarrow &{\bf B} \propto {\bf v} \times {\bf r}\\
I &  & {\bf v} = v\,\hat{\bf z} & & {\bf r} = r\,\hat{{\bf r}}& & {\bf B} = B_\theta\,\hat{{\bf \theta}}
\end{matrix}
```

Therefore it should not come as a great surprise that the effect on a charge $Q$ moving with velocity ${\bf v}$ in a magnetic field ${\bf B}$ is a force 
that also acts in a perpendicular direction to both the field and the velocity $F \propto {\bf v} \times {\bf B}$, thus the magnetic force follows:
```{math}
{\bf F}_B = Q\,\left({\bf v}\times {\bf B} \right)
```
We can write the total force acting on a charge $Q$ moving with a velocity ${\bf v}$ in an electric field ${\bf E}$ and a magnetic field ${\bf B}$ 
```{math}
:label: LorentzForce
{\bf F} = {\bf F}_E + {\bf F}_B = Q\left({\bf E} + {\bf v} \times {\bf B} \right)
```
This is know as the <b>Lorentz</b> force and shows a few differences between the electric ${\bf E}$ and magnetic ${\bf B}$ fields acting on charges $Q$:
- The force ${\bf F}_E$ due to the electric field acting on a charge $Q$ is simply proportional and in the same direction of the the field ${\bf E}$.

- The force ${\bf F}_B$ due to the magnetic field acting on a charge $Q$ is proportional to the magnitude of the magnetic field and charge velocity, 
but moves in a perpendicular direction to both, due to the cross product ${\bf v}\times{\bf B}$.

- The magnetic force $|{\bf F}_B| = Q|{\bf v}||{\bf B}|\sin(\theta)$, which means that if $|{\bf v}| = 0$, there is no charge due to the magnetic field.  Therefore 
we see that if there is no charge velocity, the magnetic field has no effect on charges, it is only because moving charges produce a magnetic field that an external 
field may then interact with it.  Additionally this means if the magnetic field ${\bf B}$ is directed parallel to the charge velocity ${\bf v}$ i.e. $\theta = 0$, 
then the magnetic field has no effect on charges.  Likewise we see a maximum force felt with $\theta = \frac{\pi}{2}$, i.e. perpendicular charge velocity to magnetic field.



## Ampère's Force Law*
Using this expression for the forces on charges, we find that a current element in wire 2, $I_2\,\mathrm{d} {\bf \ell}_2 = \mathrm{d} Q_1 \,{\bf v}_1$ 
would feel a force due to a moving charge element in wire 1, $I_1\,\mathrm{d} {\bf \ell}_1$ producing a magnetic field, according to:
```{math}
:label: AmpereForceLaw
{\bf F}_{12} = \frac{\mu_0\,I_1\,I_2}{4\pi}\int_{\ell_1}\int_{\ell_2}\frac{\mathrm{d} {\bf \ell}_1\times \mathrm{d} {\bf \ell}_2\times \hat{{\bf r}}}{|{\bf r}|^2} 
```
For the case of an infinite parallel current carrying wires, separated by a distance $d$, the force on wire 2 due to current in wire 1 is given by:
```{math}
{\bf B}_1 = \frac{\mu_0\,I_1}{2\pi\,d}\,\hat{{\bf \theta}} \Longrightarrow 
{\bf F}_{12} = Q_2\,{\bf v}_2\times {\bf B}_1 = \frac{\mu_0\,I_1}{2\pi\,d}\,I_2\,\hat{{\bf z}}\times \hat{{\bf \theta}} = -\frac{\mu_0\,I_1\,I_2}{2\pi\,d}\,\hat{{\bf r}}
```
where as we see the force is attractive between the two wires carrying currents in the same direction.  Obviously is the currents are reversed then a 
repulsive force would be detected between the wires.  If the wires are not parallel, then the cross products in Equation {eq}`AmpereForceLaw` 
would take care of the necessary resolving of components.

