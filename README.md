# i3wm password generator
Python script to create a complex password and copy it to the clipboard

#Installing a dependency:
  
  pip install pyperclip
  
#You need to add a line to the i3wm config, changing it to fit your data:

  bindsym $mod+Shift+x exec --no-startup-id "/usr/bin/python /path/to/i3wm-paswd.py; notify-send 'Password created'"
