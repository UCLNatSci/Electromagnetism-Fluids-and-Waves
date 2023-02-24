(ch_navstok)=
# Shear stress and viscosity

**In this section:**
* What does the viscosity of a fluid measure?
* How is viscosity related to shear stress?
* Can we ever safely ignore shear-stress effects?
* Do the famous Navier-Stokes equations apply to all fluids?

## The inviscid case

At the end of the last section we saw that if there is no shear stress within the fluid then we obtain the following equation:

```{math}
:label: consofmom7
\frac{\partial \underline{u}}{\partial t}+\underline{u}.\nabla\underline{u}=-\frac{1}{\rho}\nabla p+\underline{F}.
```

This circumstance would occur within a body of fluid that is moving uniformly, as shown in the flow profile below. Each fluid element moves in perfect lockstep with its neighbours and so no shear force is exerted.

<br>

```{image} navstok_img/uniform.png
---
name: uniform flow
alt: alternative description
align: center
scale: 80%
---
```
<br>

However, in most real scenarios we do not encounter fluids moving uniformly and so adjacent fluid elements exert shear stresses on their neighbours. Consider, for example, the below profile in which the upper layers of fluid flow faster. Each layer then exerts a resistive force on the one above it, due to internal "friction".

```{image} navstok_img/shear.png
---
name: shear flow
alt: alternative description
align: center
scale: 80%
---
```
<br>

For non-uniform motion, the assumption of no shear stress implies that layers of fluid can slip smoothly past each other without experiencing any internal fluid resistance. It also implies that the fluid would slip past a solid boundary without any transfer of momentum.

This assumption is unphysical. However, it may be a good approximation for fluids that are not very *viscous* if the fluid region that we are interested in is not close to a solid boundary. For a description of viscosity, see {ref}`newtonian-case`.

```{admonition} Superfluids
:class: theorem
All fluids have some internal resistance (viscosity) except for an exotic class of fluids called [superfluids](https://www.britannica.com/science/superfluidity). Liquid helium is a superfluid at temperatures close to absolute zero. Research has also been undertaken at UCL to demonstrate superfluid properties of structures involving [polariton](https://qlm-ucl.org/) quasi-particles, which result from interaction between light (photons) and matter (excitons).

```

(newtonian-case)=
## The Newtonian case

The amount of internal friction depends on properties of the fluid. In a so-called "Newtonian" fluid the shear stress is linearly proportional to the velocity gradient, which may be written as

```{math}
:label: consofmom6
\underline{\tau}_{i,j}=\mu\left(\frac{\partial u_i}{\partial x_j}+\frac{\partial u_j}{\partial x_i}\right)
```

The figure below illustrates a flow profile with a nonlinear shear velocity gradient $\displaystyle \frac{\partial u}{\partial z}$. We will see later on that this type of flow profile tends to arise near to a solid boundary, due to fluid particles "sticking" to the boundary.

<br>

```{image} navstok_img/blasius.png
---
name: strong-shear
alt: a strong shear
align: center
scale: 80%
---
```
<br>

The constant of proportionality $\mu$ appearing in the formula above is called the viscosity (or "dynamic viscosity"), measured in $\mathrm{Pa.s}$ (Pascal-seconds). It measures the tendency for fluid layers to be dragged by their neighbours and can therefore be thought of as a measure of the "diffusivity of momentum". It is a material property of the fluid under particular conditions, such as temperature. A list of viscosities of common fluids, and some not-so-common, can be found at: https://en.wikipedia.org/wiki/List_of_viscosities

```{admonition} Understanding viscosity
:class: theorem
Viscosity is a measure of a fluid's thickness, or how easily it flows. Elements in more viscous fluids exert greater internal resistance during fluid motion. Honey, for example, has a much higher viscosity than water so it flows slowly when you try to pour it.

A more accurate way to understand and measure viscosity is to consider an object such as a marble dropped into a cylinder of the fluid under gravity. In a low viscosity fluid the marble will reach the bottom of the fluid cylinder quickly, as its momentum is not substantially diffused by the fluid, whilst in a high viscosity fluid the marble will take a long time to reach the bottom as its momentum is diffused to surrounding layers of fluid.
```

## The non-Newtonian case

The Newtonian fluid relationship {eq}`consofmom6` is an experimental result. It holds under a wide range of conditions for a wide range of fluids, including air, water and most oils and syrups. However, it does not hold for all fluids under all conditions. In fact, due to the abundance of long-chain polymers in biological fluids, Newtonian behaviour may be the exception in biological contexts, rather than the rule.

### Nonlinear response to shear
In real fluids there may be a nonlinear relationship between the shear stress and the velocity gradient. This may also be interpreted as an increase/decrease in the effective viscosity under application of shear. Examples  of shear-thinning fluids include paint, whipped cream, blood, saliva, lava and toothpaste. Examples of shear-thickening fluid include oobleck (which is a mixture of cornstarch and water) and the synovial fluid that lubricates our joints. Some fluids exhibit these properties only above/below a certain shear threshold.

**Fun demonstrations:**

* [How to put ketchup on your fries like a pro](https://www.youtube.com/watch?v=KB43fM_ozKQ)
* [Kaye effect for shampoos](https://www.youtube.com/watch?v=eADS4oDTS4o)
* [The science of cornstarch and water (oobleck)](https://www.youtube.com/watch?v=mYTerCbDUzE&t=119s)

### Viscoelasticity
Some fluids become elastic when they are compressed or stretched, in the manner of an elastic solid. For these fluids, the application of a strain results in a stress in the same direction. Such fluids are called *viscoelastic* fluids. Examples include polyelectrolytes in which the electrostatic forces resist a change of shape, and liquid polymers in which the tangled polymers act as springs.

The relationship between stress and strain is generally Hookean (i.e. linear) and so the equations of motion can be modified adding a stress term that is proportional to the strain.

**Fun demonstrations:**

* [Boger fluid (constant viscosity elastic fluid)](https://www.youtube.com/watch?v=fZSUToTkkW0&t=275s)
* [Viscoelastic fluid simulation](https://www.youtube.com/watch?v=MCHw6fUyLMY)


(navstokeqn)=
## Navier-Stokes equations

The conservation of momentum equation for a Newtonian fluid, together with the conservation of mass equation for incompressible flow are called the Navier-Stokes equations. The equations are given below, where $p$ is the hydrostatic pressure (mean normal stress), and $\nu=\frac{\mu}{\rho}$ is called the kinematic viscosity.

\begin{equation}\frac{\partial\underline{u}}{\partial t}+\underline{u}.\nabla\underline{u}=-\frac{1}{\rho}\nabla p+\nu \nabla^2 \underline{u}+\underline{F},\end{equation}
\begin{equation}\nabla.\underline{u}=0.\end{equation}

The first equation (conservation of mass) represents a balance between convective acceleration, pressure forces and viscous diffusion. The second equation represents the incompressibility condition.

```{admonition} Euler's equations
:class: theorem
The inviscid form of the Navier-Stokes equations (with $\nu=0$) is called Euler's equations.
```

These equations were first derived and studied in the 1800s. However, despite many decades of research it has still not been proven that the problem is well-defined in the sense of having smooth solutions in all geometries. At the turn of the century the Clay Mathematics institute announced this unsolved problem as one of its seven "[Millennium Prize Problems](https://www.claymath.org/millennium-problems)", with $1 million offered for a solution. The problem remains unsolved today. Nevertheless, mathematicians, scientists and engineers have been using them for nearly 200 years to very good effect for modelling fluid behaviour. The equations have been used for nearly any fluid phenomenon you can think of, from modelling mucous transport to making racing cars as good as they can be, to studying sunspots or the rings of Jupiter!

(navstok-cylindrical)=
## Navier-Stokes in cylindrical coordinates

Written out in cylindrical coordinates, the components of the Navier-Stokes equations for $\underline{u}=(u_r,u_{\theta},u_z)$ are given by

**Conservation of momentum:**
\begin{align}\frac{\partial u_r}{\partial t}+(\underline{u}.\nabla)u_r-\frac{u_{\theta}^2}{r} &=-\frac{1}{\rho}\frac{\partial p}{\partial r}+\nu\left(\nabla^2 u_r-\frac{u_r}{r^2}-\frac{2}{r^2}\frac{\partial u_{\theta}}{\partial \theta}\right)\\ \frac{\partial u_{\theta}}{\partial t}+(\underline{u}.\nabla)u_{\theta}+\frac{u_r u_{\theta}}{r}&=-\frac{1}{\rho r}\frac{\partial p}{\partial \theta}+\nu\left(\nabla^2u_{\theta}+\frac{2}{r^2}\frac{\partial u_r}{\partial \theta}-\frac{u_{\theta}}{r^2}\right)\\ \frac{\partial u_z}{\partial t}+(\underline{u}.\nabla)u_z&=-\frac{1}{\rho}\frac{\partial p}{\partial z}+\nu\nabla^2 u_z \end{align}

**Incompressibility:**
\begin{equation}\frac{1}{r}\frac{\partial}{\partial r}(r u_r)+\frac{1}{r}\frac{\partial u_{\theta}}{\partial \theta}+\frac{\partial u_z}{\partial z}=0\end{equation}
where
\begin{equation}\underline{u}.\nabla = u_r\frac{\partial}{\partial r}+\frac{u_{\theta}}{\partial \theta}+u_z\frac{\partial}{\partial z}\qquad \qquad \nabla^2=\frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial}{\partial r}\right)+\frac{1}{r^2}\frac{\partial^2}{\partial \theta^2}+\frac{\partial^2}{\partial z^2} \end{equation}


## Chapter exercises

**Question 1**<br>
Research one example of a non-Newtonian fluid, and write 150 words about why it is non-Newtonian.

**Question 2**<br>
Taking the body force $\underline{F}$ to be zero, write out the Navier-Stokes equations in component form, where $\underline{x}=(x,y,z)$ and $\underline{u}=(u,v,w)$. For the conservation of momentum equation, you may write each of the $(x,y,z)$ components as a separate equation.