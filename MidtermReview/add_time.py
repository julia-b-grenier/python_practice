def add_time(minutes1, seconds1, minutes2, seconds2):
    minutes = minutes1 + minutes2
    seconds = seconds1 + seconds2
    
    minutes += seconds//60
    seconds = seconds % 60
    
    hours = minutes // 60
    minutes = minutes%60
    
    print(hours, minutes, seconds)