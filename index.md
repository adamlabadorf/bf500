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
      {%- if lec.lecnum != "" -%}
        {% assign url = "/lectures/" | append: lec.theory_slug %}
        {% assign page = site.lectures | where:"slug", lec.theory_slug | first  %}
        <a href="lectures/{{ lec.theory_slug }}.html">{{ page.title }}</a>
      {%- else -%}
        {{ lec.comment }}
      {%- endif -%}
    </td>
    <td>
      {%- if lec.lecnum != "" -%}
        {% assign page = site.lectures | find:"id", lec.practice_slug %}
        <a href="lectures/{{ lec.practice_slug }}.html">{{ page.title }}</a>
      {%- endif -%}
    </td>
    <td>
      {%- if lec.lecnum != "" -%}
        {% assign page = site.lectures | find:"id", lec.project_slug %}
        <a href="project/{{ lec.project_slug }}.html">{{ page.title }}</a>
      {%- endif -%}
    </td>
  </tr>
{% endfor %}
</table>

{% for lec in site.lectures %}
  {{ lec.id }}<br/>
{% endfor %}

{{ site.lectures["/lectures/intro"]}}

{{ site.lectures | where: "id", "the_scripting_workflow" }}

![pipeline project](bf550_pipeline.png)
