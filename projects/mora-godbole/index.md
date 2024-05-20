---
layout: project
title: "Synthetic Programming Elicitation for Text-to-Code in Very Low-Resource Programming Languages"
authors:
  - "Federico Mora"
  - "Adwait Godbole"
links: 
  - "[Project Report (pdf)](mora-godbole.pdf)"
---

## Abstract

Low-resource programming languages (LPLs) include domain-specific languages,
less-used programming languages, old legacy languages, and languages used
internal to tools and tool-chains. In this paper, we consider the text-to-code
problem for the low end of LPLs, a class we term very low-resource programming
languages (VLPLs). Specifically, we propose synthetic programming elicitation
and compilation (SPEAK), an approach that lets users of VLPLs keep using their
favorite languages and still get good text-to-code support from large language
models (LLMs). We implement SPEAK by using an intermediate language (IL) to
bridge the gap between what LLMs are good at generating and what users want to
generate (code in a target VLPL). This IL must satisfy two conditions. First, LLMs
must be good at generating code in the IL (e.g., Python). Second, there must exist a
well-defined subset of this language that can easily be compiled to the target VLPL
(e.g., Python regular expression strings can be directly translated to POSIX regular
expressions). Given such an IL, SPEAK follows a four step pipeline for text-to-
code generation. First, it asks an LLM to generate a program in the IL. Second,
it uses the definition of the IL subset to automatically generate a partial program.
Third, it completes the partial program with LLM calls, iterating as necessary.
Finally, it compiles the complete IL program to the the target VLPL. We instantiate
SPEAK in a case study for a verification language, and compare the performance
of our generator to existing baselines. We find that SPEAK substantially improves
the performance of text-to-code tools on both VLPLs.
