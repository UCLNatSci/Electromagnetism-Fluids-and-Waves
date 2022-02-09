# Bernoulli's equation

**In this section:**
* Under what conditions does Bernoulli's theorem hold?
* If you partially cover the hole of an escaping water jet with your finger, what happens to the pressure?

## Statement

If we assume no viscosity, steady flow, constant density, then the following result applies on a streamline:

```{math}
:label: bernoulli
\frac{p}{\rho}+\phi +\frac{1}{2}v^2=\text{const}
```

In the special case where the body force is gravity, we have $\phi=gz$

```{warning}
The equation only applies on a streamline, except in the case of irrotational flow $\underline{\omega}=\underline{0}$, where the constant is the same on all streamlines.

Since the relationship holds only for steady flows, the streamlines are identical to the particle paths.
```

*Note: There is also a version of Bernoulli's equation that applies to unsteady potential flows, but we do not consider it here*

(bernoulli-derivation)=
## Derivation

We start with the inviscid form of the momentum equation

```{math}
\frac{\partial \underline{u}}{\partial t}+\underline{u}.\nabla\underline{u}=-\frac{1}{\rho}\nabla p+\underline{F}.
```

Recall that if the body force $\underline{F}$ is conservative (does no work), then it can be expressed as the gradient of a scalar potential. By convention, we usually introduce a negative sign, so that that work done against $\underline{F}$ increases the potential, while work done by $\underline{F}$ decreases the potential:
\begin{equation}\underline{F}=-\nabla\phi.\end{equation}
Now, let us further assume that the fluid is uniform density, $\rho$ is constant, so that we may write:
\begin{equation}\frac{\partial \underline{u}}{\partial t}+\underline{u}.\nabla\underline{u}=-\nabla\left(\frac{p}{\rho}+\phi\right).\end{equation}
Using the vector identity $\underline{u}.\nabla\underline{u}=(\nabla\times\underline{u})\times\underline{u}+\nabla\left(\frac{1}{2}\underline{u}.\underline{u}\right)=(\underline{\omega}\times\underline{u})+\nabla\left(\frac{1}{2}v^2\right)$ then gives
```{math}
:label: vorticity-head
\frac{\partial \underline{u}}{\partial t}+(\underline{\omega}\times \underline{u})=-\nabla H, \qquad H=\frac{p}{\rho}+\phi+\frac{1}{2}v^2
```
where $H$ is known as the "head".

```{exercise}
Try to prove the strange-looking vector identity for $\underline{u}.\nabla\underline{u}$, by writing out each expression in component form.
```

```{toggle}
Let $\underline{u}=(u,v,w)$. Then,

$\displaystyle \nabla\left(\frac{1}{2}\underline{u}.\underline{u}\right)=\nabla\left(\frac{1}{2}(u^2+v^2+w^2)\right)=\begin{pmatrix}
u\frac{\partial u}{\partial x}+v\frac{\partial v}{\partial x}+w\frac{\partial w}{\partial x}\\
u\frac{\partial u}{\partial y}+v\frac{\partial v}{\partial y}+w\frac{\partial w}{\partial y}\\
u\frac{\partial u}{\partial z}+v\frac{\partial v}{\partial z}+w\frac{\partial w}{\partial z}\\
\end{pmatrix}$

$\displaystyle\underline{\omega}=\nabla\times\underline{u}=\begin{vmatrix}\underline{e}_x &\underline{e}_y &\underline{e}_z \\\frac{\partial}{\partial x} & \frac{\partial}{\partial y} &\frac{\partial}{\partial z}\\ u & v & w \end{vmatrix}=\begin{pmatrix}
\frac{\partial w}{\partial x}-\frac{\partial v}{\partial z}\\
\frac{\partial u}{\partial z}-\frac{\partial w}{\partial x}\\
\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}
\end{pmatrix}$

$\displaystyle \underline{\omega}\times\underline{u}=\begin{vmatrix}\underline{e}_x &\underline{e}_y &\underline{e}_z \\\frac{\partial w}{\partial x}-\frac{\partial v}{\partial z} & \frac{\partial u}{\partial z}-\frac{\partial w}{\partial x} &\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}\\ u & v & w \end{vmatrix}=\begin{pmatrix}
w\frac{\partial u}{\partial z}-w\frac{\partial w}{\partial x}-v\frac{\partial v}{\partial x}+v\frac{\partial u}{\partial y}\\
u\frac{\partial v}{\partial x}-u\frac{\partial u}{\partial y}-w\frac{\partial w}{\partial y}+w\frac{\partial v}{\partial z}\\
v\frac{\partial w}{\partial y}-v\frac{\partial v}{\partial z}-u\frac{\partial u}{\partial z}+u\frac{\partial w}{\partial x}
\end{pmatrix}$

Therefore

$\displaystyle (\underline{\omega}\times\underline{u})+\nabla\left(\frac{1}{2}\underline{u}.\underline{u}\right) = \begin{pmatrix}
u\frac{\partial u}{\partial x}+v\frac{\partial u}{\partial y}+w\frac{\partial u}{\partial z}\\
u\frac{\partial v}{\partial x}+v\frac{\partial v}{\partial y}+w\frac{\partial v}{\partial z}\\
u\frac{\partial w}{\partial x}+v\frac{\partial w}{\partial y}+w\frac{\partial w}{\partial z}
\end{pmatrix}$

This result is identical to $\underline{u}.\nabla\underline{u}$
```

We may yet further simplify if we assume that the flow is steady, so $\displaystyle \frac{\partial \underline{u}}{\partial t}=0$, and by taking the scalar product with vector $\underline{u}$ to eliminate the vorticity term:
\begin{equation}\underline{u}.((\nabla\times\underline{u})\times\underline{u})=-\underline{u}.\nabla H\end{equation}
Since $\underline{a}.(\underline{b}\times\underline{a})=0$ for any vectors $\underline{a},\underline{b}$ this can be simplified to $\underline{u}.\nabla H=0$. The result says that the head remains constant on a streamline, since the directional derivative along $\underline{u}$ is zero.

## Applications

### Venturi effect

The Venturi effect is the name given to the observed phenomenon that through a constricted section of pipe there is an increase in velocity and hence a decrease in pressure. In the illustration below and in the accompanying analysis, the flow has been idealised such that it is assumed to be steady and laminar (smooth). For a more realistic depiction, see for example [this paper](https://www.sciencedirect.com/science/article/pii/S0020746200001049?via%3Dihub) - especially figure 9, which gives a treatment in two dimensions using finite difference numeric methods.

On the diagram, $A,B$ denote the cross-sectional areas at the narrowest and widest points of the tube. The pressure and flow speed on a streamline through the centre of the pipe are denoted $p_0,u_0$ at the narrowest point and by $p_1,u_1$ at the widest point. The density $\rho$ is assumed to be constant.

<br>

```{image} navstok_img/venturi.png
---
name: venturi
alt: a particle moving through a potential field
align: center
scale: 80%
---
```
<br>


By conservation of mass, we may write down the following result for the volumetric flow rate:
\begin{equation}A u_0 = B u_1.\end{equation}
By Bernoulli's theorem for the central streamline we may also say that
\begin{equation}p_0+\frac{1}{2}\rho u_0^2=p_1+\frac{1}{2}\rho u_1^2.\end{equation}
Rearranging the two results together gives (for example)
\begin{equation}p_1-p_0 = \frac{1}{2}\rho u_0^2\left(1-\frac{A^2}{B^2}\right).\end{equation}

We can see that through the choke point there will be an increase in velocity and a decrease in pressure compared to the inlet/outlet.

In general, when we observe bunching of streamlines the constrainment in volume implies a velocity increase due to mass conservation, since to maintain the same flux through a surface the velocity must increase. As a result, if the assumptions of Bernoulli are met, we see a pressure decrease. This result is sometimes used to explain the lift over an airfoil or the magnus effect on a rotating cylinder.

**However, we must be careful as Bernoulli’s theorem assumes inviscid fluid, and it turns out the viscosity is very important when fluid moves past a boundary.**

### Attaching a manometer

We now attach a second tube as shown in the diagram below, and allow the fluid in the second tube to come to rest as shown.

<br>

```{image} navstok_img/manometer.png
---
name: manometer
alt: a particle moving through a potential field
align: center
scale: 80%
---
```
<br>


According to Bernoulli's theorem $p_1-p_0=\rho g h$, so using the result for the pressure difference that we obtained previously gives:
\begin{equation}u_0=\sqrt{\frac{2gh}{1-A^2/B^2}}.\end{equation}
If we know the ratio of the two cross-sectional areas, then by measuring height $h$ in the fluid column we may determine the flow speed through the narrow part of the pipe.

````{exercise}

Water flows along a horizontal pipe, through a contraction and out into the atmosphere, as shown. Given that the volumetric flow rate is $Q$, estimate the maximum height $h$ for which water can be drawn into the main flow from a lower reservoir that is open to the atmosphere.

<br>

```{image} navstok_img/reservoir.png
---
name: reservoir
alt: a particle moving through a potential field
align: center
scale: 80%
---
```
<br>
````

```{toggle}
Taking the speed of the fluid on a central streamline to be $u_A,u_B$ at $A,B$, mass conservation gives

\begin{equation*}u_A=\frac{Q}{A}, \quad u_B=\frac{Q}{B}\end{equation*}

Taking the pressure to be $p_A,p_B$ at $A,B$, Bernoulli's theorem for the central streamline gives

\begin{equation*}p_B+\frac{1}{2}\rho u_B^2=p_A+\frac{1}{2}\rho u_A^2\end{equation*}

And Bernoulli's equation for particles drawn from the reservoir gives

$p_0=p_A+\rho g h$

where $p_0$ is atmospheric pressure, and we also have $p_0=p_B$ since the pipe is open at $B$.

Combining the equations gives the result

\begin{equation*}h=\frac{Q^2}{2g}\left(\frac{1}{A^2}-\frac{1}{B^2}\right)\end{equation*}
```


### A rotating bucket

Consider an ideal fluid of zero viscosity, rotating under gravity $g$ about the $z$ axis with constant angular velocity $\Omega=\dot{\theta}$.
The particle paths for this motion satisfy
\begin{equation}x=r\cos(\theta), \quad y=r\sin(\theta),\quad z=\mathrm{constant,}\end{equation}
where $\dot{r}=0$ and $\dot{\theta}=\Omega$. From these results we may obtain the velocity field relative to Cartesian axes:
\begin{equation}\dot{x}=-\dot{\theta}r\sin(\theta)=-\Omega y, \quad \dot{y}=\dot{\theta}r\cos(\theta)=\Omega x \quad \Rightarrow \underline{u}=\Omega(-y,x,0).\end{equation}
This is an example of vortex flow. You are encouraged to verify that the vorticity for this fluid is $\omega$ and that the flow is divergence-free. Verify also that $\dot{\underline{u}}=\underline{0}$ and so the streamlines are the same as the particle paths.

Bernoulli's equation {eq}`bernoulli` applies on a streamline, but the constant of integration varies from streamline to streamline since the flow is not irrotational. Therefore solving the equation for $h$ in terms of $x,y$ and $p_0$ will not give us the shape of the fluid surface. If you try this, it would suggest that the shape of the fluid surface is an upturned parabola, which is exactly the opposite of what we observe when we spin a bucket!

To find the fluid surface, we can go back to Euler's formula, which applies throughout the fluid, not only on a streamline:
\begin{equation}\frac{\partial \underline{u}}{\partial t}+\underline{u}.\nabla\underline{u}=-\frac{1}{\rho}\nabla p+\underline{f}, \qquad \underline{f}=(0,0,-g)\end{equation}

````{exercise}
:label: bucket-exercise
Substitute in the velocity field $\underline{u}=\Omega(-y,x,0)$ and solve for each component to deduce the result
```{math}
z =\frac{p_0-p}{\rho g} + \frac{\Omega^2}{2g}(x^2+y^2), \qquad p_0=p(0,0,0).
```
````

```{toggle}
Substituting into the equation gives

\begin{align*}
-\Omega^2 x &=-\frac{1}{\rho}\frac{\partial p}{\partial x} \quad \Rightarrow \quad p=\rho\Omega^2\frac{x^2}{2}+C_1(y,z)\\
-\Omega^2 y &=-\frac{1}{\rho}\frac{\partial p}{\partial y}\quad \Rightarrow \quad p=\rho\Omega^2\frac{y^2}{2}+C_2(x,z)\\
0 &=-\frac{1}{\rho}\frac{\partial p}{\partial z}-g \quad \Rightarrow \quad p=C_3(x,y)-\rho g z
\end{align*}

For consistency, we have
\begin{equation*}p=\frac{\rho \Omega^2}{2}(x^2+y^2)-\rho g z+p_0,\end{equation*}

which rearranges to give the claimed result for $z$
```

From this relationship, we can see that the constant pressure surfaces are parabolic, and we can also calculate the height of streamlines on a given pressure surface. The plot below shows the pressure surface and streamlines for $p=p_0$. The velocity field is also shown on the plot.

<br>

```{image} navstok_img/bucket.png
---
name: bucket
alt: a particle moving through a potential field
align: center
scale: 60%
---
```
<br>

```{exercise}
Produce a figure similar to the one above, by plotting the vector field, streamlines and isosurface in Python. You can take arbitrary values for $p_0,\Omega,\rho,g$, since they do not affect the shape.
```
