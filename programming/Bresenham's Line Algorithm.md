(also what's used by GRBL to avoid floating point calculations in straight line interpolation)
https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm



## |Slope| <= 1
Goal: draw a straight line pixel-by-pixel from `(x0, y0)` to `(x1, y1)` where slope <= 1. The ideal line is:

$$y = \frac{y_1-y_0}{x_1-x_0}(x-x_0)+y_0$$
$$f(x, y) = 0 = (\Delta y)x - (\Delta x)y + (\Delta x)y_0 - (\Delta y)x_0$$

Of course, since we can only increment `x` and `y` by interger values, we can't fit the ideal line. When slope <= 1, each time we increment `x` by 1, we decide whether we increment `y` by 1 depending on:
$$D=f(x_0+1, y_0 + 0.5) - f(x_0$$

Step 1: determine which axis to increment
```python
dx = x1 - x0
dy = y1 - y0
xsign = 1 if dx > 0 else -1
ysign = 1 if dy > 0 else -1
dx = abs(dx)
dy = abs(dy)

if dx > dy:
	# increment x
else:
	# increment y
```

$$f(x,y) = (\Delta y)x - (\Delta x)y + (\Delta x)b$$