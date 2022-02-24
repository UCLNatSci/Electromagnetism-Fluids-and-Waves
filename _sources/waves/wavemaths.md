# Mathematical Preliminaries

Since waves involve changes in both space and time $u(x,\,t)$, the definitions of first and second partial derivatives in terms of limits
are useful here.  Recall that partial derivatives are found when we have two or more variables that can change and we are interested in 
how the machinery of calculus works in this case.  Partial derivatives typically involve allowing one variable to change whilst keeping 
all other variables constant.

First derivative of a function $u(x,\,t)$ is found from taking the limit:

```{math}
:label: partialderiv
\frac{\partial u(x,\,t)}{\partial x} = \lim_{\Delta x \rightarrow 0} \frac{u(x + \Delta x,t) - u(x,t)}{\Delta x} 
```
Notice that this defintion keeps the variable $t$ constant whilst this limit is taken.  Likewise if we took the $t$ derivative here:
```{math}
\frac{\partial u(x,\,t)}{\partial t} = \lim_{\Delta t \rightarrow 0} \frac{u(x,\,t + \Delta t) - u(x,\,t)}{\Delta t} 
```
The second derivative can be thought of as a derivative of a derivative:
```{math}
\frac{\partial^2 u(x,\,t)}{\partial x^2} &=&\, \frac{\partial}{\partial x}\left(\frac{\partial u(x,\,t)}{\partial x}\right) \\
&=&\, \lim_{\Delta x \rightarrow 0} \frac{1}{\Delta x}\left[\frac{\partial u(x+\Delta x,\,t)}{\partial x} - \frac{\partial u(x,\,t)}{\partial x} \right] \\
&=&\, \lim_{\Delta x \rightarrow 0} \frac{1}{\Delta x}\left[\frac{u(x + 2\Delta x,\,t) - u(x+ \Delta x,\,t)}{\Delta x} - \frac{u(x + \Delta x,\, t) - u(x,\, t)}{\Delta x} \right] \\
```
Which means we can write a second partial derivative using a limit definition as:
```{math}
:label: 2ndpartialderiv
\frac{\partial^2 u(x,\,t)}{\partial x^2} = \lim_{\Delta x \rightarrow 0} \frac{u(x+2\Delta x,t) - 2u(x+\Delta x,t) + u(x,t)}{{\Delta x}^2} 
```

## Binomial Series

It is sometimes useful to think about taking binomial expansion of terms in a series (this is formally equivalent to taking a Taylor expansion, but it's a little 
easier to actually find the terms this way)!

Recall that for $a,\, b \in \mathbb{R}$ and $n \in \mathbb{N}$, the following binomial series holds and gives exactly $n+1$ terms:
```{math}
(a+b)^n &=& a^n\,b^0 + n\,a^{n-1}\,b^1 + \frac{n(n-1)}{2!}\,a^{n-2}\,b^2 + \dots + n\,a^{1}\,b^{n-1} + a^0\,b^n \\
&=& \sum_{r=0}^n \frac{n!}{(n-r)!\,r!}\,a^{n-r}\,b^{r}
```
However if we have $n \in \mathbb{R}$, it is still possible to find a converent series, although the seris itself must be of the form:
```{math}
(1 + x)^n,\, |x|<1
``` 
i.e. the radius of convergence of the series requires a restriction on the size of $x$.  This means that if we are presented with a binomimal of the 
original form, we have to transform it into:
```{math}
(a + b)^n = a^n\left( a + \frac{b}{a}\right)^n
```
where $|a| > |b|$ such that $|b / a| < 1$.  

Consider the example from special relativity, for the energy matter relation $E = \gamma\,m_0\,c^2 = m_0\,c^2/\sqrt{1 - v^2/c^2}$:
```{math}
E = \frac{m_0\,c^2}{\sqrt{1-\frac{v^2}{c^2}}} = m_0\,c^2\left(1-\frac{v^2}{c^2}\right)^{-1/2} 
```
Since $|v| < |c|$ here, then the second term is of the form $v^2/c^2 < 1$ and hence we can do a binomial expansion:
```{math}
E = m_0\,c^2\left( 1 -\frac{1}{2}\left(-\frac{v^2}{c^2}\right) + \dots \right)
```
and we can see that this means:
```{math}
E \simeq m_0\,c^2 + \frac{1}{2}m_0v^2 
```
i.e. the two main contributions to a particles energy are the rest mass-energy and then the classical kinetric energy (the higher order corrections 
occcur when $v/c$ are a larger fraction.

This usually allows us to approximate more complication functions with one or two order series expansions.
