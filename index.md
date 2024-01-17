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
