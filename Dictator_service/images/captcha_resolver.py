import os
from captcha_solver import CaptchaSolver

with open('sbi.jpg','rb') as inp:
	raw_data=inp.read()

solver=CaptchaSolver('browser')
#print str(os.listdir())

decoded=solver.solve_captcha(raw_data)
print "Decoded is :"+str(decoded)
  
