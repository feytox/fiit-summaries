### Эквивалентность функций
$f(x)$ - эквивалентна $g(x)$ при $x \to a$, если
```spoiler-markdown
$$\lim_{x \to a} \dfrac{f(x)}{g(x)} = 1,~~~ f(x) \sim g(x)$$
```

### o-малое
$f(x) = o(g(x))$ при $x \to a$, если
```spoiler-markdown
$\exists{\alpha(x)}~~ f(x) = \alpha(x)g(x) \land \alpha(x) \to 0$
Если $g(x) \neq 0$: $\lim_{x \to a} \dfrac{f(x)}{g(x)} = 0$
```

### Свойства o 
$n > m$
```spoiler-markdown
1) $Co(x^{n}) = o(x^{n})$
2) $o(x^{n}) + o(x^{n}) = o(x^{n})$
3) $o(x^{n}) - o(x^{n}) = o(x^{n})$
4) $o(x^{n}) + o(x^{m}) = o(x^{m})$
5) $o(x^{n}) \cdot x^{m} = o(x^{n+m})$
6) $o(x^{n}) \cdot o(x^{m}) = o(x^{n+m})$
```