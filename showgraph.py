
def show_hang_man(stage):
    lines=[None]*7
    lines[0] = "+-----+"
    lines[1] = "|     |"
    lines[2] = "|"
    lines[3] = "|"
    lines[4] = "|"
    lines[5] = "|"
    lines[6] = "|________"
    if stage > 0:
        lines[2] = "|     O"
    if stage > 1:
        lines[3] = "|     |"
        lines[4] = "|     |"
    if stage > 2:
        lines[3] = "|    \|"
    if stage > 3:
        lines[3] = "|    \|/"
    if stage > 4:
        lines[5] = "|    /"
    if stage > 5:
        lines[5] = "|    / \\"
    for line in lines:
        print(line)