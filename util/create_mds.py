import csv
import pathlib

with open('../_data/schedule.csv') as f :
    for r in csv.DictReader(f) :
        if r['theory_slug'] is not None :
            p = pathlib.Path('../_theory/{}.md'.format(r['theory_slug']))
            if not p.exists() :
                with open(p,'wt') as w :
                    w.write((
                        '---\n'
                        'title: {slug}\n'
                        '---\n'
                        '\n'
                        '# {{ page.title }}').format(slug=r['theory_slug'])
                    )


        if r['practice_slug'] is not None :
            p = pathlib.Path('../_practice/{}.md'.format(r['practice_slug']))
            if not p.exists() :
                with open(p,'wt') as w :
                    w.write((
                        '---\n'
                        'title: {slug}\n'
                        '---\n'
                        '\n'
                        '# {{ page.title }}').format(slug=r['practice_slug'])
                    )

        if r['project_slug'] is not None :
            p = pathlib.Path('../_project/{}.md'.format(r['project_slug']))
            if not p.exists() :
                with open(p,'wt') as w :
                    w.write((
                        '---\n'
                        'title: {slug}\n'
                        '---\n'
                        '\n'
                        '# {{ page.title }}').format(slug=r['project_slug'])
                    )


