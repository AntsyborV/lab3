import subprocess as sb
import threading

def timeout():
    print('timeout')
    exit(3)

t = threading.Timer(10, timeout)
proc = sb.Popen("./program", shell=True, stdin=sb.PIPE, stdout=sb.PIPE,
    stderr=sb.PIPE)
out, err = proc.communicate('hello\n')
t.cancel()
assert proc.returncode == 0
assert out == 'hello\n'
assert err == ''
sb.check_call("chocolate", shell=True)
