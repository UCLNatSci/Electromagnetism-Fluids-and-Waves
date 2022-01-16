# Standing Waves

A standing wave, sometimes called a stationary wave, is a wave that remains in a constant position, as seen in {numref}`StandingWave`.  This can occur 
because in a stationary medium, two waves are traveling in opposite directions and end up interfering with each other or the medium is moving in the opposite 
direction to the wave.  

```{figure} ../figures/StandingWave.png
---
name: StandingWave
---
A closed standing wave on a string, with pattern oscillating back and forth between the top, middle and bottom panels.  We identify nodes, i.e. points that 
remain stationary, with points along the string.
```

Standing waves can arise when some kind of boundary blocks waves propagating and this causes the wave to get reflected and now there are two waves moving in 
opposite directions in the same domain.  At either end of the wave domain, the two opposed waves are in <b>anti-phase</b> and cancel each other, producing a 
<b>node</b>. Halfway between two nodes there is an <b>anti-node</b>, where the two opposite directed waves constructively interfere. For standing waves, 
there is no net propagation of energy over time - it is all confined within the wave domain. 

To describe a standing wave over a closed length $L$, with boundary conditions:

```{math} 
u(0,t) = u(L,t) = 0
```
so we find by summing left and right moving waves:

```{math}
u(x,t) &=&\, \left(A \cos(kx-\omega t) + B\cos(kx+\omega t) \right) \\
u(0,t) &=&\, \left(A \cos(\omega t) + B\cos(\omega t) \right) = \cos(\omega t)\left(A  + B\right) = 0 \\ 
&\Rightarrow&\, B = -A \\
u(L,t) &=&\, A \Big[\cos(kL-\omega t) - \cos(kL+\omega t) \Big] = 0  \\ 
&\Rightarrow&\, 2A\sin(kL) \sin(\omega t) = 0
```

To solve this second condition, given the cyclic symmetry of $\sin(kL)$, we will have: 

```{math}
kL = \frac{2 \pi L}{\lambda} =  \dots,\,-2\pi,\,-\pi,\,0,\,\pi,\,2\pi,\,3\pi,\,4\pi,\,\dots
```

We can also consider this from the phase shift as well, as a half wavelength $\lambda/2$ corresponds to a phase of $\pi$, for a full wavelength $\lambda$, the 
phase is $2\pi$ etc, hence we get $k = 2 \pi/\lambda$ for the whole wave and then later solve for $\lambda(L)$.

Thus for positive solutions, we find distinct harmonics (or notes) emerge:

```{math}
L = \frac{\lambda}{2},\,\lambda,\,\frac{3\lambda}{2},\,2\lambda,\dots, 
```
and we can rewrite each notes wavelength $\lambda$ in terms of the boundary size $L$:

```{math}
\lambda = 2L,\,L,\,\frac{2L}{3},\,\frac{L}{2},\dots, 
```

Similar considerations can also apply to a standing wave that is closed at one end and open at the other, which will have different boundary conditions.  

It is clear that different values of $x$ correspond to maxima, where the argument of $u(x,\,t)$ will be odd multiples of $\pi/2$:

```{math}
\frac{2\pi x}{\lambda} = \dots, -\frac{3\pi}{2}, -\frac{\pi}{2}, \frac{\pi}{2}, \frac{3\pi}{2}, \dots,
```

these are the anti-nodes of the standing waves, located at $x \geq 0$:

```{math}
x = \frac{\lambda}{4},\, \frac{3\lambda}{4},\, \frac{5\lambda}{4}, \,\dots
```

Equally we can find values of $x$ where there are minima, the argument of $u(x,\,t)$ will be even multiples of $\pi/2$:

```{math}
\frac{2\pi x}{\lambda} = \dots, -2\pi, -\pi, 0, \pi, 2\pi, \dots 
```

these are the nodes of the standing waves, located at $x \geq 0$:

```{math}
x = 0, \,\frac{\lambda}{2}, \,\lambda, \frac{3\lambda}{2},\,\dots
```


