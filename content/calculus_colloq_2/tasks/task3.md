(задача тоже с практик, но я уже не помню, как её решали)

Условие:
Пусть функция $f(x)$ непрерывна на отрезке $[a, b]$ за исключением конечного числа точек $x_{1}, x_{2}, \dots, x_{n}$. Докажите, что функция $f(x)$ интегрируема на $[a, b]$.

Д-во:
Пусть $X = [a, b] \setminus \{x_{1}, \dots, x_{n}\}$. Непрерывность $f(x)$:
$$\forall{\varepsilon > 0}~~ \exists{\delta(\varepsilon)}~~ \forall{x \in X}\mathpunct{:}~~ |x - x_{0}| < \delta \Rightarrow |f(x) - f(x_{0})| < \varepsilon$$
Пусть $\mu = \min \{x_{i} - x_{j} | i,j \in \overline{0, n} \land i \neq j\}$ - минимальное расстояние, между точками, а ${} \eta = \sup\limits_{x \in \{x_{1}, \dots, x_{n}\}} |f(x)| {}$
Возьмём разбиение $\tau = \{a = t_{0} < t_{1} < \dots < t_{n} = b\}$ такое, что ${} \lambda(\tau) < \min \left\{\dfrac{\varepsilon}{4\eta}, \mu\right\} {}$. 
Распишем разность сумм Дарбу:
$$\overline{S}_{\tau} - \underline{S}_{\tau} = \sum_{k=0}^{n-1} (M_{k} - m_{k})\Delta t_{k} = \sum_{k \in K_{1}} (M_{k} - m_{k})\Delta t_{k} + \sum_{k \in K_{2}} (M_{k} - m_{k})\Delta t_{k}$$
где $K_{1}$ - отрезки, содержащие точку $x_{1}, x_{2}, \dots, x_{n}$ (одну из выбора диаметра разибиения), $K_{2}$ - все остальные.

Вторая сумма $< \dfrac{\varepsilon}{2}$ по доказательству интегрируемости непрерывной функции. 

Рассмотрим $K_{1}$ и тогда:
$$\sum_{k \in K_{1}} (M_{k} - m_{k})\Delta t_{k} < \dfrac{\varepsilon}{4\eta}\sum_{k \in K_{1}} M_{k} - m_{k} \leq \dfrac{\varepsilon}{4\eta} \cdot 2\eta = \dfrac{\varepsilon}{2}$$
Тогда исходная сумма $< \dfrac{\varepsilon}{2} + \dfrac{\varepsilon}{2} = \varepsilon$, а значит $f(x)$ интегрируема на $[a, b]$.
$\square$