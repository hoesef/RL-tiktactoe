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

[ ] Create surface that grows to fit text


# Thoughts
A collection of thoughts or improvements that I would like to come back to at some point, jut not right now

## Thought 001
Location: screen.py
Thought : I don't think I'm a fan of how I am doing the screen updates. At the moment to update a button I have to update
          entire screen, what I want is to only update the area of the screen that has changed since the last frame was drawn. 
Fix     : I created 2 helper draw functions, partial_draw() and full_draw(). The draw() function now checks if we need to do a 
          full redraw of if we can get away with a partial.

## Thought 002 - NOT IMPLEMENTED
Location: text.py
Thought : Although I have just spent a while getting it so that text will shrink and wrap to fit within a text box, I think
          I actually want the oposite to happpen - the text box to grow to fit the text. This will mean that all text  elements that are placed have the font size that we assign to them, rather than one that it gives itself (as this  is already something that is annoying me).
Fix     : Create a function that takes in some max width (or max height), and keeps adding text to a line as long as it 
          doesn't excede the max width. Once all words have been processed, return the dimensions of the text box.