# Vortex transport

**In this section:**
* How is "vortex stretching" involved in tornado formation?
* The persistence of irrotational flow in an inviscid fluid
* Can we have lift without drag?

## The vorticity transport equation
Let us begin with the Navier-Stokes conservation of momentum equation for a conservative body force $\underline{F}=\nabla\phi$, and follow the same steps outlined in section {numref}`bernoulli-derivation` to obtain
\begin{equation}\frac{\partial \underline{u}}{\partial t}+\underline{\omega}\times\underline{u}=-\nabla H +\nu \nabla^2\underline{u}. \qquad H=\frac{p}{\rho}+\phi+\frac{1}{2}v^2,\end{equation}
Since "curlgrad"=0, we can eliminate the head by taking the curl:
\begin{equation}\frac{\partial \underline{\omega}}{\partial t}+\nabla\times(\underline{\omega}\times\underline{u})=\nu \nabla^2\underline{\omega}.\end{equation}
The second term can be expanded using vector identities to obtain the following equation for the material derivative of the vorticity:
\begin{equation}\frac{D\underline{\omega}}{D t}=(\underline{\omega}.\nabla)\underline{u}-\underline{\omega}(\nabla.\underline{u})+\nu \nabla^2\underline{\omega}.\end{equation}
In an incompressible flow there is no divergence of the velocity field and so we obtain the vorticity transport equation
\begin{equation}\frac{D\underline{\omega}}{D t}=(\underline{\omega}.\nabla)\underline{u}+\nu \nabla^2\underline{\omega}.\end{equation}
The first term on the right is called the "vortex stretching" term. It gets its non-zero contribution from the component of the velocity gradient parallel to $\underline{\omega}$, in which case vortex lines are "stretched" by the velocity field, causing them to spin faster. This effect is involved in the formation of tornadoes.

For two-dimensional flows the vortex stretching term is zero:
\begin{equation}\underline{u}=(u(x,y),v(x,y)) \quad \Rightarrow \quad \underline{\omega}=(0,0,\omega), \quad \omega=\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y} \qquad \Rightarrow \quad (\underline{\omega}.\nabla)\underline{u}=\underline{0}\end{equation}


````{admonition} Tornado formation
:class: theorem
The presence of strong winds near to the ground creates a shear gradient, which can cause the formation of a vortex line as shown in the image below, which is taken from [a 1984 research paper](https://doi.org/10.1175/1520-0469(1984)041%3C2991:SVTOOU%3E2.0.CO;2). Thermal updrafts can then tilt the vortex tube upwards to form a vertical column of rotating air. The simultaneous stretching effect of the thermal updrafts can cause tornadoes to spin very fast.

```{image} navstok_img/tornado.png
---
name: tornado formation
alt: alternative text
align: center
scale: 60%
---
```
*Note: It should be recognised that the formation of a vortex line is a viscous phenomenon!*
````

## Vorticity transport in inviscid flows

If the fluid is inviscid then the vorticity transport equation reduces to:

\begin{equation}\frac{D\underline{\omega}}{D t}=(\underline{\omega}.\nabla)\underline{u}.\end{equation}

If the fluid is initially irrotational then the vorticity will be zero along all fluid paths. The Euler equation cannot produce vorticity - it can only maintain it!

For example, this is the case for flows that are started from rest. The implication is that irrotational flows are more common than you might expect. Recall, too that the combination of inviscid and irrotational flow satisfies Laplace's equation $\nabla^2\phi=0.$

However, the assumption of inviscid flow can lead to a paradox, as discussed below.

(dalembert-paradox)=
## An apparent paradox : flow past a cylinder

Here we will model flow past a cylinder as an inviscid, irrotational flow. By artificially introducing circulation, we will find that we can obtain a lift force without the presence of drag.

### Potential flow derivation
In accordance with the inviscid, irrotational assumptions, we begin with Laplace's equation $\nabla^2\phi=0.$ In cylindrical polars we obtain:

\begin{align}\frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial \phi}{\partial r}\right)+\frac{1}{r}\frac{\partial}{\partial\theta}\left(\frac{1}{r}\frac{\partial\phi}{\partial\theta}\right)&=0\\\Rightarrow \quad \frac{\partial^2\phi}{\partial r^2}+\frac{1}{r}\frac{\partial\phi}{\partial r}+\frac{1}{r^2}\frac{\partial^2\phi}{\partial\theta^2}&=0.\end{align}

You may verify that the following result satisfies this equation, where $\Gamma$ is an arbitrary constant representing the circulation, and $U$ is the free stream velocity:

\begin{equation}\phi=Ur\left(1+\frac{a^2}{r^2}\right)\cos(\theta)+\frac{\Gamma\theta}{2\pi},\end{equation}

The velocity components $\left(v_r,v_{\theta}\right)=\left(\frac{\partial\phi}{\partial r},\frac{1}{r}\frac{\partial\phi}{\partial\theta}\right)$ are

\begin{equation}v_r=U\left(1-\frac{a^2}{r^2}\right)\cos(\theta), \quad v_{\theta}=-U\left(1+\frac{a^2}{r^2}\right)\sin(\theta)+\frac{\Gamma}{2\pi r}.\end{equation}

```{warning}
Notice for this solution there is evidently **slip** on the surface of the cylinder, since
\begin{equation*}v_{\theta}(r=a)=-2U\sin(\theta)+\frac{\Gamma}{2\pi a}.\end{equation*}
```

The pattern of streamlines depends on the circulation. If $\Gamma=0$ then the flow is symmetric, as shown in the top-left figure below, with stagnation points at the fore and aft of the cylinder. As the circulation in the clockwise direction increases, the stagnation points move towards the underside of the cylinder. Eventually, as the circulation is increased still further, the stagnation points coalesce and then move off the surface of the cylinder. The location of the stagnation points can be calculated:

\begin{equation}v_{\theta}(r=a)=0 \quad \Rightarrow \sin(\theta)=-\frac{\Gamma}{4\pi U a}=-\frac{1}{2}B \quad \text{where }B=-\frac{\Gamma}{2\pi U a}\end{equation}

<br>

```{image} navstok_img/stagnation.png
:name: Stagnation point on cylinder
:alt: stagnation point on cylinder
:align: center
:scale: 100%
```
<br>

The cylinder can be mapped via a change of variables (called "conformal mapping") to derive results for a flat plate or a cambered airfoil. The streamline patterns look similar to what we see here.

### Bernoulli's theorem:

Since the cylinder is a streamline, and the motion is steady, $\frac{p}{\rho}+\frac{1}{2} v^2$ is constant on $r=a$. Therefore on the surface of the cylinder

\begin{align}\frac{p}{\rho}+\frac{1}{2}\left(-2U\sin(\theta)+\frac{\Gamma}{2\pi a}\right)^2=\mathrm{const}\\\Rightarrow\frac{p}{\rho}=\mathrm{const}-2U^2\sin^2(\theta)-\frac{U\Gamma\sin(\theta)}{\pi a}\end{align}

The pressure distribution is symmetric in the $y$-axis, so the net force must be perpendicular to the oncoming stream. The $y$-component of the force is $-p a\sin(\theta)\mathrm{d}\theta$, so the net force is:

\begin{equation}F=\rho\int_0^{2\pi}\left(2U^2\sin^2(\theta)-\frac{U\Gamma}{\pi a}\sin(\theta)\right)a\sin(\theta)\mathrm{d}\theta=-\rho U \Gamma\end{equation}

We therefore obtain a lift force if there is positive circulation. The fact that there is no net force in the downstream direction (no drag) is known as *D'Alembert's paradox*.


### Resolving the paradox

The circulation has been artificially introduced here. There is nothing in the physical setup of this problem that would explain where it comes from. In reality, circulation can arise for a cylinder that is rotating relative to the oncoming stream or for an airfoil with a sharp trailing edge that attacks the oncoming flow an angle. **Viscosity is essential**. In each case it is the separation of the viscous boundary layer that generates the circulation via vortex shedding.

In the case of a cambered airfoil we see a "starting vortex" created around the trailing edge, which eventually breaks away and sets up an opposing circulation around the airfoil, as shown below.

Comparison of the paradoxical and physical cases gives us insight to suggest that if an airfoil is very well designed to avoid dramatic boundary layer separation, then very low drag forces may indeed be obtained.

<br>

```{image} navstok_img/image085.jpg
:name: cambered airfoils
:alt: cambered airfoils
:align: center
:scale: 100%
```
<br>

In cases where the development of the starting vortex does not have a preferred direction, such as for a non-rotating cylinder placed in an oncoming stream, we may see a [Von Karman street](https://en.wikipedia.org/wiki/K%C3%A1rm%C3%A1n_vortex_street) of alternating vortices being shed from the cylinder.



```{exercise}
Look up the meaning of the term "stall" in the context of fluid dynamics, and provide a description of this term in your own words. Draw pictures to illustrate.
```

```{toggle}

When an airfoil attacks an oncoming fluid stream, the deflection of the air below and above the wing causes a pressure gradient perpendicular to the direction of curvature, which generates lift. The sharp trailing edge is important. If the trailing edge is blunt then the air flows back around the edge, which reduces lift.

Increasing the attack angle between the airfoil and the oncoming stream increases lift, but if the angle is increased too far then the fluid breaks away from the boundary and begins to recirculate, leading leads to a sudden loss of lift called stall.

The geometry of the wing also affects how much lift it can generate, with long slender wings able to generate more lift.

**Bonus: How bumblebees fly**

A bumblebee, with its short, stubby wings, would not be expected to produce a vast amount of lift, even at angles near to the critical angle for a steady stall. Having cambered wings, and flapping really fast helps!

But bumblebees have 2 more tricks:

Firstly, they are able to invert their wings, so that they produce nearly as much lift on the upstroke as the downstroke, whilst birds (for example) do not have this ability.

Secondly, the bee is able to increase the attack angle beyond the critical angle for a steady stall by rotating its wing so that the flow stays adhered. This is known as a dynamic stall. Because the bumblebee operates in a regime of dynamic stall, its flight path is unstable: small deviations in flow pattern can lead to dramatic changes in direction. Dealing with this requires the bee to make rapid adjustments. It does, however, have the added benefit of an ability to manoeuvre very quickly. Fighter jets also operate in an unsteady flow regime.

```
