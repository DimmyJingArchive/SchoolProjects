from subprocess import call
import re

call(['npm', 'run', 'build'])
call(['rm', '-r', 'docs'])
call(['mv', 'dist', 'docs'])

with open('./docs/index.html') as f:
    text = re.sub('(src=|href=)', '\\1/SchoolProjects', f.read())

with open('./docs/index.html', 'w') as f:
    f.write(text)

call(['git', 'add', '.'])
call(['git', 'commit', '-m', '"fixed stuff"'])
call(['git', 'push'])
