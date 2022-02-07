(water-waves)=
# Unsteady: Water waves

**In this section:**

* Wavy solutions of the Laplace equation
* Use of a "small amplitude" condition
* Different dispersive properties for deep and shallow water
* What are the paths followed by particles on the water surface?

## The flow geometry
We consider the scenario shown below, where the axis $x$ points in the direction of wave motion, and axis $z$ points perpendicular to the water surface. We will assume plane motion, so there is no $y$ dependence.

```{image} navstok_img/sea.png
:name: a wavetrain
:alt: a wavetrain
:align: center
:scale: 100%
```

## Mass transport
We make the simplifying assumption that the flow is irrotational, so that the velocity field can be written as the gradient of a potential $\underline{u}=\nabla\phi(\underline{x},t)$, and we obtain from the incompressibility condition
\begin{equation}\nabla^2\phi=\frac{\partial^2\phi}{\partial x^2}+\frac{\partial^2\phi}{\partial z^2}=0.\end{equation}
Seeking a travelling plane wave solution of the form $\phi=F(z)G(x-c t)$ provides
\begin{equation}\frac{F^{\prime\prime}}{F}=-\frac{G^{\prime\prime}}{G}=-k^2.\end{equation}
This choice of separation constant gives us exponential behaviour in the $z$ direction, and oscillating behaviour in the $x$-direction:
```{math}
:label: phi-relation
\phi=\left[Ce^{k z}+De^{-kz}\right]\sin(k x-\omega t+\phi_0), \quad \omega=c k.
```
We will take $k>0$ and $\phi_0=0$, without loss of generality.

## Bernoulli's equation for unsteady potential flow
Recall that in equation {eq}`vorticity-head` we obtained the following result from Euler's equation, with a body force $\underline{F}=\underline{g}$
\begin{equation}\frac{\partial \underline{u}}{\partial t}+(\underline{\omega}\times\underline{u})=-\nabla H, \quad H=\frac{p}{\rho}+gz+\frac{1}{2}|\underline{u}|^2\end{equation}
Previously, we assumed that the flow was steady, and we took the scalar product with $\underline{u}$ to eliminate the vorticity term, obtaining a result for the head $H$ along a streamline.
Here, we will not assume that the flow is steady, but we will instead note that for potential flow $\underline{u}=\nabla\phi(\underline{x},t)$ the vorticity is identically zero, and so the equation of motion simplifies to
\begin{equation}\nabla\left(\frac{\partial\phi}{\partial t}+H\right)=\underline{0}.\end{equation}
Integrating gives the following result, where $F(t)$ is an arbitrary function that does not affect the velocities, since they are obtained by taking the gradient:
\begin{equation}\frac{\partial\phi}{\partial t}+\frac{p}{\rho}+\frac{1}{2}|\underline{u}|^2+gz=F(t), \quad \underline{u}=\nabla\phi.\end{equation}  

## Free surface conditions
The surface equation is of the form $z=\eta(x,t)$. We will assume that the free surface displacement $\eta$ is small and apply Taylor expansion to the derivatives of $\phi$ in the following manner:

\begin{equation}\frac{\partial\phi}{\partial z}\biggr|_{z=\eta}=\frac{\partial\phi}{\partial z}\biggr|_{z=0}+\eta\frac{\partial^2\phi}{\partial z^2}\biggr|_{z=0}+\dots\end{equation}

Any terms that are quadratic order or higher will be neglected. We will justify this approach a posteriori.

### Dynamic boundary condition
We will apply Bernoulli's theorem on the surface. Since $F(t)$ is arbitrary, we will take $F(t)=\frac{p_0}{\rho}$, where $p_0$ is the surface pressure (atmospheric pressure). Therefore we obtain:
\begin{align}
&&\frac{\partial\phi}{\partial t}+\frac{1}{2}(u^2+w^2)+ gz&=0 \qquad \text{on $z=\eta(x,t)$}\\
\text{i.e } &&\frac{\partial \phi}{\partial t}+ g \eta &=0 \qquad \text{on $z=0$ (linearizing)}
\end{align}

### Kinematic boundary condition
We define
\begin{equation}S(x,z,t)=z-\eta(x,t).\end{equation}
Since fluid particles on the surface must remain there, $S$ is constant following the fluid. Application of $\frac{DS}{Dt}=0$ with $(u,v,w)=\nabla\phi$ gives
\begin{align}
&&\frac{\partial \eta}{\partial t}+\frac{\partial \phi}{\partial x}\frac{\partial \eta}{\partial x}&=\frac{\partial\phi}{\partial z} \qquad \text{on $z=\eta(x,t)$}\\
\text{i.e } &&\frac{\partial\eta}{\partial t}&=\frac{\partial \phi}{\partial z} \qquad \text{on $z=0$ (linearizing)}
\end{align}


### Combined surface condition
The two conditions can be combined by eliminating $\eta$ to obtain

```{math}
:label: combined-surface
\frac{\partial^2\phi}{\partial t^2}+g\frac{\partial\phi}{\partial z}=0\quad \text{on }z=0.
```

## Bottom conditions

### Deep water
For deep water, we impose a requirement that the velocity remains bounded as $z\rightarrow -\infty$. For the solution given in {eq}`phi-relation`, we find that $D=0$ and we have
```{math}
:label: deepwater
\phi=Ce^{k z}\sin(k x-\omega t)
```

### Finite depth
For shallow/finite depth water, we impose a condition of no flow through the bed at $z=-h$. That is,
\begin{equation}
w\biggr|_{z=-h}=\frac{\partial \phi}{\partial z}\biggr|_{z=-h}=0.
\end{equation}
For the solution given in {eq}`phi-relation`, we find that $Ce^{-kh}=De^{kh}$ and we have

```{math}
:label: finitewater
\phi=A\cosh(kz+kh)\sin(k x-\omega t)
```
after defining $A=2C$.

## Dispersion relations

### Deep water
Application of the combined surface condition {eq}`combined-surface` to the deep water solution {eq}`deepwater` gives the dispersion relation
\begin{equation}
\omega^2 = gk \quad \Rightarrow \quad c=\sqrt{\frac{g\lambda}{2\pi}},
\end{equation}
where $c$ is the phase velocity. The result demonstrates that longer waves travel faster. Atlantic storms generate long waves of small amplitude (swell), which travel quickly (up to thousands of kilometers per day), and these waves arrive on the West Coast of Britain well before the slower-moving storm.

```{exercise}
Surface waves generated by a mid-Atlantic storm arrive at the British coast with a period of 15 seconds. A day later the period of the waves arriving has dropped to 12.5 seconds. Roughly how far away did the storm occur?
```

### Finite depth
Application of the combined surface condition {eq}`combined-surface` to the deep water solution {eq}`finitewater` gives the dispersion relation
\begin{equation}
\omega^2 = gk\tanh(kh).
\end{equation}

```{exercise}
Consider the case of shallow water, so that $\frac{1}{k}\gg h$. Use the result $\tanh(\theta)\simeq \theta$ for $\theta\ll 1$ to simplify the finite depth dispersion relation, and state in words what the result tells us about dispersion in shallow water.

Show also that when $\frac{1}{k}\ll h$ the finite depth dispersion relation approaches the result given for deep water.
```


## "Small amplitude" condition
In the dynamic boundary condition, we neglected $u^2$ and $v^2$ compared to $g\eta$, and in the kinematic boundary condition we neglected $u\partial\eta/\partial x$ compared to $w$. Both of these assumptions are justified if $Ak\ll 1$, which therefore requires that the wave amplitude $A$ is vanishingly small compared to the wavelength $\frac{2\pi}{k}$.
For the longest ocean waves, such as waves generated by earthquakes, the approximation breaks down. For the seas around Europe the depth of the water over the continental shelf is far less than 1km, so a revised theory for shallow water is needed.

## Particle paths
Assume that the particle motion is small compared to the initial displacement $(x_0,z_0)$, so that we can write
\begin{align}x&=x_0+\epsilon X(x,z,t)\\ z&=z_0+\epsilon Z(x,z,t).\end{align}
Then
\begin{align}
\epsilon \frac{\mathrm{d}X}{\mathrm{d}t}&=u(x_0+\epsilon X, z_0+\epsilon Z,t)\simeq u(x_0,z_0,t)\\
\epsilon \frac{\mathrm{d}Z}{\mathrm{d}t}&=w(x_0+\epsilon X, z_0+\epsilon Z,t)\simeq w(x_0,z_0,t)\end{align}

For deep water this gives

\begin{align}
\epsilon \frac{\mathrm{d}X}{\mathrm{d}t}&=A\omega e^{k z_0}\cos(k x_0-\omega t),\\
\epsilon \frac{\mathrm{d}Z}{\mathrm{d}t}&=A\omega e^{k z_0}\sin(k x_0-\omega t).
 \end{align}

[If you are wondering how these can balance, it is because the wave amplitudes are small: $Ak\sim \epsilon$.]
Integrating with respect to $t$ and combining the results gives
\begin{equation}(\epsilon X)^2+(\epsilon Z)^2 = (Ae^{kz_0})^2.\end{equation}
The particle paths are therefore circular, and the radius of the circles $Ae^{k z_0}$ decreases exponentially with depth.

```{exercise}
By assuming that the particle motions for shallow water gravity waves are small, describe the shape of the particle paths for this case.
```
