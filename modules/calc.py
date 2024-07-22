import subprocess


def run():
  print('Execute module: calc ...')
  calc = subprocess.call('calc.exe')
  return calc
