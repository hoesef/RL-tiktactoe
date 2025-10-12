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
Thought : I don't think I'm a fan of how I am doing the screen updates. At the moment I am doing one WIN.fill when the 
          screen is instancaiated and then only updating the area that changes each frame, if any. While this is efficient it aldo means that if I want to do a full screen update I either have to add the entire screen to 
          appContext.updateArea or I have to add another variable (bool: fullScreenUpdate, for example) to handle this case. Neither seem very nice
Fix     :