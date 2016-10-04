def frangeld(start_x, end_x, inc_x):
    while start_x <= end_x:
        yield start_x
        
def frangeld_2(start_x, end_x, inc_x, start_y, end_y, inc_y):
    for i in frangeld(start_x, end_x, inc_x):
        for j in frangeld(start_y, end_y, inc_y):
            yield start_x, start_y
    
            
