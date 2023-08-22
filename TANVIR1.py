import os,platform
os.system('git pull')
 
TANVIR=platform.architecture()[0]
if TANVIR=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif TANVIR=="64bit":
     __import__("tan1_en")