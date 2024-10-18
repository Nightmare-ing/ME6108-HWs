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
