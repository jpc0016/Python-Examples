import angr
import monkeyhex

b = angr.Project( "/home/jpc0016/projects/rootme/cracking/ch27-elf-mips/ch27.bin")

def hook(state):
    print("Hooked!!! Yes!")

myBlockAddr = 0x4007c0

state = b.factory.blank_state( addr=myBlockAddr )
b.hook(myBlockAddr+4, hook, length=5)

p = b.factory.path(state)
p.step()
