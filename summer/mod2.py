import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("UNIT_TEST"))
if os.getenv("UNIT_TEST"):
    import fake_mod1 as mod1
else:
    import mod1
    
def summer(x:int , y:int):
    return mod1.preamble() + f"{x+y}"
