import subprocess
import sys

RUN = 'RUN'
BUILD = 'BUILD'
ARCHIVE = 'ARCHIVE'

mode = 'run'

if len(sys.argv) > 1:
    if sys.argv[1] == 'build':
        mode = BUILD
    elif sys.argv[1] == 'archive':
        mode = ARCHIVE

command = [
    'pygbag',
    '--app_name', 'youre_the_os',
    '--ume_block', '0',
    '--title', "你是操作系统!",
]

if mode == BUILD:
    command.append('--build')
elif mode == ARCHIVE:
    command.append('--archive')

command.append('src')

subprocess.run(command)
