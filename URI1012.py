values = [ float(x) for x in input().split(" ")]
print(values)
print(f"TRIANGULO: {(.5*values[0]*values[2]):.3f}\nCIRCULO: {(3.14159*values[2]*values[2]):.3f}\nTRAPEZIO: {(.5*(values[0]+values[1])*values[2]):.3f}\nQUADRADO: {(values[1]*values[1]):.3f}\nRETANGULO: {(values[0]*values[1]):.3f}")