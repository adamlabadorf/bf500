---
permalink: /
---

# BF550 - Foundations in Programming, Data Analytics, and Machine Learning in Python

(unofficial title: Bioinformatics Engineering)

<table>
  <tr>
    <th>Lec Num</th>
    <th>Date</th>
    <th>Theory Topic</th>
    <th>Practice Topic</th>
    <th>Project Topic</th>
  </tr>
{% for lec in site.data.schedule %}
  <tr>
    <td>{{ lec.lecnum }}</td>
    <td>{{ lec.date }}</td>
    <td>
      {%- if lec.lecnum != nil and lec.theory_slug != nil -%}
        {% assign page = site.theory | where:"slug", lec.theory_slug | first  %}
        <a href="theory/{{ lec.theory_slug }}.html">{{ page.title }}</a>
      {%- else -%}
        {{ lec.comment }}
      {%- endif -%}
    </td>
    <td>
      {%- if lec.practice_slug != nil -%}
        {% assign page = site.practice | where:"slug", lec.practice_slug | first %}
        <a href="practice/{{ lec.practice_slug }}.html">{{ page.title }}</a>
      {%- endif -%}
    </td>
    <td>
      {%- if lec.project_slug != nil -%}
        {% assign page = site.project | where:"slug", lec.project_slug | first %}
        <a href="project/{{ lec.project_slug }}.html">{{ page.title }}</a>
      {%- endif -%}
    </td>
  </tr>
{% endfor %}
</table>

![pipeline project](/assets/bf550_pipeline.png)
