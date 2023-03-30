def total_volume(*boxes):
    return sum([x*y*z for x,y,z in boxes])