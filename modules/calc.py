import fcntl
import subprocess


def run(**args):
  print('Execute module: calc ...')
  calc = subprocess.call('calc.exe')
  return calc
