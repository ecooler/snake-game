
def drawOne(canvas, start, cell_size, color, p):
    """
    draw one cell
    :param p:
    :return:
    """
    rec = canvas.create_rectangle(start+p[0]*cell_size, start+p[1]*cell_size, start+(p[0]+1)*cell_size,
                                  start+(p[1]+1)*cell_size, fill=color)
    return rec