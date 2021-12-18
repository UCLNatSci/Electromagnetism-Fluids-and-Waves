# Mathematical Preliminaries

Since waves involve changes in both space and time $u(x,\,t)$, the definitions of first and second partial derivatives in terms of limits
are useful here.  Stating with the first derivative:

```{math}
:label: partialderiv
\frac{\partial u(x,t)}{\partial x} = \lim_{\Delta x \rightarrow 0} \frac{u(x + \Delta x,t) - u(x,t)}{\Delta x} 
```
The second derivative can be thought of as a derivative of a derivative:
```{math}
\frac{\partial^2 u(x,t)}{\partial x^2} &=&\, \frac{\partial}{\partial x}\left(\frac{\partial u(x,t)}{\partial x}\right) \\
&=&\, \lim_{\Delta x \rightarrow 0} \frac{1}{\Delta x}\left[\frac{\partial u(x+\Delta x,t)}{\partial x} - \frac{\partial u(x,t)}{\partial x} \right] \\
&=&\, \lim_{\Delta x \rightarrow 0} \frac{1}{\Delta x}\left[\frac{u(x + 2\Delta x,t) - u(x+ \Delta x,t)}{\Delta x} - \frac{u(x + \Delta x,t) - u(x,t)}{\Delta x} \right] \\
```
Which means we can write a second partial derivative using a limit definition as:
```{math}
:label: 2ndpartialderiv
\frac{\partial^2 u(x,t)}{\partial x^2} = \lim_{\Delta x \rightarrow 0} \frac{u(x+2\Delta x,t) - 2u(x+\Delta x,t) + u(x,t)}{{\Delta x}^2} 
```