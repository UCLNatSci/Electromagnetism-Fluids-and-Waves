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