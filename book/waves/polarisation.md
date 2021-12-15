# Polarisation of Waves

In our discussion of transverse waves, we outlined that the direction of propogation is perpendicular to the direction of oscillation. In a two dimensional system 
this means we could align a wave along the $(x,\,y)$ axes, however if we look at three dimensions we see this leaves an ambiguity as <em> any </em> oscillation 
orientation in the $(y,\,z)$ plane is perpendicular to a wave propogation along the $x$ axis.  The proces of fixing the specific geometric orientation is known 
as the wave <b> Polarisation. </b>  

```{figure} ../figures/WavePolarisation.png
---
name: WavePolarisation
---
Schematic of two different wave polarisations in the $y$ (red wave) or $z$ (blue wave) axes, with wave propogating along the $x$ axis.
```

As {numref}`WavePolarisation` shows, we can make different choices for the orientation and many materials have the property of being able to filter out or 
rotate the plane of plane polarised light.  But what is the mathematical description of such a phenomena?  Lets go back to a travelling wave in three dimensions:

```{math}
{\bf u}(x,\,t) = {\bf u_0} \,\exp\left(i({\bf k}\cdot {\bf x} - \omega t)\right)
```
where ${\bf u_0}$ is known as the wave polarisation vector.  The orentiation of ${\bf k}$ specifies the direction of progation and ${\bf u_0}$ specifies the 
direction of oscillation, such that:
```{math}
{\bf k} \cdot {\bf u_0} = 0
```
if we for instance align a wave to propogate along the $x$ axis, then we find:
```{math}
\begin{bmatrix}
k_x \\
0 \\
0
\end{bmatrix} \cdot \begin{bmatrix}
0 \\
u_y \\
u_z 
\end{bmatrix} = 0
```
If we pick one of $u_y,\, u_z$ to be zero also, then the waves are confined to the $z,\, y$ axes repsectively, giving a <b> Linear </b> polarisation.  This condition is 
not the only solution though, for both $u_y,\, u_z$ non-zero, these waves can have an alternative polariation state, that of <b> Circular </b> or <b> Elliptical </b> 
polarisation, as shown in {numref}`CircPolarisation`.

```{figure} ../figures/CircPolarisation.png
---
name: CircPolarisation
---
Schematic of two different types of wave polarisations, plane polarisation in green and blue and circular polarisation in red.
```

If we take the triple vector product of the wave vector and polarisation vector, we find a vector ${\bf S}$ which indicates the flow of energy in the system:
```{math}
{\bf u_1} &=&\, {\bf k} \times {\bf u_0} \\
{\bf S} &=&\, C\,{\bf u_0} \times {\bf u_1} 
``` 
where $C$ is some constant to be found.  To understand how this works, lets pick a choice of linearly polarised placen waves:
```{math}
{\bf k} = \begin{bmatrix}
k_x \\
0 \\
0
\end{bmatrix}\quad \quad
{\bf u_0} = \begin{bmatrix}
0 \\
u_y \\
0 
\end{bmatrix}
```
then the components of ${\bf S}$ are found by:
```{math}
{\bf u_1} &=&\, {\bf k} \times {\bf u_0} = \begin{vmatrix}
\hat{\bf x} & \hat{\bf y} & \hat{\bf z}\\
k_x & 0 & 0 \\
0 & u_y & 0
\end{vmatrix} = k_x\,u_y\,\hat{\bf z}\\
{\bf S} &=&\, {\bf u_0} \times {\bf u_1} = C\begin{vmatrix}
\hat{\bf x} & \hat{\bf y} & \hat{\bf z}\\
0 & u_y & 0 \\
0 & 0 & k_x\,u_y
\end{vmatrix} = C\,k_x\,(u_y)^2\,\hat{\bf x}\\
```
which indicates that energy flows along the $x$ axis - in the same direction as the wave propogration and with a magntiude 
$S = |{\bf S}| = C\,k_x\,(u_y)^2 = E_\lambda$ which from Equation {eq}`energywavelength` gives $C = \pi\,c^2\,\rho_L$.