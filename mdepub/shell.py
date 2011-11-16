import logging
import subprocess
import os

log = logging.getLogger('html')

def run(args, shell=False):
    log.debug("run(): %s", args)
    #p = subprocess.Popen(args, shell = True)
    p = subprocess.Popen(args, shell=shell)
    os.waitpid(p.pid, 0)

def pipe(args, input):
    log.debug("pipe(): %s", args)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return p.communicate(input)[0].strip()

def save_output(args, output_file):
    with file(output_file, 'w') as f:
        p = subprocess.Popen(args, stdout=f)
        os.waitpid(p.pid, 0)
