import time
import math

width = 60
height = 40
A = 0.0
B = 0.0

while True:
    canvas = [" "] * width * height # сетка
    z_buffer = [-9999.0] * width * height

    x = -2.0
    while x <= 2.0:
        y = -2.0
        while y <= 2.0:
            
            #передняя стенка ---
            z = 2.0
            #вертим по z
            new_x = x * math.cos(A) - y * math.sin(A)
            new_y = x * math.sin(A) + y * math.cos(A)
            #вертим по x
            new_z = new_y * math.sin(B) + z * math.cos(B)
            new_y = new_y * math.cos(B) - z * math.sin(B)
            
            screen_x = int(width / 2 + new_x * 6)
            screen_y = int(height / 2 + new_y * 3)

            if 0 < screen_x < 59 and 0 < screen_y < 39:
                index = screen_y * width + screen_x
                if new_z > z_buffer[index]:
                    z_buffer[index] = new_z
                    canvas[index] = "#" # передняя грань

            #задняя стенка
            z = -2.0
            #вертим по z
            new_x = x * math.cos(A) - y * math.sin(A)
            new_y = x * math.sin(A) + y * math.cos(A)
            #вертим по x
            new_z = new_y * math.sin(B) + z * math.cos(B)
            new_y = new_y * math.cos(B) - z * math.sin(B)
            
            screen_x = int(width / 2 + new_x * 6)
            screen_y = int(height / 2 + new_y * 3)

            if 0 < screen_x < 59 and 0 < screen_y < 39:
                index = screen_y * width + screen_x
                if new_z > z_buffer[index]:
                    z_buffer[index] = new_z                
                    canvas[index] = "." # задняя грань

            y += 0.1
        x += 0.1

    y = -2.0
    while y <= 2.0:
        z = -2.0
        while z <= 2.0:
            
            #правая стенка
            x_side = 2.0
            new_x = x_side * math.cos(A) - y * math.sin(A)
            new_y = x_side * math.sin(A) + y * math.cos(A)
            new_z = new_y * math.sin(B) + z * math.cos(B)
            new_y = new_y * math.cos(B) - z * math.sin(B)
            
            screen_x = int(width / 2 + new_x * 6)
            screen_y = int(height / 2 + new_y * 3)

            if 0 < screen_x < 59 and 0 < screen_y < 39:
                index = screen_y * width + screen_x
                if new_z > z_buffer[index]:
                    z_buffer[index] = new_z
                    canvas[index] = "~"

            #левая стенка
            x_side = -2.0
            new_x = x_side * math.cos(A) - y * math.sin(A)
            new_y = x_side * math.sin(A) + y * math.cos(A)
            new_z = new_y * math.sin(B) + z * math.cos(B)
            new_y = new_y * math.cos(B) - z * math.sin(B)
            
            screen_x = int(width / 2 + new_x * 6)
            screen_y = int(height / 2 + new_y * 3)

            if 0 < screen_x < 59 and 0 < screen_y < 39:
                index = screen_y * width + screen_x
                if new_z > z_buffer[index]:
                    z_buffer[index] = new_z
                    canvas[index] = "*"

            z += 0.1
        y += 0.1

    x = -2.0
    while x <= 2.0:
        z = -2.0
        while z <= 2.0:
            
            #верхняя стенка
            y_side = 2.0
            new_x = x * math.cos(A) - y_side * math.sin(A)
            new_y = x * math.sin(A) + y_side * math.cos(A)
            new_z = new_y * math.sin(B) + z * math.cos(B)
            new_y = new_y * math.cos(B) - z * math.sin(B)
            
            screen_x = int(width / 2 + new_x * 6)
            screen_y = int(height / 2 + new_y * 3)

            if 0 < screen_x < 59 and 0 < screen_y < 39:
                index = screen_y * width + screen_x
                if new_z > z_buffer[index]:
                    z_buffer[index] = new_z
                    canvas[index] = "+"

            #ижняя стенка
            y_side = -2.0
            new_x = x * math.cos(A) - y_side * math.sin(A)
            new_y = x * math.sin(A) + y_side * math.cos(A)
            new_z = new_y * math.sin(B) + z * math.cos(B)
            new_y = new_y * math.cos(B) - z * math.sin(B)
            
            screen_x = int(width / 2 + new_x * 6)
            screen_y = int(height / 2 + new_y * 3)

            if 0 < screen_x < 59 and 0 < screen_y < 39:
                index = screen_y * width + screen_x
                if new_z > z_buffer[index]:
                    z_buffer[index] = new_z
                    canvas[index] = "%"

            z += 0.1
        x += 0.1

    for i in range(height):
        canvas[i * width + 59] = '\n'
    
    new_canvas = ''.join(canvas)
    
    print('\x1b[2J\x1b[H' + new_canvas, end='', flush=True)

    A += 0.05
    B += 0.03
    time.sleep(0.01)