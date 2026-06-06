"""
ascii_art.py – Contains the ASCII art stages for Snowman Meltdown.
Each stage represents a progressively melting snowman.
"""

STAGES = [
    # Stage 0: Full snowman
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
    # Stage 1: Bottom part starts melting
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
    # Stage 2: Torso melted
    """
      ___  
     /___\\ 
     (o o) 
     """,
    # Stage 3: Body melted, only hat remains
    """
      ___  
     /___\\ 
     """,
    # Stage 4: Snowman completely melted
    """
    *  .  *
      . * .
    *  . * 
    (puddle)
    """,
]
