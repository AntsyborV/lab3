import subprocess as sb
import threading

def timeout():
    print('timeout')
    exit(3)

t = threading.Timer(10, timeout)
proc = sb.Popen("./program", shell=True, stdin=sb.PIPE, stdout=sb.PIPE,
    stderr=sb.PIPE)
out, err = proc.communicate(b'hello\n')
t.cancel()
assert proc.returncode == 0
assert out == b'hello\n'
assert err == b''
print("Success!")
