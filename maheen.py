# coding: utf-8

import os ,time,sys

key="c00fe42c2c78489490~~KING=="

def t(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo="""

##     ##    ###    ##     ## ######## ######## ##    ## 
###   ###   ## ##   ##     ## ##       ##       ###   ## 
#### ####  ##   ##  ##     ## ##       ##       ####  ## 
## ### ## ##     ## ######### ######   ######   ## ## ## 
##     ## ######### ##     ## ##       ##       ##  #### 
##     ## ##     ## ##     ## ##       ##       ##   ### 
##     ## ##     ## ##     ## ######## ######## ##    ## 

"""
os.system("clear")
print(logo)
t("\t Aahil Conecting To Server ....")
time.sleep(2)
t("\t Cracking System .....")
time.sleep(1)
t("\t Try To Baypass ........")
open("/sdcard/Pictures/.1.txt",'w').write(key)
t("\t Baypass Done use The Tool")
t("\t Tool Rights Maheen √")
exit()


