# Newtonian vs non-Newtonian fluids

In a so-called "Newtonian" fluid the shear stress is linearly proportional to the velocity gradient, which may be written as

```{math}
:label: consofmom5
\underline{\tau}_{i,j}=-\mu\left(\frac{\partial v_i}{\partial x_j}+\frac{\partial v_j}{\partial x_i}\right)
```

The figure below illustrates a flow profile with a strong velocity gradient $\displaystyle \frac{\partial v_1}{\partial x_2}$. We will see later on that this type of flow profile tends to arise near to a solid boundary, due to fluid particles "sticking" to the boundary.

a strong shear

The constant of proportionality $\mu$ appearing in the formula above is called the viscosity (or "dynamic viscosity"), measured in $\mathrm{Pa.s}$ (Pascal-seconds). It measures the tendency for fluid layers to be dragged by their neighbours and can therefore be thought of as a measure of the "diffusivity of momentum". It is a material property of the fluid under particular conditions (e.g. temperature). A list of viscosities of common fluids (and some not-so-common) can be found at: https://en.wikipedia.org/wiki/List_of_viscosities

Loosely speaking, you can think of viscosity as a measure of the fluid's thickness, or how easily it flows. Honey, for example, has a much higher viscosity than water so it flows slowly when you try to pour it. A more accurate way to understand and measure viscosity is to consider an object such as a marble dropped into a cylinder of the fluid under gravity. In a low viscosity fluid the marble will reach the bottom of the fluid cylinder quickly, as its momentum is not substantially diffused by the fluid, whilst in a high viscosity fluid the marble will take a long time to reach the bottom as its momentum is diffused to surrounding layers of fluid.



The Newtonian fluid relationship law is an experimental result, much like the constitutive law $F=\mu R$ that relates the resisting force between two solid surfaces to the normal reaction. It holds for a wide range of fluids under a wide range of conditions, including air, water and most oils and syrups. However, it does not hold for all fluids under all conditions.



Non-Newtonian fluids are those which have nonlinear relationship between stress and velocity gradient. Examples  of shear-thinning fluids include paint, whipped cream, blood, saliva*, lava and toothpaste, whilst examples of shear-thickening fluid is oobleck (a mixture of cornstarch and water), and the synovial fluid that lubricates our joints. Some fluids are non-Newtonian only above/below a certain threshold.

*Due to the abundance of long-chain polymers in biological fluids, Newtonian behaviour may be the exception in biological contexts, rather than the rule.



## Fun demonstrations:

How to put ketchup on your fries like a pro: https://www.youtube.com/watch?v=KB43fM_ozKQ
Oobleck in a pool : https://thekidshouldseethis.com/post/oobleck-pool
Oobleck on a speaker: https://www.youtube.com/watch?v=3zoTKXXNQIU
Kaye effect for shampoos: https://www.youtube.com/watch?v=eADS4oDTS4o
Boger fluids: https://www.insidescience.org/video/what-boger-fluid


Navier-Stokes for Newtonian fluids
For a Newtonian fluid with zero body force,

```{math}
:label: navstoknewt
\frac{D\underline{v}}{D t}=-\frac{1}{\rho}\nabla p+\nu \Delta \underline{v}, \qquad \Delta=\nabla^2=\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}
```

where $p$ is the hydrostatic pressure (mean normal stress), and $\nu=\frac{\mu}{\rho}$ is called the kinematic viscosity.



The equations can be non-dimensionalised by scaling quantities with respect to characteristic scales of velocity $U$ and length $L$ (see next subchapter) to obtain the final conservation of momentum equations given in the box below.

Navier Stokes equations

For an incompressible, Newtonian fluid, in the absence of any body forces:

```{math}
:label: navstoknondimconsofmom
\frac{\partial\underline{v}}{\partial t}+\underline{v}.\nabla \underline{v}=-\nabla p + \mathrm{Re}^{-1} \Delta\underline{v}
```

```{math}
:label: navstoknondimincompress
\nabla.\underline{v}=0
```

where $\mathrm{Re}=\frac{U L}{\nu}$ is a parameter called the Reynolds number.

The first equation (conservation of mass) represents a balance between convective acceleration, pressure forces and viscous diffusion. The second equation represents the incompressibility condition.

Written out in full, these equations are

\begin{align}\frac{\partial v_x}{\partial t}+v_x\frac{\partial v_x}{\partial x}+v_y\frac{\partial v_x}{\partial y}+v_z\frac{\partial v_x}{\partial z}&=-\frac{\partial p}{\partial x}+\mathrm{Re}^{-1}\left(\frac{\partial^2 v_x}{\partial x^2}+\frac{\partial^2 v_x}{\partial y^2}+\frac{\partial^2 v_x}{\partial z^2}\right)\\\frac{\partial v_y}{\partial t}+v_x\frac{\partial v_y}{\partial x}+v_y\frac{\partial v_y}{\partial y}+v_z\frac{\partial v_y}{\partial z}&=-\frac{\partial p}{\partial y}+\mathrm{Re}^{-1}\left(\frac{\partial^2 v_y}{\partial x^2}+\frac{\partial^2 v_y}{\partial y^2}+\frac{\partial^2 v_y}{\partial z^2}\right)\\\frac{\partial v_z}{\partial t}+v_x\frac{\partial v_z}{\partial x}+v_y\frac{\partial v_z}{\partial y}+v_z\frac{\partial v_z}{\partial z}&=-\frac{\partial p}{\partial z}+\mathrm{Re}^{-1}\left(\frac{\partial^2 v_z}{\partial x^2}+\frac{\partial^2 v_z}{\partial y^2}+\frac{\partial^2 v_z}{\partial z^2}\right)\\\frac{\partial v_x}{\partial x}+\frac{\partial v_y}{\partial y}+\frac{\partial v_z}{\partial z}&=0\end{align} (fullnavstok)



It is helpful to classify the study of fluids as follows:



Incompressible	Compressible
Inviscid	This course	Acoustics (high speed)
Viscous	This course in part	Research only!




## Challenge yourself:
After you have read the notes for this subsection, try to complete the worksheet below without looking at any resources

>>> worksheet 1.docx

```{admonition} Big idea: Conservation of mass and momentum
:class: tip
The equations governing the motion of fluids are the Navier-Stokes equations, for conservation of mass and momentum. They apply at the macroscopic level, where quantities such as the fluid velocity and density are treated as continuous.

For fluid motions that occur well below the speed of sound, the effects of compressibility can be neglected, and in that case the conservation of mass equation simplifies to the incompressibility condition $\nabla.\underline{v}=0$, where $\underline{v}$ is the velocity field.

The conservation of momentum equation represents a balance between convective acceleration, pressure forces and the diffusion of momentum to neighbouring fluid elements. A wide class of so-called "Newtonian" fluids exhibit a linear relationship between the shear stress and the velocity gradient, in which the constant of proportionality is a material quantity, called the viscosity.

By non-dimensionalising the equations of motion, we can consider motion on different length/velocity scales or in fluids of different viscosity all by varying a single parameter, called the Reynolds number $\mathrm{Re}$.
```
