# -*- coding: utf-8 -*-

import subprocess

child1 = subprocess.Popen(['ls', '-l'], stdout = subprocess.PIPE)
child2 = subprocess.Popen(['wc'], stdin = child1.stdout, stdout = subprocess.PIPE)
out = child2.communicate()
print(out)

print('------------------------------------')

def runCommandWithOutput(cmd, stdinstr = ''):
    p = subprocess.Popen(cmd, shell = True, universal_newlines = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    # p.stdin.write(stdinstr)
    stdoutdata, stderrdata = p.communicate(stdinstr)
    # p.stdin.close()
    return p.returncode, stdoutdata, stderrdata

opentxt = subprocess.Popen(['cat', 'sub_process.txt'], universal_newlines = True, stdout = subprocess.PIPE)
openres = opentxt.communicate()
txtstr = openres[0] 
print(runCommandWithOutput(['wc'], stdinstr = txtstr))
