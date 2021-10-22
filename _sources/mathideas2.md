# More mathematical ideas

* What is a "potential flow"? [possibly move to its own section]

## The material derivative

THIS SECTION NEEDS A REWRITE

According to the chain rule for an arbitrary function $\phi(\underline{x},t)$,

```{math}
:label: chainrule
\frac{\mathrm{d}\phi}{\mathrm{d}t}=\frac{\partial \phi}{\partial t}+\frac{\mathrm{d}\underline{x}}{\mathrm{d}t}.\nabla\phi
```

If we put $\frac{\mathrm{d}\underline{x}}{\mathrm{d}t}=\underline{v}$, which defines the path of a fluid element, then we obtain :

```{math}
:label: materialderivative
\frac{D\phi}{Dt}=\frac{\partial \phi}{\partial t}+\underline{v}.\nabla\phi
```

The differential operator $\frac{D}{Dt}$ is called the "material derivative" or "convective derivative".

The operator $\underline{v}.\nabla$ gives the directional derivative tangent to $\underline{v}$. It is often called convection, since it captures the motion/transfer arising due to the existence of the velocity field. For example, $\underline{v}.\nabla\underline{v}$ is called convective acceleration. The term $\frac{\partial \phi}{\partial t}$ accounts for...

An illustration of the idea is shown below.

<br>

```{image} navstok_img/potentialfun.gif
---
name: potential_fun
alt: a particle moving through a potential field
align: center
scale: 80%
---
```
<br>




Suppose that a fluid particle follows the path marked in blue through the potential field $\phi$, which is indicated by the background colour scheme and equipotential contours shown. The vectors (arrows) shown on the plot depict the instantaneous gradient field of $\phi$. At each point on the trajectory, the experienced change in $\phi$ is given by the projection of the particle's own direction vector $\underline{v}$ with the gradient field, $\nabla \phi$, plus the instantaneous change in the potential field $\phi$ at that point due to time evolution.

The material derivative can also be applied to each element of a vector field $\underline{\phi}$, to give the change in $\underline{\phi}$ following the motion of a fluid particle.

An interesting example description of these ideas can be found at https://www.youtube.com/watch?v=l4F2bZgwcpU
