---
layout: post
lead: Tyler, Jeremy
title: Functional Programming with Datalog
paper: ./papers/functional-programming-datalog.pdf
---

## Summary

We love Datalog. However, it is not easy to write and maintain large, complex
Datalog programs. "Functional Programming with Datalog" presents a small
functional language that compiles to Datalog rules; these rules can be
evaluated efficiently by existing Datalog engines like
[Soufflé](https://souffle-lang.github.io/) and
[IncA](https://dl.acm.org/doi/10.1145/3453483.3454026). The core language
supports mututally recursive functions, if expressions, and variable bindings,
and uses the standard *demand transformation* to "control" the flow of
bottom-up evaluation. The language is extended first to support algebraic data
types (ADTs); then to support first-class sets, and first-class functions (via
*defunctionalization*). To evaluate their implementation, the authors write
various program analyses and an interpreter for the untyped lambda calculus.

## Suggested reading strategy

<style>
  .rd-strat {
    border-collapse: collapse;
  }

  .rd-strat td, .rd-strat th {
    vertical-align: top;
    padding: 6px;
  }

  .rd-strat th {
    text-align: left;
  }

  .rd-strat tr:first-child td {
    border-top: 1px solid;
  }

  .rd-strat tr td {
    border-top: 0.5px solid gray;
  }

  .rd-strat td:nth-child(2), .sc {
    font-variant: small-caps;
  }

  .rd-strat {
    margin-top: 8px;
  }

  #only-read:checked ~ * tr[data-not-read] {
    display: none;
  }
</style>

<table class="rd-strat">
  <input type="checkbox" id="only-read"/>&nbsp;
  <label for="only-read">Hide sections not labeled "Read"</label>
  <thead>
    <tr>
      <th colspan="2" width="25%">Section</th>
      <th>Strategy</th>
      <th>Summary / Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.</td>
      <td>Introduction</td>
      <td markdown="span">**Read thoroughly**</td>
      <td markdown="span">
        Motivates the problem well; provides a good high level overview.
      </td>
    </tr>
    <tr>
      <td>2.</td>
      <td>Datalog Frontends: State of the Art</td>
      <td markdown="span">Read</td>
      <td markdown="span">
        Constrasts the paper's approach with existing work, and suggests that
        Datalog could become an internal representation (IR) for future
        languages to target.
      </td>
    </tr>
    <tr>
      <td>3.1</td>
      <td>Compilation by example</td>
      <td markdown="span">**Read thoroughly**</td>
      <td markdown="span">
        Presents the core language with a motivating example.
        See the notes for [background on
        range-restriction.](#range-restriction)
      </td>
    </tr>
    <tr data-not-read>
      <td>3.2</td>
      <td>Translating functional programs to Datalog, technically</td>
      <td markdown="span">Skim / skip</td>
      <td markdown="span">
        Technical details on how to compile <span
        class="sc">functional&nbsp;IncA</span> to Datalog. See the notes for an
        explanation of [Figure&nbsp;5.](#figure-5)
      </td>
    </tr>
    <tr>
      <td>3.3</td>
      <td>Demand-driven bottom-up evaluation</td>
      <td markdown="span">**Read thoroughly**</td>
      <td markdown="span">
        Overview of the demand transformation. The demand transformation was
        presented in the <span class="sc">[Slog](2024-02-14-slog)</span> class
        and a precursor was presented as <span class="sc">[Magic
        Sets](2024-02-05-datalog#magic-sets)</span> in the Datalog lecture.
        </td>
    </tr>
    <tr>
      <td>4.1</td>
      <td>Compiling user-defined data types by example</td>
      <td markdown="span">**Read thoroughly**</td>
      <td markdown="span">
        Overview of technique, and example with `plus` and `twice` for Peano
        numbers encoded in an ADT (`0 = Zero()`, `1 = Succ(Zero())`, etc.).
      </td>
    </tr>
    <tr data-not-read>
      <td>4.2</td>
      <td>Extending functional IncA with ADTs</td>
      <td markdown="span">Skim / skip</td>
      <td markdown="span">
        Technical details on how to extend <span class="sc">functional
        IncA</span> to support Algebraic Data Types.
      </td>
    </tr>
    <tr>
      <td>5</td>
      <td>Case study: Type Checking, Type Erasure, and Interpretation</td>
      <td markdown="span">Read</td>
      <td markdown="span">
        Description of type checker and interpreter written in <span
        class="sc">functional IncA</span> with ADTs.
      </td>
    </tr>
    <tr data-not-read>
      <td>6</td>
      <td>Mixing functions and relations</td>
      <td markdown="span" style="overflow-wrap: break-word;">
        Skim; read 6.3 (pg.&nbsp;20) if you are interested in defunctionalization
      </td>
      <td markdown="span">
        Motivation, overview, and technical description on how to encode set
        objects in <span class="sc">functional IncA</span> as relations in
        Datalog.
      </td>
    </tr>
    <tr>
      <td>7</td>
      <td>Case Studies: Data-Flow Analyses and Clone Detection</td>
      <td markdown="span">Read</td>
      <td markdown="span">
        Description of flow-sensitive reaching definitions and interval
        analyses; clone detection of Java bytecode, written in <span
        class="sc">functional IncA</span>.
      </td>
    </tr>
    <tr>
      <td>8</td>
      <td>Implementation and Performance Evaluation</td>
      <td markdown="span">Read</td>
      <td markdown="span"></td>
    </tr>
    <tr data-not-read>
      <td>9</td>
      <td>Related work</td>
      <td markdown="span" style="overflow-wrap: break-word;">
        Skim
      </td>
      <td markdown="span">
        Comparisons to and background for <span class="sc">Flix</span>, <span
        class="sc">Formulog</span>, <span class="sc">Datafun</span>, <span
        class="sc">Soufflé</span>, and <span class="sc">Dedalus/Bloom</span>.
      </td>
    </tr>
    <tr data-not-read>
      <td>10</td>
      <td>Conclusion</td>
      <td markdown="span" style="overflow-wrap: break-word;">
        Skip
      </td>
      <td markdown="span">
      </td>
    </tr>
  </tbody>
</table>

## Notes

### Range-restriction

Section 3.1 of the paper presents a factorial function that does not terminate
because it is not range-restricted.

```
fact(n, out) := n = 0, out = 1
fact(n, out) := n != 0, fact(n-1, out'), out = n * out'
```

While the paper is not wrong---the computation would not terminate in Soufflé
because `fact` is not range restricted---this is in our opinion is a confusing
example. The reason is because one could imagine a Datalog implementation where
`n-1` is not an entirely different constant than `n`, but rather a lookup into
an infinite `successor` relation:

```
fact(n, out) := n != 0, successor(k, n), fact(k, out'), out = n * out'
```

in which case `fact` would indeed be range-restricted. However, bottom-up
computation of e.g. `fact(5)` would still not terminate because the `successor`
relation has infinite size.

#### Intuition for range-restriction

Consider the model-theoretic semantics of Datalog. Recall that the Herbrand
universe $\mathcal{U}$ of a Datalog program $P$ is the set all non-variable
constants appearing in $P$, while the Herbrand base $\mathcal{B}$ is a set
containing predicates with their variables replaced with all possible values in
the the Herbrand universe $\mathcal{U}$. For example, given the Datalog program

```
edge(1, 2) :-
edge(2, 3) :-
edge(3, 4) :-

P(x, y) :- edge(x, y)
P(x, y) :- P(x, y), edge(y, z)
```

The Herbrand universe $\mathcal{U}$ is $\mathcal{U} = \\\{1, 2, 3, 4\\\}$ and the Herbrand base
$\mathcal{B}$ is:

$$
\def\E{\texttt{edge}}
\def\P{\texttt{path}}
\mathcal{B} = \left\{\;
\begin{alignat*}{3}
  &\E(1, 1),\;\;    &\E(1, 2),\;\;    &\E(1, 3)\;\;    &\E(1, 4) \\
  &\E(2, 1),\;\;    &\E(2, 2),\;\;    &\E(2, 3)\;\;    &\E(2, 4) \\
  &\E(3, 1),\;\;    &\E(3, 2),\;\;    &\E(3, 3)\;\;    &\E(3, 4) \\
  &\E(4, 1),\;\;    &\E(4, 2),\;\;    &\E(4, 3)\;\;    &\E(4, 4) \\
  &\P(1, 1),\;\;    &\P(1, 2),\;\;    &\P(1, 3)\;\;    &\P(1, 4) \\
  &\P(2, 1),\;\;    &\P(2, 2),\;\;    &\P(2, 3)\;\;    &\P(2, 4) \\
  &\P(3, 1),\;\;    &\P(3, 2),\;\;    &\P(3, 3)\;\;    &\P(3, 4) \\
  &\P(4, 1),\;\;    &\P(4, 2),\;\;    &\P(4, 3)\;\;    &\P(4, 4) \\
\end{alignat*}
\;\right\}
$$

An *interpretation* $I$ of a Datalog program $P$ is a subset $I \subseteq B$,

and a model $M$ is an interpretation where every rule is satisfied over
substition of the rule's variables with constants from $\mathcal{U}$. That is,
every model of $P$ must satisfy the following (combinatorially many) sentences:

$$
\begin{align*}
  \E(1, 2) \\
  \E(2, 3) \\
  \E(3, 4) \\
\end{align*}
$$

$$
\begin{align*}
  \E(1, 1) &\rightarrow \P(1, 1) \\
  \E(1, 2) &\rightarrow \P(1, 2) \\
  \E(1, 3) &\rightarrow \P(1, 3) \\
           &\ldots               \\
  \E(2, 1) &\rightarrow \P(2, 1) \\
  \E(2, 2) &\rightarrow \P(2, 2) \\
           &\ldots               \\
  \E(4, 3) &\rightarrow \P(4, 3) \\
  \E(4, 4) &\rightarrow \P(4, 4) \\
\end{align*}
$$

$$
\def\AND{\;\wedge\;}
\begin{align*}
  \P(1, 1) \AND \E(1, 1) &\rightarrow \P(1, 1) \\
  \P(1, 2) \AND \E(2, 1) &\rightarrow \P(1, 1) \\
  \P(1, 3) \AND \E(3, 1) &\rightarrow \P(1, 1) \\
  \P(1, 4) \AND \E(4, 1) &\rightarrow \P(1, 1) \\
  \P(1, 1) \AND \E(1, 2) &\rightarrow \P(1, 2) \\
  \P(1, 2) \AND \E(2, 2) &\rightarrow \P(1, 2) \\
                         &\ldots               \\
  \P(2, 1) \AND \E(1, 1) &\rightarrow \P(2, 1) \\
  \P(2, 2) \AND \E(2, 1) &\rightarrow \P(2, 1) \\
                         &\ldots               \\
  \P(4, 3) \AND \E(3, 4) &\rightarrow \P(4, 4) \\
  \P(4, 4) \AND \E(4, 4) &\rightarrow \P(4, 4) \\
\end{align*}
$$

Note that most of the above sentences are trivially satisifed because their
antecedent is false (for example, $\E(1, 1) = \texttt{false}$, which means the
minimal model excludes $\P(1, 1)$, since its antecedent is never satisfied).

However, what happens if we add a rule whose head has an unbound variable, like
`bad(x, y, n) :- edge(x, y)`? This injects even more sentences into the set
of sentences a model has to satisfy:

$$
\def\B{\texttt{bad}}
\begin{align*}
  \E(1, 1) &\rightarrow \B(1, 1, 1) \\
  \E(1, 1) &\rightarrow \B(1, 1, 2) \\
  \E(1, 1) &\rightarrow \B(1, 1, 3) \\
  \E(1, 1) &\rightarrow \B(1, 1, 4) \\
  \E(1, 2) &\rightarrow \B(1, 2, 1) \\
  \E(1, 2) &\rightarrow \B(1, 2, 2) \\
  \E(1, 2) &\rightarrow \B(1, 2, 3) \\
  \E(1, 2) &\rightarrow \B(1, 2, 4) \\
           &\ldots                  \\
\end{align*}
$$

and in particular, since our model must satisfy the sentences with $\E(1, 2)$
or $\E(2, 3)$ or $\E(3, 4)$ in the antecedent, the minimal model must contain
many "useless" facts $\B(1, 2, 1), \B(1, 2, 2), \B(1, 2, 3), \ldots$, and so
on. In addition, if the Herbrand universe is not finite (e.g. it contains all
integers), the minimal model could be infinite, and a bottom up evaluation
would never terminate!

This is the motivation behind range-restriction. A rule is range-restricted
if every variable in the head is bound in the body. Intuitively, for every
rule, the facts generated by that rule must have constants constants that
appear in some relation in the body of the rule. Thus, the sizes of the body
relations serve as a bound on the size of the head relation, and if the body
relations have finite size, then the head relation also has finite size.

### Figure 5

Translating an expression in <span class="sc">functional IncA</span> to Datalog
results in a set of tuples. It is a set containing tuples $(t, a)$, where
the expression evaluates to value $t$ if the conditions in $a$ are satisfied.
$a$ is a collection of Datalog antecedents, and can be roughly thought of
encoding the "control-flow" paths (branches, function calls) the program must
take in order to evaluate to $t$.


For example, the rewrite rule for `if` is the union of two sets. The first set
denotes the possible values the entire if-expression could evaluate to if the
condition is true. This requires that $t_1$ evaluates to $\textsf{true}$,
guarded by its own guards $a_1$. The resulting value $t_2$ must also be guarded
by its own tuples $a_2$ (consider an if expression nested within another if
expression). The second set is analogous, except for the false case.
The union of both sets represents all possible values the entire expression
might evaluate to in either case.

### Reading questions

### Discussion questions



See also:
- [The demand transformation](https://dl.acm.org/doi/abs/10.1145/1836089.1836094)
- [Magic sets](https://dl.acm.org/doi/10.1145/28659.28689)
