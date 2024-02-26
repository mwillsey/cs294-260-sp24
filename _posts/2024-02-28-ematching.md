---
layout: post
lead: Federico, Jacob, Jiwon
title: "Efficient E-matching for SMT Solvers"
paper: ./papers/efficient-ematching.pdf
---

## Summary
SMT solvers are good at “ground reasoning” (solving boolean combinations of formulas with no free or bound variables). To support quantifiers, these solvers need to somehow connect quantified formulas (which are not ground since they contain bound variables) to ground formulas. One (now) standard way to do this is to treat universal (existential) quantifiers as infinite conjunctions (disjunctions) of ground formulas (each called an instance of the quantifier) and then heuristically selecting a subset of these instances to include in the ground reasoning. This paper goes deep into the nitty gritty details of the heuristic selection process used by Z3 and how it is efficiently implemented.

At a high-level, the heuristic selection process works as follows for a single quantified formula. First, take subterms from the body of the quantified formula to be patterns (the bound variables become the pattern variables). Second, search the e-graph built from the currently asserted set of ground formulas for terms that match the previously collected patterns. Each match will be demonstrated by a substitution. Finally, select the ground formulas obtained by applying these substitutions to the body of the quantifier. This approach is based on [[1](https://www.hpl.hp.com/techreports/2003/HPL-2003-148.pdf)] (and there is a healthy amount of copy-pasting to show it). The main novel contributions seem to be (1) improving the empirical performance of matching using code trees and (2) improving the empirical performance of <ins>incremental</ins> matching using inverted path indices.

### E-matching code-trees
The main idea is to compile sets of patterns into instructions by partially evaluating the matching algorithm [[2](https://pdfs.semanticscholar.org/d63e/9e8d1e89841a327a91dfb1c90985af3b7675.pdf)]. Code trees are used to remove redundant work when dealing with multiple patterns, offering performance improvements over a naive approach. When the solver encounters a quantified formula, a pattern is added to a “code tree” with branching instructions. Instructions that match with multiple patterns are encoded in the same node, allowing for compact representation of a set of patterns. The paper formulates an algorithm for inserting patterns into this tree. Instead of matching a term individually against each pattern, the term is used to “run” the code tree, which matches with a set of multiple patterns at once. “Running” a code tree on a term (from your ground terms) will generate (repeatedly yield) substitutions that demonstrate how a pattern (from the set of patterns represented by the code tree) matches that input term.

### Incremental matching
Even with code-trees, a set of instructions introduces a lot of redundant matching processes. To decrease the number of matching to perform, the authors integrated optimization techniques from the Simplify prover [[1](https://www.hpl.hp.com/techreports/2003/HPL-2003-148.pdf)]. We are interested in finding relevant terms and patterns producing new matches for union operation. When *union(t1,t2)* is executed, ancestors of *t1* and *t2*’s set of congruent terms might change. The mod-time optimization finds relevant terms by marking the already checked terms to prevent redundant matching and pattern-element optimization finds relevant patterns by looking at the relation of terms *t1* and *t2*, such as *parent-child* or *parent-parent*. However, mod-time and pattern optimization still introduce redundant matches. The authors introduce inverted path string for further optimization. The inverted path string can be thought of as a path to the term from the subterm of interest. By collecting all the terms that can be reached from the subterm we can identify all relevant terms for the new matches and using the prefix of the inverted path string we can identify which pattern matching can be skipped.

## Suggested Reading Strategy
Watch [[5](https://youtu.be/GOE9CpqXOHw?feature=shared)] at 14:55 for an overview of the SMT architecture and at 25:43 for a high-level summary of this paper. Do this before reading the paper and watch it at 1.5x.

Read Section 5 of [[1](https://www.hpl.hp.com/techreports/2003/HPL-2003-148.pdf)] until just before Section 5.1 instead of (or along with) Section 2.1 of the paper. It is longer but more clear.

Spend all your energy reading Sections 5 and 6 so that you can explain them to us (half joking but it is really tough, don’t feel bad if it doesn’t make that much sense. Do your best.). Go through the example on slides 39 to 57 of [[7](https://leodemoura.github.io/files/SAT-SMT-2012.pdf)].

Skip Section 6. 

The last 6 rows of Fig. 11 are the best part of the evaluation. Focus on that and work backwards on your second read of the paper. I think it is worth doing a first read following the order laid out in this guide first.

## Reading Questions
- What’s the deal with free variables? What happens to them? 
- What instances would be selected for the quantified formula  $\forall x P(x + 1)$ using the pattern $x + 1$ if the currently asserted set of ground formulas is ${P(1 + a)}$? Would we be able to prove $(\forall x P(x+1)) \Rightarrow P(1+a)$ with that set of instances? Why or why not?
- If we trigger the matching process every time that a new ground term is created, then we may enter an infinite loop. Can you give an example formula and pattern that demonstrates this?

## Discussion Questions
- Which optimizations were impactful empirically? Why do you think this is? What could they have evaluated that they didn’t? What numbers would you have liked to see?
- How impactful is the pattern, what is their strategy, and what else could you do to get these patterns? What makes a “good” pattern?
- Is this the only way to do quantifier instantiation? What other ways can you think of that might be fun to try? What would be the tradeoffs? In other words, if e-matching is NP-Hard, do we really need to do it?

## References
[1] https://www.hpl.hp.com/techreports/2003/HPL-2003-148.pdf 

[2] [Leo's slide](https://pdfs.semanticscholar.org/d63e/9e8d1e89841a327a91dfb1c90985af3b7675.pdf)

[3] [paper](https://www.cs.upc.edu/~oliveras/dpllt.pdf)

[4] [Andrew's slide](https://resources.mpi-inf.mpg.de/departments/rg1/conferences/vtsa17/slides/reynolds-vtsa-part1.pdf)

[5] https://youtu.be/GOE9CpqXOHw?feature=shared (start at 14:55 and 25:43)

[6] https://leodemoura.github.io/files/qsmt.pdf (slide 32)

[7] https://leodemoura.github.io/files/SAT-SMT-2012.pdf (slides 39 to 57)
