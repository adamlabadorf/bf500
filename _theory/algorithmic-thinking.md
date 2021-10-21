---
title: Algorithmic Thinking
---

1. Problem Spaces
    1. Every problem has an input/problem space and an output/solution/search
       space
    2. A "space" is the set of all possible configurations/combinations of
       an input or output
    3. Algorithms, and more generally functions, provide a mapping from
       coordinates in the input space to coordinates in the output space
    4. Example: a 1D function $$y = x^2$$ maps from the input space of all
       real numbers ($$x \in \mathbb{R}$$) to the output space of all real
       numbers ($$y \in \mathbb{R}$$). $$x = 5$$ is one instance of the problem
       space, and $$x^2 = 25$$ is the mapping the output space.
    5. Example: 
2. Your algorithm explores a search space
    1. Every search space as a *structure*, examples:
        1. Parabola - structure of search space is continuous, regular, convex
        2. Energy landscapes - [protein folding configurations](https://www.researchgate.net/figure/Illustration-of-a-protein-folding-energy-landscape-A-Two-dimensional-representation_fig1_299537797),
           search space is continuous, irregular, but broadly "convex"
        2. Gene-gene interaction network - combinatorial space of all pairs of
           genes
        3. Genetic algorithm - search space is the total set of all possible
           states of a set of N boolean variables ($$N!$$), each mapping to a
           'fitness', discontinuous, irregular
    2. Some algorithms can exploit search space structure to find solutions
       faster
        1. Continuous, differentiable spaces - analytical solutions usually
           exist
        2. Continuous, undifferentiable spaces - numerical methods, e.g.
           gradient descent
        3. Discrete, regular spaces -
