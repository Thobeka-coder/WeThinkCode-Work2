

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input('Shape?: ')
    while True:
        if shape == 'pyramid':
            return 'pyramid'
        elif shape == 'square':
            return 'square'
        elif shape == 'triangle':
            return 'triangle'
        elif shape == 'rhombus':
            return 'rhombus'
        elif shape == 'rectangle':
            return 'rectangle'
        elif shape == 'diamond':
            return 'diamond'
        else:
            try:
                shape = input('Shape?: ')
            except:
                pass
            


# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = input("Height?: ")
    if height.isnumeric() and int(height) <=80:
        return(int(height))
    else:
        while height.isnumeric() != True or int(height) > 80:
            height = input("Height?: ")
        return(int(height))

# TODO: Step 2
def draw_pyramid(height, outline):
    h = height
    if outline:
        for i in range(1, h + 1):
            for j in range(0, h - i, + 1):
                print(' ', end='')
            for j in range(1, 2 * i):
                if j == 1 or j == 2 * i - 1 or i == h:
                    print('*',end='')
                else: 
                    print(' ', end='')
            print()


    else:
        for i in range(1, h + 1):
            for j in range(0, h - i, + 1):
                print(' ', end='')
            for j in range(1, 2 * i):
                if j == 1 or j == 2 * i - 1:
                    print('*', end='')
                else:
                    print('*', end='')
            print()


# TODO: Step 3
def draw_square(height, outline):
    h = height
    if outline:
        for i in range(h):
            for j in range(h):
                if i==0 or i== h-1 or j==0 or j== h-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("")
    else:
        for i in range(h):
            for i in range(h):
                print('*', end='')
            print()

# TODO: Step 4
def draw_triangle(height, outline):
    h = height
    if outline:
        for i in range(h):
            for j in range(i+1):
                if j==0 or j==i or i==h-1:
                    print('*', end='')
                else:
                    print(' ',end='')
            print()
    
    else:
        for i in range(1, h + 1):
            for j in range(1, i + 1):
                print('*', end='')
            print()            


def draw_rhombus(height, outline):
    h = height
    if outline:
        for i in range(1, h + 1):
            for j in range(1, h - i + 1):
                print(end=' ')
            if i == 1 or i == h:
                for j in range(1, h + 1):
                    print('*', end='')
            else:
                for j in range(1, h + 1):
                    if j == 1 or j == h:
                        print('*', end='')
                    else:
                        print(end=' ')
            print()
    
    else:
        for i in range(1, h +1):
            for j in range(1, h - i + 1):
                print(end=' ')
            for j in range(1, h + 1):
                print('*', end='')
            print()

def draw_rectangle(height, outline):
    h = height
    w = h * 3       # w / width represents the columns
    if outline:
        for i in range(0, h):
            for j in range(0, w):
                if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                    print('*', end= '')
                else:
                    print(' ', end='')
            print()
    
    else:
        for i in range(h):
            for i in range(w):
                print('*', end= '')
            print()


def draw_diamond(height, outline):
    h = height
    if outline:
        for i in range(1, h + 1):
            for j in range(0, h - i, + 1):   #range must actually start from 0 in order to be in line with the bottom part
                print(' ', end='')
            for j in range(1, 2 * i):
                if j == 1 or j == 2 * i - 1:
                    print('*', end='')
                else:
                    print('', end=' ')
            print()
    
        for i in range(h - 1, 0, - 1):
            for j in range(0, h - i, + 1):
                print(' ', end='')
            for j in range(1, 2 * i):
                if j == 1 or j == 2 * i - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    
    
    
    else:
        for i in range(1, h + 1):
            for j in range(0, h - i, + 1):
                print(' ', end='')
            for j in range(1, 2 * i):
                if j == 1 or j == 2 * i - 1:
                    print('*', end='')
                else:
                    print('*', end='')
            print()
    
        for i in range(h - 1, 0, - 1):
            for j in range(0, h - i, + 1):
                print(' ', end='')
            for j in range(1, 2 * i):
                if j == 1 or j == 2 * i - 1:
                    print('*', end='')
                else:
                    print('*', end='')
            print()
        
        

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    elif shape == 'square':
        draw_square(height, outline)
    elif shape == 'triangle':
        draw_triangle(height, outline)
    elif shape == 'rhombus':
        draw_rhombus(height, outline)
    elif shape == 'rectangle':
        draw_rectangle(height, outline)
    elif shape == 'diamond':
        draw_diamond(height, outline)
        
        

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (y/N): ")
    if outline ==  "y" or outline == "Y":
            return True
    else:
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)