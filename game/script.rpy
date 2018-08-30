# Welcome to LoreMaster! This game was created for the 1st Steem Monster game jam (https://itch.io/jam/steem-monsters-1000-invitational)
# as part of the Steem Monster+ collection. The work here is not canon is distributed in accordance with the Steem Monster license.
# Steem Monsters universe, lore, images, cards, and names belong to Steem Monsters (http://www.steemmonsters.com).
# Check out their Discord at https://discord.gg/CAFJRjY, and their official steem account http://steemit.com/@steemmonsters. 
# This is the script that controls the game.

# Here are the characters we are using. We define them in a variable so when we are typing out the script
# we can just use one letter to display who is talking

define k = Character("Kiara")
define a = Character("Alric")
define l = Character("Lyanna")
define m = Character("Malric")
define t = Character("Tyrus")
define z = Character("Zintar")
define s = Character("Selenia")

# Here we are defining some of the other images that are usef, like the card images.
# The xalign and yalign decimals allow us to position them exactly where we want
# them on the screen.

image sabreshark = Image("sabreshark.png", xalign=0.75, yalign=0.25)
image spirit = Image("spiritoftheforest.png", xalign=0.25, yalign=0.25)
image selenia = Image("selenia_sky.png", xalign=0.5, yalign=0.25)

# The game starts here.

label start:
# Here is where the bedroom background is disaplyed
    scene bedroomnight
# Here's where we tell it to start playing the music
    play music "thesplinterlands.mp3"
# The narrating character does not need a character name displayed for their script
    "..."

    "I'm so glad I got my first pack of Steem Monster cards..."
# Here we display the cards one at a time for the player, with the dissolve
# characteristic to make the transition smoother. I also added the pause
# command otherwise the cards would all appear at once
    show spirit
    with dissolve
    pause
    show sabreshark
    with dissolve
    pause
    show selenia
    with dissolve
    pause

    "Selenia is my favourite so far. I heard she has mysterious powers..."

    "Hmm...it's getting late."

    "Time for bed. Guess I'll have to try out my first match tomorrow."

    "Hope I'm up to the challenge!"

    "Zzzzz..."

    scene fantasyforest
    with fade

    scene fantasyforest
    with fade
# Here's our first sound effect! Ren'Py allows you to run both music and sound effects.
    play sound "arrival.mp3"
    show kiara
    with dissolve
# Because it is Kiara speaking, we used the k here in the script. This tells Ren'Py to display
# her name when she's talking to us.
    k "Hey..."

    "..."

    k "Hey...are you okay?"

    "..."

    play sound "kiara.mp3"
    k "You look pretty shook up there!"

    "...where am I?"

    k "Welcome to the Splinterlands. You must be a new player."

    "The Splinterlands...that's the world of Steem Monsters, right?"

    "Am I dreaming?"

    k "Heh maybe...you can choose to believe so if it helps."

    "What...?"

    k "Guess you took the plunge, huh? Got your first cards and now...you'll have to test your knowledge."

    "..."

    play sound "kiara.mp3"
    k "You *do* know about that, right?"

    "Mm...my head's a little fuzzy..."

    k "I'll say!"

    k "You're here to pass a test. After all, not just anyone can wield the power of monsters, right?"

    "Ahh...well..."

    k "Don't worry! I'm sure you'll do fine! You have good motivation after all!"

    "What's that?"

    k "Well of course...you can't go home until you pass the test!"

    k "I'd say that's some pretty good motivation! Well, I wish you luck!"

    "Thanks? Wait, what?!"

    k "Heh. Don't worry. Just journey on over to Alric Stormbringer. He'll set you straight! He'll have some questions for you."

    k "Once you've passed his challenge, each of the summoners that could be your battling partners will give you challenges of their own."

    k "Your job is to answer their questions correctly! If you do, you'll progress until you meet the one that has the power to send you home."

    k "Be careful, though. If you get 3 wrong, they'll send you all the way back to the beginning and it will be like you never met us."

    "..."

    k "Cheer up! On the bright side, you're lucky you ran into me first, right? A summoner instead of a monster right away, heh... At least I could give you some good advice!"

    "..."

    k "Hurry up, now! Alric is waiting! And you don't want to become dragon food out here..."
    #The labels define sections of our game, making it easier to run loops of gameplay and
    #jump the player around as we need.
    label alric:

    scene fantasyforest
    show alric
    with dissolve
    #Here's where we start of the quiz scoring. We set it to zero to make sure we're starting with a clean slate.
    $ quiz_score = 0

    a "Greetings traveller."

    a "Do you believe you have what it takes to get past me?"

    a "Keep your eyes open and your wits sharp. You never know where you'll find the answers."

    a "Whether you are ready or not...we begin."

    a "First question. How many elements are known in Splinterlands lore?"
#Here we use the menu function as the mechanic for our quiz. A wrong answer will add +1 to the quiz score and
#a right answer will send us to the next section without adding anything.
    menu:

        "5":
            $ quiz_score += 1
            jump alric_1stwrong

        "4":
            $ quiz_score += 1
            jump alric_1stwrong

        "6":
            jump alric_2nd

        "2":
            $ quiz_score += 1
            jump alric_1stwrong

#Here you can see if the player gets it wrong, we play the sound of the summoner's discontent and then
#tell the game to check the player's score. If the player has gotten 3 wrong, the summoner will say their
#dialogue and game will skip them to the end. If the player has gotten less than three wrong, the summoner
#will prompt them to try again. Each summoner follows the same formula. I believe there is a more elegant way
#to do this function rather than the repetition I used but because this was created for a game jam, I wanted
#to use a formula I knew would work.
    label alric_1stwrong:
    play sound "alric.mp3"
    # Check the quiz score
    if quiz_score == 3:
        a "You are not ready for the challenge. Begone until you have improved your skills."
        jump end

    else:
        a "Hmm... Disappointing... Try again. How many elements are known in Splinterlands lore?"

    menu:

        "5":
            $ quiz_score += 1
            jump alric_1stwrong

        "4":
            $ quiz_score += 1
            jump alric_1stwrong

        "6":
            jump alric_2nd

        "2":
            $ quiz_score += 1
            jump alric_1stwrong

#Here we tell the game to play a sound when the player gets it right. It really adds something interactive.
#I used the same sound for every correct answer to give the game a sense of cohesion.
    label alric_2nd:
    play sound "win.mp3"
    a "Correct. There are 6 elements currently known in the Splinterlands."

    a "Second question. How many different kinds of playable cards are there in Steem Monsters?"

    menu:

        "6":
            $ quiz_score += 1
            jump alric_2ndwrong

        "3":
            $ quiz_score += 1
            jump alric_2ndwrong

        "4":
            $ quiz_score += 1
            jump alric_2ndwrong

        "2":
            jump alric_3rd

    label alric_2ndwrong:
    play sound "alric.mp3"
    if quiz_score == 3:
        a "You are not ready for the challenge. Begone until you have improved your skills."
        jump end

    else:
        a "Unfortunate. Once again. How many different kinds of playable cards are there in Steem Monsters?"

    menu:

        "6":
            $ quiz_score += 1
            jump alric_2ndwrong

        "3":
            $ quiz_score += 1
            jump alric_2ndwrong

        "4":
            $ quiz_score += 1
            jump alric_2ndwrong

        "2":
            jump alric_3rd

    label alric_3rd:
    play sound "win.mp3"
    a "Correct. You are showing promise. There are two kinds of cards: Summoner cards and Monster cards."

    a "Third question. Are Summoner cards stats higher than Monster card stats?"

    menu:

        "No":
            jump alric_4th

        "Yes":
            $ quiz_score += 1
            jump alric_3rdwrong

        "Sometimes":
            $ quiz_score += 1
            jump alric_3rdwrong

        "They are the same":
            $ quiz_score += 1
            jump alric_3rdwrong

    label alric_3rdwrong:
    play sound "alric.mp3"
    if quiz_score == 3:
        a "You are not ready for the challenge. Begone until you have improved your skills."
        jump end

    else:
        a "Are you sure you're ready for this? Try again. Are summoner stats higher than monster stats?"

    menu:

        "No":
            jump alric_4th

        "Yes":
            $ quiz_score += 1
            jump alric_3rdwrong

        "Sometimes":
            $ quiz_score += 1
            jump alric_3rdwrong

        "They are the same":
            $ quiz_score += 1
            jump alric_3rdwrong

    label alric_4th:
    play sound "win.mp3"
    a "Well done. The answer is no. True seekers of knowledge know that Summoners themselves do not have stats."

    a "Fourth question. Can Splinters from different elements work together?"

    menu:

        "Always":
            $ quiz_score += 1
            jump alric_4thwrong

        "Only Dragon element and one other.":
            jump alric_5th

        "Never.":
            $ quiz_score += 1
            jump alric_4thwrong

        "Only Death element and one other.":
            $ quiz_score += 1
            jump alric_4thwrong

    label alric_4thwrong:
    play sound "alric.mp3"
    if quiz_score == 3:
        a "You are not ready for the challenge. Begone until you have improved your skills."
        jump end

    else:
        a "Hmm... I believe you need more study in the arcane arts. I repeat...can splinters from different elements work together?"

    menu:

        "Always":
            $ quiz_score += 1
            jump alric_4thwrong

        "Only Dragon element and one other.":
            jump alric_5th

        "Never.":
            $ quiz_score += 1
            jump alric_4thwrong

        "Only Death element and one other.":
            $ quiz_score += 1
            jump alric_4thwrong

    label alric_5th:
    play sound "win.mp3"
    a "Perhaps you are indeed worthy...you have answered my questions correctly."

    a "Continue on to Lyanna and see if your luck holds..."
#We're using the same background for Lyanna as we did Alric, so here only his sprite dissolves
#and we do not change scene yet.
    hide alric
    with dissolve

    label lyanna:

    scene fantasyforest2
    show lyanna
    with dissolve

    l "Oh hello! Welcome!"

    l "I'm glad you made it this far. But make no mistake!"

    l "I won't go easy on you!"

    l "First question. I am Confident, Self-Sacrificing, and Relentless. What element am I?"

    menu:

        "Water":
            $ quiz_score += 1
            jump lyanna_1stwrong

        "Life":
            $ quiz_score += 1
            jump lyanna_1stwrong

        "Earth":
            $ quiz_score += 1
            jump lyanna_1stwrong

        "Death":
            jump lyanna_2nd


    label lyanna_1stwrong:
    play sound "lyanna.mp3"

    if quiz_score == 3:
        l "Uh oh. Sorry but you've failed this test! I'll have to send you back to the beginning!"
        jump end

    else:
        l "Oh dear. Are you sure you're cut out for this?"

    l "Try again. I am Confident, Self-Sacrificing, and Relentless. What element am I?"

    menu:

        "Water":
            $ quiz_score += 1
            jump lyanna_1stwrong

        "Life":
            $ quiz_score += 1
            jump lyanna_1stwrong

        "Earth":
            $ quiz_score += 1
            jump lyanna_1stwrong

        "Death":
            jump lyanna_2nd


    label lyanna_2nd:
    play sound "win.mp3"
    l "Well done!"

    l "Second question. I am Creative, Destructive, and Energetic. What element am I?"

    menu:

        "Fire":
            jump lyanna_3rd

        "Dragon":
            $ quiz_score += 1
            jump lyanna_2ndwrong

        "Water":
            $ quiz_score += 1
            jump lyanna_2ndwrong

        "Earth":
            $ quiz_score += 1
            jump lyanna_2ndwrong

    label lyanna_2ndwrong:
    play sound "lyanna.mp3"
    if quiz_score == 3:
        l "Uh oh. Sorry but you've failed this test! I'll have to send you back to the beginning!"
        jump end

    else:
        l "Hmm...I don't know about that..."

    l "One more time! I am Creative, Destructive, and Energetic. What element am I?"

    menu:

        "Fire":
            jump lyanna_3rd

        "Dragon":
            $ quiz_score += 1
            jump lyanna_2ndwrong

        "Water":
            $ quiz_score += 1
            jump lyanna_2ndwrong

        "Earth":
            $ quiz_score += 1
            jump lyanna_2ndwrong

    label lyanna_3rd:
    play sound "win.mp3"

    l "Great job! Next! I am Unpredictable, Intuitive, and Controlling. What element am I?"

    menu:

        "Wind":
            $ quiz_score += 1
            jump lyanna_3rdwrong

        "Water":
            jump lyanna_4th

        "Earth":
            $ quiz_score += 1
            jump lyanna_3rdwrong

        "Dragon":
            $ quiz_score += 1
            jump lyanna_3rdwrong

    label lyanna_3rdwrong:
    play sound "lyanna.mp3"
    if quiz_score == 3:
        l "Uh oh. Sorry but you've failed this test! I'll have to send you back to the beginning!"
        jump end

    else:
        l "Are you really listening to me?"

    l "I am Unpredictable, Intuitive, and Controlling. What element am I?"

    menu:

        "Wind":
            $ quiz_score += 1
            jump lyanna_3rdwrong

        "Water":
            jump lyanna_4th

        "Earth":
            $ quiz_score += 1
            jump lyanna_3rdwrong

        "Dragon":
            $ quiz_score += 1
            jump lyanna_3rdwrong

    label lyanna_4th:
    play sound "win.mp3"
    l "Impressive!"

    l "Alright, let's get serious! Which of these is NOT an element in Splinterlands?"

    menu:

        "Earth":
            $ quiz_score += 1
            jump lyanna_4thwrong

        "Dragon":
            $ quiz_score += 1
            jump lyanna_4thwrong

        "Wind":
            jump lyanna_5th

        "Water":
            $ quiz_score += 1
            jump lyanna_4thwrong

    label lyanna_4thwrong:
    play sound "lyanna.mp3"
    if quiz_score == 3:
        l "Uh oh. Sorry but you've failed this test! I'll have to send you back to the beginning!"
        jump end

    else:
        l "...maybe you should take up gardening instead?"

    l "Again. Which of these is NOT an element in Splinterlands?"

    menu:

        "Earth":
            $ quiz_score += 1
            jump lyanna_4thwrong

        "Dragon":
            $ quiz_score += 1
            jump lyanna_4thwrong

        "Wind":
            jump lyanna_5th

        "Water":
            $ quiz_score += 1
            jump lyanna_4thwrong

    label lyanna_5th:
    play sound "win.mp3"

    l "Okay okay...you win that one."

    l "Last chance! This one will get you for sure!"

    l "Which element is distinguished in the Splinterlands by the colour silver?"

    menu:

        "Dragon":
            $ quiz_score += 1
            jump lyanna_5thwrong

        "Fire":
            $ quiz_score += 1
            jump lyanna_5thwrong

        "Wind":
            $ quiz_score += 1
            jump lyanna_5thwrong

        "None":
            jump lyanna_6th

    label lyanna_5thwrong:
    play sound "lyanna.mp3"
    if quiz_score == 3:
        l "Uh oh. Sorry but you've failed this test! I'll have to send you back to the beginning!"
        jump end

    else:
        l "Haha! You're so funny. Stop joking around!"

    l "Which element is distinguished in the Splinterlands by the colour silver?"

    menu:

        "Dragon":
            $ quiz_score += 1
            jump lyanna_5thwrong

        "Fire":
            $ quiz_score += 1
            jump lyanna_5thwrong

        "Wind":
            $ quiz_score += 1
            jump lyanna_5thwrong

        "None":
            jump lyanna_6th

    label lyanna_6th:
    play sound "win.mp3"
    l "Looks like I'm all out of questions!"

    l "You're made of tougher stuff than you look! Head over to Malric and see if you can keep measuring up!"

    hide lyanna
    with dissolve

    label malric:

    scene court
    show malric
    with dissolve

    m "Hmm...seems you've come quite far."

    m "I'm impressed."

    m "Not any further, however."

    m "Prepare yourself."

    m "Now I will test your knowledge of summoners."

    m "I carry a purple flame. Which summoner am I?"

    menu:

        "Malric Inferno":
            $ quiz_score += 1
            jump malric_1stwrong

        "Alric Stormbringer":
            jump malric_2nd

        "Zintar Mortalis":
            $ quiz_score += 1
            jump malric_1stwrong

        "Tyrus Paladium":
            $ quiz_score += 1
            jump malric_1stwrong


    label malric_1stwrong:
    play sound "malric.mp3"
    if quiz_score == 3:
        m "Argh! A waste of my time! Begone!"
        jump end

    else:
        m "Disappointing..."
        m "Have you been paying attention?"

    m "I carry a purple flame. Which summoner am I?"

    menu:

        "Malric Inferno":
            $ quiz_score += 1
            jump malric_1stwrong

        "Alric Stormbringer":
            jump malric_2nd

        "Zintar Mortalis":
            $ quiz_score += 1
            jump malric_1stwrong

        "Tyrus Paladium":
            $ quiz_score += 1
            jump malric_1stwrong



    label malric_2nd:
    play sound "win.mp3"
    m "Hmph, let's continue."

    m "My hair is graced by an orange flower. Which summoner am I?"

    menu:

        "Zintar Mortalis":
            $ quiz_score += 1
            jump malric_2ndwrong

        "Tyrus Paladium":
            $ quiz_score += 1
            jump malric_2ndwrong

        "Lyanna Natura":
            jump malric_3rd

        "Selenia Sky":
            $ quiz_score += 1
            jump malric_2ndwrong

    label malric_2ndwrong:
    play sound "malric.mp3"
    if quiz_score == 3:
        m "Argh! A waste of my time! Begone!"
        jump end

    else:
        m "Get serious or I'll send you back to the forest!"

    m "My hair is graced by an orange flower. Which summoner am I?"

    menu:

        "Zintar Mortalis":
            $ quiz_score += 1
            jump malric_2ndwrong

        "Tyrus Paladium":
            $ quiz_score += 1
            jump malric_2ndwrong

        "Lyanna Natura":
            jump malric_3rd

        "Selenia Sky":
            $ quiz_score += 1
            jump malric_2ndwrong

    label malric_3rd:
    play sound "win.mp3"

    m "Impressive. Let's turn up the heat, shall we?"

    m "My face is always cloaked in shadow. Which summoner am I?"

    menu:

        "Alric Stormbringer":
            $ quiz_score += 1
            jump malric_3rdwrong

        "Selenia Sky":
            $ quiz_score += 1
            jump malric_3rdwrong

        "Malric Inferno":
            $ quiz_score += 1
            jump malric_3rdwrong

        "Zintar Mortalis":
            jump malric_4th

    label malric_3rdwrong:
    play sound "malric.mp3"
    if quiz_score == 3:
        m "Argh! A waste of my time! Begone!"
        jump end

    else:
        m "Maybe a fire under your backside will motivate you! Again!"

    m "My face is always cloaked in shadow. Which summoner am I?"

    menu:

        "Alric Stormbringer":
            $ quiz_score += 1
            jump malric_3rdwrong

        "Selenia Sky":
            $ quiz_score += 1
            jump malric_3rdwrong

        "Malric Inferno":
            $ quiz_score += 1
            jump malric_3rdwrong

        "Zintar Mortalis":
            jump malric_4th

    label malric_4th:
    play sound "win.mp3"

    m "Hmph, your knowledge of the Splinterlands is quite formidable. But can you answer this one?"

    m "In my left hand, I carry a staff as the symbol of my power. Which summoner am I?"

    menu:

        "Tyrus Paladium":
            jump malric_5th

        "Alric Stormbringer":
            $ quiz_score += 1
            jump malric_4thwrong

        "Selenia Sky":
            $ quiz_score += 1
            jump malric_4thwrong

        "Lyanna Natura":
            $ quiz_score += 1
            jump malric_4thwrong

    label malric_4thwrong:
    play sound "malric.mp3"

    if quiz_score == 3:
        m "Argh! A waste of my time! Begone!"
        jump end

    else:
        m "Hahaha...if you can't beat something as simple as this, you'll never handle my flame!"

    m "Again. In my left hand, I carry a staff as the symbol of my power. Which summoner am I?"

    menu:

        "Tyrus Paladium":
            jump malric_5th

        "Alric Stormbringer":
            $ quiz_score += 1
            jump malric_4thwrong

        "Selenia Sky":
            $ quiz_score += 1
            jump malric_4thwrong

        "Lyanna Natura":
            $ quiz_score += 1
            jump malric_4thwrong

    label malric_5th:
    play sound "win.mp3"

    m "Arrrrggghhh!! I have been defeated!"

    m "Begone, traveller."
    m "Carry on to Tyrus and hope that the next time we meet I am in a sweeter mood..."

    hide malric
    with dissolve

    label tyrus:

    scene court
    show tyrus
    with dissolve

    t "Greetings. I have been expecting you."

    t "To succeed in the battles ahead, you will be expected to understand deeply the power of the monsters you unleash."

    t "Are you ready for that?"

    t "Pay close attention. I will now test your knowledge of monsters."

    t "First question."

    t "I carry a candlestick on my head and a pickaxe in my hand. Who am I?"

    menu:

        "Ice Soldier":
            $ quiz_score += 1
            jump tyrus_1stwrong

        "Fire Beetle":
            $ quiz_score += 1
            jump tyrus_1stwrong

        "Stonesplitter Orc":
            $ quiz_score += 1
            jump tyrus_1stwrong

        "Kobold Miner":
            jump tyrus_2nd

    label tyrus_1stwrong:
    play sound "tyrus.mp3"

    if quiz_score == 3:
        t "A pity..."
        jump end

    else:
        t "Sigh..."

    t "I carry a candlestick on my head and a pickaxe in my hand. Who am I?"

    menu:

        "Sabre Shark":
            $ quiz_score += 1
            jump tyrus_1stwrong

        "Fire Beetle":
            $ quiz_score += 1
            jump tyrus_1stwrong

        "Stonesplitter Orc":
            $ quiz_score += 1
            jump tyrus_1stwrong

        "Kobold Miner":
            jump tyrus_2nd

    label tyrus_2nd:
    play sound "win.mp3"

    t "Adequate. Next."

    t "I carry a shield and spear of ice. Who am I?"

    menu:

        "Naga Warrior":
            $ quiz_score += 1
            jump tyrus_2ndwrong

        "Ice Soldier":
            $ quiz_score += 1
            jump tyrus_2ndwrong

        "Frozen Soldier":
            jump tyrus_3rd

        "Goblin Sorceror":
            $ quiz_score += 1
            jump tyrus_2ndwrong

    label tyrus_2ndwrong:
    play sound "tyrus.mp3"
    if quiz_score == 3:
        t "A pity..."
        jump end

    else:
        t "Are you sure you're in the right place?"

    t "I carry a shield and spear of ice. Who am I?"

    menu:

        "Naga Warrior":
            $ quiz_score += 1
            jump tyrus_2ndwrong

        "Ice Soldier":
            $ quiz_score += 1
            jump tyrus_2ndwrong

        "Frozen Soldier":
            jump tyrus_3rd

        "Goblin Sorceror":
            $ quiz_score += 1
            jump tyrus_2ndwrong

    label tyrus_3rd:
    play sound "win.mp3"
    t "Acceptable."

    t "I am large enough to carry an elephant...which I do. Who am I?"

    menu:

        "Frost Giant":
            $ quiz_score += 1
            jump tyrus_3rdwrong

        "Giant Roc":
            jump tyrus_4th

        "Pit Ogre":
            $ quiz_score += 1
            jump tyrus_3rdwrong

        "Elemental Phoenix":
            $ quiz_score += 1
            jump tyrus_3rdwrong

    label tyrus_3rdwrong:
    play sound "tyrus.mp3"
    if quiz_score == 3:
        t "A pity..."
        jump end

    else:
        t "If you insist on wasting my time, you'd be better off just leaving."

    t "I am large enough to carry an elephant...which I do. Who am I?"

    menu:

        "Frost Giant":
            $ quiz_score += 1
            jump tyrus_3rdwrong

        "Giant Roc":
            jump tyrus_4th

        "Pit Ogre":
            $ quiz_score += 1
            jump tyrus_3rdwrong

        "Elemental Phoenix":
            $ quiz_score += 1
            jump tyrus_3rdwrong

    label tyrus_4th:
    play sound "win.mp3"
    t "Hmm...maybe you do have some potential after all. We shall see."

    t "Next. I use a modified trident as my weapon and wear seashells. Who am I?"

    menu:

        "Mischievous Mermaid":
            jump tyrus_5th

        "Medusa":
            $ quiz_score += 1
            jump tyrus_4thwrong

        "Water Elemental":
            $ quiz_score += 1
            jump tyrus_4thwrong

        "Spineback Turtle":
            $ quiz_score += 1
            jump tyrus_4thwrong

    label tyrus_4thwrong:
    play sound "tyrus.mp3"
    if quiz_score == 3:
        t "A pity..."
        jump end

    else:
        t "Please don't embarrass us both."

    t "I use a modified trident as my weapon and wear seashells. Who am I?"

    menu:

        "Mischievous Mermaid":
            jump tyrus_5th

        "Medusa":
            $ quiz_score += 1
            jump tyrus_4thwrong

        "Water Elemental":
            $ quiz_score += 1
            jump tyrus_4thwrong

        "Spineback Turtle":
            $ quiz_score += 1
            jump tyrus_4thwrong

    label tyrus_5th:
    play sound "win.mp3"
    t "Despite the odds, you managed to progress."

    t "I am not sure if I believe in your powers but good luck with Zintar."

    t "...you'll need it."

    hide tyrus
    with dissolve

    label zintar:

    scene moon
    with dissolve
    show zintar
    with dissolve

    z "Heh! End of the line!"

    z "Think you got what it takes to get past me and reach the heavens?"

    z "Not a chance! To get past me, you'll need deeper knowledge of the monsters that can be summoned."

    z "Here I come!"

    z "By the time you hear the Twisted Jester's cackling laugh, it will already have your ripe _______."

    menu:

        "Fortune":
            $ quiz_score += 1
            jump zintar_1stwrong

        "Soul":
            jump zintar_2nd

        "Power":
            $ quiz_score += 1
            jump zintar_1stwrong

        "Sword":
            $ quiz_score += 1
            jump zintar_1stwrong

    label zintar_1stwrong:
    play sound "zintar.mp3"
    if quiz_score == 3:
        z "Heh, better luck next time, kid..."
        jump end

    else:
        z "Haha. Who would be interested in that? Try again..."

    z "By the time you hear the Twisted Jester's cackling laugh, it will already have your ripe _______."

    menu:

        "Fortune":
            $ quiz_score += 1
            jump zintar_1stwrong

        "Soul":
            jump zintar_2nd

        "Power":
            $ quiz_score += 1
            jump zintar_1stwrong

        "Sword":
            $ quiz_score += 1
            jump zintar_1stwrong

    label zintar_2nd:
    play sound "win.mp3"
    z "Alright alright. You got lucky! See if you can handle this next one!"

    z "The Feral Spirit lives in the __________ Forest."

    menu:

        "Stone":
            $ quiz_score += 1
            jump zintar_2ndwrong

        "Jade":
            $ quiz_score += 1
            jump zintar_2ndwrong

        "Evergreen":
            $ quiz_score += 1
            jump zintar_2ndwrong

        "Crystal":
            jump zintar_3rd

    label zintar_2ndwrong:
    play sound "zintar.mp3"
    if quiz_score == 3:
        z "Heh, better luck next time, kid..."
        jump end

    else:
        z "Are you serious? Are you sure you didn't sneak your way past the others?"

    z "The Feral Spirit lives in the __________ Forest."

    menu:

        "Stone":
            $ quiz_score += 1
            jump zintar_2ndwrong

        "Jade":
            $ quiz_score += 1
            jump zintar_2ndwrong

        "Evergreen":
            $ quiz_score += 1
            jump zintar_2ndwrong

        "Crystal":
            jump zintar_3rd

    label zintar_3rd:
    play sound "win.mp3"
    z "Oh ho ho! Now things are getting interesting!"

    z "But can you keep it up?"

    z "In his memories, the Skeleton Assassin remembers these words 'An assassin has no _______. An assassin has no _______.'"

    menu:

        "Heart, Emotions":
            jump zintar_4th

        "Loyalty, Fear":
            $ quiz_score += 1
            jump zintar_3rdwrong

        "Needs, Desires":
            $ quiz_score += 1
            jump zintar_3rdwrong

        "Will, Individuality":
            $ quiz_score += 1
            jump zintar_3rdwrong

    label zintar_3rdwrong:
    play sound "zintar.mp3"
    if quiz_score == 3:
        z "Heh, better luck next time, kid..."
        jump end

    else:
        z "Hahaha. I should destroy you where you stand. It would be kinder."

    z "In his memories, the Skeleton Assassin remembers these words 'An assassin has no _______. An assassin has no _______.'"

    menu:

        "Heart, Emotions":
            jump zintar_4th

        "Loyalty, Fear":
            $ quiz_score += 1
            jump zintar_3rdwrong

        "Needs, Desires":
            $ quiz_score += 1
            jump zintar_3rdwrong

        "Will, Individuality":
            $ quiz_score += 1
            jump zintar_3rdwrong

    label zintar_4th:
    play sound "win.mp3"
    z "Hmm... You know, I like you. You've got spunk."

    z "But that doesn't mean you'll go any farther!"

    z "Prepare yourself!"

    z "Before she was the Haunted Spider, her talent was as a ________."

    menu:

        "weaver":
            $ quiz_score += 1
            jump zintar_4thwrong

        "tracker":
            $ quiz_score += 1
            jump zintar_4thwrong

        "seer":
            jump zintar_5th

        "chef":
            $ quiz_score += 1
            jump zintar_4thwrong

    label zintar_4thwrong:
    play sound "zintar.mp3"
    if quiz_score == 3:
        z "Heh, better luck next time, kid..."
        jump end

    else:
        z "Oh ho! Better try a little harder before I zap you back to the beginning!"

    z "Before she was the Haunted Spider, her talent was as a ________."

    menu:

        "weaver":
            $ quiz_score += 1
            jump zintar_4thwrong

        "tracker":
            $ quiz_score += 1
            jump zintar_4thwrong

        "seer":
            jump zintar_5th

        "chef":
            $ quiz_score += 1
            jump zintar_4thwrong

    label zintar_5th:
    play sound "win.mp3"

    z "What?! I take it back! I don't like you at all!"

    z "Get out of here before I find out how you cheated!"

    z "Let's see if you're so sure of yourself once you meet Selenia, Rider of Dragons!"

    hide zintar
    with dissolve

    label selenia:

    scene moon
    show seleniasky
    with dissolve

    s "Well...this is quite a surprise..."

    s "You have journeyed quite far...but no farther."

    s "While you may have the skills to wield summoners from other Splinters, I will not be so easily handled."

    s "To best me, you will have to have a mind sharper than a dragon's claws."

    s "These answers will be much harder to find."

    s "First Question. What is the name of my people?"

    menu:

        "Winged Warriors":
            $ quiz_score += 1
            jump selenia_1stwrong

        "Gloridrax":
            jump selenia_2nd

        "Dragonflyers":
            $ quiz_score += 1
            jump selenia_1stwrong

        "Sun folk":
            $ quiz_score += 1
            jump selenia_1stwrong

    label selenia_1stwrong:
    play sound "selenia.mp3"
    if quiz_score == 3:
        s "May the Sun have mercy on you...because I surely won't."
        jump end

    else:
        s "Have faith in the light of the Sun and try again."

    s "What is the name of my people?"

    menu:

        "Winged Warriors":
            $ quiz_score += 1
            jump selenia_1stwrong

        "Gloridrax":
            jump selenia_2nd

        "Dragonflyers":
            $ quiz_score += 1
            jump selenia_1stwrong

        "Sun folk":
            $ quiz_score += 1
            jump selenia_1stwrong

    label selenia_2nd:
    play sound "win.mp3"
    s "Good."

    s "Second. What do we worship?"

    menu:

        "Solely the Sun":
            $ quiz_score += 1
            jump selenia_2ndwrong

        "Dragonfire":
            $ quiz_score += 1
            jump selenia_2ndwrong

        "Artifacts":
            $ quiz_score += 1
            jump selenia_2ndwrong

        "The Sun mainly, but some few worship the Moon":
            jump selenia_3rd

    label selenia_2ndwrong:
    play sound "selenia.mp3"
    if quiz_score == 3:
        s "May the Sun have mercy on you...because I surely won't."
        jump end

    else:
        s "Careful...my dragon grows hungry..."

    s "What do we worship?"

    menu:

        "Solely the Sun":
            $ quiz_score += 1
            jump selenia_2ndwrong

        "Dragonfire":
            $ quiz_score += 1
            jump selenia_2ndwrong

        "Artifacts":
            $ quiz_score += 1
            jump selenia_2ndwrong

        "The Sun mainly, but some few worship the Moon":
            jump selenia_3rd

    label selenia_3rd:
    play sound "win.mp3"

    s "Hmph, how would an outsider like you know of *that*? Impressive..."

    s "But be careful of whom you speak of that to. Next."

    s "Through a process of first liquifying the light, and then distilling it with Dragonfire..."

    s "we Gloridrax are able to capture and contain the essence of magic."

    s "Where do we store this magic?"

    menu:

        "Ruby Pendants":
            $ quiz_score += 1
            jump selenia_3rdwrong

        "Crystal Orbs":
            $ quiz_score += 1
            jump selenia_3rdwrong

        "Heliostones":
            jump selenia_4th

        "Sun discs":
            $ quiz_score += 1
            jump selenia_3rdwrong

    label selenia_3rdwrong:
    play sound "selenia.mp3"
    if quiz_score == 3:
        s "May the Sun have mercy on you...because I surely won't."
        jump end

    else:
        s "I grow weary of this..."

    s "Where do we store distilled magic?"

    menu:

        "Ruby Pendants":
            $ quiz_score += 1
            jump selenia_3rdwrong

        "Crystal Orbs":
            $ quiz_score += 1
            jump selenia_3rdwrong

        "Heliostones":
            jump selenia_4th

        "Sun discs":
            $ quiz_score += 1
            jump selenia_3rdwrong

    label selenia_4th:
    play sound "win.mp3"

    s "Well done. It seems I have underestimated you."

    s "Now...for my final question."

    s "Besides being a summoner, what is my role in Gloridrax society?"

    menu:

        "Sun Priestess":
            $ quiz_score += 1
            jump selenia_4thwrong

        "Warrior Princess":
            $ quiz_score += 1
            jump selenia_4thwrong

        "Flight Commander":
            jump selenia_5th

        "Dragon Trainer":
            $ quiz_score += 1
            jump selenia_4thwrong

    label selenia_4thwrong:
    play sound "selenia.mp3"
    if quiz_score == 3:
        s "May the Sun have mercy on you...because I surely won't."
        jump end

    else:
        s "It would be a shame to have to destroy you now..."

    s "What is my role in Gloridrax society?"

    menu:

        "Sun Priestess":
            $ quiz_score += 1
            jump selenia_4thwrong

        "Warrior Princess":
            $ quiz_score += 1
            jump selenia_4thwrong

        "Flight Commander":
            jump selenia_5th

        "Dragon Trainer":
            $ quiz_score += 1
            jump selenia_4thwrong

    label selenia_5th:
    play sound "finish.mp3"

    s "Well...it seems that your knowledge of the Splinterlands is extensive indeed."

    s "I shall use my power to return you to your home."

    s "We shall meet again when you are ready to wield the cards in battle."

    s "But in acknowledgement of your wisdom, I will give you a warning..."

    s "Wielding the cards is only the beginning."

    s "You've opened the door to something you cannot truly comprehend...yet."

    s "Begone!"

    label finish:
    scene bedroom
    with fade

    "..."

    "I'm home and it's morning..."

    "Was it really a dream?"

    "Selenia..."

    show selenia
    with dissolve
    pause

    "We will meet again..."
    pause

    # This ends the game. This is also where we defined the sword sound effect that you get when the game ends.
    label end:
    play sound "sword.mp3"
    return
