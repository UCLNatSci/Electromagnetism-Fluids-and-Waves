(sound-waves)=
# Unsteady: Sound waves

**In this section:**

* Derivation of the 3D wave equation from linearised conservation of mass and momentum
* How the speed of sound arises from a linear relationship between pressure and density
* Under what conditions can we safely treat a fluid as incompressible?


## Sound waves

We begin with the equations of mass and momentum. Crucially, this time we do NOT assume that the fluid is incompressible, but we neglect viscosity. We assume a constant background $p_0, \rho_0$, which is perturbed by a small disturbance $p_1, \rho_1, \underline{u}_1$ so that

```{math}
:label: perturbations
\underline{u}=\underline{u}_1, \qquad
p=p_0+p_1,\qquad
\rho=\rho_0+\rho_1.
```

Linearising the equations of motion means keeping only the terms that are linearly proportional to any of $\underline{u}_1$, $p_1$, $\rho_1$. Nonlinear products of these quantities are assumed to be much smaller. We obtain

```{math}
:label: linearsound
\begin{align}
\frac{\partial \rho}{\partial t}+\nabla.(\rho \underline{u})&=0 \qquad &\Rightarrow && \qquad \frac{\partial \rho_1}{\partial t}+\rho_0\nabla .\underline{u}_1&=0,\\
\rho\left(\frac{\partial \underline{u}}{\partial t}+\underline{u}.\nabla\underline{u}\right)&=-\nabla p \qquad &\Rightarrow && \qquad \rho_0\frac{\partial \underline{u}_1}{\partial t}&=-\nabla p_1.
\end{align}
```

We can take the divergence of the first equation and combine with the second equation to eliminate $\nabla.\underline{u}_1$. This gives

```{math}
:label: lineq
\frac{\partial^2 \rho_1}{\partial t^2}=-\nabla^2 p_1.
```

To obtain the result fully in terms of a single quantity, we consult the Taylor expansion for $p$ about $\rho=\rho_0$, which gives

\begin{align}
p&=p(\rho_0)+(\rho-\rho_0)\frac{\mathrm{d}p}{\mathrm{d}\rho}\biggr|_{\rho=\rho_0}+\dots \\
&= p_0+\rho_1\frac{\mathrm{d}p}{\mathrm{d}\rho}\biggr|_{\rho=\rho_0}+\dots
\end{align}

Thus, we have

\begin{equation}p_1=\rho_1 a_0^2, \qquad a_0^2=\frac{\mathrm{d}p}{\mathrm{d}\rho}\biggr|_{\rho=\rho_0}\end{equation}

We can finally use this result to eliminate $\rho_1$ from {eq}`lineq`, from which we obtain the 3D wave equation for waves travelling with velocity $a_0$ :

```{math}
:label: waveeqn
\frac{\partial^2 p_1}{\partial t^2}=a_0^2\nabla^2 p_1.
```

```{exercise}
It is trivial to show that the pressure $\rho_1$ satisfies {eq}`waveeqn`. It can also be shown that if the flow is irrotational then both the velocity and the velocity potential also satisfy this equation. Can you do it?

Hint: Take the gradient of the first expression in {eq}`linearsound` and use the following vector identity:
\begin{equation*}
\nabla(\nabla.\underline{u})=\nabla^2\underline{u}+\nabla\times(\nabla\times \underline{u})
\end{equation*}
```


```{toggle}
Taking the gradient of the first expression in {eq}`linearsound` gives

\begin{equation*}\frac{\partial}{\partial t}\left(\nabla \rho_1\right)+\rho_0\nabla^2\underline{u}_1+\nabla\times(\nabla\times\underline{u}_1)\end{equation*}

If the flow is irrotational then $(\nabla\times\underline{u})=0$. We can also use the result $p_1=\rho_1 a_0^2$, to obtain

\begin{equation*}\frac{1}{a_0^2}\frac{\partial}{\partial t}\left(\nabla p_1\right)+\rho_0\nabla^2 \underline{u}_1\end{equation*}

Finally, using the result for $\nabla p_1$ from the second expression in {eq}`linearsound` gives

\begin{equation*}\frac{\partial^2 \underline{u}_1}{\partial t^2}=a_0^2\nabla^2\underline{u}_1\end{equation*}

```

The speed at which sound waves travel is found to be

\begin{equation}
a_0=\sqrt{\frac{\gamma p_0}{\rho_0}},
\end{equation}

where $p_0, \rho_0$ are the background pressure and density, and $\gamma$ is constant for the gas in question. The derivation requires some tricky thermodynamics, which uses the first and second laws of thermodynamics, along with the ideal gas law and isentropic assumption. These assumptions were shown by Laplace to produce an estimate for the speed of sound in a gas that closely matches observation. You don't need to know the details of the derivation, but they are given in {numref}`thermal-physics` for anyone interested.


```{admonition} Incompressibility assumption
:class: theorem
From an order of magnitude estimate in {eq}`waveeqn` we can see that the term on the left side scales as $U^2/L^2$ and the term on the right scales as $a_0^2/L^2$, where $U$ and $L$ are characteristic velocity and length scales of motion. Thus, if $U^2 \ll a_0^2$ then the fractional change in pressure due to the fluid motion will be small and will result in little expansion or compression of fluid elements. Incompressible flow theory is aerodynamically useful of the flow speed is much smaller than the speed of sound.
```

### Boundary conditions

There are two types of boundary conditions that are normally given when solving sound wave problems. Either the pressure is specified at the boundary or the velocity is specified at the boundary.

The second case is equivalent to providing the derivative of the pressure at the boundary, using the relationship that we found in {eq}`linearsound` :

\begin{equation}
\frac{\partial p_1}{\partial t}=-\rho_0 \nabla.\underline{u}_1
\end{equation}

```{exercise}
The human ear canal can be modelled as a straight 1D tube between $x=0$ and $x=L$, which is open at the ear lobe end ($x=0$) and closed at the ear drum end ($x=L$). A sound wave in the air surrounding the ear produces a pressure fluctuation $Pe^{-i\Gamma t}$ at the ear lobe end.

Verify that the following results satisfies the equation of motion and use suitable boundary conditions to find expressions for the amplitudes $A$ and $B$
\begin{equation}p_1=Ae^{i\Gamma(x/c-t)}+Be^{-i\Gamma(x/c+t)}\end{equation}
Under what conditions does resonance occur? Find the fundamental resonant frequency, given that the human ear canal is approximately 2.5cm long and that the speed of sound in air is approximately 340ms$^{-1}$.

```

```{toggle}
Differentiating the given expression provides
\begin{equation*}\frac{\partial^2 p_1}{\partial t^2}=-\Gamma^2 p_1, \qquad \frac{\partial^2 p_1}{\partial x^2}=-\frac{\Gamma^2}{c^2} p_1\end{equation*}

Hence,
\begin{equation*}\frac{\partial^2 p_1}{\partial t^2}=c^2\frac{\partial^2 p_1}{\partial x^2}\end{equation*}

This is the 1D wave equation, for wave velocity $c$.

**Boundary conditions:**

Closed end : $u(L)=0 \quad \Rightarrow \frac{\partial p_1}{\partial t}\biggr|_{x=L}=0$

Open end: $p(0)=P e^{-i\Gamma t}$

Applying these conditions gives:

\begin{equation*}A+B=P, \quad Ae^{i\Gamma L/c}-Be^{-i\Gamma L/c=0}\end{equation*}

Solving the two equations together gives

\begin{equation*}A=\frac{Pe^{-i\Gamma L/c}}{\cos(\Gamma L/c)}, \quad B=-\frac{Pe^{-i\Gamma L/c}}{\cos(\Gamma L/c)}\end{equation*}

Resonance occurs when $\cos\left(\frac{\Gamma L}{c}\right)=0$, i.e when $\Gamma=\frac{(2n-1)\pi c}{2L}$, where $n$ is a natural number.

The fundamental (angular) response frequency is $\Gamma= \frac{\pi c}{2L}$.

Taking $L=2.5\times 10^{-2}\mathrm{m}$ and $c=340\mathrm{ms}^{-1}$ gives

\begin{equation*}f=\frac{\Gamma}{2\pi} = \frac{340}{4\times 2.5\times10^{-2}}=3400\mathrm{Hz}\end{equation*}

In reality the resonant response is not infinite, but it is much greater than at other frequencies. This means that the human ear is particularly sensitive to at frequencies near 3.4kHz. Resonance also occurs at higher harmonic frequencies, but the strength of the response at these frequencies is diminished.

```


## The supersonic airfoil

If the derivation above is repeated for the case of steady two-dimensional flow with uniform background motion $\underline{u}=(U,0,0)$ then the equation of motion reduces to

\begin{equation}
(1-M^2)\frac{\partial^2\phi}{\partial x^2}+\frac{\partial^2\phi}{\partial y^2}=0, \qquad M=\frac{U}{a_0}.
\end{equation}

The quantity $M$ is called the Mach number. If this value is much smaller than smaller than 1, then the result is the solution can be well approximated by taking $M=0$ so that the result reduces to the case of incompressible flow.

The value $M=1$ is a critical value at which the streamlines for the flow take on a different pattern. For values in the range $M\geq 1$ there is no disturbance to the fluid ahead of a cone extending backwards from the leading edge of the airfoil. This is related to the phenomenon of a [sonic boom](https://www.youtube.com/watch?v=JO4_VHM69oI).


(thermal-physics)=
## Speed of sound derivation

*The material in this subsection is optional.*

### Thermal physics

According to the first law of thermodynamics, the total change of internal energy of a system is given by the relationship below, where $\mathrm{d}Q$ is the change in heat energy and $p\mathrm{d}V$ represents work done by pressure:

\begin{equation}
\mathrm{d}U=\mathrm{d}Q-p\mathrm{d}V,
\end{equation}

 The change in heat energy can be related to the change in entropy $\mathrm{d}S$ by the second law of thermodynamics $\mathrm{d}S=\frac{\mathrm{d}Q}{T}$, and the total change of internal energy can be replaced by the change of enthalpy $H=U+pV$ to give

```{math}
:label: entropy
\mathrm{d}S=\frac{1}{T}\mathrm{d}H-\frac{V}{T}\mathrm{d}p.
```

For an ideal gas, the following relationships also hold, in which where $c_p$ is the specific heat capacity at constant temperature and $c_v$ is the specific heat capacity at constant volume:

\begin{equation}pV=nRT, \qquad nR=(c_p-c_v), \qquad c_p=\frac{\mathrm{d}H}{\mathrm{d}T}, \qquad c_v=\frac{\mathrm{d}U}{\mathrm{d}T}\end{equation}

Thus, we can rewrite {eq}`entropy` as

\begin{equation}
\mathrm{d}S=\frac{c_p}{T}\mathrm{d}T-\frac{(c_p-c_v)}{p}\mathrm{d}p.
\end{equation}

For an adiabatic process, there is no change in entropy, $\mathrm{d}S=0$, and so integrating this expression gives

\begin{equation}
c_p\ln(T/T_0)=(c_p-c_v)\ln(p/p_0)
\end{equation}

Finally, by using the relationship $p=\rho R T$ to eliminate $T/T_0$, we may write the result

```{math}
:label: isentropic
p\rho^{-\gamma}=\mathrm{const}, \qquad \gamma=\frac{c_p}{c_v}.
```

The value of $\gamma$ is approximately 1.40 for dry air at atmospheric pressure.

### Small amplitude perturbations

Taking the small perturbation approach used in {eq}`perturbations` and substituting into the isentropic relation {eq}`isentropic` gives

\begin{align}
p\rho^{-\gamma}&=p_0\rho_0^{-\gamma}\left(1+\frac{p_1}{p_0}\right)\left(1+\frac{\rho_1}{\rho_0}\right)^{-\gamma}\\
&=p_0\rho_0^{-\gamma}\left(1+\frac{p_1}{p_0}\right)\left(1-\gamma\frac{\rho_1}{\rho_0}+\dots\right)\\
&=p_0\rho_0^{-\gamma}\left(1+\left(\frac{p_1}{p_0}-\gamma\frac{\rho_1}{\rho_0}\right)+\dots\right)
\end{align}

Since the result should be constant, the first order (linear) approximation shows that

```{math}
:label: soundspeed
\frac{p_1}{p_0}=\gamma\frac{\rho_1}{\rho_0}\quad \Rightarrow p_1=a_0^2\rho_1, \qquad a_0^2=\frac{\gamma p_0}{\rho_0}.
```
