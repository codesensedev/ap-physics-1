# Solutions · 04 · Constant acceleration

Back to the [problems](04-constant-acceleration-problems.md). Don't read these before you've tried.

---

### 1 *(Type A)*

Knowns: $v_{x0} = 4.0$ m/s, $v_x = 10.0$ m/s, $t = 3.0$ s. Unknowns: $a_x$ and $\Delta x$.

$a_x = \dfrac{v_x - v_{x0}}{t} = \dfrac{10.0 - 4.0}{3.0} = 2.0$ m/s²

$\Delta x = \tfrac12(v_{x0} + v_x)\,t = \tfrac12(4.0 + 10.0)(3.0) = 21$ m

Check with another equation: $v_{x0}t + \tfrac12 a_x t^2 = 12 + 9 = 21$ m ✓.

### 2 *(Type A)*

Knowns: $v_{x0} = 0$, $a_x = 3.0$ m/s², $\Delta x = 150$ m. Unknowns: $v_x$ and $t$. For $v_x$, time is not involved, so use the equation without $t$:

$v_x^2 = v_{x0}^2 + 2a_x\Delta x = 0 + 2(3.0)(150) = 900$, so $v_x = 30$ m/s.

Then $t = \dfrac{v_x - v_{x0}}{a_x} = \dfrac{30}{3.0} = 10$ s.

Check: $\Delta x = \tfrac12 a_x t^2 = \tfrac12(3.0)(10)^2 = 150$ m ✓.

### 3 *(Type A)*

Knowns: $v_{x0} = +30$ m/s, $v_x = 0$, $a_x = -1.5$ m/s².

$\Delta x = \dfrac{v_x^2 - v_{x0}^2}{2a_x} = \dfrac{0 - 900}{2(-1.5)} = 300$ m

$t = \dfrac{v_x - v_{x0}}{a_x} = \dfrac{0 - 30}{-1.5} = 20$ s

Check: average speed $15$ m/s × $20$ s $= 300$ m ✓.

### 4 *(Type B)*

**Stage 1** (speeding up): $v_{x0} = 10$ m/s, $a_x = +2.0$ m/s², $t = 6.0$ s.

- $v_1 = 10 + (2.0)(6.0) = 22$ m/s
- $\Delta x_1 = (10)(6.0) + \tfrac12(2.0)(6.0)^2 = 60 + 36 = 96$ m

**Stage 2** (braking): the initial velocity is stage 1's final velocity, $v_{x0} = 22$ m/s. Then $v_x = 0$ and $a_x = -4.0$ m/s².

- $\Delta x_2 = \dfrac{0 - 22^2}{2(-4.0)} = 60.5$ m
- $t_2 = \dfrac{0 - 22}{-4.0} = 5.5$ s

**Totals:** distance $= 96 + 60.5 = 156.5$ m $\approx 157$ m; time $= 6.0 + 5.5 = 11.5$ s.

### 5 *(Type C)*

(a) Slope of each segment (rise over run):

- 0–4 s: $\dfrac{8 - 0}{4 - 0} = +2.0$ m/s²
- 4–8 s: flat, so $0$
- 8–10 s: $\dfrac{0 - 8}{10 - 8} = -4.0$ m/s²

(b) Displacement is the area under the graph: a triangle, a rectangle and a triangle.

- 0–4 s: $\tfrac12(4)(8) = 16$ m
- 4–8 s: $(4)(8) = 32$ m
- 8–10 s: $\tfrac12(2)(8) = 8$ m

Total: $16 + 32 + 8 = 56$ m.

(c) $v_{\text{avg}} = \dfrac{\Delta x}{\Delta t} = \dfrac{56}{10} = 5.6$ m/s.

Check: 5.6 m/s is below the 8 m/s top speed, as it must be, because the cart spends time slower than 8 m/s ✓.

### 6 *(Type D)*

Same brakes means the same $a_x$. Starting from $v_x^2 = v_{x0}^2 + 2a_x\Delta x$ with $v_x = 0$:

$$\Delta x = -\frac{v_{x0}^2}{2a_x}$$

(a) The distance is proportional to $v_{x0}^2$. Doubling the speed makes the distance **4 times** as large.

(b) From $t = \dfrac{v_x - v_{x0}}{a_x} = -\dfrac{v_{x0}}{a_x}$, the time is proportional to $v_{x0}$. Doubling the speed makes the time **2 times** as large.

(c) The original braking: $a_x = \dfrac{0 - 20^2}{2(40)} = -5$ m/s². At 40 m/s:
$\Delta x = \dfrac{0 - 40^2}{2(-5)} = 160$ m (which is $4 \times 40$ ✓), and $t = \dfrac{0 - 40}{-5} = 8$ s (which is $2 \times 4$ ✓).

Why it matters: this is why higher speeds are so much more dangerous. Twice the speed needs four times the road.

### 7 *(Type D)*

Both start from rest, so $v_x = a_x t$, $\Delta x = \tfrac12 a_x t^2$ and $v_x^2 = 2a_x\Delta x$.

(a) Same time: $v_x = a_x t$ is proportional to $a_x$, so B's speed is **2 times** A's. $\Delta x = \tfrac12 a_x t^2$ is also proportional to $a_x$, so B's distance is **2 times** A's.

(b) Same distance: $v_x = \sqrt{2a_x\Delta x}$ is proportional to $\sqrt{a_x}$, so B's speed is **$\sqrt{2} \approx 1.41$ times** A's. (Doubling the acceleration does *not* double the speed at a given distance.)

### 8 *(Type E)*

Starting from rest, $x = \tfrac12 a t^2$.

(a) Graph **$x$ against $t^2$**. The equation then has the form $y = (\text{slope}) \times u$, a straight line through the origin.

(b) The slope equals $\tfrac12 a$, so the **acceleration is twice the slope**.

(c) Compute $t^2$: 0.25, 1.00, 2.25, 4.00 s². Each ratio $x/t^2$ is $0.40$ m/s², so the slope is $0.40$ m/s² and

$a = 2(0.40) = 0.80$ m/s².

(d) Every measurement has some error. A best-fit line through all the points averages those errors out, and a point that is off stands out visibly instead of silently ruining the answer.

### 9 *(Type A)*

(a) $v_x = v_{x0} + a_x t$:

- at $t = 2.0$ s: $12 + (-3.0)(2.0) = +6$ m/s
- at $t = 6.0$ s: $12 + (-3.0)(6.0) = -6$ m/s (now moving in the $-x$ direction)

(b) $\Delta x = v_{x0}t + \tfrac12 a_x t^2 = (12)(6.0) + \tfrac12(-3.0)(6.0)^2 = 72 - 54 = +18$ m.

(c) The cart stops and turns around when $v_x = 0$, at $t = 12/3.0 = 4.0$ s. Its position then is $(12)(4) + \tfrac12(-3.0)(4)^2 = 48 - 24 = 24$ m. In the last 2 s it comes back $24 - 18 = 6$ m. So the **distance** is $24 + 6 = 30$ m. The displacement (18 m) only compares the start and the end; the distance counts the whole path.

---

## Self-check answers (from the lesson)

1. **$v_x^2 = v_{x0}^2 + 2a_x\Delta x$.**
2. **Speeding up.** Velocity and acceleration both point in the $-x$ direction (same sign).
3. **Slope is the acceleration; area under the line is the displacement.**
4. **3 m/s each second.** That is what 3 m/s² means.
