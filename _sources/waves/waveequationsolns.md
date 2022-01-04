# Solutions to the Wave Equation

The wave equation interestingly is a rare example of a partial differential equation (PDE) which exhibits 
fairly simple solutions, despite its complexity (in general PDEs are quite difficult to solve exactly).  

## Analysis of the Wave Equation PDE

One way to find solutions is to rewrite the wave equation in a factorised form (by analogy to the difference of two squares)

```{math}
\frac{\partial^2 u}{\partial t^2} - c^2 \frac{\partial^2 u}{\partial x^2 } = 0 \Rightarrow 
\left(\frac{\partial }{\partial t} - c \frac{\partial}{\partial x}\right)\left( \frac{\partial }{\partial t} + c\frac{\partial }{\partial x}\right)u = 0
``` 
which we can rewrite in terms of an intermediate variable $v$:
```{math}
:label: uPDE
\frac{\partial u}{\partial t} + c \frac{\partial u}{\partial x} = v 
```
```{math}
:label: vPDE
\frac{\partial v}{\partial t} - c\frac{\partial v}{\partial x} = 0 
```
The form of Equation {eq}`vPDE` suggests that we can write $v = v(y)$, where $y = y(x,\,t)$, meaning that
```{math}
:label: yODE
\frac{\mathrm{d} v}{\mathrm{d} y}  \left(\frac{\partial y}{\partial t} - 
c \frac{\partial y}{\partial x}\right)= 0
``` 
which can be satisfied by $y = x + ct$ and so $v = v(x + ct)$.  Solving Equation {eq}`uPDE`, which is now a sourced PDE:
```{math}
\frac{\partial u}{\partial t} + c \frac{\partial u}{\partial x} = v(x+ct)
```
The function $u$ here will have a homogeneous and an inhomogeneous part:
```{math}
u = u_h + u_{PI}
```
We find $u_h$ satisfies:
```{math}
:label: uhPDE
\frac{\partial u_h}{\partial t} + c \frac{\partial u_h}{\partial x} = 0 
```
which we can write as $u_h(z)$, where $z  = z(x,\,t)$, meaning that
```{math}
\frac{\mathrm{d} u_h}{\mathrm{d} z}  \left(\frac{\partial z}{\partial t} + 
c \frac{\partial z}{\partial x}\right)= 0
``` 
which can be satisfied by $z = x - ct$ and so $u_h = u_h(x - ct)$.  For $u_{PI}$ we can see that:
```{math}
\frac{\partial u_{PI}}{\partial t} + c \frac{\partial u_{PI}}{\partial x} = v(x+ct)
```
and through a similar process as Equation {eq}`yODE`, we can show that that $u_{PI} = u_{PI}(x+ct)$.  

The general solution to the wave equation is therefore:
```{math}
:label: WEfuncform
u(t,x) = A(x+ ct) + B(x - ct) 
```
where $A,\,B$ are functions that we still have not yet found.

We call these <b>travelling wave</b> solutions and we can interpret these two functions as left and right
 moving wave solutions here, to see how consider the functions first at $t = 0$:
```{math}
u(x,0) = A(x) + B(x)
```
if we now move to a time $t \rightarrow 1$, then the function has the form:
```{math}
u(x,1) = A(x + c) + B(x - c)
```
For $u(t,x)$ to stay invariant under this change:
- For the $A$ function, $x \rightarrow x - c $, suggesting it is a <b> left moving wave</b>.
- For the $B$ function, $x \rightarrow x + c$ suggesting it is a <b> right moving wave</b>. 

## Separable Ansatz for Wave Equation PDE

Although this analysis gives us the functional dependence of the functions $A,\,B$, it does not narrow down 
their form.  We can however use the fact that the PDE is also separable into two ODEs to solve here, our 
ansatz for the form of $u$:
```{math}
u(t,x) =  f(x)\,g(t)
```
Plugging this into the different sides of the wave equation, we find two ODEs result:
```{math}
u_{xx} &=&\,  \frac{\mathrm{d}^2 f}{\mathrm{d} x^2}\,g(t) \\
u_{tt} &=&\,  f(x)\,\frac{\mathrm{d}^2 g}{\mathrm{d} t^2}
```
this allows us to separate out the variables of the wave equation, which we will write in the form:
```{math}
\frac{c^2}{f}\frac{\mathrm{d}^2 f}{\mathrm{d} x^2} = \frac{1}{g}\frac{\mathrm{d}^2 g}{\mathrm{d} t^2} 
```
These two equations are also <em> equal to a constant</em>.  How? Well the LHS here does not vary when we 
change variable $t$, so the right hand side cannot either! Equally the RHS does not vary when changing 
variable $x$, so the LHS cannot either - meaning there is no dependence on $x,\,t$ on either side, 
making them both equal to the same constant.  

We are free to pick whichever constant we like here, but lets choose a negative value $-a^2,\, a\in \mathbb{R}$.  
Picking the constant is mathematically arbitrary, but for physical oscillating solutions, we <em>need</em> a negative constant.
```{math}
\frac{c^2}{f}\frac{\mathrm{d}^2 f}{\mathrm{d} x^2} &=&\,  -a^2 \\ 
\frac{1}{g}\frac{\mathrm{d}^2 g}{\mathrm{d} t^2} &=&\,  -a^2
```
We can solve for $f(x)$ equation to find:
```{math}
f(x) = A\,\exp\left(\frac{iax}{c}\right) + B\,\exp\left(-\frac{iax}{c}\right)
```
We can do the same with $g(t)$:
```{math}
g(t) = C\,\exp(iat) + D\,\exp(-iat)
```
and putting these together means we have:
```{math}
u(x,\,t) \,&&= AC\,\exp\left(\frac{ia}{c}(x + ct)\right)+ BD\,\exp\left(-\frac{ia}{c}(x + ct)\right)  \\
 && + AD\,\exp\left(\frac{ia}{c}(x - ct)\right) + BC\,\exp\left(-\frac{ia}{c}(x - ct)\right) 
```
where we have grouped together the first two terms as the left hand moving wave solutions and last term terms
as the right hand moving wave solutions, which matches the functional form of Equation {eq}`WEfuncform`.

One thing we should try to take care about when writing functions like this is to endure that the 
arguments of the functions are dimensionless - consider the function $f(x) = e^x$ where $x$ is a length, 
if we look at the Maclaurin expansion:
```{math}
f(x) = e^x = 1 + x + x^2 + x^3 + \dots
```
adding a dimensionless number to a length to an area to a volume really is meaningless!  Therefore 
we should really write functions in the form:
```{math}
f(x) = e^{x/a} = 1 + \frac{x}{a} + \left(\frac{x}{a}\right)^2 + \left(\frac{x}{a}\right)^3 + \dots
```
which in each case has a dimensionless quantity being manipulated and $a$ carries the same units as $x$.

So lets rewrite $u(x,\,t)$ in the form:
```{math}
:label: fullwaveeqnsoln1
u(x,\,t) \, && =  AC \exp\left(i(kx + \omega t)\right) + BD\exp\left(-i(kx + \omega t)\right) \\
&& + AD \exp\left(i(kx - \omega t)\right) + BC\exp\left(-i(kx - \omega t)\right)
```
where $k$ is a quantity with units $[\textrm{length}]^{-1}$ and $\omega$ is a quantity with units 
$[\textrm{time}]^{-1}$.  We can make this change, with no less of 
generality, as we have not fixed a value of  constant $a$ previously and also because it is a 
more useful way to understand wave behaviour.

We can reduce the form of these wave solutions further, consider the addition of two complex exponentials:
```{math}
f(x) = A e^{ix} + B e^{-ix} = (A+B)\cos(x) + i(A-B)\sin(x)
```
since we know through trigonometric angle identites that:
```{math}
\cos(x-\phi) = \cos(x)\cos(\phi) + \sin(x)\sin(\phi)
```
and therefore we can make the association:
```{math}
i(A - B)\, && = \sin(\phi) \\
A + B \,&& = \cos(\phi) \\
 \Rightarrow \tan(\phi) \,&& = i\frac{A-B}{A+B}
```
and therefore we can write:
```{math}
f(x) &=& \,\cos(x - \phi) \, = \, \mathrm{Re}\left[e^{i(x-\phi)}\right] \\
\, &=&\, \mathrm{Re}\left[e^{-i\phi}e^{ix}\right] = \mathrm{Re}\left[A'e^{ix}\right]
``` 
where $A'$ is some constant to be found.  So if we use the condition that we will eventually just take the real parts 
of our complex solutions, it dramatically simplifies the form of the equations.  We call writing our complex solutions
of oscillating functions in this way the <b>phasor</b> representation.

Therefore we rewrite Equation {eq}`fullwaveeqnsoln1`:
```{math}
:label: fullwaveeqnsoln
u(x,\,t) =  A' \exp\left(i(kx + \omega t)\right) + B' \exp\left(i(kx - \omega t)\right) 
```
where $A',\, B'$ are constants to be found.

## Features of Wave Solutions
Lets examine these quantities $k,\, \omega$ a little more closely too, start with a right travelling wave $u$:
```{math}
u(x,\,t) = u_0 \,\exp\left(i(kx - \omega t)\right)
```
where $u(x=0,\, t=0) = u_0$.  

If we shift $t \rightarrow t + 2\pi/\omega$, then we see that $u(x,\,t)$ remains invariant, due to the 
periodic nature of $e^{i\omega t}$.  This suggests that $2\pi/\omega$ is the <b> time period </b> of the 
waves oscillation $T = 2\pi/\omega$ and in fact it is clear that $\omega = 2\pi/T = 2\pi f$ 
is just the angular frequency of the wave.  

Likewise if we shift $x \rightarrow x + 2\pi/k$, then $u(x,\,t)$ remains invariant, due to the periodic nature 
of $e^{i k x}$ and this suggests that $2\pi/k$ is the <b> wavelength </b> of the wave, hence 
$k = 2\pi/\lambda$.  This is known as the <b> wave vector </b> of the wave.  

Although it seems strange that a scalar quantity is being called a vector, this is only true in the one 
dimensional case, for a right travelling wave propagating in three dimensions:
```{math}
{\bf u}(x,\,t) = {\bf u_0} \exp\left(i(\bf{k}\cdot\bf{x} - \omega t)\right)
```
where ${\bf k},\, \,{\bf u},\, {\bf u_0}$ are now vector quantities, with ${\bf k} = (k_x,\, k_y,\, k_z),\ {\bf x} = (x,\, y,\, z)$, and 
$k = |\bf{k}| = 2\pi/\lambda$.  ${\bf u_0}$ is known as the waves <b>Polarisation Vector</b> (more on this later).

The quantity $\Phi = kx-\omega t$ is often known as the <b> phase </b> of the wave and comparing these 
between two travelling waves $|\Phi_1 - \Phi_2|$ allows us to look at the <b> phase difference </b> 
between waves, which is important in phenomena such as interference.  All of these considerations also apply to left 
hand moving waves also.
