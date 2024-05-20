---
layout: project
title: "Anti-Unification and Library Learning: An Exploratory Review"
authors:
  - "[Eric Rawn](ericrawn.media)"
links: []
---

An Exploratory Literature Review of Anti-Unification and Library Learning: Future Directions and Open Questions

## Introduction
Anti-Unification has been a problem of continuous interest since the 1970's in Computer Science. Across a variety of application domains, anti-unification (AU) is a general approach to finding *generalizations* between symbolic expressions (Cerna 2023). First introduced by Plotkin (Plotkin 1970), it seeks to find a generalization which captures the common structure between a set of expressions. Consider Plotkin's example:


$$ BitOfIron (1) \land Heated (1,419) \subset Melted (1) $$  

$$ BitOfIron (2) \land Heated (2,419) \subset Melted (2) $$  

$$ (x)~BitOfIron (x) \land Heated (x, 419) \subset Melted (x) $$  


In this example, we retain shared elements of the expression, replacing elements not shared with a variable ($x$), which we then add as an input to our resulting generalization. While other generalizations exist, namely ($x$) $x$ for any set of expressions, anti-unification is generally considered the problem of finding the *least general generalization* (lgg), in which a generalization which captures more of the common structure of the expression set does not exist. 

Where anti-unification usually refers to a class of generalization problems for logical expressions of various orders and under various equational theories (Cerna 2023), *Library Learning* (LL) refers to a practical problem of finding programming functions which capture common structure within a corpus of computer programs. By "structure", I refer to either shared syntactical expressions or shared semantic expressions (under an equational theory and rewrite system). While many papers discuss library learning in the context of anti-unification (Cao 2023, Bowers 2023), others do not (Dumancic 2021). 

In this report, I try to understand the relationship between Anti-Unification and Library Learning and outline interesting directions for future work. I attempt to answer three questions:
1. Why are anti-unification and library learning interesting problems? That is, what do we hope to accomplish with these techniques?
2. Are there related problems which could benefit from introducing ideas from these domains?
3. What research directions remain open? What new questions will need to be answered for successful application of anti-unification and library learning techniques?

In this report I'll sketch two main areas to which LL and AU have been applied. I'll contextualize these papers with other domain-specific research to raise questions and potential goals for these methods in future work. I'll then explore the potential of LL and AU techniques to a related domain of program repair. 

## Software Development and Abstraction

A common argument for Library Learning research rests on the importance of *Abstraction* (Cao 2023, Bowers 2023, Dumancic 2021, Ellis 2021). While none of the authors cited define abstraction, we can generally understand abstraction to mean *a technical and conceptual relation, in which a practitioner can understand or leverage a thing according to its practical dimensions for the practitioner's current problem*[^1]. While abstraction has always been an important part of computer programming (Dijkstra 1972, Pierce 2002), library learning literature seems to frame the LL task as an abstraction problem, as *finding functions which capture the common structure within a corpus of code*.

To build an argument for why library-learned functions serve as abstractions, we can look at the gaps between our first definition of abstraction:*a technical and conceptual relation, in which a practitioner can understand or leverage a thing according to its practical dimensions for the practitioner's current problem*, and the LL problem framed as an abstraction problem:*finding functions which capture the common structure within a corpus of code*. The implicit assumption in equating these two problem definitions is that the parts of a code corpus which share structure are less relevant for a programming task than where that corpus differs. What makes a library-learned function an *abstraction*, under this conception, is its ability to hide irrelevant information, namely the pieces of code which are repeated, or at least the common "structure" as subject to rewrites. A few specific claims within this literature is that abstractions aid in writing new, similar programs more easily (Bowers 2023), making programs more legible (Bowers 2023, Cao 2023), and making programs more concise (Bowers 2023, Cao 2023, ). 

Based on these arguments, a number of hypotheses emerge:
1. When software engineers write similar code to elsewhere in a corpus, this new code varies in the same places which previous code has varied. That is to say that newly written code can be fit into already-learned functions, or can use these already-learned functions effectively.
2. Software engineers can often ignore the parts of code which share structure -- the places where common code fragments differ have at least a strong overlap with the *practical dimensions* of the programmer's current problem. 
3. Programs within a corpus are more legible when they have their shared structure hidden within a library-learned function.

Each of these hypotheses opens additional questions for future work:
#### Abstraction Repair
How might we empirically evaluate this claim? Does this hold more effectively for some domains over others? When new code cannot cleanly fit into an existing generalization, how do we decide to either grow the existing generalization to accommodate this new code, create new generalizations, or opt to leave this new code as is? We might call this process of accommodating new code to existing generalizations *abstraction repair*. What kind of interactions and tooling might best serve such repair in practice?
#### Interactive Library Learning
How might we empirically evaluate this claim? Which situations might this hypothesis hold for, and which might it not? Between a traditional LL system and a fully manual process of creating new functions, how might we support software developers in creating new abstractions by delimiting which parts of similar code are relevant? Could better tooling around annotation, explanation, and analysis help programmers understand programs which are composed with generalizations they did not create themselves? 

Interactive Library Learning could be especially helpful given opportunistic planning behaviors of programmers (Davies 1991), where "planning is seen as [a] process where interim decisions in the planning space can lead to subsequent decisions at either higher or lower levels of abstraction in the plan hierarchy". If programmers are not only implementing a pre-planned schema (a mental representation of what the program ought to accomplish, and how) while they program, but also developing, refining, or modifying that schema based on what they learn while programming, how might library learning techniques be leveraged to support programmers in this iterative process? Library learning techniques are powerful tools to transforming the organization of programs along different levels of abstraction -- how might we use them to support programmers as they learn what kinds of abstractions are most useful to them?
#### Conceptual Organization
How might we empirically evaluate this claim? Looking to (Guarino 1978), how might we support programmers in utilizing library-learned generalizations among the other abstractions they leverage, especially for function and variable naming? As Alan Blackwell writes, "Giving something its proper name is the way that we capture the nature of the thing" (Blackwell 2008) -- programs and abstractions do not just accomplish technical work (i.e. compressing a corpus), they also accomplish *conceptual* work by allowing programmers to think in certain ways with and about the programs they write.[^2]

How easily, for example, can programmers find suitable names for library-learned functions? Can they utilize those functions in practice in the same way they could a hand-written function? For example, many programmers might see a function ```sortList(x)``` and not need to look at its implementation to use it effectively. ```sortList(x)``` is an effective (i.e. legible) abstraction not just because it captures a common operation which might be done repeatedly through a corpus, but also because it captures a coherent conceptual operation: sorting a list. What challenges do programmers face in trying to utilize library-learned functions as both technical generalizations of code but also conceptual organizations of that code? Following a similar argument for variable naming, how might library learning systems preserve variable naming schemes, or interactively guide programmers in giving legible names to variables within learned functions?

#### Contextualizing Current Research
While understanding how library-learned functions operate as abstractions can provide new questions, it might also help us understand the value of current research. For example (Cao 2023) and (Bowers 2023) both offer recent examples of library learning techniques. While Cao et al demonstrate higher compression using a more comprehensive equational theory and e-graphs, the learned programs could bear little resemblance to the original programs due to the amount of rewrites applied. On the other hand, Bowers et al present a more pragmatic top-down search algorithm which uses a small number of rewrites to overcome syntactic hurdles (e.g. $(x * y) = (y * x)$). If the goal is to understand shared structure which is perhaps unknown to the programmer (i.e. it only appears after significant rewriting), an e-graph approach could help programmers identify connections among their corpus they hadn't yet identified, or aid in transforming new code to fit existing abstractions. On the other hand, if the goal is to learn functions that a programmer might be able to immediately identify as conceptually organized but just had not been put into a function (e.g. the programmer was manually sorting many lists in the same way throughout the corpus), then a top-down search might help find more appropriate generalizations. 


#### Idioms 
Related to library learning is the task of learning software *idioms*, similar syntactic program fragments (M. Allamanis 2014). While Allamanis et al use a probabilistic approach, we could imagine reframing a search for common idioms as a library learning problem constrained under (1) which types of transformations are within our equational theory (which would have to be minimal) (2) the total size of the library function. While Allamanis argues that previous work has been unsuccessful in mining idioms through more traditional anti-unification methods, a library learning system which anti-unifies under some rewrite system might be less brittle to simply finding syntactic similarities. Within this direction, we might ask (1) how we might find a set of rewrite rules which sufficiently transform the programs to find shared structure (across different layers of function calls, for example) and (2) how we might encode on our e-graph cost function a notion of finding an optimal generalization which generalizes the most code while also remaining useful as an idiom. 

## Program Optimization

Apart from user-facing applications, much of the current library learning literature centers back-end optimization tasks which software developers do not have visibility into. 

Existing work has explored how to optimize programs by matching program idioms with vendor-specific or library-specific functions (Ginsbach 2018) within a specialized DSL, and utilizing a similar approach but also using an e-graph to find "*latent* idioms" (although these "idioms" don't share syntactic similarity, only semantic similarity) under significant rewrites (Van der Cruysse 2024). 

Crucially, both techniques attempt to match hand-written idioms in an intermediate representation with input code. This work makes the assumption that software development and hardware design will remain largely independent (and hardware vendors or library designers will continue to write new idioms for their hardware and libraries). For many cases this is a reasonable assumption, and allows software developers to write code without an awareness or particular understanding of specific hardware platforms.

Library learning may come to play a role with the development of domain-specific hardware, where code and hardware will mutually evolve for bespoke tasks. Library learning would reverse the order of these idiom-based optimization works, learning the shared structure of operations in a program to identify the optimal hardware architecture for this specific program, rather than look to fit a new program into an existing hardware's idioms. 

We might imagine continuing the direction explored by (VanHattum 2021), who explored finding small, optimal kernels for irregular data with equality saturation. Beyond optimizing individual functions, a library-learning approach could attempt to find the most efficient shared structures across the corpus to learn idioms which could be optimized for directly with custom hardware. 

In another area, we could imagine applying library learning directly to hardware specification languages such as Calyx (Nigam 2021) to identify areas where distinct operations can share architecture. Because Calyx also encodes control flow information, the system is already able to accomplish these optimizations when two areas of work can share components as written, but a library learning approach might explore how to identify greater opportunities for resource sharing under rewrite rules, in addition to common patterns which might maximize resource sharing. 


## Program Repair
A separate domain of *Program Repair*, synthesizing code patches which fix errors, is a neighboring domain to library learning, but important in a key way: code patches *change* the semantics of the code they transform, which means that equational rewrite techniques such as e-graphs cannot be immediately applied. Although recent work uses anti-unification to identify common patches within a version control system (Bader 2019, Winter 2022), anti-unification is applied to the differences between ASTs between commits, using anti-unification to find least-general generalizations of common patches. On the whole, the most successful patches were very simple -- with a flagship example of a null pointer guard to fix a null pointer exception. With a more robust transformation under an equational theory (as with an e-graph), might we learn more complex patches?  

While (Weimer 2013) explored the semantic equivalence of code patches previously, it is a very minimal notion of semantic equivalence, exploring identical syntax, dead-code elimination, and a dataflow analysis. A more robust notion of semantic equivalence of code patches might allow systems (and the programmers who use them) to identify stylistically different but semantically equivalent patches, versus syntactically similar but semantically different patches, allowing us to see what is merely convention or code culture (Alexandru 2018) and what might cause unexpected bugs. 


## Conclusion

This report explored how library learning, especially with the tools of anti-unification and e-graphs, might be used in future work. I've attempted to sketch future questions and guides for two directions which library learning is already heading, and one new direction in which I think it could be of use. Rather than authoritatively summarize the papers of this domain and compare deeply between them (which Cerna et al do expertly), I've instead tried to put library learning research into conversation with neighboring areas.

As many papers have written before me, abstraction seems to remain one of the most uniquely powerful (and dangerous) tools computer science has to offer. In this report I've pointed to a few ways I think library learning can help us understand and manipulate abstractions in better ways.  


[^1]: Guarino highlights many forms of abstraction in programming languages besides callable subroutines (which we commonly call functions): labeled instruction memory addresses (subroutine names), input arguments, output arguments, control flow abstractions, and variable naming, for example, are all different forms of abstraction within common programming languages today. 

[^2]: For existing work in suggesting names automatically, see Allamanis 2015, which trained a probabilistic language model on functions and their names. It remains an open question how we might properly evaluate the efficacy of such a model under the conception that effective function names are not just plausible, but indicate a practical conceptual organization. 



## References

Plotkin, Gordon D. (1970). Meltzer, B.; Michie, D. (eds.). "A Note on Inductive Generalization". Machine Intelligence. 5: 153–163. 

D. M. Cerna and T. Kutsia, “Anti-unification and Generalization: A Survey,” in Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence, Aug. 2023, pp. 6563–6573. doi: 10.24963/ijcai.2023/736.

D. Cao, R. Kunkel, C. Nandi, M. Willsey, Z. Tatlock, and N. Polikarpova, “babble: Learning Better Abstractions with E-Graphs and Anti-unification,” Proc. ACM Program. Lang., vol. 7, no. POPL, p. 14:396-14:424, Jan. 2023, doi: 10.1145/3571207.

M. Bowers et al., “Top-Down Synthesis for Library Learning,” Proc. ACM Program. Lang., vol. 7, no. POPL, pp. 1182–1213, Jan. 2023, doi: 10.1145/3571234.

S. Dumancic, T. Guns, and A. Cropper, “Knowledge Refactoring for Inductive Program Synthesis,” Proceedings of the AAAI Conference on Artificial Intelligence, vol. 35, no. 8, Art. no. 8, May 2021, doi: 10.1609/aaai.v35i8.16893.

E.W. Dijkstra. 1972. The humble programmer [1972 ACM Turing
Award Lecture]. Commun. ACM 15, 10 (1972), 859–866. https://doi.
org/10.1145/355604.361591

Benjamin C Pierce. 2002. Types and Programming Languages. MIT
Press.

Guarino, Loretta Rose, "The Evolution of Abstraction in Programming Languages", Computer Science Department Report, Carnegie-Mellon University, May 1987

K. Ellis et al., “DreamCoder: bootstrapping inductive program synthesis with wake-sleep library learning,” in Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation, Virtual Canada: ACM, Jun. 2021, pp. 835–850. doi: 10.1145/3453483.3454080.

A. F. Blackwell, L. Church, and T. Green, “The Abstract is an Enemy: Alternative Perspectives to Computational Thinking,” 2008.

S. P. DAVIES, “Characterizing the program design activity: neither strictly top-down nor globally opportunistic,” Behaviour & Information Technology, vol. 10, no. 3, pp. 173–190, May 1991, doi: 10.1080/01449299108924281.

J. Van Der Cruysse and C. Dubach, “Latent Idiom Recognition for a Minimalist Functional Array Language Using Equality Saturation,” in 2024 IEEE/ACM International Symposium on Code Generation and Optimization (CGO), Edinburgh, United Kingdom: IEEE, Mar. 2024, pp. 270–282. doi: 10.1109/CGO57630.2024.10444879.

M. Allamanis and C. Sutton, “Mining idioms from source code,” in Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering, in FSE 2014. New York, NY, USA: Association for Computing Machinery, Nov. 2014, pp. 472–483. doi: 10.1145/2635868.2635901.

Miltiadis Allamanis, Earl T. Barr, Christian Bird, and Charles Sutton. 2015. Suggesting accurate method and class names. In Proceedings of the 2015 10th Joint Meeting on Foundations of Software Engineering (ESEC/FSE 2015). Association for Computing Machinery, New York, NY, USA, 38–49. https://doi-org.libproxy.berkeley.edu/10.1145/2786805.2786849

P. Ginsbach, T. Remmelg, M. Steuwer, B. Bodin, C. Dubach, and M. F. P. O’Boyle, “Automatic Matching of Legacy Code to Heterogeneous APIs: An Idiomatic Approach,” in Proceedings of the Twenty-Third International Conference on Architectural Support for Programming Languages and Operating Systems, Williamsburg VA USA: ACM, Mar. 2018, pp. 139–153. doi: 10.1145/3173162.3173182.

A. VanHattum, R. Nigam, V. T. Lee, J. Bornholt, and A. Sampson, “Vectorization for digital signal processors via equality saturation,” in Proceedings of the 26th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, in ASPLOS ’21. New York, NY, USA: Association for Computing Machinery, Apr. 2021, pp. 874–886. doi: 10.1145/3445814.3446707.

Rachit Nigam, Samuel Thomas, Zhijing Li, and Adrian Sampson. 2021. A Compiler Infrastructure for Accelerator Generators. In Proceedings of the 26th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS ’21), April 19ś23, 2021, Virtual, USA. ACM, New York, NY, USA, 14 pages. https://doi.org/10.1145/3445814. 3446712

W. Weimer, Z. P. Fry, and S. Forrest, “Leveraging program equivalence for adaptive program repair: models and first results,” in Proceedings of the 28th IEEE/ACM International Conference on Automated Software Engineering, in ASE ’13. Silicon Valley, CA, USA: IEEE Press, Nov. 2013, pp. 356–366. doi: 10.1109/ASE.2013.6693094.

E. R. Winter et al., “Towards developer-centered automatic program repair: findings from Bloomberg,” in Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering, Singapore Singapore: ACM, Nov. 2022, pp. 1578–1588. doi: 10.1145/3540250.3558953.

J. Bader, A. Scott, M. Pradel, and S. Chandra, “Getafix: learning to fix bugs automatically,” Proc. ACM Program. Lang., vol. 3, no. OOPSLA, pp. 1–27, Oct. 2019, doi: 10.1145/3360585.

C. V. Alexandru, J. J. Merchante, S. Panichella, S. Proksch, H. C. Gall, and G. Robles, “On the usage of pythonic idioms,” in Proceedings of the 2018 ACM SIGPLAN International Symposium on New Ideas, New Paradigms, and Reflections on Programming and Software, in Onward! 2018. New York, NY, USA: Association for Computing Machinery, Oct. 2018, pp. 1–11. doi: 10.1145/3276954.3276960.

A. Baumgartner, T. Kutsia, J. Levy, and M. Villaret, “Term-Graph Anti-Unification,” p. 17 pages, 526688 bytes, 2018, doi: 10.4230/LIPICS.FSCD.2018.9.

R. K. Jones, P. Guerrero, N. J. Mitra, and D. Ritchie, “ShapeCoder: Discovering Abstractions for Visual Programs from Unstructured Primitives,” ACM Trans. Graph., vol. 42, no. 4, p. 49:1-49:17, Jul. 2023, doi: 10.1145/3592416.

C. K. Roy, J. R. Cordy, and R. Koschke, “Comparison and evaluation of code clone detection techniques and tools: A qualitative approach,” Science of Computer Programming, vol. 74, no. 7, pp. 470–495, May 2009, doi: 10.1016/j.scico.2009.02.007.

M. Sotoudeh and A. V. Thakur, “Analogy-Making as a Core Primitive in the Software Engineering Toolbox.” arXiv, Sep. 14, 2020. Accessed: Apr. 29, 2024. [Online]. Available: http://arxiv.org/abs/2009.06592

A. Hindle, E. T. Barr, M. Gabel, Z. Su, and P. Devanbu, “On the naturalness of software,” Commun. ACM, vol. 59, no. 5, pp. 122–131, Apr. 2016, doi: 10.1145/2902362.
