from display import *
from matrix import *


def add_circle( points, cx, cy, cz, r, step ):
    interval = 0
    while interval <= 1:
        if interval == 0 or interval == 1:
            x = cx + r*math.cos(2*math.pi*interval)
            y = cy + r*math.sin(2*math.pi*interval)
            add_point(points,matrix,x,y,cz)
            interval += step
        x = cx + r*math.cos(2*math.pi*interval)
        y = cy + r*math.sin(2*math.pi*interval)
        add_point(points,x,y,cz)
        add_point(points,x,y,cz)
        interval += step


def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    xPoints = generate_curve_coefs(x0,x1,x2,x3,curve_type]
    xa=xPoints[0][0]
    xb=xPoints[0][1]
    xc=xPoints[0][2]
    xd=xPoints[0][3]
    
    yPoints = generate_curve_coefs(y0,y1,y2,y3,curve_type]
    ya=yPoints[0][0]
    yb=yPoints[0][1]
    yc=yPoints[0][2]
    yd=yPoints[0][3]
    
    interval = 0
    while interval <= 1:
        if interval == 0 or interval == 1:
            x = xa*(math.pow(interval,3)+xb*(math.pow(interval,2)+xc*interval+xd
            y = ya*(math.pow(interval,3)+yb*(math.pow(interval,2)+yc*interval+yd
            add_point(points,x,y,0)
            interval+=step
        else:
            x = xa*(math.pow(interval,3)+xb*(math.pow(interval,2)+xc*interval+xd
            y = ya*(math.pow(interval,3)+yb*(math.pow(interval,2)+yc*interval+yd
            add_point(points,x,y,0)
            add_point(points,x,y,0)
            interval+=step


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )
    



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
