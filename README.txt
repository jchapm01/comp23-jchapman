Jessie Chapman
Comp23, Lab 3 - The Battle for Ram Aras
Date: 2/22/2014

#########################################
# What has been correctly implemented   #
#########################################

I believe I have implemented everything in both
Laser.py and Battlecruiser.py correctly.
The Battlecruiser only shoots out one laser per
space bar press, and that laser continues up the
screen until it "dies." 

The only thing I am unsure of (though everything
works correctly from the user's/player's perspective)
is I don't update my background image within the game
loop - I update it (using screen.blit()) within the
Battlecruiser and Laser update() functions. From a
game programming perspective I'm not sure if this
is the right way to go about it.

####################
# Collaboration    #
####################

Jared Bronen helped me with the idea of having a
.fire() method for the Battlecruiser, because 
my original implementation had a constant
stream of lasers shoot out every time the
user pressed the space bar, instead of just
a single laser being shot. It turns out I was just
assigning the pressed variable the value "SPACE"
instead of just adding a laser immediately after
the key event for K_SPACE was received, and
within my Battlecruiser's update() function
I was adding a laser to the group - so the game
loop updated the laser group out of order and
therefore showed a constant stream of lasers until
the next key press. 

########################
# Approx. hours spent  #
########################
4 hours
