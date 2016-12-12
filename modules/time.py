from datetime import datetime

def run(**args):
    print "[*] In time module."
    time = str(datetime.now())
    return time
run()
