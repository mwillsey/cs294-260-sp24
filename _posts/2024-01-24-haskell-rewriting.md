---
layout: post
paper: ./papers/haskell-rules.pdf
title: "Playing by the Rules: Rewriting as a practical optimisation technique in GHC"
lead: Tianrui, Shreyas
---

### Summary

Fundamentally, the GHC rewrite system in this paper makes a tradeoff between simplicity and functionality in
favor of practical implementation. Rewrite rules are written in Haskell itself as programmer-defined pragmas
and are constrained to mapping function applications to a presumably simpler RHS. However, there are few
guardrails on board; rules aren’t automatically checked for correctness, confluence, or termination by GHC.
How can this power be wielded safely?

The authors put forward this system mainly as a compiler extension intended for library authors rather than
general users. By design, rules are meant to be easily verified—possibly by feeding them into a theorem
prover. Moreover, compiler metadata can accompany library code and aid in downstream optimization
without the user ever explicitly managing it.

List fusion serves as a nice example with significant practical performance gains. The core idea with the
“short-cut deforestation approach” is to eliminate intermediate list materialization when we find pairs of
“consumer” and “producer” functions; `foldr` and `build`, respectively. `foldr`’s implementation is
straightforward; `build` seems a bit alien with some FP abstractions. Essentially, it abstracts the notion of
“cons” and “nil” list constructors such that “nil” is just a starting value and “cons” incorporates an element
into some amalgamation of elements. The rewrite rule transforms terms where `foldr` is applied to `build`:
we’re able to fold the values as we generate the list, skipping an intermediate allocation.

Here’s the hydrocarbon example annotated so you can see how pairs can be eliminated:

```
foldr (length) -> Int
  build (outer list comprehension) -> [(i_1, j_1, k_1), (i_2, j_2, k_2)...]
    foldr (tuple consumer) -> (i, j k)
      build (multiple list ranges) -> [0...n]
```

Inlining complicates things: we have a phase ordering problem as `foldr` and `build` shouldn’t be inlined,
until their rule can’t be used anymore. We need a “rewrite strategy,” ideally where we start from the top of
the ADT hierarchy, rewrite all we can, inline and repeat at a lower level. Again, in the interest of simplicity,
this system has the programmer specify phases when inlining should happen with respect to the compiler.
However, this isn’t ideal as it requires knowledge of GHC’s phases. Additionally, isolated calls to functions
which use `foldr` and `build` are a performance drain as fusion isn’t possible. As a fail-safe for efficiency, a
“back-out” function definition and corresponding rewrite rule can be added to prevent this.

Moreover, sometimes we want transformations that end up substituting a redex into a lambda body in order
to trigger a `foldr`/`build` rewrite. GHC fights against this with conventional wisdom and prevents fusion,
so we need to identify “one-shot lambdas” where extraction would be useless as it’s only called once
anyway. Type-based analysis for this problem is worth looking into—although a simple hardcoded solution
for `build` works here. Sharing computation in general can prevent fusion in other contexts; one potential
approach is to use a “virtual data type” which the compiler can inline without worrying about sharing. This
section is left open in the paper.

Having established how programmers can write rules, the paper discusses a few ways in which the compiler
can dynamically generate them by performing a local transformation and generating + applying a
corresponding rule. This is particularly useful for specializing functions or cases that are often used, like type-
specification and boxing/unboxing literals. Usage-based specialization is an interesting area to explore
further, as this system provides a clean mechanism to incorporate this information as extra arguments which
can be rule-matched.

The paper concludes with a more involved application in the context of CSPs and outlines the benefits of an
explicit tree-based approach in Haskell with optimizations courtesy of this system. The approach is very
analogous to the earlier list fusion example, only applied to rose tree fusion. Although there is still a slight
performance gap between this and imperative approaches, the extensibility and ease-of-use is a massive
advantage; only 2 components need to be modified: the labeler and pruner, which check and remove nodes
to maintain consistency.

However, the same sorts of issues pop up here. Notably, now inlining list functions should happen after tree
functions (which can be enforced through phase ordering on module dependencies). Additionally, a key
practical note is the need for programmer feedback when there are failures; currently, it’s not always clear
whether these indicate a legitimate no-fusion situation or simply programmer error.

### Reading Questions

1. What form does a rewrite rule take, and what guarantee does it provide?
2. Describe how the approach described in the paper generate dynamic rewrite rules in compiler?
3. Describe how this approach prevents redundant rewrites from being generated.
4. Describe what the original approach to the deforestation paper[^2] is, and how it differs from the
approach described in this paper.
5. How could we provide useful feedback to the programmer about effectiveness and why rules
are/aren’t firing?
6. In what other applications could you use usage-based specializations for compiler-generated rules?
7. How can the compiler use a “virtual data type” to break its conventional wisdom in cases like
sharing?

### Discussion Questions

1. What’s a good way for ordering of rewrites / how to schedule rewrite phases?
2. Describe the Wansbrough[^3] approach to program analysis
3. What would be the appropriate way to perform sharing, with the problem described in[^1]? Future
paper references are possible.
4. How would you compare the dynamic rules generated by compiler with program synthesis based
approaches?
5. (Open Ended) How to deal with side effects?
6. (Open Ended) How can we check the rewrites for correctness/performance?

### Resources

- [Very nice Haskell Rewrite Rules Documentation](https://downloads.haskell.org/~ghc/7.0.1/docs/html/users_guide/rewrite-rules.html)
- [Relatively recent talk about verifying Haskell’s rewrite rules](https://www.youtube.com/watch?v=Z68SseWlxT0)
- [Deforestation even has its own section on the Wiki!](https://wiki.haskell.org/Research_papers/Compilation#Fusion_and_deforestation)

[^1]:
    Conal Elliott, Sigbjørn Finne, and Oege de Moor. Compiling Embedded Languages.

[^2]:
    Andrew Gill, John Launchbury, and Simon L. Peyton Jones. 1993. A short cut to deforestation. In
    Proceedings of the conference on Functional programming languages and computer architecture, July
    1993, Copenhagen Denmark. ACM, Copenhagen Denmark, 223–232. .
    https://doi.org/10.1145/165180.165214

[^3]: 
    Keith Wansbrough and Simon Peyton Jones. 1999. Once upon a polymorphic type. In Proceedings of the
    26th ACM SIGPLAN-SIGACT symposium on Principles of programming languages (POPL ’99), January 01,
    1999, New York, NY, USA. Association for Computing Machinery, New York, NY, USA, 15–28. .
    https://doi.org/10.1145/292540.292545