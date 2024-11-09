# ME6108-HWs

## Homework 1

There are two problems in HW1, one is to draw a line or a circle with
Bresenham algorithm, the other is to implement a required animation.

### Problem 1

I implemented the Bresenham algorithm in the `scanning_algorithm.py` file, 
with the standard serial scanning algorithm and the optimized 
parallel scanning algorithm for line, and the standard serial scanning 
algorithm for circle.

To test the correctness of the parallel algorithm, I wrote tests in 
`tests/test_algos.py` file, to compare the output of the optimized 
algorithm with the standard algorithm. There's also a test for comparing 
the performance of those two algorithms.

I didn't implement the optimized algorithm for scanning a circle.

> **ATTENTION**
> 
> I didn't implement the complete algorithm for supporting lines with all 
> kinds of slopes, especially for the slope less than 0. I just implemented 
> algorithms for lines with slopes greater than 1.

### Problem 2

I implemented the required animation in the `animation.py` file. I didn't 
write it in a very standard way, I just implemented the animation in a 
script file.

You can press any key to stop or continue the animation, but the **SPACE** 
key is recommended.

### Running

I only implement the terminal UI, so you just run the `main.py`, and input as the terminal prompted.
The demo is shown as following

![Demo](HW1/demo/UI_demo.gif)

An example with starting point $(6, 6)$ and $(20, 10)$ is shown as following:

![Example](HW1/demo/demo_line.png)

An example with center $(10, 10)$ and radius $5$ is shown as following:

![Example](HW1/demo/demo_circle.png)

A recording for Problem 2 is shown as following:

![Recording](HW1/demo/demo_animation.gif)

## Homework 2

Homework 2 requires to draw the Three View and the Isometric View of an object.
The coordinates of the vertex of the object are given in the `data*.
csv` file under the `HW2/data` directory.

Linear transformation algorithm is implemented in `HW2/trivs.py`, and the main 
script is in `HW2/main.py` for interacting with 
user input, and the `drawer.py` are for drawing the transformed figure.

The demo of user interface is shown as following:

![HW2 Demo](HW2/demo/HW2_demo.gif)

The Three View of the `data1.csv` is shown as following:

![Three View of data1](HW2/demo/data1_three_view.png)

The Isometric View of the `data1.csv` is shown as following:

![Isometric View of data1](HW2/demo/data1_iso.png)

The Three View of the `data2.csv` is shown as following:

![Three View of data2](HW2/demo/data2_three_view.png)

The Isometric View of the `data2.csv` is shown as following:

![Isometric View of data2](HW2/demo/data2_iso.png)

## Homework 3

HW3 requires to draw the Mandelbrot Set. I use python script to implement this.
First mesh the drawing region to a grid, and then calculate the Mandelbrot Set for each grid point.
You can change the parameters in the `HW3.py` file to draw different Mandelbrot Set.
The color based on the number of iterations within $\lvert z_n \rvert <= 2$, 
and I 
also write a function to normalize this 
number to RGB color value.

Some examples are shown as following:

![figure 1.png](HW3/demo/figure%201.png)

![figure 2.png](HW3/demo/figure%202.png)

![figure 3.png](HW3/demo/figure%203.png)

![figure 4.png](HW3/demo/figure%204.png)

![figure 5.png](HW3/demo/figure%205.png)
