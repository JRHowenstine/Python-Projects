"""
Creating a parent class and two child classes
with their own added attributes
"""

# Define Parent Class with default values
class Animal:
    species = "None"
    body_covering = " "
    avg_lifespan = 0
    top_speed = 0

# Define Child classes who inherit from parent and have unique attributes as well
class Bird(Animal):
    wingspan = 0
    color_of_eggs = " "

class Fish(Animal):
    number_of_fins = 0
    depth_live_at = 0
    
    
    
