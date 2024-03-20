---
layout: post
title: "Project Proposals"
---

The final project is an opportunity to explore a topic of your choice
 related to the course material.
You may work 
 in groups of up to 3 people.
Working alone is totally fine.

Based on the proposals, I may try to combine
 or shuffle groups if there seems to be overlap or something.

The project is meant to be flexible and open-ended,
 here are some ways that you might approach it:

<ul markdown="1">
<li> Re-implement or extend a tool from a paper.  </li>
<li>
  Perform a survey on a few papers in a deeper area than we got a chance to cover in class.
  (I like this project idea a lot, and there can be several different flavors of it!)
  Some quick topic ideas:
  <ul>
    <li> Sparse tensors and the connection to relational algebra </li>
    <li> Advanced term rewriting / matching techniques, especially modulo theories like AC </li>
    <li> Rewriting strategies </li>
    <li> Modern Datalog flavors that deal with existentials, semirings, etc.  </li>
    <li> Rewriting / e-graphs inside SMT solvers, and how that differs with equality saturation </li>
    <li> Connecting any of these these up would be great too!  </li>
  </ul>
</li>
<li> Apply some of the ideas from the course to your own research.  </li>
<li>
<details markdown="1">
 <summary>
 Visualization Project Idea from <a href="http://www.cs.columbia.edu/~ewu/">Eugene Wu</a>
 </summary>
**Background**: Graphical perception studies ask users to answer simple data questions given varying visualization designs. These have been collected into visualization principles that rank visualization effectiveness (e.g., scatter plots are better than pie charts). However, these results are limited in two ways: visualization designs confound data transformations with visual encoding, and tasks are expressed in ambiguous English language and thus non-generalizable.

We want to estimate visualization effectiveness by modeling visualizations and tasks
using the same representation -- data transformations.  The visualization is the result of transformation operators on an input dataset, and the task asks users to answer a query (operators) over the input dataset.

The setup is roughly as follows.
Let D be the input dataset, and there is a library of table transformations (e.g., filter, map, group, aggregate) and arithmetic expressions.  Visualization $V = f_V(f_T(D))$ is the result of applying a sequence of transformations $f_T(D)$ to the dataset, and then mapping its data attributes to visualization attributes via $f_V()$.  A user task $Q(D)$ estimates a result over $D$, however the user only has access to $V$.

1. is $Q(D)$ expressible as $Q'(V)$?   
2. If so, and there is a ''user effort cost'' associated with each operator, then what is the lowest cost $Q'$?

The idea is to use egg to quickly search the space of transforms and extract a lowest cost $Q'$.

Please contact ew2493@columbia.edu for details.
</details>
</li>
<li> Explore/expand the state-of-the-art on <a href="https://github.com/egraphs-good/extraction-gym">e-graph extraction</a>.</li>
<li> Anything else! </li>
</ul>

In any case, feel free to chat with me about what you're thinking about doing. Just send me an email!

### Proposals

On this date, proposals are due on bCourses.
The proposal should be a short document (1-2 pages, 700ish words) that outlines
 what you plan to do for your project, including the papers / sources that you plan to base it on.
The proposal can be informal, 
 but should be clear about what you plan to do.

### Proposal Presentation

During this class, groups will give a 5-minute presentation on their project proposal.
This is an opportunity to get feedback on your project idea,
 and to help you refine your project scope.
Also, groups may shuffle or combine based on the proposals.

The presentation can be informal and doesn't have to use slides.

### Meetings

A large chunk of the course is dedicated to the final project.
During that time,
 each group will meet with me weekly to discuss their progress.
These meetings are an opportunity to get early feedback on your project,
 and to help hone in the scope of your project
 so that you can make the best presentation by the end of the course.

### Final Presentations and Report

The final deliverables for the project are:
- A 20ish minute presentation given during the last week of class
- A short report (4-6 pages) due before the first day of project presentations
  - Report length should vary based on the kind of project. 
    For example, a survey report should be longer than that of an implementation project.