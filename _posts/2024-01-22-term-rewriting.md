---
layout: post
type: lecture
---

Equational reasoning 
 is a powerful technique in programming languages and many other domains.
In essence,
 you have a set of equations and you are interested 
 in the consequences of these equations.
Maybe you want to prove that two expressions are equal,
 or maybe you want to simplify an expression.

Term rewriting is the 
 most common mechanism for equational reasoning;
 it's the basis of 
 optimizing compilers,
 theorem provers,
 computer algebra systems,
 and many other systems that need to reason about programs.

The purpose of this lecture is to give a (rather quick)
 introduction to term rewriting,
 so we can discuss various applications via papers in later discussions.

## Basics

For the purposes of this lecture,
 we will skip the formal definition of a term
 and just say they are composed of 
 *functions*, *constants*, and *variables*
 in the usual way.
For example,
 $f(x, g(a))$ is a term with function $f$,
 variable $x$ (we'll use $x, y, z$ for variables),
 and constant $a$ (we'll use $a, b, c$ for constants).
If a term has no variables,
 it is called a ground term.
If it has variables,
 we may also call it a "pattern".

A *rewrite rule* or *rewrite* 
 between two terms $l$ and $r$
 is written $l \to r$.
Intuitively,
 applying rewrite $l \to r$ to a term $t$
 replaces an instance of $l$ in $t$ with $r$.

Which instances of $l$ are replaced?
Typically, we think of rewrites as
 non-deterministically choosing 
 an instance of $l$ to replace.
A later topic of this lecture will be
 *strategies*,
 which give the user more control over
 not only when to use which rewrite,
 but also how it may apply in a given term. 

If we want to refer to a specific application of a rewrite,
 $l \to r$, applied to $t$,
 then we can use a 
 the notions of a substitution and context.
A *substitution* $\sigma$ is a 
 mapping from variables in the rewrite to subterms of $t$.
We say that a substitution $\sigma$ *unifies*
 two terms $s$ and $t$ if $s\sigma = t\sigma$.
The *context* 
 allows us to refer to a specific location or subterm
 of $t$.[^context]
So a rewrite $l \to r$ to $t$
 means finding a substitution $\sigma$
 that unifies a subterm of $t$ with $l$;
 in other words there is a
 a context $c$
 such that $c[l\sigma] = t$,
 is rewritten to $c[r\sigma]$.

[^context]:
    Some literature uses the concept of a *position* instead of a context. 
    A position is basically a list of directions to a subterm, i.e., 
    in $f(g(a, b, h(c)), d)$, the position $[0, 2, 0]$ refers to $c$.

Here's an example. 
Let's consider the rewrite $x + 0 \to x$.
Let term $t = (a + 0) + (b + 0)$.
Applying our rewrite to $t$,
 could result in a couple different outcomes.
Using the above machinery,
 we can consider only applying the rewrite to the left subterm:

$$
\begin{align*}
    t &= (a + 0) + (b + 0) \\
    c &= \_ + (b + 0) \\
    \sigma &= \{x \mapsto a\} \\
    l\sigma &= a + 0 \\
    r\sigma &= a \\
    &\text{now putting it all together...} \\
    t = c[l\sigma] &= (a + 0) + (b + 0) \\
    &\to \\
    c[r\sigma] &= a + (b + 0)
\end{align*}
$$

Now let's consider a somewhat more interesting rewrite system.
The following set of rewrites allows us to do (a limited form of) symbolic differentiation:[^diff]

[^diff]:
    Example from Term Rewriting and All That, chapter 1.

$$
\begin{align}
    d_X(X) &\to 1 \label{dx} \\
    d_X(Y) &\to 0 \label{dy} \\
    d_X(u + v) &\to d_X(u) + d_X(v) \\
    d_X(u * v) &\to u * d_X(v) + v * d_X(u) \\
\end{align}
$$

What are the limitations of this system?
Well first,
 let's observe that in the above rewrites, 
 capital $X$ and $Y$ are constants.
We cannot use variables here,
 because then rules $\ref{dx}$ and $\ref{dy}$ 
 would be alpha-equivalent,
 and would rewrite *everything* to both 1 and 0!

The next 
 questions we might ask about our
 term rewriting system (TRS) are about its
 termination or confluence.
Both of these properties are desirable
 yet **undecidable** in general.

## Word Problem

One of the big applications of term rewriting
 is to solve the *word problem*.
Given a set of (non-oriented) equations,
 and two terms, are they equal?
A classic example is the theory of groups,
 given by the following equations:

$$
\begin{align}
  (x + y) + z &= x + (y + z) \\
  x + 0 &= x \\
  x + (-x) &= 0 \\
\end{align}
$$

This problem is undecidable in general,
 but if we can find a confluent and terminating TRS,
 then we can solve it!
The idea is to take the two terms,
 and rewrite each to its *normal form*,
 i.e., 
 a term that cannot be rewritten further.
Then, if the two normal forms are the same,
 then the original terms are equivalent.
Note that you need both ingredients 
 for this to be a decision procedure:
- termination gives you the existence of the normal form.
- confluence gives you the uniqueness of the normal form.
 
## Termination

Termination matches its intuitive meaning:
 a TRS terminates if
 there are no infinite sequences of rewrites.
While termination
 is undecidable in general,
 we can still come up with a semi-decision procedure.
The idea is place an order on terms
 such the rewriting always goes down in the order.
If you can additionally prove that
 there are no infinite descending chains
 in the order, then you have termination!

More formally, we can state it as follows:
- A *rewrite relation* has a somewhat complex
  [definition](https://en.wikipedia.org/wiki/Rewrite_order),
  but the gist is that it's a binary relation over terms
  generated by a set of rewrites.
- If that relation is (strictly) ordered,
  then it's a *rewrite ordering*.
- If that ordering is [well-founded](https://en.wikipedia.org/wiki/Well-founded_relation),
  then it's a *reduction ordering*.

Well-foundedness is a key property here;
 it captures the notion that there are no infinite descending chains.
It's typically defined by saying that 
 every non-empty subset has a minimal element.
For reduction orderings,
 a common way to establish well-foundedness
 is by homomorphism to the natural numbers.

Typically, an ordering like "size of term" is too simple
 and doesn't allow all kinds of rewrites.
Consider a TRS with just the rewrite:

$$x * (y + z) \to x * y + x * z$$

This clearly terminates,
 as it "pushes" the multiplication down the tree.
But a simple size ordering or counting of operators
 would not be able to capture this.
Instead, a common ordering is called
 the [path ordering](https://en.wikipedia.org/wiki/Path_ordering_(term_rewriting)).
To create a path ordering,
 you place a total order on the function symbols,
 in this case, $* > +$.
This induces a reduction order on terms, where:

$$
f(...) > g(s_1,...s_n) \text{ iff }
  f > g \text{ and }
  f(...) > s_i \text{ for all } i
$$


## Confluence

Confluence,
 put simply,
 means that the order of rewrites doesn't matter.
Say we have a term $t$,
 and different sequences of rewrites
 lead to distinct terms $t_1$ and $t_2$.
If the TRS is confluence,
 then there exists a term $t'$
 derivable from both $t_1$ and $t_2$.
Confluence is typically illustrated something like this,
 where $\to^*$ means "rewrites to in zero or more steps":

$$
\begin{array}{ccc}
    t &\to^*  &t_1 \\
    \downarrow^* & &\downarrow^* \\
    t_2 &\to^* &t' \\
\end{array}
$$

Our differentiation TRS is confluent as well.
Proving confluence can be involved,
 but in this case we can take a shortcut.
We can see that our TRS corresponds to a
 pattern-matching
 functional program in the following way:
- a term can only match one of the left-hand sides
- none of the left-hand sides refer to the same variable twice

Such a TRS is called *orthogonal*,
 and orthogonal TRSs are confluent.

Orthogonality or confluence does not imply termination.
A good example of that is the SKI combinator calculus,
 which is Turing complete:

$$
\begin{align}
    ((Sx)y)z &\to (xz)(yz) \\
    (Kx)y &\to x \\
    Ix &\to x \\
\end{align}
$$

Just because a TRS is confluent and terminating,
 doesn't mean it's as good as it gets!
Consider the term $d_X(X + 0)$ in our differentiation TRS.
We'd like to be able to simplify this to 1,
 but our TRS doesn't know about the identity of addition.
So let's add it: $v + 0 \to v$.
Now we have a problem:

$$
\begin{array}{lll}
  d_X(X + 0) &\to d_X(X)          &\to 1 \\
             &\to d_X(X) + d_X(0) &\to 1 + d_X(0) \\
\end{array}
$$

Here we've observed a *critical pair*:[^critical-pair]
 a term that can be rewritten in two different ways.
We say that a critical pair is *joinable*
 if both terms can then be rewritten to the same term.
Non-joinable critical pairs witness 
 a lack of confluence.

[^critical-pair]:
    Critical pairs' real definition is a bit more involved,
    necessitating that the term that is rewritten
    to two different terms is the *most general* such term
    for that pair of rewrites.

In this case,
 we can fix confluence by
 looking at the critical pair and 
 adding another rule:
 $d_X(0) \to 0$.
Completion is an algorithm 
 to make a TRS confluent
 by generating new rewrites from critical pairs.


## Completion

Now we can get to the main event:
 [completion](https://en.wikipedia.org/wiki/Knuth%E2%80%93Bendix_completion_algorithm#Generalizations),
 a semi-decision procedure for the word problem.
It may fail or not terminate,
 but if it succeeds,
 then it gives you a confluent and terminating TRS.

With no further ado, here's the completion algorithm:

- Inputs:
  - $E$ a set of (non-oriented) equations,
  - $>$ a reduction order on terms
- Output:
  - $R$ a finite, terminating, and confluent TRS equivalent to $E$
  - or failure
- Set the initial TRS $R$ to the empty set.
- Repeat any of the following steps until none apply:
  - **Delete** any trivial equations ($l = l$) from $E$.
  - **Simplify** either side of any equation in $E$ using a rewrite in $R$.
  - **Orient** an equation $l = r \in E$:
    - Remove the equation add $l \to r$ to $R$ such that $l > r$.
  - **Compose** two rewrites:
    - Replace $s \to t \in R$ with $s \to u \in R$ if $t \to_R u$.
  - **Collapse** a rewrite $s \to t \in R$:
    - Pick a rewrite $l \to r \in R$ that:
       - rewrites $s \to u$,
       - and $l$ **cannot** be rewritten via $s \to t$.
    - Remove $s \to t$ from $R$ and add $s = u$ to $E$.
  - **Deduce** a new equation:
    - Add a critical pair of $R$ to $E$.

The steps can be performed in any order,
 but different orders will have different performance 
 (or even termination) characteristics.
One simple version is:
- loop simplify and delete
- orient a new rewrite
- loop compose
- loop collapse
- deduce a new equation and repeat

Unfortunately,
 examples are quite verbose,
 so I'll leave it to [Wikipedia](https://en.wikipedia.org/wiki/Knuth%E2%80%93Bendix_completion_algorithm#A_terminating_example).

There's a lot more to say about 
 completion and term rewriting,
 but I'll leave it here for now.

## Strategies

Strategies is a somewhat orthogonal topic 
 to a lot of theoretical term rewriting literature.
But it's important to many practical 
 applications of term rewriting,
 as we'll see in the [strategies paper](./2024-01-31-opt-strategies)
 in a couple lectures.

The essence of strategies is
 to establish a meta-language that controls the applications
 of term rewriting.
Strategies are compositional,
 so you can build up complex strategies
 from simpler ones.

A typical strategy language[^strat]
 has the following features:
- Primitive strategies like `skip` and `fail`.
- Rewrites as strategies.
- Sequencing of strategies, e.g., `s1; s2`.
- Choice between strategies:
  - `s1 <+ s2` means try `s1`, and if it fails, try `s2`.
  - `s1 <+> s2` is a non-deterministic choice.
- A fixed-point operator `fix X. s` that allows you to write things like:
  - e.g. `repeat(s) = fix X. (s ; X) <+ skip`.

[^strat]:
    A strategic rewriting calculus called *System S* is summarized in
    the background of this
    [recent POPL paper](https://michel.steuwer.info/files/publications/2024/POPL-2024-1.pdf).

In addition to the practical benefits of strategies,
 they allow to get around some of the limitations
 in certain TRSs.
Consider our differentiation TRS;
 recall that it's limited by only working 
 on pre-baked constants $X$ and $Y$.
The problem is that we need 
 differentiate all constants to 0, 
 *except* for the one we're differentiating with respect to.
We can't express this in our TRS
 (although richer things like conditional rewrites could),
 but can express it in strategies
 using the "left-choice" operator:

```
diffConst_X = ...all other rewrites... <+ (d_X(u) -> 0)
```

This allows us to use a *variable* in the
 rewrite for differentiation of constants,
 but that's only correct if we know that
 no other rewrite applies!
As this example demonstrates,
 reasoning about termination and confluence
 is different when strategies are involved.

## References

- [Term Rewriting and All That](https://www.cambridge.org/core/books/term-rewriting-and-all-that/71768055278D0DEF4FFC74722DE0D707)
- [A Taste of Rewriting](./papers/taste-of-rewrite-systems.pdf)
- [Rewriting](./papers/handbook-ar-rewriting.pdf) chapter from the Handbook of Automated Reasoning
