(ch_rotfram)=
# Rotational reference frames

This section of the notes is based on Chapter 17 of {cite}`classmech`, which is available in digitised form from UCL library. The material is concerned with relativistic transformation of Newton's second law of motion from an inertial frame of reference to a rotating frame of reference, such as the frame of the rotating Earth. It introduces the important idea of the *Coriolis force*, which influences large scale fluid motions on the Earth surface, such as ocean currents. The Coriolis force can be neglected in all of the scenarios that we will consider in this course.

 ```{admonition} Hurricanes
 :class: theorem
 A neat video explanation of how the Coriolis force determines the direction of hurricanes in the North and South hemisphere can be found at
 [National Geographic](https://www.nationalgeographic.org/encyclopedia/coriolis-effect/)

 Note: it is popularly thought that the same effect causes bathtub vortices to drain in different directions in the North and South hemispheres, but on this small scale the Coriolis forces involved are insignificant compared with other sources of fluid disturbance. To demonstrate the Coriolis effect in a bathtub would require a very large tub containing very still water that is then drained through a very small hole under very controlled conditions. The experiment has been [done](https://www.nature.com/articles/2071084a0.pdf)!

 For the same reason, the direction of rotation of a tornado is not due to the Coriolis effect. Tornadoes are relatively small in size compared to hurricanes. Tornadoes typically due to a strong shear wind gradient, which creates a line of vortices rotating about an axis parallel to the ground. The vortex line is then tilted upwards and stretched by warm updrafts.
 ```

## It's all a matter of perspective

In the image below, $\mathcal{F}$ and $\mathcal{F}^{\prime}$ are two different frames of reference, which are in relative motion. Each frame is defined by its own origin and vector basis, $\mathcal{F}:\{O;\underline{e}_1,\underline{e}_2,\underline{e}_3\}$ and  $\mathcal{F}^{\prime}:\{O^{\prime};{\underline{e}_1}^{\prime},{\underline{e}_2}^{\prime},{\underline{e}_3}^{\prime}\}$. We take $\mathcal{F}$ to be a fixed ("true") frame, and suppose that frame $\mathcal{F}^{\prime}$ is embedded in a rigid body $\mathcal{B}^{\prime}$, which is moving with translational velocity $\underline{V}$ and angular velocity $\underline{\Omega}$ relative to $\mathcal{F}$, as shown.

<br>

```{image} navstok_img/rot_frame.png
---
name: rotational reference frame
alt: alternative description
align: center
scale: 60%
---
```
<br>

We now consider the motion of an arbitrary point $P$ as measured by an observer within each frame. We will take $\underline{r}$ to be the position of the point relative to frame $\mathcal{F}$ and $\underline{r}^{\prime}$ to be the position relative to frame $\mathcal{F}^{\prime}$. According to the triangle law for vectors, we may then write

\begin{equation}\underline{r}=\underline{D}+\underline{r}^{\prime},\end{equation}

in which $\underline{D}$ is the position vector of $O^{\prime}$ relative to frame $\mathcal{F}$. Differentiating this expression gives the rate of change of position of point $P$. We will examine the change from the perspective of frame $\mathcal{F}$, as indicated by the subscript in the expression below:

```{math}
:label: rotfram1
\left(\frac{\mathcal{d}\underline{r}}{\mathcal{d}t}\right)_{\mathcal{F}}=
\left(\frac{\mathcal{d}\underline{D}}{\mathcal{d}t}\right)_{\mathcal{F}}+
\left(\frac{\mathcal{d}\underline{r}^{\prime}}{\mathcal{d}t}\right)_{\mathcal{F}}.
```

The term on the left is the velocity of $P$ seen by an observer in frame $\mathcal{F}$. The first term on the right is the translational velocity of body $\mathcal{B}^{\prime}$. The second term on the right is a little more complicated, because vector $\underline{r}^{\prime}$ was defined relative to frame $\mathcal{F}^{\prime}$ but the time derivative is taken with respect to frame $\mathcal{F}$. We must account for the fact that the basis vectors in $\mathcal{F}^{\prime}$ are *changing* relative to frame $\mathcal{F}$, due to the angular rotation of body $\mathcal{B}^{\prime}$. Seen from the perspective of frame $\mathcal{F}$, the basis vectors satisfy

\begin{equation}\left(\frac{\mathrm{d}{\underline{e}_j}^{\prime}}{\mathrm{d}t}\right)_{\mathcal{F}}=\underline{\Omega}\times{\underline{e}_j}^{\prime}\end{equation}

and hence for a general vector $\underline{h}={h_1}^{\prime}{\underline{e}_1}^{\prime}+{h_2}^{\prime}{\underline{e}_2}^{\prime}+{h_3}^{\prime}{\underline{e}_3}^{\prime}$
we have the following result :
\begin{align}\left[\frac{\mathrm{d}\underline{h}^{\prime}}{\mathrm{d}t}\right]_{\mathcal{F}}&=\left[(\dot{h_1}^{\prime}{\underline{e}_1}^{\prime}+\dot{h_2}^{\prime}{\underline{e}_2}^{\prime}+\dot{h_3}^{\prime}{\underline{e}_3}^{\prime})+({h_1}^{\prime}\dot{\underline{e}_1}^{\prime}+{h_2}^{\prime}\dot{\underline{e}_2}^{\prime}+{h_3}^{\prime}\dot{\underline{e}_3}^{\prime})\right]_{\mathcal{F}}\\
&=\left[\frac{\mathrm{d}\underline{h}^{\prime}}{\mathrm{d}t}+(\underline{\Omega}\times\underline{h}^{\prime})\right]_{\mathcal{F}^{\prime}}.\end{align}

Putting this together with result {eq}`rotfram1` we obtain

\begin{equation}\underline{v}=\underline{V}+\underline{v}^{\prime}+(\underline{\Omega}\times\underline{r}^{\prime}),\end{equation}

where $\underline{v}$ is the velocity measured in frame $\mathcal{F}$ and $\underline{v}^{\prime}$ is the velocity measured in frame $\mathcal{F}^{\prime}$. Differentiating this expression again gives a result for the acceleration:

\begin{equation}\left[\frac{\mathrm{d}\underline{v}}{\mathrm{d}t}\right]_{\mathcal{F}}=\left[\frac{\mathrm{d}\underline{V}}{\mathrm{d}t}\right]_{\mathcal{F}}+\left[\frac{\mathrm{d}}{\mathrm{d}t}\biggr(\underline{v}^{\prime}+(\Omega\times\underline{r}^{\prime})\biggr)\right]_{\mathcal{F}^{\prime}}+\Omega\times\biggr(\underline{v}^{\prime}+(\Omega\times\underline{r}^{\prime})\biggr),\end{equation}

which simplifies to

\begin{equation}\underline{a} =\underline{A}+\underline{a}^{\prime}+(\dot{\underline{\Omega}}\times\underline{r}^{\prime})+2(\underline{\Omega}\times\underline{v}^{\prime})+\underline{\Omega}\times(\underline{\Omega}\times\underline{r}^{\prime})\end{equation}
in which $\underline{a}$, $\underline{a}^{\prime}$ are the accelerations observed in each frame and $\underline{A}$ is the translational acceleration of $\mathcal{F}^{\prime}$.

## Transformation of Newton's law

Recall that Newton's second law $\underline{F}=m\underline{a}$ was defined for an inertial frame of reference. If the displacement, velocity and acceleration are measured from the perspective of our rotational frame of reference, the law becomes

\begin{equation}\underline{F}=m\biggr[\underline{A}+\underline{a}^{\prime}+(\dot{\underline{\Omega}}\times\underline{r}^{\prime})+2(\underline{\Omega}\times\underline{v}^{\prime})+\underline{\Omega}\times(\underline{\Omega}\times\underline{r}^{\prime})\biggr].\end{equation}

The result can be rearranged in the manner

\begin{equation}m\underline{a}^{\prime}=\underline{F}+(-m\underline{A})+(-m\dot{\underline{\Omega}}\times\underline{r}^{\prime})+(-2m\underline{\Omega}\times\underline{v}^{\prime})+(-m\underline{\Omega}\times(\underline{\Omega}\times\underline{r}^{\prime})),\end{equation}

which resembles the standard Newton's second law with the addition of extra terms; which are described as "fictitious forces". The term $(-2m\underline{\Omega}\times\underline{v}^{\prime})$ is known as the Coriolis force, and the term $(-m\underline{\Omega}\times(\underline{\Omega}\times\underline{r}^{\prime}))$ is known as the Centripetal force.

*Note: the semantic distinction of what is "actual" and what is "fictitious" is made purely so that Newton's law holds in its inertial form.*

**Example**

Consider a person walking at constant speed towards the centre of a roundabout that is rotating at constant angular velocity $\Omega$, as illustrated below:

<br>

```{image} navstok_img/roundabout.png
---
name: a person on a roundabout
alt: alternative description
align: center
scale: 70%
---
```
<br>

The origin of reference frame $\mathcal{F}^{\prime}$ is stationary with respect to the inertial frame $\mathcal{F}$, so $\underline{A}=0$ in the transformed Newton's law. The roundabout is rotating at constant angular velocity, so $\dot{\underline{\Omega}}=0$. The person is not accelerating from the perspective of frame $\mathcal{F}^{\prime}$, so $\underline{a}^{\prime}=0$.

We have $\underline{\Omega}=\Omega{\underline{e}_3}^{\prime}$ and $\underline{v}^{\prime}=-V{\underline{e}_1}^{\prime}$. For the displacement we may write $\underline{r}^{\prime}=(R-Vt){\underline{e}_1}^{\prime}$ where $R$ is the radius of the roundabout and $t$ is the time since the person started their motion.

Let $\underline{X}$ be the force exerted by the roundabout on the person. The total force on the person is therefore given by $\underline{X}-mg{\underline{e}_3}^{\prime}$ and the transformed Newton's law gives

\begin{align*}\underline{X}-mg{\underline{e}_3}^{\prime} &= 2m(\underline{\Omega}\times\underline{v}^{\prime})+m(\underline{\Omega}\times(\underline{\Omega}\times\underline{r}^{\prime}))\\\Rightarrow\quad \underline{X}&=-m(R-Vt)\Omega^2{\underline{e}_1}^{\prime}-2m\Omega V{\underline{e}_2}^{\prime}+mg{\underline{e}_3}^{\prime}\end{align*}

The reaction forces to the left and to the centre oppose the Coriolis and centripetal forces, respectively. Since the person is not a point, they must also lean forward and to the left to counter these two forces.

(rotfram-navstok)=
## Application to the Navier-Stokes equations

Treating the Earth as a uniformly rotating body with angular velocity $\underline{\Omega}$ gives

\begin{equation}\left(\frac{\mathrm{D}\underline{u}}{\mathrm{D}t}\right)_{\mathcal{F}}=\left(\frac{\mathrm{D}\underline{u}}{\mathrm{D}t}\right)_{\mathcal{F}^{\prime}}+2(\underline{\Omega}\times\underline{u})+\underline{\Omega}\times(\underline{\Omega}\times\underline{x}).\end{equation}

Hence, in the Earth frame of reference the conservation of momentum equation becomes

\begin{equation}\frac{\partial \underline{u}}{\partial t}+(\underline{u}.\nabla\underline{u})+\biggr[2(\underline{\Omega}\times\underline{u})+\underline{\Omega}\times(\underline{\Omega}\times\underline{x})\biggr]=-\frac{1}{\rho}\nabla p+\nu \nabla^2\underline{u}\end{equation}

The equation can be simplified by using the following vector identity, which applies when $\underline{\Omega}$ is constant:

\begin{equation}\underline{\Omega}\times(\underline{\Omega}\times\underline{x})=-\nabla\left(\frac{1}{2}(\underline{\Omega}\times\underline{x})^2\right).\end{equation}

By defining a reduced pressure $p_R=p-\frac{1}{2}\rho(\underline{\Omega}\times\underline{x})^2$ we may therefore write  
```{math}
:label: rotfram-navstok-eqn
\frac{\partial \underline{u}}{\partial t}+(\underline{u}.\nabla\underline{u})=-\frac{1}{\rho}\nabla p_R+\nu\nabla^2\underline{u}-2(\underline{\Omega}\times\underline{u}).
```

The term $-2(\underline{\Omega}\times\underline{u})$ is called the Coriolis force.

````{exercise}
The Rossby number is defined by
 ```{math}
 \mathrm{Ro}=\frac{U}{Lf}, \quad f=2\Omega\sin(\phi),
 ```
 where $U$ and $L$ are characteristic velocity and length scales of the phenomenon, $\Omega = 7.2921 × 10^{−5} \mathrm{rad/s}$ is the angular frequency of planetary rotation and $\phi$ is the latitude. The quantity $f$ is called the Coriolis frequency.

 The Rossby measures the ratio of inertial to Coriolis forces. If this number is much smaller than one then Coriolis forces dominate. If the number is much bigger than one then inertial terms dominate. For Rossby numbers close to one, both inertial and Coriolis forces are important.

a. When Hurricane Katrina made landfall in Louisiana at $23.4^{\circ}$N latitude, it was registered a category 3 hurricane, covering a diameter of approximately 400 miles, with wind speeds up to 125mph. Estimate the Rossby number using these values and state which forces would need to be taken into modelling consideration.

b. Are Coriolis forces important near to the equator?

c. Jupiter rotates much faster than the Earth. Do you think that Coriolis forces are more prevalent on Earth or on Jupiter? By looking up the rotation rates of the Earth and Jupiter, calculate the ratio of Coriolis forces on Earth and on Jupiter (at equivalent latitude)

d. Estimate the Rossby number for a bathtub in central London. Use your own estimates for the appropriate length scale and speed of the water!
````

## References

```{bibliography}
:filter: docname in docnames
```
