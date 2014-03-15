"The Mansion" by "Jessie Chapman"

memento_points is a number variable. memento_points is 0.


Unlocking is an action applying to one thing.
Understand "unlock [container]" as unlocking.

Carry out unlocking:
	if the chest is closed:
		now the chest is unlocked;
		say "Unlocking the chest gets you one step closer to accomplishing your goal";
	otherwise:
		now the chest is unlocked;
		say "I guess you can unlock an already open chest...it must have ghostly magic by the rest of this place".


Locking is an action applying to one thing.
Understand "lock [container]" as locking.

Carry out locking:
	if memento_points is less than 5 and chest is closed:
		now the chest is locked;
		say "Not just yet...there's more to put in here. You won't rest until all your mementos are safely hidden away.";
	otherwise if memento_points is less than 5 and chest is open:
		now the chest is locked;
		say "Locking an open chest...interesting choice. Ghosts can do whatever they want, I guess.";
	otherwise:
		now the chest is locked;
		end the story saying "All of your mementos are safely tucked away. Your restless soul is now at peace.".


Putting it in is an action applying to two things.
Understand "put [thing] in [container]" as putting it in.


Petting is an action applying to one thing.
Understand "pet [animal]" as petting.

Carry out petting:
	If the thing is the mouse:
		say "The mouse squeaks.";
	Otherwise if the thing is the cat:
		say "The cat purrs. But don't pet it for too long, cats 			are finicky.";
	Otherwise if the thing is the dog:
		say "The dog barks and wags its tail.";
	Otherwise:
		say "Ain't nothin' to pet here.".


Quizzing it about is an action applying to two things.
Understand "ask [someone] about [thing]" as quizzing it about.

Instead of quizzing mouse about something:
	decrease the score by 2;
	say "This isn't Micky Mouse here. He doesn't know anything. That was silly of you!".
Instead of quizzing cat about something:
	decrease the score by 2;
	say "It can only purr, silly. It probably doesn't care what you have to say anyway...it's a cat.".
Instead of quizzing dog about something:
	decrease the score by 2;
	say "Man's best friend...you wish he could talk! So silly. I'm sure he'd have some great stories to tell.".

After quizzing the maid about watch:
	award 5 points;
	say "She replies, 'Ah yes, I know that watch well. 			Your father passed it down to you on your 21st 			birthday, remember?. Unfortunately, after everyone else passed, it has just been lying in the dining room ever since...'".
After quizzing maid about book:
	award 5 points;
	say "Oh, you mean the violin sheet music? You used to love playing all those beautiful songs. You remember, don't you?".
After quizzing maid about violin:
	award 5 points;
	say "Your old violin! I'm surprised it hasn't disintegrated after all these years.".
After quizzing maid about hat:
	award 5 points;
	say "That's always looked so lovely on you. Not that anyone else could tell you that, they wouldn't be able to see you anyway...".
After quizzing maid about ring:
	award 5 points;
	say "What a sad memento...I can't believe you found your old wedding ring. We all thought it was lost forever after that fatal car crash. Your wife looked so beautiful in her wedding dress that day and you in your tuxedo. They were able to recover both your bodies but no one could find the ring...".
After quizzing maid about reading glasses:
	award 5 points;
	say "Yes, your vision wasn't so great. Pretty glad you don't have to worry about that anymore, now do you?".
	
After quizzing the butler about watch:
	award 5 points;
	say "Yeah, you used to tell time with that. Time is relative in life, right? I guess it's irrelevant to those in the afterlife though...".
After quizzing butler about book:
	award 5 points;
	say "Those were beautiful songs you used to play. What I'd give to hear you play one more time. But alas, that's impossible now given your...condition...".
After quizzing butler about violin:
	award 5 points;
	say "I remember you saving up all your allowance money for that when you were young. It was your proudest purchase.".
After quizzing butler about hat:
	award 5 points;
	say "You almost wore that hat to your wedding but your fiance wouldn't let you! She said you'd look foolish wearing that hat with a tuxedo in a chapel. It pains me to talk about that day - I can't imagine how you felt. I wonder if death hurts at all...".
After quizzing butler about ring:
	award 5 points;
	say "Yes, your fiance certainly loved that ring.".
After quizzing butler about reading glasses:
	award 5 points;
	say "Your vision is probably still terrible, even as a ghost!".


When play begins:
	say "You are a lost soul traveling infinitely through the mortal world...and something is unsettling to you. You must find out why to have your soul finally rest in peace forever."


The courtyard is a room.
The description of the courtyard is "You are in a grand courtyard located south of the mansion. To the east is an iron gate. To the north is the mansion. There is a wooden door to the mansion, which is closed.".
Understand "grand courtyard" or "yard" as the courtyard.


The gate is east of the courtyard. The gate is south of the cellar. The gate is a door.
Understand "iron gate" as the gate.
After opening the gate, say "A narrow passage leads to an opening at the end...seems intriguing.".


The wooden door is north of the courtyard. The wooden door is south of the lobby.  The wooden door is a closed door. 
After opening the wooden door:
	say "You see a lobby inside.".


North of the wooden door is a room called the lobby. The description of the lobby is "You are in a long lobby. Down the hall you see a dim light, north of where you stand. There are pictures on the walls of the lobby.".
A pictures is a thing in the lobby. The description of the pictures is "A couple old photos hang askew on the walls. A woman and...a man... . You. You are with the woman, who is wearing a flowing white dress and a veil. You are wearing a tuxedo. How can this be? What does this mean?".


North of the lobby is a room called the dining room. The description of the dining room is "A candle sits on a dining room table, flickering. There are ceramic plates and bowls set on the table as if leftover from dinner. There are openings to other rooms to the east and west.".
A table is in the dining room.
A watch is in the dining room. The description of the watch is "The face of the watch seems vaguely familiar. You recall seeing it many times, but are not sure where. This seems important.".
Instead of taking the table:
	say "You can't carry [the noun] around!".


West of the dining room is a room called the kitchen.
The description of the kitchen is "You have come upon an old, dilapidated kitchen with stains on the floor and moldy food in the sink. A maid stands by the sink.".
A maid is in the kitchen. The maid is a woman.


South of the kitchen is a room called the cellar.
The description of the cellar is "You entered a dark cellar. There isn't much in here besides a small friendly-looking mouse and a ring in the corner.".
A ring is in the cellar. The description of the ring is "Upon examination you see that it is a small ring.".
A mouse is in the cellar. The mouse is an animal.


East of the dining room is a room called the study.
The description of the study is "This room is so comforting...a study of sorts. A cat is curled up in the middle of the room. A bookcase on the opposite room has fallen over, revealing what looks like a door.".
A book is in the study. The description of the book is "A book of sheet music for the violin.".
A bookcase is in the study. The description of the bookcase is "It's a big ol' bookcase that crumbled on itself from termites gnawing at it.".
Instead of taking the bookcase:
	say "You don't have pockets big enough for that...".
A cat is in the study. The cat is an animal.


East of the study is an iron door. West of the panic room is an iron door. The iron door is a door.


East of the iron door is a room called the panic room.
The description of the panic room is "A wave of nostalgia comes over you as you enter this room - it is completely sealed off from the rest of the mansion: a panic room. A single chest stands in the middle of the room. You have an urge to fill the chest with those things that are most important to you and keep them there forever, unable to be unlocked by anyone ever again...".


A chest is in the panic room. The chest is a closed lockable container. The description of the chest is "An ornate chest with music notes printed all over it: notes to your favorite song on the violin.".
		

After putting the ring in the chest for the first time:
	increment memento_points;
	now the ring is in the chest;
	say "The ring fits perfectly!".
After putting the ring in the chest:
	now the ring is in the chest;
	say "Yep, this seems like the spot for it.".
	
After putting the book in the chest for the first time:
	increment memento_points;
	now the book is in the chest;
	say "The book fits perfectly!".
After putting the book in the chest:
	now the book is in the chest;
	say "Yep, this seems like the spot for it.".
	
After putting the watch in the chest for the first time:
	increment memento_points;
	now the watch is in the chest;
	say "The watch fits perfectly!".
After putting the watch in the chest:
	now the watch is in the chest;
	say "Yep, this seems like the spot for it.".
	
After putting the violin in the chest for the first time:
	increment memento_points;
	now the violin is in the chest;
	say "The violin fits perfectly!".
After putting the violin in the chest:
	now the violin is in the chest;
	say "Yep, this seems like the spot for it.".
	
After putting the hat in the chest for the first time:
	increment memento_points;
	now the hat is in the chest;
	say "The hat fits perfectly!".
After putting the hat in the chest:
	now the hat is in the chest;
	say "Yep, this seems like the spot for it.".
	
After putting the reading glasses in the chest for the first time:
	increment memento_points;
	now the reading glasses is in the chest;
	say "The reading glasses fit perfectly!".
After putting the reading glasses in the chest:
	now the reading glasses is in the chest;
	say "Yep, this seems like the spot for it.".
	

North of the dining room is a room called the lounge.
The description of the lounge is "Upon entering a lounge you see a butler. He gives you a long, empty stare. It's kind of creepy. A closed door is to the right of the butler, who you really want to get away from, but considering he's one of few people who can tell you anything about this place, you may as well talk to him.".
A violin is in the lounge.
A butler is in the lounge. The butler is a man.


The red door is west of the lounge. The red door is east of the bedroom. The red door is a closed door.


West of the red door is a room called the bedroom.
The description of the bedroom is "You entered a bedroom. It seems like the kind of place you would sleep - a plush, queen-sized bed...and a dog. Curled up on the bed. He wags his tail when he sees you.".
A hat is in the bedroom.
A dog is in the bedroom. The dog is an animal.


North of the bedroom is a room called the attic.
The description of the attic is "You found yourself in a dusty attic. You feel a sneeze coming on because of the dust but can't seem to bring yourself to sneeze...weird. Your allergies kick in but your eyes aren't tearing either...still weird. It's like your body can't respond to anything...if you even have a body at all...".
A pair of reading glasses is in the attic. Understand "glasses" or "reading glasses" as the pair of reading glasses.