---
layout: post
lead: Sora, Eric
title: "Achieving High Performance the Functional Way: Expressing High-Performance Optimizations as Rewrite Strategies"
paper: ./papers/high-perf-the-functional-way.pdf
---

### Problem: 
Mixing hardware-specific optimizations with functionality-concerned code presents a huge challenge to portability across hardware. Existing approaches to separating optimizations rely on developer-written API calls, in which users 1. have limited ability to inspect and reason about 2. can't easily build and reuse higher abstractions 3. have difficulty separating optimizations from functionality because these optimizations are written within the same program and scope. 

### Solution: 
In short, the solution is functional programming. Authors apply a functional paradigm to the scheduling process itself, which allows users to express optimizations via rewrite rules in a functional language, which, they argue, avoids the issues listed above. Importantly, they allow the expression of 1. Rewrite rules as strategies 2. Transformations of strategies as traversals. Authors present two functional languages: RISE, a language for expressing data-parallel algorithms, and ELEVATE, a language for describing optimization strategies in the form of rewrite rules. 

We see the main contribution as providing 1. A high-level functional language, RISE, which allows programmers to succinctly express high-dimensional array computations with a focus on intent and functionality. 2. A functional language, ELEVATE, in which programmers dictate how high-level RISE primitives are re-written to low-level RISE primitives. 3. **a set of low-level RISE primitives** and a *strategy preserving* code generator for those primitives. Ultimately, this separates both the algorithm and scheduling concerns for the programmer, but also separates the compilation process into discrete optimization and code generation steps. 

Some things to look out for as you read the paper: 
1. Pay attention to how authors *normalize* programs, relying on a initial rewrite step to put programs into a standard form (the *data-flow normal form*). The algorithm is explained in much greater detail in the full paper (linked below), but the big idea is that we have to do some significant transformation on the programs initially to get them into a suitable form for later pattern matching. 
2. Spend some time looking at how *traversals* are used to dictate where and when rewrite rules are applied. For instance, see how they can implement the “tryAll” strategy using their fairly simple primitives, which allows them to describe fairly complex behavior about how specific rewrites are each applied. 
3. Think through how each of the goals the authors outline (1. Separation of concerns, 2 facilitating reuse, 3. Enabling composability, 4. Allow reasoning, 5. Making explicit) are accomplished, and which design choices influence these factors. 

## Questions For Discussion:

1. Comparing this paper to “Playing by the Rules”, does this paper implement a rewriting system which addresses some of the earlier paper’s shortcomings?
 a. In particular, to our discussion last Wednesday of the three “roles” of end-user programmer, library designer, and compiler engineer, how does this paper construe these three roles? What design decisions do they make which influence the separation (or lack thereof) between these roles? 
 b. What specific skills or knowledge does this system presuppose of the programmer? 
2. How does ELEVATE decide the priority of rewrite rules? (Hint: the programmer defines it explicitly). How should we be thinking about termination here? What are the pros/cons of thinking about rewrite priority this way? 
 a. The authors indicate that a type system could address some of these issues - do you think so? 
3. One of the big concerns of the authors is in separating the algorithm from the schedule, citing the case with TensorFlow where programmers have to change the algorithm in response to the scheduling code, breaking the separation of concerns. Do the authors here actually get out of this? Does writing a good RISE program already require some kind of mental model of how it will be rewritten in ELEVATE, and if so, have we made optimization conceptually easier for programmers actually? 

For more information, you can also check out the full-length version of this paper: https://bastianhagedorn.github.io/files/publications/2020/ICFP-2020.pdf 

See also this short commentary on the paper:
[Reconsidering the Design of User-Schedulable Languages](https://dl.acm.org/doi/pdf/10.1145/3580370).
Also, see a 
 bigger [survey of rewriting strategies](https://inria.hal.science/hal-01143486/file/HK-RewStrat.pdf)
 or a recent paper on
 [formal semantics for strategies](https://michel.steuwer.info/files/publications/2024/POPL-2024-1.pdf).
