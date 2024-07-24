from subprocess import Popen, PIPE


def run(**args):
  print('[*] Launch module...')
  process = Popen(['ipconfig'], stdout=PIPE, stderr=PIPE)
  data = process.stdout.read()
  return str(data)
