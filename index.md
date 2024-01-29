---
layout: default
---

- Instructor: [Max Willsey](https://mwillsey.com)
- Time: Mon/Wed 14:30-16:00
- Room: Soda 405
- Office Hours in Max's office (Soda 725):
  - Mon 10:00-11:30
  - Thu 14:00-15:30
  - or by appointment

This course aims to give students experience with some of the many
 declarative techniques for program analysis and optimization.
In particular, we will study term rewriting systems, datalog, and equality saturation.

# Schedule

The topics of future weeks are subject to change.

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
    .holiday td:nth-child(4)::before { 
      content: "🏖️"; 
      font-style: normal;
      padding-right: 0.2em;
    }
    .lecture td:nth-child(4)::before { content: "️Lecture: "; font-weight: bold }
    /* .lecture td:nth-child(4) { font-weight: bold; } */
  </style>
{% for post in site.posts reversed %}
  <tr class="{{ post.type }}">
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
      {% else %}
        <a href="{{ post.url | relative_url}}">{{ post.title }}</a>
      {% endif %}
    </td>
    <td>
      {{ post.lead }}
    </td>
  </tr>
{% endfor %}
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
