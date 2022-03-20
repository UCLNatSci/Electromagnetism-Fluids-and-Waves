(steady-soln)=
# Steady solutions

**In this section:**
* We derive the steady flow profiles for some classic geometries


## General technique

The incompressibility condition is the simplest equation to work with, and for these simple geometries it often shows one of the flow components to be zero, so always look at the incompressibility condition first.

Then we write out the components in the conservation of momentum equations. The examples given here are all ones that can be solved by hand. Some other classic flow profiles that we do not study here can be found by series solution.

To find the particular solutions we must impose boundary conditions. The most important boundary condition to be aware of here is the **"no-slip"** condition, which means that at a solid boundary fluid particles have no velocity component parallel to the boundary. Literally they do not slip along the boundary. This condition is now known to be correct, but was historically contentious and will be discussed in more detail in a later section.

Other boundary conditions employed in this section include a condition that no fluid can flow through a solid boundary, and that at a free surface there is no shear stress.

## Couette flow (flow driven by a moving boundary)
In this example, we consider the motion of fluid between two horizontal planes. The lower plane is held at rest and the upper plan is moved at speed $U$ as shown. We will assume that there is no pressure gradient in the horizontal direction, so that the flow is entirely driven by viscosity. We will assume that the flow is independent of $x$ so that $\underline{u}=(u(y),v(y),0)$.

```{image} navstok_img/couette.png
:name: couette flow
:alt: Couette flow
:align: center
:scale: 100%
```

The equations of motion are:
\begin{equation}\nabla.\underline{u}=0, \quad \underline{u}.\nabla\underline{u}=-\frac{1}{\rho}\nabla p +\nu \nabla^2\underline{u}.\end{equation}
It follows from the incompressibility condition that $v$ is constant, and since $v(0)=0$ this component must be identically zero everywhere, so the conservation of momentum equations simplify to:
\begin{equation}\frac{\mathrm{d}^2 u}{\mathrm{d}y^2}=0, \quad \frac{\mathrm{d} p}{\mathrm{d} y}=0.\end{equation}
The velocity solution satisfying the no-slip condition $u(0)=0$ and $u(h)=U$ is the linear profile:
\begin{equation}\underline{u}=\left(\frac{U}{h}y,0,0\right).\end{equation}
The shear stress is constant throughout the fluid. In the downstream direction
\begin{equation}\mu\left(\frac{\partial u}{\partial y}+\frac{\partial v}{\partial x}\right)=\mu\frac{U}{h}.\end{equation}
It is also possible to solve the problem for an applied pressure gradient. For example if we take a constant pressure gradient $\frac{\partial p}{\partial x}=G$ then we obtain
\begin{equation}u=\frac{U}{h}y+\frac{G}{2\mu}y(h-y).\end{equation}

## Steady flow under gravity down an inclined plane
In this example, we will consider gravity driven flow down an inclined plane, with a free surface at $y=h$, as shown. We will assume that the flow is independent of $x$ so that $\underline{u}=(u(y),v(y),0)$.

```{image} navstok_img/inclined_plane.png
:name: inclined plane
:alt: flow down an inclined plane
:align: center
:scale: 80%
```


The equations of motion are:
\begin{equation}\nabla.\underline{u}=0, \quad \underline{u}.\nabla\underline{u}=-\frac{1}{\rho}\nabla p +\underline{F}+\nu \nabla^2\underline{u}.\end{equation}
It follows from the incompressibility condition that $v$ is constant, and since $v(0)=0$ this component must be identically zero everywhere. The conservation of momentum equations then simplify to:

```{math}
:label: steadygravy1
\begin{align}
0 &= -\frac{1}{\rho}\frac{\partial p}{\partial x}+ \nu \frac{\partial^2 u}{\partial y^2}+g\sin(\alpha)\\
0 &= \frac{1}{\rho}\frac{\partial p}{\partial y} - g\cos(\alpha)
\end{align}
```

By integrating the latter of these two equations we obtain $p=-\rho g y \cos(\alpha)+f(x)$ and we can find $f(x)$ by applying an atmospheric pressure condition on the free surface:
\begin{equation}p(h)=p_0, \ \forall x \qquad \Rightarrow f(x)=p_0-\rho g h\cos(\alpha).\end{equation}

Therefore the pressure is independent of $x$ and the first equation in {eq}`steadygravy1` reduces to
\begin{equation}\nu \frac{\mathrm{d}^2 u}{\mathrm{d}y^2}=-g\sin(\alpha).\end{equation}
The solution satisfying the no-slip condition $u(0)=0$ and free surface stress shear "no stress" condition $u'(h)=0$ is the parabolic profile:
\begin{equation}u=\frac{g}{2\nu}y(2h-y)\sin(\alpha).\end{equation}
The velocity flux is therefore
\begin{equation}Q=\int_0^h u\mathrm{d}y=\frac{gh^3}{3\nu}\sin(\alpha).\end{equation}

```{exercise}
Incompressible fluid of uniform density $\rho$ and viscosity $\nu$ flows steadily under
gravity $g$ between two vertical planes at $x = 0$ and $x = a$. The plane at $x = 0$
is at rest, but the plane at $x = a$ is moving vertically upwards at speed $V$. By
assuming that the pressure is constant throughout the fluid and that the velocity
field does not depend on the vertical coordinate, solve the equations of motion
to find the velocity field.
```

`````{toggle}

````{panels}
:card: border-0
**Euler:**

$\underline{u}.\nabla\underline{u}=-\frac{1}{\rho}\nabla p +\nu\nabla^2\underline{u}$

$\nabla.\underline{u} =0$

Take $p=\mathrm{constant}$, $\underline{u}=(u(x),v(x),0)$
---
```{image} navstok_img/walls.png
:align: center
:scale: 60%
```
````

From the incompressibility condition, $\displaystyle \frac{\partial u}{\partial x}=0$, so $u$ is independent of $x$.
Since we already assumed that $u$ is independent of $y$ this component must be constant, and since there is no flow through the boundaries $u=0$.

From the conservation of momentum equation,
\begin{equation*}\frac{\partial^2 v}{\partial x^2}=-\frac{g}{\nu} \quad \Rightarrow \quad v=-\frac{g}{\nu}\frac{x^2}{2}+kx +C\end{equation*}

$v(0)=0 \quad \Rightarrow C=0$

$v(x=a)=-V \quad \Rightarrow k=\frac{g}{\nu}\frac{a}{2}-\frac{V}{a}$

\begin{equation*}v=\frac{g(ax-x^2)}{2\nu}-\frac{Vx}{a}\end{equation*}

`````

(plane-poiseuille)=
## Plane Poiseuille flow
In this example, we will consider flow between two parallel planes driven by a constant pressure gradient $\frac{\partial p}{\partial x}=-P$. We will assume that the flow is independent of $x$ so that $\underline{u}=(u(y),v(y),0)$.
\begin{equation}\frac{}{}\end{equation}

```{image} navstok_img/plane_poiseuille.png
:name: plane Poiseuille flow
:alt: plane Poiseuille flow
:align: center
:scale: 100%
```

The equations of motion are:
\begin{equation}\nabla.\underline{u}=0, \quad \underline{u}.\nabla\underline{u}=-\frac{1}{\rho}\nabla p +\underline{F}+\nu \nabla^2\underline{u}.\end{equation}
It follows from the incompressibility condition that $v$ is constant, and since $v(0)=0$ this component must be identically zero everywhere.
The conservation of momentum equations simplify to:
\begin{equation}\frac{\mathrm{d}^2 u}{\mathrm{d}y^2}=-\frac{P}{\mu}, \quad \frac{\partial p}{\partial y}=0.\end{equation}
The velocity solution satisfying the no-slip conditions $u(0)=0$ and $u(h)=0$ is the parabolic profile:
\begin{equation}\underline{u}=\left(\frac{P y}{2\mu}(h-y),0,0\right).\end{equation}
The mass flux is given by
\begin{equation}Q=\int_0^h \left(\frac{Pyh}{2\mu}-\frac{Py^2}{2\mu}\right)\mathrm{d}y=\frac{Ph^3}{12\mu}.\end{equation}

(pipe-flow)=
## Poiseuille pipe flow

In this example we will consider flow along a pipe of circular cross-section $r=a$, under constant pressure gradient $\frac{\mathrm{d}p}{\mathrm{d}z}=-P$. An illustration of the geometry is provided below:

<br>

```{image} navstok_img/piper.png
:name: plane Poiseuille flow
:alt: plane Poiseuille flow
:align: center
:scale: 100%
```
<br>

We will work in cylindrical polar coordinates, using the equations given in {numref}`navstok-cylindrical`. It is clear from the flow geometry that $v_{\theta}=0$, and that $v_r,v_z$ are independent of $\theta$. We also assume that $v_r,v_z$ are independent of the downstream position $z$.

From the incompressibility condition with $v_r=v_r(r)$, $v_{\theta}=0$, $v_z=v_z(r)$, we then obtain

\begin{equation}\frac{\partial^2 v_r}{\partial r^2}+\frac{1}{r}\frac{\partial v_r}{\partial r}=0\quad \Rightarrow \quad \frac{\partial}{\partial r}\left(r\frac{\partial v_r}{\partial r}\right)=0.\end{equation}

The solution for $v_r$ is required to satisfy $v_r(r=a)=0$, so that there is no flow through the boundary. This gives

\begin{equation}v_r=K\ln\left(\frac{r}{a}\right).\end{equation}

However, when $r=0$ the result is infinite unless $K=0$, so we conclude that there is no radial component of velocity and we may take $\underline{v}=(0,0,v_z(r)).$

The third conservation of momentum equation then gives

\begin{equation}r\frac{\partial^2 v_z}{\partial r^2}+\frac{\partial v_z}{\partial r}=-\frac{P}{\mu}r \quad \Rightarrow \quad \frac{\partial }{\partial r}\left(r\frac{\partial v_z}{\partial r}\right)=-\frac{P}{\mu} r.\end{equation}

The solution for $v_z$ that satisfies the no-slip condition $v_z(r=a)=0$ is

\begin{equation}u_z=\frac{P}{4\mu}(a^2-r^2)+A\ln\left(\frac{r}{a}\right).\end{equation}

Again, we find that $u_z$ is infinite on $r=0$ unless $A=0$, which finally gives the result:

\begin{equation}v_z=\frac{P}{4\mu}(a^2-r^2), \quad v_r=v_\theta=0.\end{equation}


```{admonition} A bloody difficult problem
:class: theorem
Poiseuille flows are named after the physician who first studied the problem in connection with blood flow. Their instability under certain conditions constitutes one of the most important problems of fluid dynamics.
```
