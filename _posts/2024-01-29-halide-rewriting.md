---
layout: post
lead: Federico, Manish, Charles
title: Verifying and Improving Halide’s Term Rewriting System with Program Synthesis
paper: ./papers/verifying-halide-trs.pdf
---


We begin with a high-level summary of the paper, some questions to guide your reading, and some discussion questions. At the end of the document, we cover some background that may help readers understand the details of the approach that are related to program verification and synthesis.

### Summary

The Halide compiler improves performance and proves properties about code using a term rewriting system, which consists of over 1000 handwritten rules, applied greedily. However, these rules are not formally proven to be correct, nor is the rule application algorithm proven to terminate. The main contributions of the work include:

___Formal Verification___: Using an SMT solver and the proof assistant Coq, the authors prove the correctness of existing rewrite rules and termination of the rewriting system. The termination proof relies on a formalization of the rewrite strategy (a reduction order). After amending 8 rules, they are able to construct a reduction order and prove termination.

___Automatic Rule Synthesis___: An automatic program synthesis system is developed to create new, provably correct rules that fix failure cases of the current TRS. The reduction order limits synthesis to rules that rewrite expressions in a useful direction, and an SMT solver is used to check that the LHS is equal to the RHS. Candidate rule LHS are enumerated and pruned heuristically, aiming for shorter terms that could match a portion of the input expression. Rule RHS are generated via 1) “delayed” AC matching, where associativity and commutativity are applied to the LHS, and the resulting term is passed to the existing TRS, and 2) CEGIS [^2], where the LHS is superoptimized. The authors use synthesis to generate 4127 new rewrite rules, which significantly reduce memory usage of compiled programs while barely increasing compile time. They also show that their system can synthesize 58% of existing rules (that are supported by the synthesizer implementation) when matching expressions are provided as input.

___Bug Fixes and Improvement___: The authors identify and fix a number of incorrect rules. The synthesizer is also shown to produce more general rules than developers did in a case study of five PRs that added rules to Halide’s TRS.

Overall, the authors show that formal verification and synthesis can be used to improve existing unsound or insufficiently general rules and that they can also generate new rules that significantly improve the performance of compiled code (such as reducing memory usage by up to 50%).


## Reading Questions
1. How does Halide utilize its term rewriting system? Is there one set of rules that is universally useful to all applications? 
2. Why does Halide use a custom simplification algorithm? What are the benefits of this algorithm?
3. How is the synthesis algorithm different from the Knuth-Bendix completion algorithm?
4. Summarize the termination proof provided in this paper.
5. Compare the effectiveness of AC matching and CEGIS (see background section below) for rule RHS synthesis.


## Discussion Questions
1. The authors removed/modified 8 rules from the Halide TRS in order to construct a reduction order. What might these rules have looked like?
2. Does this work provide evidence that synthesizing rewrite rules is better than handwriting them? If so, is the evidence convincing?
3. The paper makes an interesting point that the TRS is used to prove properties (expr) true AND false. What could be the advantage of having separate TRS rulesets for these two cases?
4. Are there any aspects of Halide’s TRS that the authors did not study but should have?

----

### Additional Non-Rewriting Background

__Satisfiability modulo theories (SMT) solvers and verification.__ SMT) solvers are tools that determine if a given first-order formula `φ`, which has no free variables and uses symbols from certain background theories, is valid. They return "Yes" if the formula is valid and "No" otherwise.

SMT solvers are good at queries of the form `∃x φ(x)` where `φ` is a quantifier-free formula. They can prove "Yes" by finding a satisfying assignment for the existentially bound variables or "No" by deriving a contradiction using resolution. The Conflict-Driven Clause Learning (CDCL) algorithm [^3] is particularly effective for this purpose.

However, SMT solvers struggle with queries containing universal quantifiers (`∀`). For a query like `∀x φ(x)`, where `φ(x)` is quantifier-free, solvers attempt to prove "No" by generating many instances of the formula and looking for contradictions. This is based on Herbrand's theorem [^4] and may terminate if the answer is "No," but it can run indefinitely if the answer is "Yes," except in certain special theories.

In the context of the paper, the SMT solver is used to answer questions like `∀x LHS[x] = RHS[x]`. But from above, we know this is a hard problem, but the authors circumvent it by instead asking `∃x LHS[x] ≠ RHS[x]`. If the solver returns "No" for this negated query, the original query is valid, meaning the rewrite rule `LHS -> RHS` is correct. If it returns "Yes", the provided witness serves as a counterexample, indicating the rewrite rule is incorrect. This check-the-negation strategy is a common technique in modern verification engines.

__Counterexample guided inductive synthesis (CEGIS).__ Classic CEGIS algorithms combine a “tester”, a “verifier”, and an “enumerator” to generate a correct program from a formal specification. For this paper, we can think of the RHS of a rewrite rule as the desired program, and we can think of the input formal spec as “is equal to a given LHS”. In this paper, they use __Sketch__ [^2] as the “enumerator” and the “tester,” but it is easier to understand CEGIS when these are distinct.
1. The “enumerator” generates program guesses, often by just traversing a context-free grammar that describes the set of possible programs. 
2. The “verifier” takes a candidate program and verifies it against the formal specification (see the background section on SMT for how this works). If the program is correct, then the CEGIS algorithm returns that program. Otherwise, a counterexample is generated.
3. Verification can be expensive, so CEGIS algorithms usually try to avoid calling verification engines where possible. Here, a “tester” runs tests to quickly rule out a guessed program. But where do we get tests from? We can use the counterexamples generated by the verifier!

In this paper, Sketch is used to generate guesses that satisfy the tests, i.e., both the “enumerator” and the “tester.”


[^1] Solar-Lezama, A., Jones, C.G. and Bodik, R., 2008, June. Sketching concurrent data structures. In Proceedings of the 29th ACM SIGPLAN Conference on Programming Language Design and Implementation (pp. 136-148).

[^2] Solar-Lezama, Armando. "The sketching approach to program synthesis." Asian symposium on programming languages and systems. Berlin, Heidelberg: Springer Berlin Heidelberg, 2009.

[^3] Marques-Silva, Joao P., and Karem A. Sakallah. "GRASP: A search algorithm for propositional satisfiability." IEEE Transactions on Computers 48.5 (1999): 506-521.




