import subprocess

def run(**args):
    print "[*] In time module."
    time1 = subprocess.check_output("cal",shell=True)
    return time1
