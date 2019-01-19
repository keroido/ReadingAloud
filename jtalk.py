#coding: utf-8
import subprocess
import tempfile

def run(message, voice_path='voice.wav'):
    speed = 0.75
    dic_path = "/usr/local/Cellar/open-jtalk/1.10_1/dic"
    model_path = "/usr/local/Cellar/open-jtalk/1.10_1/voice/mei/mei_normal.htsvoice"

    with tempfile.NamedTemporaryFile(mode='w+') as tmp:
        tmp.write(message)
        tmp.seek(0)
        command = 'open_jtalk -x {} -m {} -r {} -ow {} {}'.format(dic_path, model_path, speed, voice_path, tmp.name)
        print(command)
        proc = subprocess.run(
            command,
            shell  = True,
        )

if __name__ == "__main__":
  run()
