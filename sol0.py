import os
from subprocess import Popen, PIPE

p = Popen('./target0', stdin=PIPE) #NOTE: no shell=True here
p.communicate(b"Jose      A+")