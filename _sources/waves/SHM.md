# Harmonic and Oscillatory Motion
Waves are connected to oscillations and describe the transfer of energy from different parts of a system through oscillating phenomena within said system.  This 
should be seen differently to other ways that energy may be transferred, e.g. thermodynamically or by doing work by applying a force over a distance.  The study 
of oscillations can be started by looking at the simplest kind of oscillating system, that of Simple Harmonic Motion (SHM) and Simple Harmonic Oscillators (SHO), before 
moving on to consider damped and forced harmonic systems.

## Simple Harmonic Motion
Lets consider a simple system with a mass on a idealised spring, which follows Hooke's law 
```{math}
\bf{F}_H = k \bf{x}
```
where $\bf{F}$ is the force applied, $x$ is the extension measured in the spring from the application of the force $\bf{F}$ and $k$ is the spring constant, 
a material property of the spring. 

```{figure} ../figures/massonaspring.png
---
name: massonaspring
---
Mass on a spring demonstrating SHM
```
As we see in {numref}`massonaspring`, a mass hanging from a spring will settle into an equilibrium position where the downward weight from the mass 
$\bf{W}$ (the spring here is considered mass-less) and the upward tension $\bf{F}_H$ from the spring balance out, producing no net force and 
therefore no net acceleration (by Newton's second law).  At this equilibrium position the spring extension will be denoted by $\bf{e}$
```{math}
\Sigma \bf{F} = m\bf{a} \Rightarrow \bf{W} - k\bf{e}
```

If we displace the mass downwards, with an additional extension $\bf{x}$ (which we have denoted is the positive direction), then the Hooke's 
law tension from the spring will be directed upwards (which will be in the negative direction)
```{math}
\Sigma \bf{F} = m\bf{a} \Rightarrow \bf{W} - k(\bf{e} + \bf{x}) = m\bf{a}
```
we can express the acceleration $\bf{a}$ in terms of a second derivative of the displacement $\bf{x}$ so we can rewrite as
```{math}
\ddot{\bf{x}}= - \frac{k}{m}\bf{x}
```
which is often rewritten as 
```{math}
\ddot{\bf{x}} = -{\omega_0}^2\bf{x}
```
where we denote $\omega_0 = \sqrt{k/m}$ is the natural angular frequency of this system.  
Recall from our discussions of calculus that we can solve this second order ODE to give:
```{math}
:label: SHMsolution
x(t) = A \cos(\omega_0 \,t) + B \sin(\omega_0 \,t) 
```
To solve for $A,\,B$ here we need initial conditions, which we could consider from the physical situation of displacing the mass 
from equilibrium to an additional displacement $x = 1$ and then releasing the mass from rest and examining the resulting motion. 
This tell us that $x(t = 0) = 1$ and $\dot{x}(t=0) = v(t = 0) = 0$ and therefore:
```{math}
x(t) &=& A \cos(\omega_0 \,t) + B \sin(\omega_0 \,t) \Longrightarrow x(0) = A = 1 \\
\dot{x}(t) &=& - \omega_0 A \sin(\omega_0 \,t) + B  \omega_0 \cos(\omega_0 \,t)  \Longrightarrow \dot{x}(0) = B \omega_0 = 0
```
which gives us $A = 1,\, B = 0$ and so 
```{math} 
x(t) = \cos(\omega_0\,t)
```

We say this system presents <b>Simple Harmonic Motion (SHM)</b>, because it represents the simplest kind of harmonic 
(also called oscillating or repetitive) motion that we can have.  We put energy into the system by extending the spring 
(which is a form of potential energy $E_k = \frac{1}{2}kx^2$) and then this is converted into kinetic energy and then back into potential 
(this time as gravitational potential energy) as the mass oscillates up and down.  What is truly stunning about this system is that SHM can be 
seen a many different systems but always has the same hallmarks - there is some natural angular frequency $\omega_0$ we can find from the equations 
of motion and the energy in the system oscillates between potential and kinetic.  

Another feature of this motion is the similarities it brings to circular motion, in fact we can see from {numref}`CircMotionSHM` that uniform 
circular motion projected into one dimension is just SHM.  The natural angular frequency of the system $\omega_0$ here is now the angular speed $\omega$ of 
the circular motion 
```{math}
\omega = \frac{\textrm{d}\theta}{\textrm{d}t}
```

```{figure} ../figures/CircMotionSHM.jpg
---
name: CircMotionSHM
---
Projection of a ball on a spinning wheel undergoing uniform circular motion, the balls shadow displays SHM - this stretched out in time shows wave motion.
```

## Energy in a Simple Harmonic System
Going back to the mass and spring system, we can also think about the stored energy in the system, 
```{math}
E = KE + PE
```
where the kinetic energy has the usual defintion, $KE = \frac{1}{2}mv^2 = \frac{1}{2}m{\dot{x}}^2$ and the potential energy is elastic potential energy 
$PE = \frac{1}{2}kx^2$, but in a different system this could be replaced with the relevant form of potential.  Using the solutions for SHM, {eq}`SHMsolution`:
```{math}
x(t) &=& \, A \cos(\omega_0 \,t) + B \sin(\omega_0 \,t) \\
\dot{x}(t) &=& \, \omega_0(-A \sin(\omega_0 \,t) + B \cos(\omega_0 \,t) )\\
\Rightarrow E &=& \, \frac{1}{2}m{\omega_0}^2(-A \sin(\omega_0 \,t) + B \cos(\omega_0 \,t) )^2 + \frac{1}{2}k(A \cos(\omega_0 \,t) + B \sin(\omega_0 \,t) )^2
```
Given that ${\omega_0}^2 = k / m$, this can be expanded and tidied up becoming:
```{math}
:label: SHMenergy
E = \frac{1}{2}k\left(A^2 + B^2\right)
```
Which therefore means that the total amount of energy in the system is a constant, even if the energy flucuates between kinetic and potential in the course
of the harmonic motion.

## Damped Motion and Forced Harmonic Systems*

This SHM model presupposes that there are no losses in energy in this system and this is not always a good model for real world systems, usually there are 
<b> damping </b> terms in our equations of motion, often this is due to air resistance but can also be caused by frictional forces.  This has the effect of adding a 
first derivative term to the equations of motion 
```{math}
m\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} + c \frac{\mathrm{d} x}{\mathrm{d} t} + kx = 0 
```
We could also think of oscillating systems, such as an AC electrical system with an input voltage $V = V_0 \cos(\Omega t)$, pushing round a current $I = I_0\cos(\omega t)$ and 
with some fixed resistances $R$.  Such systems can be described as <em> forced </em> harmonic osciallators, because energy is constantly being put into and 
given out from the system.  We can calculate the electrical power, $P = V^2 / R = {V_0}^2\,\cos^2(\Omega t)/R$ - suggesting the power and oscillation amplitude are 
related according to $P \propto {V_0}^2$.  The most general form of these systems can be written as:
```{math}
a\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} + b \frac{\mathrm{d} x}{\mathrm{d} t} + cx = F(t)
```
where $F(t)$ is the driving term. We can rewrite in the :
```{math}
\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} + 2\zeta\omega_0 \frac{\mathrm{d} x}{\mathrm{d} t} + {\omega_0}^2 x = F(t) 
```
where $\omega_0$ is the natural angular frequency of the system and $\zeta$ is the damping ratio.  If energy is put into the system at a rate of $\Omega$, such as 
$F(t) = F_0 \cos(\Omega \,t)$ and this frequency conicinces with the natural frequency $\omega_0$, i.e. $\Omega \rightarrow \omega_0$, this gives rise to the phenomena of 
<b> resonance </b>.  


## 


