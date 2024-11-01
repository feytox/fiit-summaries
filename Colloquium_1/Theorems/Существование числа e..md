Формулировка:
```spoiler-markdown
Число $e$ существует (или просто "$e!$")
```

Д-во:
```spoiler-markdown
Рассмотрим $a_{n} = \left(1 + \dfrac{1}{n}\right)^{n+1}$. $a_{n} \geq 0 \Rightarrow a_{n}$ ограничено снизу.
Рассмотрим также $n+1$ число: $1; 1 - \dfrac{1}{n}; 1 - \dfrac{1}{n}; ...; 1 - \dfrac{1}{n}$, тогда по неравенству о средних: 
$$\dfrac{n+1-1}{n+1} \geq \sqrt[n+1]{\left(1 - \dfrac{1}{n}\right)^{n}} \Rightarrow \left(\dfrac{n}{n+1}\right)^{n+1} \geq \left(1 - \dfrac{1}{n}\right)^{n} \Rightarrow \left(\dfrac{n+1}{n}\right)^{n+1} \leq \left(\dfrac{n}{n-1}\right)^{n} \Rightarrow a_{n} \leq a_{n-1}$$
А значит $a_{n}$ монотонно убывает.
$a_{n}$ монотонно убывает и ограничено снизу, а значит по теореме Вейерштрасса $\exists{\lim_{n \to \infty} a_{n} = e}$
Тогда: $$\lim_{n \to \infty} \left(1 + \dfrac{1}{n}\right)^{n} = \dfrac{\lim_{n \to \infty} \left(1 + \dfrac{1}{n}\right)^{n+1}}{\lim_{n \to \infty} \left(1 + \dfrac{1}{n}\right)} = \dfrac{e}{1} = e~~~ \square$$

```



