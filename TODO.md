# TODO:
[ ] Finish settings up agnet vs agent
    [ ] Alternating agent start
    [ ] Adjust value function
[ ] Visualization with pygame
    [ ] Select agent (random vs)
    [ ] Train agent
    [ ] Agent vs Agent or Agent vs user
[ ] Tidy up code
    [ ] comments and docs


# Thoughts
A collection of thoughts or improvements that I would like to come back to at some point, jut not right now

## Thought 001
Location: screen.py
Thought : I don't think I'm a fan of how I am doing the screen updates. At the moment to update a button I have to update
          entire screen, what I want is to only update the area of the screen that has changed since the last frame was drawn. 
Fix     : I created 2 helper draw functions, partial_draw() and full_draw(). The draw() function now checks if we need to do a 
          full redraw of if we can get away with a partial.