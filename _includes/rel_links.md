{%- for item in site.data.schedule -%}
    {%- assign i = forloop.index0 -%}
    {%- if item.theory_slug == include.slug -%}
        {%- assign type = "theory" -%}
        {%- break -%}
    {%- elsif item.practice_slug == include.slug -%}
        {%- assign type = "practice" -%}
        {%- break -%}
    {%- elsif item.project_slug == include.slug -%}
        {%- assign type = "project" -%}
        {%- break -%}
    {%- endif -%}
{%- endfor -%}

{%- assign curr = site.data.schedule[i] -%}

{%- if i == empty -%}
    Could not find flanking links for {{ include.slug }}
{%- else -%}
    {%- if type == "project" -%}

    {%- else -%}
        {%- if i > 0 -%}
            {%- assign prev_i = i | minus: 1 -%}
            {%- assign prev = site.data.schedule[prev_i] -%}
            {%- if type == "theory" -%}
                {%- assign page = site.theory | where:"slug", prev.theory_slug | first  -%}
<a href="theory/{{ prev.theory_slug }}.html">{{ page.title }}</a>
            {%- else -%}
                {%- assign page = site.practice | where:"slug", prev.practice_slug | first  -%}
<a href="practice/{{ prev.practice_slug }}.html">{{ page.title }}</a>
            {%- endif -%}
        {%- endif -%}
        {%- assign next_i = i | plus: 1 -%}
        {%- assign next = site.data.schedule[next_i] -%}
        {%- if next  -%}
            {%- if type == "theory" -%}
                {%- assign page = site.theory | where:"slug", next.theory_slug | first  -%}
<a href="theory/{{ next.theory_slug }}.html">{{ page.title }}</a>
            {%- else -%}
                {%- assign page = site.practice | where:"slug", next.practice_slug | first  -%}
<a href="practice/{{ next.practice_slug }}.html">{{ page.title }}</a>
            {%- endif -%}
        {%- endif -%}

    {%- endif -%}
{%- endif -%}
