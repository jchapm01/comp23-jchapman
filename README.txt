Jessie Chapman
<<<<<<< HEAD
Comp23, Lab 3 - The Battle for Ram Aras
Date: 2/22/2014

Note: I used the Lasers-group.y and multisteaks game as references
for building my two modules; I found there was a lot of overlap
between the Laser.py I wrote and Lasers-group.py, as they
were functionally the same program.

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
=======
Comp23 Lab 2 README
2/20/2014

***What has been correctly implemented:

ip_addresses.py: Since this program prints out every possible IP address
		 (4 3-digit numbers separated by a . with each number
		 in the range [0, 255] inclusive), it has been implemented
		 correctly.
reverselist.py: I hard-coded a simple list in the program itself,
		and just used the .reverse() python function to
		reverse the list. It prints out in reverse order
		as expected.
word_count.py: This prints out every unique word in a given input file,	
	       with its corresponding frequency in the file itself,
	       and the total number of words in the original file
	       (including the multiples of a unique word).


***I don't believe I implemented anything incorrectly.


***Collaborated with Jared Bronen

***I spent approximately 2 hours completing Lab 2
>>>>>>> 7a4f8240280980c14b7256f54b7771134be59ec6
