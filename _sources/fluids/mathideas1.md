---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Visualising fluid motion

**In this section:**
* Can snapshots of the velocity field tell us about the paths taken by individual fluid particles?
* Does a streak of dye injected into a fluid tell us about the paths taken by individual fluid particles?

## Background: what is a **field**?
A field is a map of a physical quantity at each point in space and time. You are probably already familiar with graphical representations of fields, in the form of weather maps showing temperature and wind velocity :

| Physical quantity      | Example notation | Type of field     |
| :---        |    :----:   |          ---: | ---: |
| Temperature | $\Phi(x,y,z,t)$       | Scalar (magnitude only)  |
| Wind velocity  | $\underline{v}(x,y,z,t)$        | Vector (magnitude and direction) |

Further examples of **scalar field** quantities are mass and pressure. A scalar field can be represented using a surface plot, or a contour plot (e.g. pressure isobars), or a colour/grayscale map. The example below shows a grayscale map of the scalar field defined by
\begin{equation}
\Phi(x,y)=x\ \mathrm{sinc}(x^2+y^2),\quad -3\leq x,y \leq 3.
\end{equation}

```{code-cell}
---
render:
  image:
    align: center
    alt: fun-fish
---
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

x = np.linspace(-3., 3., 256)     #x coordinates arranged on [-3,3]
y = np.linspace(-3., 3., 256)     #y coordinates arranged on [-3,3]
X, Y = np.meshgrid(x, y)          #make the plot grid

Z = X * np.sinc(X ** 2 + Y ** 2)  #define the scalar field values at each point

# options to prettify the plot
fig,ax=plt.subplots(figsize=(5,5))
ax.set_title('A scalar field')
ax.axis([-3,3,-3,3])
ax.xaxis.set_ticks([]), ax.yaxis.set_ticks([])

# The "pcolormesh" function can be used to make a density plot.
ax.pcolormesh(X,Y,Z,shading='auto',cmap=cm.gray)
plt.show()
```

The most commonly encountered **vector field** quantities are velocity and force. A vector field can be represented using arrows, where the length of each arrow indicates the field strength at the point. The example below shows a plot of the vector field defined by
```{math}
:label: example_field
\underline{v}=(2x,-2y),\quad -2\leq x,y \leq 2.
```

```{code-cell}
---
render:
  image:
    align: center
---
x=np.linspace(-2, 2, 10) #x coordinates arranged on [-2,2]
y=np.linspace(-2, 2, 10) #y coordinates arranged on [-2,2]

X,Y = np.meshgrid(x, y) #make the plot grid
(U,V)=(2*X,-2*Y)        #define the vector field values at each point

# options to prettify the plot
fig,ax=plt.subplots(figsize=(5,5))
ax.set_title('A vector field')
ax.axis([-2,2,-2,2])
ax.xaxis.set_ticks([]), ax.yaxis.set_ticks([])

# The "quiver" function is used in Python to make a vector plot. It gets its name from the apparatus that
# an archer uses to carry their arrows.
ax.quiver(X,Y,U,V)
plt.show()
```

If you draw curves tangent to the arrows of a vector field, these are called "field lines". The plot below shows field line for the vector field given in the previous example, {eq}`example_field` . The field strength at each point is indicated by how close together the field lines are, assuming that the physical quantity being indicated by the field is *conserved*.

```{code-cell}
---
render:
  image:
    align: center
tags: [hide-input]
---
fig,ax=plt.subplots(figsize=(5,5))
ax.set_title('Field lines')
ax.axis([-2,2,-2,2])
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
#----------------------------------
start=[ #start points of selected field lines
    [-1.6,-2],[-1.1,-2],[-0.6,-2],[-0.1,-2],
    [+1.6,-2],[+1.1,-2],[+0.6,-2],[+0.1,-2],
    [-1.6,+2],[-1.1,+2],[-0.6,+2],[-0.1,+2],
    [+1.6,+2],[+1.1,+2],[+0.6,+2],[+0.1,+2]]
#----------------------------------

ax.streamplot(X,Y,U,V,start_points=start,density=10) # stream plot

plt.show()
```

````{exercise}
:label: streamlinesq
Choosing a plot range that you think is suitable, produce both a vector plot and a field line plot of the velocity field $\underline{v}=(2 y, 2 x,0)$. Describe the shape of the streamlines in words.
````

In the case where the field represents velocity of a fluid, the field lines are known as "streamlines". In the sections below we will discuss the difference between *streamlines*, *streaklines* and *particle paths*,for the case where the fluid velocity is a time-dependent field $\underline{v}(\underline{x},t)$.


## Streamlines

A streamline is a curve that is parallel to the velocity field $\underline{v}(\underline{x},t)$ at a given, **fixed time** $t$ and passes through a given point $\underline{x}_0$. A family of streamlines at time $t$ provides a snapshot of the velocity field.

To illustrate the concepts, we will take

```{math}
:label: examplev
\underline{v}=(1,-2te^{-t^2}).
```

This field has no spatial dependence, so the streamlines are straight lines with slope $-2t e^{-t^2}$. The direction of the streamlines changes at each instant, as shown in the plot below.

```{code-cell}
---
render:
  image:
    align: center
tags: [hide-input]
---
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x, y)
U=V=np.ones_like(X)
start=[[-1.5,-1.5],[-1,-1],[-0.5,-0.5],[0,0],[0.5,0.5],[1,1],[1.5,1.5]]

import matplotlib.gridspec as gridspec
fig = plt.figure(constrained_layout=True,figsize=(10,4))
spec = gridspec.GridSpec(ncols=5, nrows=2, figure=fig)

def slope(t):
    return -2*t*np.exp(-t**2)

tvals=np.linspace(0,3.35,100)

n=5    #number of subplots

for s in range(n):
    ax=fig.add_subplot(spec[1,s])
    ax.xaxis.set_ticks([]), ax.yaxis.set_ticks([])
    t=3*s/(n-1)
    #ax.set_title('t='+str(t))
    ax.streamplot(X,Y,U,slope(t)*V,start_points=start,density=10)

ax = fig.add_subplot(spec[0, :])
ax.plot(tvals,slope(tvals))
ax.axis([-0.35,3.35,-0.9,0.1])
ax.xaxis.set_ticks([0,0.75,1.5,2.25,3])
ax.set_title('$-2t e^{-t^2}$')

plt.show()
```


To find an equation governing each streamline, we assume a parameterisation of the form $\underline{x}(s)=(x(s),y(s)_,z(s))$. Since the streamline is tangent to the velocity field it must satisfy the following equation, where $t$ is treated as constant:

\begin{equation}\frac{\mathrm{d}\underline{x}}{\mathrm{d}s}=\underline{v}(\underline{x},t).\end{equation}

Integrating the problem gives a family of streamlines. For the example given in equation {eq}`examplev`, the streamlines satisfy

\begin{equation}\frac{\mathrm{d}x}{\mathrm{d}s}=1, \quad \frac{\mathrm{d}y}{\mathrm{d}s}=-2te^{-t^2}.\end{equation}

The solution that passes through a given point $(x_0,y_0)$ is given by

\begin{equation}\underline{x}=(x_0+s, y_0-2te^{-t^2}s).\end{equation}

````{exercise}
:label: ex-streams
Find a parameterisation governing the streamlines of the flow $\underline{v}=(2x,2yt)$.
````



## Particle paths
The streamlines indicate the instantaneous direction of motion of fluid particles at a given moment. If the fluid is not steady (time-independent), then the streamlines do **not** show the paths taken by the fluid particles. This is illustrated by the below animation, which tracks several selected fluid particles as they move tangent to the evolving velocity field given in equation {eq}`examplev`.

```{code-cell}
---
tags: [hide-input]
---
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from IPython.display import HTML

n = 15
xgrid=np.linspace(1,3,n)
ygrid=np.linspace(0,2,n)
X, Y = np.meshgrid(xgrid, ygrid)

t=0
U=np.ones(X.shape)
V=-2*t*np.exp(-t**2)*np.ones(X.shape)
tmax,fnum=3,100

def x(t0,t):
  return t+(1-t0)

def y(t0,t,y0):
  return y0+np.exp(-t**2)-np.exp(-t0**2)

#x = np.linspace(1, 3, 1000)

class testAnimation:

  def __init__(self):
    # First set up the figure, the axis, and the plot element we want to animate
    self.fig, ax = plt.subplots()
    plt.close()
    ax.set_xlim(( 1, 3))
    ax.set_ylim((0, 2))
    self.UVC = ax.quiver(X,Y,U,V)
    self.scat, = ax.plot([], [],'o', color='blue')

  # initialization function: plot the background of each frame
  def init(self):
      return (self.UVC, self.scat)

  # animation function. This is called sequentially  
  def animate(self, i):
      t=tmax/fnum*i;
      V=-2*t*np.exp(-t**2)*np.ones(X.shape)
      self.UVC.set_UVC(U,V)
      tgrid=np.arange(0,t,0.5)
      self.scat.set_data(x(0,t), y(0,t,np.linspace(0,2,10)))
      return (self.UVC, self.scat)

  def draw(self):
    global anim
    anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init,
                             frames=fnum, interval=1000*tmax/fnum, blit=True)


vis = testAnimation()
vis.draw()

# Note: below is the part which makes it work on Colab
rc('animation', html='jshtml')

#anim.save('fluid.gif', writer = 'imagemagick', fps=10)

anim
```

According to the definition of velocity, we can find the particle paths by solving the problem

\begin{equation}\frac{\mathrm{d}\underline{x}}{\mathrm{d}t}=\underline{v}(\underline{x},t).\end{equation}

For the example given in equation {eq}`examplev`, the particle paths satisfy

\begin{equation}\frac{\mathrm{d}x}{\mathrm{d}t}=1, \quad \frac{\mathrm{d}y}{\mathrm{d}t}=-2te^{-t^2}.\end{equation}

The solution that passes through a given point $(x_0,y_0)$ is given by

```{math}
:label: ptrajectory
\underline{x} (t-t_0+x_0,e^{-t^2}-e^{-t_0^2}+y_0).
```

In this example, the velocity approaches a constant value $(1,0)$ as $t$ increases. Since the evolved velocity field is "steady" (time-independent) the particle paths and streamlines for this flow eventually coincide.

````{exercise}
:label: ex-ppaths
Find the particle paths for the flow $\underline{v}=(\alpha,\beta t,0)$, where $\alpha, \beta$ are positive constants. Describe the shape of your solutions.
````


## Streaklines

Fluid particles that pass through the same point at different times generally follow different paths. A streakline is the locus of all particles that have passed through a given point $\underline{x}_0$. This is what we see when we inject smoke or dye into a moving fluid. We can find streaklines by solving the particle path problem for a range of release times $t_0$. We may plot the result at a given time $t$.

The animation below shows a sequence of particles injected into the fluid described by equation {eq}`examplev` at intervals. Due to the changing vector field, the particles follow different trajectories depending on the time of release. The $(x,y)$ trajectory of a particle released at time $t_0$ is given in equation {eq}`ptrajectory`. The set of particles together define a streakline.

```{code-cell}
---
tags: [hide-input]
---
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from IPython.display import HTML

n = 15
xgrid=np.linspace(1,3,n)
ygrid=np.linspace(0,2,n)
X, Y = np.meshgrid(xgrid, ygrid)

t=0
U=np.ones(X.shape)
V=-2*t*np.exp(-t**2)*np.ones(X.shape)
tmax,fnum=3,100

def x(t0,t):
  return t+(1-t0)

def y(t0,t):
  return 1+np.exp(-t**2)-np.exp(-t0**2)

#x = np.linspace(1, 3, 1000)

class testAnimation:

  def __init__(self):
    # First set up the figure, the axis, and the plot element we want to animate
    self.fig, ax = plt.subplots()
    plt.close()
    ax.set_xlim(( 1, 3))
    ax.set_ylim((0, 2))
    self.UVC = ax.quiver(X,Y,U,V)
    self.scat, = ax.plot([], [],'o', color='blue')

  # initialization function: plot the background of each frame
  def init(self):
      return (self.UVC, self.scat)

  # animation function. This is called sequentially  
  def animate(self, i):
      t=tmax/fnum*i;
      V=-2*t*np.exp(-t**2)*np.ones(X.shape)
      self.UVC.set_UVC(U,V)
      tgrid=np.arange(0,t,0.1)
      self.scat.set_data(x(tgrid,t), y(tgrid,t))
      return (self.UVC, self.scat)

  def draw(self):
    global anim
    anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init,
                             frames=fnum, interval=1000*tmax/fnum, blit=True)


vis = testAnimation()
vis.draw()

# Note: below is the part which makes it work on Colab
rc('animation', html='jshtml')

#anim.save('fluid.gif', writer = 'imagemagick', fps=10)

anim
```
The image below is a classic photograph taken from *An Album of FLuid Motion* (1982) by Van Dyke. The image shows streaklines over an airfoil in an oncoming fluid flow. The streaklines are illustrated by smoke particles that have been injected into the flow upstream. The flow is mostly very smooth, due to great care taken by the experimenters to reduce air disturbances, but notice that there is some disturbance occuring in the fluid near to the trailing edge of the airfoil. We will investigate this phenomenon soon.

<br>

```{image} navstok_img/bbl.png
---
name: bbl
alt: alternative description
align: center
scale: 80%
---
```
<br>

If you are interested to see images and videos of fluid flow that have been recorded more recently, you could take a look at the [Gallery of Fluid Motion](https://gfm.aps.org/), presented by the Americal Physics Society Division of Fluid Dynamics. Many of the modern entries are computer simulations of fluid, rather than experimental footage.
