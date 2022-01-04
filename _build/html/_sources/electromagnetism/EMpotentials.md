# Electromagnetic Scalar and Vector Potentials

There is a different way to view these equations of electromagnetism, using the rules of vector calculus. Lets begin simply by expressing the 
electric field ${\bf E}$ in terms of a potential:
```{math}
:label: electricpotential1
{\bf E} = -\nabla \phi
```
where $\phi = \phi(x,\,y,\,z)$ is the scalar electric potential.  Gauss's law $\nabla\cdot {\bf E} = \rho/\epsilon_0$ means this now forms a Poisson equation:
```{math}
\nabla^2\phi = -\frac{\rho}{\epsilon_0}
```
However the issue with Equation {eq}`electricpotential1` is that it lacks are time dependence, which to solve Faraday's law 
$\nabla \times {\bf E} = -\partial {\bf B}/\partial t$ can cause issues:
```{math}
\nabla \times {\bf E} = -\nabla \times \nabla \phi = 0 
```
where this result stems simply from vector calculus identities.  Therefore in order to solve problems with time dependence, we must add a vector potential ${\bf A}$:
```{math}
{\bf E} = -\nabla \phi - \frac{\partial {\bf A}}{\partial t}
```
Substituting this into Faraday's law now results in:
```{math}
\nabla \times {\bf E} = -\nabla \times \nabla \phi - \nabla \times \frac{\partial {\bf A}}{\partial t} = 
0 - \frac{\partial}{\partial t}\left(\nabla \times {\bf A}\right) = - \frac{\partial {\bf B}}{\partial t}
```
which neatly suggests that:
```{math}
{\bf B} = \nabla \times {\bf A}
```
which again through vector calculus identities satisfies $\nabla \cdot {\bf B} = 0$.  If we re-examine Gauss's and Ampère's law's in light of these additions we find:
```{math}
\nabla \cdot {\bf E} &=& \,-\frac{\partial}{\partial t}\left( \nabla \cdot {\bf A}\right) - \nabla^2\phi = \frac{\rho}{\epsilon_0}\\
\nabla \times {\bf B} &=&\, \nabla \left( \nabla \times {\bf A} \right) = \mu_0 {\bf J} + \mu_0 \epsilon_0 \frac{\partial {\bf E}}{\partial t} \\ 
&=& \,\mu_0 {\bf J} - \mu_0 \epsilon_0 \frac{\partial}{\partial t} \nabla \phi - \mu_0 \epsilon_0 \frac{\partial^2 {\bf A}}{\partial t^2}
```
which we can rearrange, collect together terms and use vector identities to find a modified wave equation:
```{math}
\frac{1}{c^2}\frac{\partial^2 {\bf A}}{\partial t^2} = 
\nabla^2 {\bf A} - \nabla \left(\nabla \cdot {\bf A} + \frac{1}{c^2}\frac{\partial \phi}{\partial t} \right) + \mu_0 {\bf J}
```
These two sets of equations are non-trivial to solve for $\phi$ and ${\bf A}$. There are however a number of symmetries in this system of equations, 
one is that we can shift the parameters $\phi,\,{\bf A}$ by functions of space and time and see what equations these should satisfy:
```{math}
{\bf A} &\rightarrow&\, {\bf A} + \alpha({\bf x},\,t) \\
\phi &\rightarrow&\, \phi + f({\bf x},\,t)
```
where $f$ is a scalar shift and $\alpha$ is a vector shift.  If these shifts are to be symmetries of the electromagnetic equations, 
then they should NOT change the electric and magnetic fields overall, which means that:
```{math}
{\bf E} & \rightarrow& -\frac{\partial}{\partial t}\left( {\bf A} + \alpha\right) - \nabla(\phi + f) = {\bf E} - \frac{\partial \alpha}{\partial t} - \nabla f \\
{\bf B} & \rightarrow& \nabla \times \left( {\bf A} + \alpha\right) = \nabla {\bf A} + \nabla \times \alpha = {\bf B} + \nabla \times \alpha 
```
and hence for unchanged fields, we must simultaneously satisfy:
```{math}
\nabla \times \alpha &=&\, 0 \\
\frac{\partial \alpha}{\partial t} + \nabla f &=&\, 0
```
Given that we can write an vector field with vanishing curl as a gradient of a scalar, 
```{math}
\alpha = \nabla \lambda
```
this means our second condition has the form
```{math}
\nabla f = -\frac{\partial \alpha}{\partial t} = -\nabla \left(\frac{\partial \lambda}{\partial t} \right)
```
which we can rewrite our initial transformations in terms of 
```{math}
{\bf A} & \rightarrow&\, {\bf A} + \nabla \lambda\\
\phi &\rightarrow&\, \phi - \frac{\partial \lambda}{\partial t}
```
Despite these transformations leaving ${\bf E},\,{\bf B}$ unchanged, the equations for Gauss's and Ampères law are not invariant, since $\nabla \cdot {\bf A}$ 
is still unconstrained.  Thus we can use different choices of $\phi$ and ${\bf A}$ here to simplify solving these.  These different choices are known as 
<b>Gauge Choices</b>.

Writing electromagnetism in this way allows for quantum ideas and conceptual issues within these theories to be seen as physical effects, 
one way these are seen physically is through the Aharonov-Bohm (AB) effect.  For more information on the AB effect, check out 
[these DAMTP notes](https://www.damtp.cam.ac.uk/user/tong/qhe/qhe.pdf).
