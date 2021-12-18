#Circulation

## Circulation
An important subtlety arises here. We have said before that if a vector field is conservative then it is irrotational. However, the converse is only true if the field is "simply connected", meaning that it contains no holes. In example (iii) we have a field that is irrotational on $r\geq a$, but it is not conservative. If we calculate the work done around a closed circuit $\mathcal{C}$ then we find

\begin{equation}\Gamma=\int_{\mathcal{C}}(\nabla\phi).d\underline{x}= \int_{\mathcal{C}}\frac{k}{r}r\mathrm{d}\theta = \biggr[k\theta\biggr]_{\mathcal{C}}\end{equation}

As we go around any circuit that does not enclose $r=a$ then $\theta$ and hence $\phi$ will return to its original value, so the path integral is zero. However, any closed curve that winds round the origin will have $\Gamma=2\pi k$. This result is called the circulation. An illustration is provided below. In the first image, the path integral indicated is 0. In the second image, the path integral is $2\pi k$ (the circulation) and in the third image the path integral is $4\pi k$.


<br>

```{image} navstok_img/circulation.png
---
name: circulation
alt: circulation diagrams
align: center
scale: 80%
---
```
<br>




(iii) Line vortex flow $\underline{v}=\frac{k}{r}\underline{e}_{\theta}$ is irrotational everywhere except at the origin, where it is not defined.
If we consider only the region $r\geq a$ then we have a potential flow:

\begin{equation}\frac{\partial \phi}{\partial r}=0, \quad \frac{1}{r}\frac{\partial \phi}{\partial \theta}=\frac{k}{r}, \quad \frac{\partial \phi}{\partial z} \qquad \Rightarrow \quad \phi=k\theta.\end{equation}
