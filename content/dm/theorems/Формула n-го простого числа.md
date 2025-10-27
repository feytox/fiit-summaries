## Асимптотическая формула распределения простых чисел
Формулировка:
```spoiler-markdown
Пусть $\pi(n)$ — количество простых чисел, не превосходящих $n$.

Одна из важнейших комбинаторных теорем утверждает, что асимптотически количество простых чисел $\pi(n)$ ведёт себя как:
$$\pi(n) \sim \frac{n}{\ln n}$$
Более точная формула:
$$\pi(n) = \frac{n}{\ln n} + O\left(\frac{n}{\ln^2 n}\right)$$
```

## Асимптотическая формула для n-го простого числа
Формулировка:
```spoiler-markdown
Асимптотическая формула для n-го простого числа $p_n$ имеет вид:
$$p_n = n \ln n + n \ln \ln n + O(n)$$
```

Д-во:
```spoiler-markdown
Пусть $p = p(n)$ — n-е простое число, тогда $\pi(p) = n$. Отсюда, используя асимптотику для $\pi(p)$:
$$n = \frac{p}{\ln p} + O\left(\frac{p}{\ln^2 p}\right)$$
Решим это уравнение относительно $p$.
Так как $O\left(\frac{p}{\ln^2 p}\right) = o\left(\frac{p}{\ln p}\right)$, то из уравнения следует, что $\frac{p}{\ln p} = O(n)$.
Тогда остаточный член можно переписать:
$$O\left(\frac{p}{\ln^2 p}\right) = O\left(\frac{n}{\ln p}\right) = O\left(\frac{n}{\ln n}\right) \text{ (т.к. } p > n \text{)}$$
Подставляя уточненный остаток в исходное уравнение, получаем:
$$\frac{p}{\ln p} = n + O\left(\frac{n}{\ln n}\right) = n\left(1 + O\left(\frac{1}{\ln n}\right)\right)$$
$$\implies p = n \ln p \left(1 + O\left(\frac{1}{\ln n}\right)\right)$$
Чтобы избавиться от $\ln p$ в правой части, прологарифмируем обе части:
$$\ln p = \ln n + \ln \ln p + O\left(\frac{1}{\ln n}\right)$$
Для больших $n$ имеем $p < n^2 \implies \ln p < 2 \ln n \implies \ln \ln p < \ln \ln n + O(1)$.
Подставляя эту оценку, получаем:
$$\ln p = \ln n + \ln \ln n + O(1)$$
Наконец, подставим это уточненное выражение для $\ln p$ обратно в выражение для $p$:
$$p = n(\ln n + \ln \ln n + O(1))\left(1 + O\left(\frac{1}{\ln n}\right)\right) = n \ln n + n \ln \ln n + O(n)$$
$\square$
```
