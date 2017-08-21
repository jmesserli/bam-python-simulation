import subprocess

player = "vlc"
returncode = subprocess.call(["which", "omxplayer"])
if returncode == 0:
    player = "omx"


def play(path):
    if player == "vlc":
        subprocess.Popen(["cvlc", "--fullscreen", path])

    elif player == "omx":
        subprocess.Popen(["omxplayer", path])
        pass
