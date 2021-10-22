# A title

```{admonition} A theorem
:class: theorem

Some Content

```

```{exercise} MY LABEL
:label: my-exercise
:nonumber:

Recall that $n!$ is read as "$n$ factorial" and defined as
$n! = n \times (n - 1) \times \cdots \times 2 \times 1$.

There are functions to compute this in various modules, but let's
write our own version as an exercise.

In particular, write a function `factorial` such that `factorial(n)` returns $n!$
for any positive integer $n$.
```

````{solution} my-exercise
:label: my-solution
:class: dropdown

Here's one solution.

```{code-block} python
def factorial(n):
    k = 1
    for i in range(n):
        k = k * (i + 1)
    return k

factorial(4)
```
````

This is a link to {ref}`my-exercise`

```{exercise}
:label: my-exercise2

Recall that $n!$ is read as "$n$ factorial" and defined as
$n! = n \times (n - 1) \times \cdots \times 2 \times 1$.

There are functions to compute this in various modules, but let's
write our own version as an exercise.

In particular, write a function `factorial` such that `factorial(n)` returns $n!$
for any positive integer $n$.
```

````{solution} my-exercise2
:label: my-solution2
:class: dropdown

Here's one solution.

```{code-block} python
def factorial(n):
    k = 1
    for i in range(n):
        k = k * (i + 1)
    return k

factorial(4)
```
````

This is a link to {numref}`my-exercise2`

```{exercise} : Here is some $x^2$ math
:label: my-exercise3

Recall that $n!$ is read as "$n$ factorial" and defined as
$n! = n \times (n - 1) \times \cdots \times 2 \times 1$.

There are functions to compute this in various modules, but let's
write our own version as an exercise.

In particular, write a function `factorial` such that `factorial(n)` returns $n!$
for any positive integer $n$.
```

````{solution} my-exercise3
:label: my-solution3
:class: dropdown

Here's one solution.

```{code-block} python
def factorial(n):
    k = 1
    for i in range(n):
        k = k * (i + 1)
    return k

factorial(4)
```
````

This is a link to {numref}`my-exercise3`

## Solutions

```{solution} ex-dir_deriv
:class: dropdown

$\nabla f = \left(yz,xz,xy\right) \Rightarrow (\nabla f)_M=\left(12,-8,-6\right)$

$D_{\hat{\underline{v}}}f=\hat{\underline{v}}.(\nabla f)_M = \frac{1}{\sqrt{3^2+4^2+12^2}}\left(3,-4,12\right).\left(12,-8,-6\right)=\frac{-4}{13}$
```
