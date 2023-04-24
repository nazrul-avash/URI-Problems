i = 0
j = 1
while(i<=2):
    if i==0 or i==1 or round(i,2)==2:
        print(f"I={i:.0f} J={i + j:.0f}")
        print(f"I={i:.0f} J={i + j + j:.0f}")
        print(f"I={i:.0f} J={i + j + j + j:.0f}")
    else:
        print(f"I={i:.1f} J={i+j:.1f}")
        print(f"I={i:.1f} J={i + j+j:.1f}")
        print(f"I={i:.1f} J={i + j+j+j:.1f}")
    j = 1
    i += 0.2
