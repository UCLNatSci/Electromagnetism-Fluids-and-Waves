# Fluids
Fluid dynamics is the study of flow. Since anything that flows can be thought of as a fluid, this field of study covers a tremendous range of applications, including aerodynamics, meteorology, hydraulics, oceanography, astrophysical dynamics, acoustics, hemodynamics (blood flow) and mucus flows. Principles of fluid dynamics have even been applied to the study of granular flows, such as dry sand, vehicular traffic and crowd dynamics.

Despite the vast range of applications, most of these phenomena can be examined by just three unifying principles:

* Conservation of mass
* Conservation of momentum
* Conservation of energy

For many flows (this course), we can neglect thermodynamic effects, and in that case we can also get by without conservation of energy. This chapter introduces the equations of conservation of mass and conservation of momentum.

## The continuum hypothesis

So that we can use the tools of calculus, we treat the fluid as if it were continuous in structure and we regard physical quantities as locally uniform. This also means we can treat gases and liquids in the same way, since the equations of motion are independent of the particle structure.

An illustration of the idea is shown below, applied to measurements of density. We ignore molecular fluctuations, and consider a locally averaged measure of density based on the mean free path between atoms.

<br>

```{image} ./navstok_img/continuum_hypothesis.png
---
name: continuum_hypothesis
alt: some alternative text
align: center
scale: 80%
---
```

<br>

In actuality, the concept of "density" does not apply very meaningfully at the microscopic level, since the density at each point is defined by either being "inside" or "outside" an atom.
