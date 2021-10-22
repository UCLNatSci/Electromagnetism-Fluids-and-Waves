#!/usr/bin/env python
# coding: utf-8

# # Mathematical ideas 3
# 
# **In this section:**
# * How can a **vortex** have zero **vorticity** ?
# * How are curl and div of velocity related to sliding and squashing?
# * What is a "potential flow"? [possibly move to its own section]
# 
# ## Vorticity
# Vorticity is a measure of the local rotation or spin of fluid particles. It is defined as the curl of the velocity vector $(u,v,w)$:
# 
# \begin{equation}\underline{\omega} = \nabla\times\underline{v}=\left(\frac{\partial w}{\partial y}-\frac{\partial v}{\partial z}\right)\underline{e}_x,+\left(\frac{\partial u}{\partial z}-\frac{\partial w}{\partial x}\right)\underline{e}_y+\left(\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}\right)\underline{e}_z\end{equation}
# 
# An illustrated interpretation of vorticity is given below, looking only at the $z$-component for simplicity. Note that the subscript notation used on the diagram represents partial differentiation, not a vector component. We consider two fluid line elements $AB$ and $AC$, which are aligned with the $x$ and $y$ axes, respectively. By the definition of the partial derivative, we can write
# 
# \begin{equation}v(x+\delta x,y,z,t)-v(x,y,z,t)=\frac{\partial v}{\partial x}\delta x\end{equation}
# 
# so
# 
# * $\displaystyle \frac{\partial v}{\partial x}$ represents the instantaneous angular velocity of the fluid line element $AB$
# * $\displaystyle\frac{\partial u}{\partial y}$ represents the instantaneous angular velocity of the fluid line element $AC$
# * The local anticlockwise spin about $A$ is therefore given by $\displaystyle \frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}$.
# 
# 
# 
# vorticity illustration
# 
# 
# 
# 
# 
# It is important to recognise that the vorticity is not related to the global rotation of the fluid. To illustrate this, we will consider the vorticity of some basic flows, which are either rotating or not rotating.
# 
# 
# 
# 
# 
# Example 1: Shear flow
# 
# Consider a two-dimensional "shear" velocity profile described by $\underline{v}=(u(y),0,0).$
# 
# This flow is a rectilinear flow; meaning that it is not rotating as a whole, as can be seen from the image below. However, the vorticity is non-zero since fluid particles are rotated by the shearing force, as would be seen by an observer following the fluid.
# 
# velocity profile
# 
# \begin{equation}\underline{\omega}=\begin{vmatrix}\underline{e}_x &\underline{e}_y &\underline{e}_z\\\frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\ u(y)& 0 & 0\end{vmatrix}=\left(0,0,-u^{\prime}(y)\right)\end{equation}
# 
# We see that the fluid elements rotate about the $z$ axis in a clockwise direction (due to the negative sign).
# 
# 
# 
# Example 2: Line vortex ('potential vortex')
# 
# Consider a flow described in cylindrical polars $(\rho,\theta,z)$, by the velocity profile $\underline{v}=\left(0,\frac{k}{\rho},0\right)$, where $k$ is a positive constant.
# 
# This flow is a swirling motion with velocity decreasing in the radial direction like $\frac{1}{\rho}$, as illustrated in the figure below
# 
# line_vortex
# 
# 
# 
# The vorticity is zero, meaning that fluid particles are swept round the origin without local rotation. To show this, we have to use the result for the gradient in cylindrical polars:
# 
# \begin{equation}\nabla\times \underline{v}=\frac{1}{\rho}\begin{vmatrix}\underline{e}_{\rho} & \rho\underline{e}_{\theta}& \underline{e}_z\\\frac{\partial }{\partial r}&\frac{\partial}{\partial \theta}&\frac{\partial}{\partial z}\\ v_{\rho}&\rho v_{\theta} & v_z\end{vmatrix}=\frac{1}{\rho}\begin{vmatrix}\underline{e}_{\rho} & \rho\underline{e}_{\theta}& \underline{e}_z\\\frac{\partial }{\partial r}&\frac{\partial}{\partial \theta}&\frac{\partial}{\partial z}\\ 0&k & 0\end{vmatrix}=\underline{0}\end{equation}
# 
# The surprising result occurs in this example because the slowing down of the fluid away from the origin is just the right strength to create a rotational shear that counterbalances the angular rotation of the fluid.
# 
# 
# 
# Helmhotz decomposition (fundamental theorem of calculus)
# Any vector field that is smooth, defined everywhere in space and vanishes at infinity together with its first derivatives can be decomposed as follows:
# 
# \begin{equation}F=\nabla \phi +\nabla \times A\end{equation}
# 
# We will not prove this result, but we will use it to simplify the equations of motion in some scenarios.
# 
# The first term is irrotational (curl-free) from the vector identity “curlgrad=$\underline{0}$” and the second term is solenoidal (divergence-free) from the vector identity “divcurl=0”.
# 
# 
# ## What is **flux**?
# 
# Consider a small (strictly infinitesimal) surface element $S$ within a field $\underline{F}$, such that the surface normal makes an angle $\theta$ to the direction of the field, as shown. The components of the field in directions parallel and perpendicular to the surface are illustrated in blue. The perpendicular component has magnitude $F\cos{\theta}$. The parallel component remains bounded by the surface.
# 
# <br>
# 
# ```{image} navstok_img/flux1.png
# ---
# name: flux
# alt: alternative description
# align: center
# scale: 80%
# ---
# ```
# <br>
# 
# Multiplying the normal component of the field by the area of the surface element gives the volume indicated by the shaded cylinder in the image below. It is a scalar quantity, which tells us the instantaneous rate of flow through the surface per unit time. Mathematically, the flow rate across the surface $S$ is given by
# 
# \begin{equation}\underline{F}.\underline{S}=\underline{F}.\hat{\underline{n}}S = FS\cos{\theta},\end{equation}
# where $\hat{\underline{n}}$ is the unit normal to the surface.
# 
# <br>
# 
# ```{image} navstok_img/flux2.png
# ---
# name: flux
# alt: alternative description
# align: center
# scale: 80%
# ---
# ```
# <br>
# 
# The quantity $\underline{F}.\hat{\underline{n}}$ gives the flow rate *per unit area*, which is called the flux. Integrating the flux over a given finite surface area $A$ is equivalent to summing the individual surface element contributions to the flow rate, in the limit. The resulting flow rate $Q$ is given by
# 
# \begin{equation}Q=\int_A{\underline{F}.d\underline{\mathrm{S}}}\end{equation}
# 
# Most authors (including me!) use the terms flow rate and flux interchangeably, though flux is more pedantically defined as the flow rate per **unit** area. However, the intended meaning is almost always clear from the context and the surrounding text.
# 
# ```{admonition} Examples
# Net volumetric flux is the rate of volume flow across a given area, $\displaystyle \int_A\underline{v}.d\underline{S}$
# 
# Net mass flux is the rate of mass flow across a given area, $\displaystyle \int_A \rho\underline{v}.d\underline{S}$
# ```
# 
# Notice that the flux $\underline{F}.\hat{\underline{n}}$ is directly proportional to the field strength $F$. For this reason, the field strength is sometimes referred to as the *flux density*. This description fits quite well with field line depictions, since the field strength can be inferred from how close together (dense) the field lines are. However, the term flux density is more commonly used in the context of electricity and magnetism, and I will not use it in the fluids part of this module.
# 
# ## What is **divergence**?
# Suppose that a given point within  a field $\underline{F}=(f_x,f_y,f_z)$ is surrounded by a **closed** surface, $S$ as illustrated below:
# 
# ```{image} navstok_img/source.png
# ---
# name: source_fun
# alt: alt text
# align: center
# scale: 80%
# ---
# ```
# 
# It can be shown (divergence theorem) that the flux $Q$ through surface $S$ is equivalent to a volume integral:
# ```{math}
# :label: divergence_thm
# Q=\oint_S \underline{F}.d\underline{S} \equiv \int_V (\nabla.\underline{F})dV,
# ````
# where the *divergence* $\nabla.\underline{F}$ is given by:
# \begin{equation}\nabla.\underline{F}=\biggr(\frac{\partial f_x}{\partial x},\frac{\partial f_y}{\partial y},\frac{\partial f_z}{\partial z}\biggr).\end{equation}
# 
# By applying the Fundamental Theorem of Calculus to {eq}`divergence_thm`, we obtain the result
# \begin{equation}\nabla.\underline{F}=\frac{\mathrm{d}Q}{\mathrm{d}V}=\lim_{V\rightarrow 0} \frac{\oint_S \underline{F}.d\underline{S}}{V}\end{equation}
# 
# Hence, divergence can be understood as the flux per unit volume through an infinitesimally-small closed surface surrounding a point. A point with positive divergence behaves like a source, and a point with negative divergence behaves like a sink.
# 
# ```{admonition} See also
# :class: readmore
# For further discussion of the divergence theorem and related concepts, visit
# [Khan Academy](https://www.khanacademy.org/math/multivariable-calculus/greens-theorem-and-stokes-theorem/divergence-theorem-articles/a/3d-divergence-theorem)
# ```
# 
# ```{exercise}
# :label: ex-divergence
# Calculate the divergence of the potential flow you looked at in {numref}`pot-fun`, and produce a grayscale plot of the divergence on the range $-2\leq x,y \leq 2.$
# ```
# 
# ##
# Path integrals for conservative and non-conservative fields
# The result that a conservative field is irrotational can be demonstrated by considering that if the line integral of $\underline{F}$ is path independent then the fundamental theorem of calculus allows us to write
# 
# \begin{equation}\int_C \underline{F}.\mathrm{d}\underline{s} = \int_C \frac{\mathrm{d}\phi}{\mathrm{d}t}\mathrm{d}t.\end{equation}
# 
# And by the chain rule we may also say that
# 
# \begin{equation} \int_C \frac{\mathrm{d}\phi}{\mathrm{d}t}\mathrm{d}t=\int_C \left(\frac{\partial \phi}{\partial x}\frac{\mathrm{d}x}{\mathrm{d}t}+\frac{\partial \phi}{\partial y}\frac{\mathrm{d}y}{\mathrm{d}t}+\frac{\partial \phi}{\partial z}\frac{\mathrm{d}z}{\mathrm{d}t}\right)\mathrm{d}t=\int_C \nabla \phi . \frac{\mathrm{d}s}{\mathrm{d}t}\mathrm{d}t =\int_C (\nabla \phi).\mathrm{d}\underline{s}\end{equation}
# 
# Calculus practice :
# 
# (1) Show that the vector field $\underline{F}=(3x^2,3y^2,3z^2)$ is irrotational (curl-free) and that it can be expressed as the gradient of a scalar potential \begin{equation}\phi=x^3+y^3+z^3 +\mathrm{const.}\end{equation}
# 
# Hence, calculate the work done by this force in moving a body from point $(1,2,1)$ to $(3,2,1)$.
# 
# 
# 
# (2) Show that the vector field $\underline{F}=(y^2,x^2,0)$ is solenoidal (divergence-free) but not irrotational.
# 
# Calculate the work done by this force in moving a body from the point $(1,0,0)$ to $(0,2,0)$
# 
# (i) Along the line $2x+y=2$
# 
# (ii) Along a piece of the parabola $4x+y^2=4$
# 
# 
# 
# Solutions:
# 
# (1) $\nabla\times\underline{F}=(0,0,0), \quad \Rightarrow\quad \underline{F}=\nabla\phi = \left(\frac{\partial \phi}{\partial x},\frac{\partial \phi}{\partial y},\frac{\partial \phi}{\partial z}\right)$
# 
# Equating components and integrating gives $\underline{F}=x^3+y^3+z^3 +\mathrm{const.}$
# 
# Hence, $\displaystyle \int_{(1,2,1)}^{(3,2,1)}\underline{F}.\mathrm{d}\underline{s} = \phi(3,2,1)-\phi(1,2,1)=26$ (independent of the path)
# 
# 
# 
# (2) $\nabla.\underline{F}=0, \quad \nabla\times\underline{F}=(0,0,2x-2y)$
# 
# $\displaystyle W=\int_{(1,0,0)}^{(0,2,0)}\underline{F}.\mathrm{d}\underline{s}=\int_{(1,0,0)}^{(0,2,0)}(y^2\mathrm{d}x+x^2\mathrm{d}y)$
# 
# (i) Let $x=t,$ $y=2-2t$. Then $\displaystyle W=\int_1^0\left[(2-2t)^2-2t^2\right]\mathrm{d}t=\frac{2}{3}$
# 
# (ii) Let $y=t,$ $x=1-\frac{t^2}{4}$. Then $\displaystyle W=\int_0^2\left[t^2\left(\frac{-t}{2}\right)+\left(1-\frac{t^2}{4}\right)^2\right]\mathrm{d}t= -\frac{14}{15}$
# 
# The result is path-dependent.
# 
# 
# ## Potential flows
# Recall that if $\underline{v}$ is irrotational, then it may be expressed as the gradient of a potential
# 
# \begin{equation}\underline{v}=\nabla\phi\end{equation}
# 
# Examples:
# 
# (i) $\underline{v}=(U,0,0)$ is irrotational. It has velocity potential $\phi=Ux$, since
# 
# \begin{equation}\frac{\partial \phi}{\partial x}=U,\quad \frac{\partial \phi}{\partial y}=0, \quad \frac{\partial \phi}{\partial z}=0.\end{equation}
# 
# (ii) Stagnation point flow $\underline{v}=(\alpha x,-\alpha y,0)$ is irrotational. It has velocity potential $\phi=\frac{1}{2}\alpha(x^2-y^2)$, since
# 
# \begin{equation}\frac{\partial \phi}{\partial x}=\alpha x,\quad \frac{\partial \phi}{\partial y}=-\alpha t, \quad \frac{\partial \phi}{\partial z}=0.\end{equation}
# 
# (iii) Line vortex flow $\underline{v}=\frac{k}{r}\underline{e}_{\theta}$ is irrotational everywhere except at the origin, where it is not defined.
# If we consider only the region $r\geq a$ then we have a potential flow:
# 
# \begin{equation}\frac{\partial \phi}{\partial r}=0, \quad \frac{1}{r}\frac{\partial \phi}{\partial \theta}=\frac{k}{r}, \quad \frac{\partial \phi}{\partial z} \qquad \Rightarrow \quad \phi=k\theta.\end{equation}
# 
# 
# Exercises
# 
# 
# 
# 3. Consider a two-dimensional unsteady flow given by $\underline{v}=(3 x/t^2, -2 y/t^2,0)$.
# 
# (i) Show that the velocity field is irrotational and calculate its divergence.
# 
# (ii) Since the velocity field is irrotational, it can be derived from a potential $\phi(x,y)$. Find an expression for this function.
# 
# (iii) In which direction do the contours of the potential function $\phi$ lie in relation to the velocity field?
# 
# (iv) Calculate the equations of the streamlines and show that for this example the streamlines and particle paths are the same.
# 
# 
# 
# 4. For the steady flow $\underline{v}=(2x,3y,-5z)$, compute the trajectories of particles starting on the ring $x=\cos(\theta)$, $y=\sin(\theta)$, $z=1$.
# 
# Show that the flow is both irrotational and solenoidal, and describe the motion of the fluid particles in words.
