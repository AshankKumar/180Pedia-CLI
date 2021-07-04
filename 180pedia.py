import sys
import os


def create_and_run_cmd(args):

    pt = args[0]
    sec = args[1]
    q = args[3]

    cmd = "open"

    if q == "LR":
        cmd += " https://180pedia.com/lsat-pt-#-section-#-LR-#"
    elif q == "RC":
        cmd += " https://180pedia.com/lsat-pt-#-section-#-passage-#"
    else:
        cmd += " https://180pedia.com/lsat-pt-#-section-#-game-#"

    for i in range(3):
        cmd = cmd.replace("#", args[i], 1)

    os.system(cmd)


create_and_run_cmd(sys.argv[1:])
