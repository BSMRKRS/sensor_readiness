import webbrowser

print "Open front camera, back camera, or both. Enter 'front', 'back', or 'both'"
if raw_input("> ") == "front":
    webbrowser.open('http://192.168.21.181/top.htm') #opens front camera
if raw_input("> ") == "back":
    webbrowser.open('http://192.168.21.182/top.htm') #opens back camera
elif raw_input("> ") == "both":
    webbrowser.open('http://192.168.21.181/top.htm')
    webbrowser.open('http://192.168.21.182/top.htm')
