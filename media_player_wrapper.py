import subprocess

player = "vlc"
returncode = subprocess.call(["which", "omxplayer"])
if returncode == 0:
    player = "omx"


def play(path):
    if player == "vlc":
        pass

    elif player == "omx":
        pass
