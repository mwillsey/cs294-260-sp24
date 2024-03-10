---
layout: post
lead: Jeremy, Charles, Shreyas
title: "Automatic Datapath Optimization using E-Graphs"
paper: "https://arxiv.org/abs/2204.11478"
---

## Background: RTL design and optimization

In hardware design, register-transfer level (RTL) refers to a level at which hardware can be implemented, typically in Verilog. As opposed to using higher-level behavioral descriptions, describing hardware from low-level primitives (those used in this work can be found in Table I) can allow you to extract the maximum performance out of your hardware, by removing ambiguity in how compilers should first take your RTL down to a [netlist](https://en.wikipedia.org/wiki/Netlist) via logic synthesis, then eventually to the physical layout of transistors and wires on a chip. However, this has a number of downsides, such as making it much more difficult to change your design, or adapt to a change in the implementation flow.

In this work, the authors focus on optimizing “datapaths,” which in this work refers to combinational design that do not use clocks (and therefore do not need to deal with the added complexity of synchronizing operations across multiple time steps), and mostly deal with arithmetic and logic operations without complex control structures. This allows the authors to use a limited set of operators, as well as cut the key metrics down to two: combinational logic delay and area (a proxy for only area is used during extraction). One key prior work to consider is that of Verma, Brisk and Ienne, which is cited frequently throughout the paper and is a frequent point of comparison. This work specifically optimizes carry-save representation in arithmetic circuits, i.e. they construct circuits in such a way that takes advantage of certain bit-level characteristics of hardware arithmetic. The hope is that e-graphs can be used to discover such optimizations with a more generally applicable framework. 

## Summary

This paper’s main contribution is applying e-graphs to the problem of datapath optimization. They work on the RTL level, transforming Verilog code into an e-graph and defining arithmetic and logical rewrite rules, which are based on common hardware optimizations and prior, more domain-specific work in RTL optimization. The problem translates into e-graphs quite similarly to previous applications of e-graphs, with the added complication of bitwidth. Each bitvector has a specified width, and this induces constraints on which rewrites can be performed. For instance, for the rewrite rule:    

${\,}_r( _pa \times {\,}_q(_sb + {\,}_tc)) \rightarrow {\,}_r(_u(_pa \times {\,}_sb) + {\,}_v(_pa \times {\,}_tc))$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(left subscripts denote bit width)

The constraint $\min(q, u, v) \geq r$ is applied, so that all the inner bit vectors have enough width to match the output bit vector.  

The other part of the e-graph work is the extraction algorithm. The authors define an ILP encoding, but don’t always use it, opting to use the default egg extraction when possible, for performance reasons. They also define a cost metric for evaluating the cost of individual e-nodes which computes the theoretical area that each operator would take up given the input and output bitwidth. This differs from the area that will actually be synthesized, due to the inherent noise in synthesis tools. However, the performance benefit from using this metric makes this tradeoff worth it. The authors measure this noisiness in Section V, although they do not propose any methods to account for it during optimization. 

In their key evaluation (Table III), the authors compare their optimized RTL design with some baseline. Using the synthesis tool, find the fastest possible delay of the slower design, then compare area with both designs set to target that same delay. Similarly, they find the smallest possible area of the larger design, then compare delay with both designs set to target that same area. The authors provide 5 benchmarks, across multiple prior works. The smoothing kernel is from within Intel, 2 benchmarks are from Verma, Brisk and Ienne, one is the multiple constant multiplication (MCM) problem, and one is a shifted FMA that is introduced because it is not solved by Verma's method. There is one case where area does not improve given the same delay, and one case where delay does not improve given the same area (delay almost doubles in this case, which makes sense given that the authors are not actually directly optimizing delay anywhere). There are also several designs from Verma which are not benchmarked.

## Reading Strategy

As this paper is on the shorter side, we don’t think that there are many sections that can be skipped. That being said, Section **II.B** is background information on e-graphs which follows the same structure we have discussed previously, so it can probably be skipped or skimmed. Section **III** provides some intuition for what is unique about RTL optimization, as this is where they explain the specific rewrites and cost model used. Section **IV** and **V** discuss the evaluation metrics and tradeoffs that are present in the different evaluations they ran, and provide some concrete examples of the optimizations found by the tool. In these sections, the bitwidth dependent optimization (**IV.B**) is interesting because it addresses one of the main challenges associated with implementing hardware at such a low level of abstraction. 

## Discussion Questions
1. This work is an example of when equality saturation is often not reached due to computational limits. The more rewrites are applied, the harder it is to do extraction and take advantage of sharing common sub-expressions, which is one of the main benefits of e-graphs. Does this indicate that rather than focusing solely on extraction, it may actually be just as important to use the right strategy for expanding the space of rewrites? Or does this just degenerate into the compiler phase ordering problem?
2. During extraction, only a proxy for area is used, when it is possible for an area-delay tradeoff to exist in many cases. Also, hardware has the interesting characteristic that in some cases, sharing common subexpressions might be preferred, whereas in some cases duplicating a circuit might actually be advantageous (like in Section IV.A). Would it be possible for such characteristics to be taken into account during extraction?
3. Is there a way to take the noisiness of synthesis into account during optimization? Or a way to use a cost function more grounded in the output of the synthesis tool?

## Follow-on work

E-graphs have many potential applications in hardware, and this Intel group in turn has several papers on the topic. These techniques are most directly applicable to designs heavy in combinational logic, such as floating point units (explored in the DAC paper below) or multipliers (also targeted in a followup work). For more complex designs, high-level synthesis (HLS) refers to automating the lowering of high-level functional descriptions of code (most commonly in C/C++) to optimized RTL. Several such tools exist across industry and academia, and in theory already carry out many of the optimizations done by this work. However, like with software compilers, e-graphs can enable new optimizations, as seen in SEER below.



See also:
- [Combining E-Graphs with Abstract Interpretation](https://arxiv.org/abs/2205.14989), a follow up work by the same authors
- [DAC Paper on similar topic](https://cas.ee.ic.ac.uk/people/gac1/pubs/CowardDAC2023.pdf)
- [SEER: Super-Optimization Explorer for High-Level Synthesis using E-graph Rewriting](https://jianyicheng.github.io/papers/ChengASPLOS24.pdf)

