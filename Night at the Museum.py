def min_rotations(exhibit_name):
    current_position = ord('a')
    total_rotations = 0
 
    for char in exhibit_name:
        target_position = ord(char)
        clockwise_rotations = (target_position - current_position) % 26
        counterclockwise_rotations = (current_position - target_position) % 26
        total_rotations += min(clockwise_rotations, counterclockwise_rotations)
        current_position = target_position
 
    return total_rotations
 
exhibit_name = input().strip()
print(min_rotations(exhibit_name))
