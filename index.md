---
permalink: /
---

# BF500 - Bioinformatics Engineering)

**Semester: NA**

**Location: NA**

**Time: NA**

This course introduces students to the key concepts, techniques, and technologies
used in implementing modern bioinformatic analyses and workflows. The materials
are split into "theory" and "practice" segments that focus on the various aspects
of software engineering, computer science, data management, and other topics
relevant to the practice of bioinformatics. There is one project that spans the
entire semester where students will incorporate what they learn into writing a
complete microbial genome analysis pipeline.

## Course Values and Policies

**Everyone is welcome.** Every background, race, color, creed, religion, ethnic
origin, age, sex, sexual orientation, gender identity, nationality is welcome
and celebrated in this course. Everyone deserves respect, patience, and
kindness. Disrespectful language, discrimination, or harassment of any kind are
not tolerated, and may result in removal from class or the University. This is
not merely [BU policy](http://www.bu.edu/policies/policy-category/harassment-discrimination/).
The instructors deem these principles to be inviolable human rights. Students
should feel safe reporting any and all instances of discrimination or
harassment to the instructor, to any of the Bioinformatics Program leadership,
or the [BU Equal Opportunity Office](http://www.bu.edu/eoo/).

**Everyone brings value.** Each of us brings unique experiences, skills, and
creativity to this course. Our diversity is our greatest asset.

**Collaboration is highly encouraged.** All students are encouraged to work
together and seek out any and all available resources when completing projects
in all aspects of the course, including sharing coding ideas and strategies with
each other as well as those found on the internet. Any and all available
resources may be brought to bear. However, consistent with BU policy, the bulk
of your code and your final reports should be written in your own words and
represent your own work and understanding of the material. Copying/pasting large
sections of code is not acceptable and will be investigated as cheating (we check).

**A safe space for dissent.** For complex topics such as those covered in this
class, there is seldom one correct answer, approach, or solution. Disagreement
fosters innovation. All in the course, including students and TAs, are
encouraged to express constructive criticism and alternative ideas on any
aspect of the content.

**We are always learning.** Our knowledge and understanding is always
incomplete. Even experts are fallible. The bioinformatics field evolves
rapidly, and Rome was not built in a day. Be kind to yourself and to others.
You are always smarter and more knowledgable today than you were yesterday.

## Project: Microbial Genome Analysis Pipeline

![pipeline project](/assets/images/bf500_pipeline.png)

Students will implement the above depicted pipeline incrementally throughout the
semester. Each box is a separate analysis (i.e. script) that should be written
independently and composed together into a holistic pipeline by the end of the
course. The number by each box indicates the order in which we will complete
the analyses. Students will not only learn how to write the analysis code needed
to implement the pipeline but will also incorporate reproducibility practices as
they go. Halfway through the semester, students will work in pairs to run each
others pipelines as a "reproducibility check." The pipeline culminates in an
automated report that describes and visualizes statistics gathered by the pipeline.

Every student will use git and github to host their pipelines and share them with
the rest of the class (and the world).

Everyone will use the same microbial genome while developing their pipeline.

## Final Project: Apply your microbial genome analysis pipeline to a different genome

For the final project, students will apply their pipeline to a different microbial
genome of their choosing and compare the results with that used in development.

## Grading

**Pipeline project - 90%** A component of the pipeline is assigned each week.
Your code should be committed and pushed to a github repo where you will receive
feedback from your TA. You will be primarily graded on effort, rather than on
whether the code works or not. Feedback will consist of stylistic commentary and
overall code organization/quality consistent with the principles covered in class.

**Final project - 10%** In the final project you will apply your pipeline to a
different microbial genome and compare the results to your previous run. You will
write a short report summarizing the results.

## Course Schedule

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

![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/)
