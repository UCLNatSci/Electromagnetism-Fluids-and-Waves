(ch_conservation)=
# Conservation law derivations

**In this section:**
* What is measured by the material derivative?
* What do the terms in the mass and momentum conservation equations mean?

## The material derivative

In {numref}`dir-deriv` ({ref}`dir-deriv`) we found that the rate of change of a steady (time-independent) field $\phi(x,y,z)$ in a given direction $\underline{u}$ can be found by a scalar projection:

```{math}
D_{\underline{u}}\phi(\underline{x})=\underline{u}.\nabla\phi.
```
Now, suppose that the background field is non-steady, so that $\phi=\phi(\underline{x},t)$. Proceeding as before by using the multi-variate chain rule, we immediately obtain

```{math}
:label: materialderivative
\frac{\mathrm{D}\phi}{\mathrm{D}t}=\frac{\partial \phi}{\partial t}+\underline{u}.\nabla\phi.
```
This result is called the "material derivative" or "convective derivative", and the notation $\mathrm{D}/\mathrm{D}t$ is used in place of the ordinary derivative to signify its special significance. The first term accounts for the temporal evolution of the background field, and the second term (convection term) accounts for changes as a consequence of moving through the field with velocity $\underline{u}.$

The material derivative can also be applied to each element of a vector field $\underline{\phi}$, to give the change in $\underline{\phi}$ following the motion of a fluid particle. For example $\frac{\mathrm{D}\underline{u}}{\mathrm{D}t}$ gives the *convective acceleration*.

```{exercise}
:label: ex-materialderivative
Write out the convective acceleration $\frac{\mathrm{D}\underline{u}}{\mathrm{D}t}$ in component form, taking $\underline{x}=(x,y,z)$ and $\underline{u}(t,\underline{x})=(u,v,w)$.
```

```{toggle}
We have $\underline{u}.\nabla = u\frac{\partial}{\partial x}+v\frac{\partial}{\partial y}+w\frac{\partial}{\partial z}$

Hence, $\frac{D\underline{u}}{Dt}=\frac{\partial\underline{u}}{\partial t}+\underline{u}.\nabla\underline{u}=\begin{pmatrix}
\frac{\partial u }{\partial t}+u\frac{\partial u}{\partial x}+v\frac{\partial u}{\partial y}+w\frac{\partial u}{\partial z}\\
\frac{\partial v }{\partial t}+u\frac{\partial v}{\partial x}+v\frac{\partial v}{\partial y}+w\frac{\partial v}{\partial z}\\
\frac{\partial w }{\partial t}+u\frac{\partial w}{\partial x}+v\frac{\partial w}{\partial y}+w\frac{\partial w}{\partial z}
\end{pmatrix}$
```

## Mass transport (continuity)
Consider the mass flow through an arbitrary volume at a fixed location, like the "bag" shown in the image on the left. We assume matter is neither created or destroyed.

```{image} navstok_img/massflux.png
---
name: mass_flux
alt: illustration of fluid element
align: left
scale: 40%
---
```

The following statement says that the change in mass of the fluid parcel is equal to the net mass flow into the enclosing surface $\delta A$ per unit time.

$$
\frac{\mathrm{d}}{\mathrm{d}t}\iiint_{\delta V}\rho\mathrm{d}V=-\iint_\mathrm{\delta A}\rho \underline{u}.\mathrm{d}\underline{S}, \qquad \mathrm{d}\underline{S}=\hat{\underline{n}}\mathrm{d}S.
$$ (massflux1)

The negative sign appearing in the formula occurs because the normal direction is outward from the surface, as illustrated in the image.

The time derivative on the left hand side of equation {eq}`massflux1` can be brought inside the integral because for a fixed fluid volume the spatial and temporal variables are independent. On the right hand side the divergence theorem can be used to write the surface integral as a volume integral. Bringing all terms over to the left then gives

```{math}
:label: netmassflow2
\iiint_{\delta V}\biggr(\frac{\partial \rho}{\partial t}+\nabla.(\rho\underline{u})\biggr)\mathrm{d}V=0,
```

and since the volume $\delta V$ is arbitrary this requires that the integrand itself is zero. By using the product rule to expand the intergrand, we can finally obtain

```{math}
:label: netmassflow3
\frac{D\rho}{Dt}+\rho\nabla.\underline{u}=0.
```

```{admonition} Important case: Mass transport for incompressible flow
:class: important
If the density of each fluid particle does not change as it moves around, then the flow is said to be **incompressible**. In that case,  $\frac{D\rho}{D t}=0$, which leads to the following condition for incompressible flow :

\begin{equation*}
\nabla.\underline{u}=0
\end{equation*}
In practice, fluid phenomena that are well below the speed of sound can be treated as incompressible
```

## Cauchy stress theorem
"Stress" is a measure of the internal forces, such as pressure or friction acting between neighbouring fluid elements. We cannot discuss stress without first defining a particular surface that the stress acts on, since friction and pressure depend on the surface orientation.

However, the stress for a given surface can be expressed as a vector of components parallel to each coordinate direction, and according to Cauchy's stress theorem, the stress vector on any plane through a point can be found by knowing the stress vector on each of three mutually perpendicular planes. We will consider planes perpendicular to the coordinate axes.

The Cauchy stress tensor (deviatoric stress tensor)

```{math}
:label: deviatoricstress1
\underline{\sigma}=\left[\begin{array}{ccc}\sigma_{1,1}&\sigma_{1,2}&\sigma_{1,3}\\\sigma_{2,1}&\sigma_{2,2}&\sigma_{2,3}\\\sigma_{3,1}&\sigma_{3,2}&\sigma_{3,3}\end{array}\right]=\left[\begin{array}{ccc}\sigma_{xx} & \tau_{xy}& \tau_{xz}\\ \tau_{yx} & \sigma_{yy} & \tau_{yz}\\\tau_{zx} &\tau{zy} &\sigma_{zz}\end{array}\right]
```

defines the normal and shear stress components $\sigma_{i,j}$ acting on a plane perpendicular to each axis, as illustrated below:


<br>

```{image} navstok_img/stress_tensor.gif
---
name: stress_tensor
alt: stress tensor
align: center
scale: 80%
---
```
<br>


We now consider the stress vector $\underline{T}^{(\underline{n})}$ acting on an arbitrary surface $\delta{A}$ perpendicular to unit vector $\hat{\underline{n}}$ as illustrated in the figure below.


<br>

```{image} navstok_img/cauchy_tensor.gif
---
name: cauchy_tensor
alt: cauchy stress
align: center
scale: 80%
---
```
<br>


 We may apply Newton's second law to the tetrahedron shown, allowing the mass of the tetrahedron to approach zero (so that the sum of the forces also approaches zero):

```{math}
:label: deviatoricstress2
\underline{T}^{(n)}\delta A-\underline{T}^{(\underline{e}_1)}\delta A_1-\underline{T}^{(\underline{e}_2)}\delta A_2-\underline{T}^{(\underline{e}_3)}\delta A_3=0,
```

where $\delta A_j$ is the projection of $\delta A$ onto the illustrated face, given by $\delta A_j=\hat{\underline{n}}.\underline{e}_j\delta A=\hat{\underline{n}}_j\delta A.$

This gives

```{math}
:label: deviatoricstress3
\underline{T}^{(n)}=\underline{\sigma}.\hat{\underline{n}}.
```



## Conservation of momentum
By Newton's second law, the change in momentum is given by the sum of all forces acting on the volume:

```{math}
:label: consofmom1
\frac{\mathrm{d}}{\mathrm{d}t}\iiint_{\delta V}\rho\underline{u}\ \mathrm{d}V=\iiint_{\delta V}\rho\underline{F}\ \mathrm{d}V+\iint_{\delta S}\underline{\sigma}(t,\underline{x}).\hat{\underline{n}}\mathrm{d}S
```

in which

* $\rho\underline{F}$ is the "body force" per unit volume, such as gravitational, magnetic or [Coriolis*](https://www.britannica.com/science/Coriolis-force) forces
* $\underline{\sigma}(t,\underline{x}).\hat{\underline{n}}$ is the deviatoric stress tensor.

This time, we have to choose a "material volume", meaning one that moves with the fluid, so that we track the same particles. In that case $\rho\mathrm{d}V$ is constant so we may rewrite the left-hand side as

```{math}
:label: consofmom2
\frac{\mathrm{d}}{\mathrm{d}t}\iiint_{\delta V}\rho\underline{u}\mathrm{d}V=\iiint_{\delta V}\rho\frac{D\underline{u}}{D t}\mathrm{d}V
```

We use the divergence theorem again on the last term, and combine the three integrals for our arbitrary material volume $\delta V$ to obtain

```{math}
:label: consofmom3
\rho\frac{D\underline{u}}{D t}=\nabla.\underline{\sigma}+\rho\underline{F}
```

The Cauchy stress tensor $\underline{\sigma}$ can be split up to separate normal stress components (pressure) and shear stress components. This gives the result

```{math}
:label: consofmom4
\rho\frac{D\underline{u}}{D t}=-\nabla p+\nabla.\underline{\tau}+\rho\underline{F}
```

The negative sign is chosen due to the fact that the pressure acts inwards on a material volume.

*A physical derivation of the Coriolis force is outlined in the (optional) section of the notes on rotational reference frames.

## Chapter exercises

**Question 1**<br>

a). Write down the continuity equation for compressible flow in component form, taking $\underline{x}=(x,y,z)$, $p=p(t,\underline{x})$ and $\underline{u}(t,\underline{x})=(u,v,w)$.

b). What single equation can be used to model a flow that is both incompressible and irrotational?

c). Is incompressible flow the same as solenoidal flow?

**Question 2**<br>
If we assume that the shear stress component is zero so that $\underline{\tau}\equiv \underline{0}$ in equation {eq}`consofmom4`, then we obtain the Euler equation
\begin{equation*}
\frac{D\underline{u}}{D t}=-\frac{1}{\rho}\nabla p+\underline{F}
\end{equation*}

Write out this equation in component form for a Cartesian system under a body force $\underline{F}=(0,0,-g)$.

The implications of ignoring the shear stress components will be explored in later sections of these notes.