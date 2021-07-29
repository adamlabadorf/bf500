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
        {% assign page = site.lectures | find:"id", lec.theory_slug %}
        <a href="lectures/{{ lec.theory_slug }}/{{ lec.theory_slug }}">{{ page.title }}</a>
      {%- else -%}
        {{ lec.comment }}
      {%- endif -%}
    </td>
    <td>
      {%- if lec.lecnum != "" -%}
        {% assign page = site.lectures | find:"id", lec.practice_slug %}
        <a href="lectures/{{ lec.practice_slug }}/{{ lec.practice_slug }}">{{ page.title }}</a>
      {%- endif -%}
    </td>
    <td>
      {%- if lec.lecnum != "" -%}
        {% assign page = site.lectures | find:"id", lec.project_slug %}
        <a href="project/{{ lec.project_slug }}/{{ lec.project_slug }}">{{ page.title }}</a>
      {%- endif -%}
    </td>
  </tr>
{% endfor %}
</table>

{% for lec in site.lectures %}
  {{ lec.id }}{{ lec }}<br/>
{% endfor %}

{{ site.lectures | where: "id", "the_scripting_workflow" }}

![pipeline project](bf550_pipeline.png)
