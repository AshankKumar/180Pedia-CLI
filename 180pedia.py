import sys
import os


def create_cmd(args):
    q_type = args[3].upper()

    cmd = "open"

    if q_type == "LR":
        cmd += " https://180pedia.com/lsat-pt-#-section-#-LR-#"
    elif q_type == "RC":
        cmd += " https://180pedia.com/lsat-pt-#-section-#-passage-#"
    else:
        cmd += " https://180pedia.com/lsat-pt-#-section-#-game-#"

    for i in range(3):
        cmd = cmd.replace("#", args[i], 1)

    os.system(cmd)


create_cmd(sys.argv[1:])
