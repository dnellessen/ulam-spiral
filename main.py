import sys

method = 'turtle'
line = False
size = 5

for arg in sys.argv:
    match arg:
        case 'turtle':
            method = 'turtle'
        case 'pygame':
            method = 'pygame'
        case '-l':
            line = True

    if arg.isdigit():
        size = int(arg)

if method == 'turtle':
    import methods.with_turtle as spiral
elif method == 'pygame':
    import methods.with_pygame as spiral

spiral.init(line, size)

try: spiral.mainloop()
except Exception: pass
