import subprocess
try:
  subprocess.run(['lvim',])
  #subprocess.run(['c:/windows/notepad.exe',])
  #subprocess.run(['Notepad.exe','texto.txt'])
except subprocess.CalledProcessError as e:
    print(e.output)