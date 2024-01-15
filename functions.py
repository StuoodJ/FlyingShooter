
def Raytrace(pgame, screen, rx, ry, rw, rh, dw, dh, rR):
    if rx < dw - 9:
        brx = rx
        bry = ry
        pgame(screen, (255, 255, 255), (brx, bry, rw, rh))
        rx += rR * 10
    elif rx >= dw:
        rx = 0
        ry += rR * 10
    elif ry >= dh:
        ry = 0
        rx = 0