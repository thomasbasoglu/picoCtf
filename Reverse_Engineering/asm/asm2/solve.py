def asm2(x,y):
    while(x<= 0xf5cf):
      y+=1
      x+=0xe4
    return y

print(hex(asm2(12,29)))
