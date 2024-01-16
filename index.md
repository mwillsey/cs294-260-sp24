---
layout: default
---

- Instructor: [Max Willsey](https://mwillsey.com)
- Time: Mon/Wed 14:30-16:00
- Room: Soda 405

This course aims to give students experience with the implementation and use of
 declarative techniques for program analysis and optimization.
In particular, we will study term rewriting systems, datalog, and equality saturation.

# Schedule

The topics of future weeks are subject to change.

<style>
    time {
        display: inline;
        float: right;
    }
</style>

<table style="border-spacing: 0">
  <thead>
    <tr>
      <th>Wk</th>
      <th colspan="2">Date</th>
      <th colspan="3">Topic</th>
    </tr>
  </thead>
  <style>
    tr { vertical-align: top; }
    td { padding: 0.4em 0.3em 0.3em; }
    tbody tr:nth-child(odd) {background-color: #00000011;}
    td:nth-child(1) { text-align: right; }
    td:nth-child(2) { padding-right: 0; }
    .holiday td:nth-child(4) { font-style: italic; }
    /* .lecture td:nth-child(4) { font-weight: bold; } */
  </style>
{% for post in site.posts reversed %}
  {% if post.skip %}
    {% assign type = "holiday" %}
  {% elsif post.lead %}
    {% assign type = "discussion" %}
  {% else %}
    {% assign type = "lecture" %}
  {% endif %}
  <tr class="{{ type }}">
    <td>
      {% assign week = post.date | date: "%V" | to_i | minus: 2 %}
      {% unless last_week == week %}
        {{ week }}
        {% assign last_week = week %}
      {% endunless %}
    </td>
    <td>{{ post.date | date: "%a" }}</td>
    <td>{{ post.date | date: "%m" | abs }}-{{ post.date | date: "%d" }}</td>
    <td>
      {% if post.skip %}
        {{ post.title }}
      {% elsif post.lead %}
        <a href="{{ post.url | relative_url}}">{{ post.title }}</a>
      {% else %}
        <b>Lecture:</b> <a href="{{ post.url | relative_url}}">{{ post.title }}</a>
      {% endif %}
    </td>
    <td>
      {{ post.lead }}
    </td>
  </tr>
{% endfor %}
  <tr class="holiday">
    <td>11</td>
    <td></td>
    <td></td>
    <td>Spring Break</td>
  </tr>
  <tr class="">
    <td>12</td>
    <td></td>
    <td></td>
    <td>Project Proposals</td>
    <td></td>
  </tr>
  <tr class="">
    <td>13</td>
    <td></td>
    <td></td>
    <td>Project Meetings</td>
    <td></td>
  </tr>
  <tr class="">
    <td>14</td>
    <td></td>
    <td></td>
    <td>Project Meetings</td>
    <td></td>
  </tr>
  <tr class="">
    <td>15</td>
    <td>Mon</td>
    <td>4-22</td>
    <td>Project Presentations</td>
    <td></td>
  </tr>
  <tr class="">
    <td></td>
    <td>Wed</td>
    <td>4-24</td>
    <td>Project Presentations</td>
    <td></td>
  </tr>
</table>

1. Course Overview
  - Wed 1-17: Welcome
2. Term Rewriting Basics
  - Mon 1-22: Lecture
  - Wed 1-24: 
    "[Playing by the Rules: Rewriting as a practical optimisation technique in GHC](papers/haskell-rules.pdf)" 
3. Confluence & Completion
  - Mon 1-29: Lecture
  - Wed 1-31:
    "[Verifying and Improving Halide’s Term Rewriting System with Program Synthesis](papers/verifying-halide-trs.pdf)"
4. Strategies
    - Mon 2-05: Lecture
    - Wed 2-07
        - "[Achieving High Performance the Functional Way: Expressing High-Performance Optimizations as Rewrite Strategies](papers/high-perf-the-functional-way.pdf)"
        - Short commentary on the paper: [Reconsidering the Design of User-Schedulable Languages](https://dl.acm.org/doi/pdf/10.1145/3580370)
5. Datalog Basics
  - Mon 2-12: Lecture
  - Wed 2-14:
    "[Doop: Strictly Declarative Specification of Sophisticated Points-to Analyses](papers/doop.pdf)"
6. More Datalog
  - *Mon 2-19: Holiday*
  - Wed 2-21 
  "[From Datalog to Flix: A Declarative Language for Fixed Points on Lattices](papers/datalog-to-flix.pdf)"
7. Datalog extensions
  - Mon 2-26: 
    "[Higher-Order, Data-Parallel Structured Deduction](https://arxiv.org/abs/2211.11573)"
  - Wed 2-28:
    "[Functional Programming with Datalog](papers/functional-programming-datalog.pdf)"
8. E-Graphs and Equality Saturation
  - Mon 3-04: Lecture
  - Wed 3-06:
    "[Efficient E-matching for SMT Solvers](papers/efficient-ematching.pdf)"
9. E-Graphs and Equality Saturation, pt 2
  - Mon 3-11:
    "[Equality Saturation: A New Approach to Optimization](https://arxiv.org/abs/1012.1802)"
  - Wed 3-13: 
    "[babble: Learning Better Abstractions with E-Graphs and Anti-Unification](https://arxiv.org/pdf/2212.04596.pdf)"
10. E-Graphs, from other perspectives
    - *Mon 3-18: No class*
        - "[ECTAs: Searching Entangled Program Spaces](https://arxiv.org/pdf/2206.07828.pdf)"
        - Supplemental [blog post](https://github.com/egraphs-good/egg/discussions/104)
    - Wed 3-20:
     "[Better Together: Unifying Datalog and Equality Saturation](https://arxiv.org/pdf/2304.04332.pdf)"
11. *Spring Break*
12. Project Consultations
  - Mon 4-01
  - Wed 4-03 
13. TBD
  - Mon 4-08
  - Wed 4-10 
14. TBD
  - Mon 4-15
  - Wed 4-17 
15. Project Presentations
  - Mon 4-22
  - Wed 4-24 
16. *RRR Week*
{: .schedule}
<!-- - Mon 4-29 -->
<!-- - Wed 5-01  -->

