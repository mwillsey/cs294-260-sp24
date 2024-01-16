import datetime
import re
from itertools import cycle

txt = """
Mon 1-29: Lecture
Wed 1-31: “Verifying and Improving Halide’s Term Rewriting System with Program Synthesis”
Mon 2-05: Lecture
Wed 2-07: “Achieving High Performance the Functional Way: Expressing High-Performance Optimizations as Rewrite Strategies”
Mon 2-12: Lecture
Wed 2-14: “Doop: Strictly Declarative Specification of Sophisticated Points-to Analyses”
Mon 2-19: Holiday
Wed 2-21 “From Datalog to Flix: A Declarative Language for Fixed Points on Lattices”
Mon 2-26: “Higher-Order, Data-Parallel Structured Deduction”
Wed 2-28: “Functional Programming with Datalog”
Mon 3-04: Lecture
Wed 3-06: “Efficient E-matching for SMT Solvers”
Mon 3-11: “Equality Saturation: A New Approach to Optimization”
Wed 3-13: “babble: Learning Better Abstractions with E-Graphs and Anti-Unification”
Mon 3-18: No class
Wed 3-20: “Better Together: Unifying Datalog and Equality Saturation”
Mon 4-01
Wed 4-03
Mon 4-08
Wed 4-10
Mon 4-15
Wed 4-17
Mon 4-22
Wed 4-24
"""

r = re.compile(r"(\w{3}) (\d{1,2})-(\d{1,2})(: (.*))?")
for line in txt.splitlines():
    if m := r.match(line):
        print(m[2], m[3], m[5])
        fname = f"_posts/2024-{int(m[2]):02}-{m[3]}.md"
        content = "---\nlayout: post\n---\n"
        with open(fname, "w") as f:
            f.write(content)


# def go(weekno, day):
#     print(weekno, day, day.strftime("%a"))


# start = datetime.date(2024, 1, 17)
# end = datetime.date(2024, 4, 26)
# start_week = start.isocalendar()[1]

# days = ["Mon", "Wed"]

# day = start
# while day <= end:
#     weekno = day.isocalendar()[1] - start_week + 1
#     if day.strftime("%a") in days:
#         go(weekno, day)
#     day += datetime.timedelta(days=1)
