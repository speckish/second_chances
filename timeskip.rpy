label cafeteria:
    yuki None
    "The next few weeks passed by quite uneventfully."
    "Yuki easily breezed through all his classes, with nothing interesting of note happening."
    play sound "audio/meow_1.mp3"
    cat "..."
    y "Don't look at me like that!"
    play sound "audio/meow_3.mp3"
    cat "Is this why I gave you a second life?"
    y "I don't know! I didn't even ask for this!"
    play sound "audio/meow_2.mp3"
    cat "But it's what you wanted."
    y "I-I..."
    "Yuki couldn't deny her words. It was true, this was what he wanted."
    play sound "audio/meow_4.mp3"
    cat "Don't waste it. You won't get another."
    y "..."
    scene bg lab with fade
    yuki None
    "Yuki spend the past few weeks doing his very best to avoid both Zethe and Quinn. He felt a gutteral response whenever he was around them."
    yuki sad show
    "Sighing, he walked to the bookshelf in the corner of his room and pulled out his book of Vednore perks."
    "He flipped through the pages."
    yN "The one I'm looking for is—"
    yuki shocked  blush startle
    y "Ow!"
    yuki startle
    "Yuki flinched and dropped the book on the ground."
    yuki blush
    "He clenched his hand in pain."
    yuki angry
    y "Crap, crap, crap!"
    play sound "audio/yuki_magic_chime.mp3"
    "Instinctively, he brought up his other hand and began to cast a basic cooling spell. Instead, icicles formed outside his window."
    yuki angry blush # TODO: grrr
    y "Dammit!"
    yuki angry
    "He cursed and sat down on his bed, waiting for the pain to subside."
    y "Phew..."
    yuki sad
    "He took a deep breath."
    yuki sad blush
    "Ever since he fell on his first day of classes, Yuki's wrist was hurting. Probably since he fell right on it."
    yuki sad
    y "Ugh..."
    yuki
    "After a couple moments rest, he walked over to where he'd dropped the book and picked it up."
    y "As I was looking..."
    "Yuki flipped over to the page that read, 'Food Delivery Tickets.' He knew he was running low but..."
    yuki angry blush # TODO: grr
    y "Goshdarnit."
    yuki angry
    "He was out of tickets. He'd used them all the past weeks."
    yuki sad
    "That meant he actually had to go to the cafeteria. Like in person. And interact with other humans."
    play sound "audio/meow_2.mp3"
    cat "Well, well, well."
    yuki angry
    y "You sure are enjoying this."
    play sound "audio/meow_4.mp3"
    cat "Of course I am. Have fun!"
    yuki sad
    "Yuki grumbled and made his way to the cafeteria."
    scene black with fade
    pause 0.0
    yuki None
    scene cafeteria with fade
    "Yuki got his food on a tray. He precariously held it so as not to aggrevate his already painful wrist."
    yuki sad
    "Looking around, all the seats were taken. Except ones next to Zethe and Quinn."
    yuki sad blush
    yN "That's what I get for showing up so late..."
    yuki sad
    "Torn, he finally decided to sit next to..."

    menu:
        "Zethe":
            yuki
            "Zethe was sitting next to a group of other nobility."
            yuki blush
            "Yuki felt a little intimidated, but wasn't about to be swayed."
            yuki sad
            "However, it appeared that the nobles were mostly conversing amongst themselves, with Zethe quietly picking at his food."
            yuki
            show zethe at offscreenright, seated
            pause 0.0
            show zethe at center, seated with move
            "Yuki sat down next to Zethe. Internally, he felt shaken. But he didn't show it."
            show zethe happy
            yuki blush
            z "Oh? Look who's here."
            yuki
            "The other noble students gave a cursory glance at Yuki before returning to their conversations."
            y "I have a name."
            show zethe neutral
            z "Yuki, I know."
            yuki angry
            y "Wow, I'm so honored."
            yuki
            show zethe happy
            z "You should be."
            show zethe neutral
            "Yuki ignored Zethe and took a spoonful of soup. He hoped that it would be easy enough to eat."
            yuki blush
            "Unfortunately, his hand shook with discomfort. Still, he raised it into his mouth and drank it."
            show zethe sad
            yuki
            z "..."
            yuki sad
            y "...What are you looking at?"
            "Yuki braced himself for a snarky retort."
            show zethe neutral
            z "Give me your hand."
            yuki shocked
            y "What?"
            yuki shocked blush
            "Without another word, Zethe grabbed Yuki's hand."
            y "W-What are you doing?!"
            yuki shocked
            show zethe sad
            play sound "audio/zethe_magic_chime.mp3"
            "Zethe began chanting silently. Yuki felt a cooling sensation on his hand as the pain began to fade away."
            show zethe neutral
            yuki blush
            y "Wow."
            yuki
            "Yuki flexed his fingers and rotated his wrist. It felt completely normal."
            yuki happy
            y "Not bad."
            yuki
            "Zethe clicked his tongue."
            show zethe angry
            z "I help you out, and I get a {i}not bad?{/i}"
            yuki happy
            show zethe
            y "That's right. I feel a little tingle, so it's not considered {i}good{/i}."
            show zethe angry
            yuki
            z "Hmph. You should be grateful: the only reason I helped you is because it's no fun fighting against an injured rival."
            show zethe
            "Yuki chuckled and went back to drinking his soup. He could've healed the injury himself much earlier, but he was conserving his magic in case of future incidents. But Zethe clearly didn't have any such reservations."
            yuki happy
            y "I doubt you'd stand a chance against me at full strength."
            yuki
            show zethe happy
            "Zethe smirked."
            z "Oh? You should worry about yourself first. Fainting on the first day of class is never a good look."
            yuki happy
            "We bickered over lunch. Surprisingly, Zethe wasn't as bad as I'd originally thought."


        "Quinn":
            yuki sad
            "Quinn was sitting at a table by herself. However, there was one empty chair next to her."
            yuki
            "Instinctively, Yuki straightened out his collar and brushed his hair."
            yuki blush
            yN "Crap. What am I doing?"
            yuki
            "Yuki shook his head to clear his thoughts. Then, he walked up to her table and sat down."
            show quinn shocked sweat at offscreenleft, seated
            pause 0.0
            show quinn shocked sweat at center, seated with move
            q "O-Oh! Hello, Yuki."
            show quinn shocked -sweat
            y "Hey Quinn. This is the only spot I found. Hope you don't mind."
            "Yuki did his best to keep the ice out of his voice. He felt strange: fluctuating between gentle desire to stay by her side, and harsh memories of his hurt in the past."
            show quinn neutral
            q "Of course not!"
            y "That's good."
            "Yuki lifted a spoonful of soup to his mouth. He'd hoped it would be easy enough to eat."
            show quinn sad
            "However, his hand began to shake with discomfort."
            yuki sad blush
            y "Hngh."
            yuki sad
            "With difficulty, Yuki brought the spoon to his mouth and swallowed."
            yuki
            show quinn sad blush
            q "..."
            show quinn sad -blush
            q "That looks difficult."
            yuki happy
            y "Haha, yeah. Don't worry about it, I'm fine."
            yuki shocked blush
            show quinn shocked blush
            "Yuki took another spoonful, but a sharp pang of pain made him drop it into the bowl."
            yuki shocked blush startle
            y "Ow!"
            yuki shocked
            show quinn sad -blush
            q "Yuki..."
            yuki
            y "I'm fine, I'm fine."
            "He didn't want Quinn to worry about him. He closed his eyes for a second and opened them."
            scene black with fade
            pause 0.0
            scene bg cafeteria
            show quinn neutral at center
            with fade
            yuki sad
            y "...?"
            "The bowl was sitting by Quinn's side now. She held the spoon in her hands."
            q "Say 'Ahh.'"
            yuki shocked
            y "H-Huh?!"
            show quinn neutral blush
            "A light blush dusted Quinn's cheeks, but she persisted."
            show quinn happy blush
            yuki shocked blush
            q "If you can't eat, I'll help you out."
            yuki shocked
            y "I-I appreciate it, but..."
            yuki shocked blush
            show quinn sad blush
            q "It's okay, you don't need to act tough."
            yuki sad blush
            "Meekly, I gave in."
            show quinn happy blush
            yuki blush
            y "Ahh."
            show quinn neutral blush
            "She smiled and helped Yuki to a spoonful of soup."
            y "Thanks."
            show quinn happy -blush
            q "It's okay. Injured people shouldn't have to do work."
            show quinn neutral -blush
            "Yuki doubted eating was considered work, but he didn't complain."
            show quinn happy -blush
            "They ate the rest of their meal in silence. Quinn was just as he'd remembered: beautiful both inside and out."
            show quinn neutral -blush
    yuki sad
    "But memories of his past life clutched his chest. He couldn't let go of them so easy."
    return

label library:
    scene black with fade
    yuki None
    "A few more weeks passed."
    "The classes began to get a lot tougher. Considering he'd been out of college for a while, Yuki struggled to remember everything."
    "So, he found himself spending more and more time at the library."
    scene bg library day with fade
    "But he was there today for a very different reason."
    yuki
    y "..."
    yuki sad
    "Yuki furrowed his brow in concentration as he read, 'Lola: My First Guardian Spirit.' to himself."
    play sound "audio/meow_5.mp3"
    cat "Are you kidding me?"
    yuki angry
    yN "Shh! I'm doing research."
    yuki sad
    "Yuki read the contents of the book to himself. It was a book about a Guardian Spirit who helps out a crying child in his quest for greatness."
    "Aurelia looked suspiciously at the book in Yuki's hands. It was comprised mostly of colorful images and baby speech."
    play sound "audio/meow_1.mp3"
    yuki
    cat "This is why I didn't want to bother with mortals."
    yuki blush
    z "It appears that our class prodigy has taken to reading children's books in his spare time."
    "Yuki ignored the voice and continued reading."
    z "I said—"
    yuki
    y "Hm... I think I hear some wind rustling in the distance."
    show zethe angry at offscreenright
    pause 0.0
    show zethe angry at center with move
    "Yuki peeked from the corner of his book to see Zethe visibly annoyed."
    show zethe angry blush
    z "Tch!"
    show zethe angry at offscreenleft with move
    "Zethe stormed off. Yuki just shook his head. He was in the middle of something important."
    yuki sad
    yN "Oh! So this Guardian Spirit took him on an adventure to a land of candy, where everything is made of fluffy sweets!"
    cat "..."
    yuki
    scene bg library dusk with fade
    "After he finished the book, Yuki put it down and picked up another."
    "All of them had widely differing plots, but Yuki was noting down the similarities and differences between them in a notebook."
    scene bg library night with fade
    "Yuki was almost finished when he looked outside."
    yuki shocked
    yN "It's extremely late."
    yuki
    "Just as he was getting ready to leave, another familiar face appeared next to him."
    yuki shocked blush
    y "Quinn?"
    show quinn at offscreenleft
    pause 0.0
    show quinn at center with move
    yuki
    q "Yuki! What a surprise. Oh, is that the 'Guardian Spirit of Love' series I see?"
    yuki blush
    show quinn happy
    "Yuki blushed as he realized he had a stack of children's books next to him. But Quinn looked delighted."
    show quinn happy # TODO: excited
    q "That was my favorite series growing up!"
    yuki
    show quinn neutral
    y "Really? I hadn't got the chance to read that series yet, though I've been looking at others. Mind telling me more about it?"
    show quinn happy # TODO: excited
    q "Sure! So there's this really mischevious spirit named Lola..."
    show quinn happy # TODO: excited
    yuki sad
    "After hearing Quinn's fantastical tale of the Guardian Spirits in the series, Yuki was convinced it had nothing to do with reality in any way."
    show quinn neutral
    yuki
    q "...And then, Lola does a backflip into the chocolate fountain!"
    yuki sad
    y "I think I get it."
    show quinn neutral sweat
    q "O-Oh. Sorry, I rambled for a bit."
    yuki
    y "It's fine. It's cute when you do that."
    show quinn neutral sweat blush
    "The words slipped out of his mouth unwittingly, and Yuki regretted them instantly."
    yuki shocked blush
    y "I-I didn't mean it like—"
    show quinn neutral -sweat blush
    q "It's... it's fine."
    "Quinn was blushing furiously."
    show quinn neutral -sweat blush at offscreenright with move
    q "I-I have to go."
    yuki sad
    "For a moment, Yuki thought about stopping her. That's what he would've done in the past. Stop her, convince her to give him another chance. But now..."
    yuki sad blush
    yN "I should let her think."
    yuki sad
    "He began to walk out when he felt a hand on his shoulder. Yuki flinched."
    yuki shocked
    y "H-Huh?!"
    show zethe at offscreenright
    pause 0.0
    show zethe at center with move
    "Yuki turned around to see Zethe glaring at him. Yuki breathed a sigh of relief."
    yuki
    y "Oh. It's you."
    z "Do not give me that."
    yuki sad
    y "What?"
    show zethe angry
    z "{i}Oh, it's you{/i}"
    yuki
    show zethe neutral
    y "Listen Zethe, I really don't have time for this—"
    show zethe angry
    z "Sure, but you were just talking to Quinn for a while now."
    show zethe neutral
    yuki sad
    "Yuki sighed. He knew Zethe was crushing on Quinn, so this would be troublesome."
    yuki
    show zethe angry
    z "Why did you talk to her, but not to me?"
    show zethe neutral
    yuki sad
    yN "Huh?"
    show zethe sad
    z "When I attempted to converse with you, you brushed me off. You refused to even look at me. But you had a full conversation with Quinn."
    yuki shocked
    "It was strange that Zethe was watching their whole conversation, but also the way he was talking... It was almost as if Zethe was jealous of Quinn, not Yuki."
    show zethe
    "Zethe shook his head."
    show zethe angry
    yuki sad
    z "I suppose you will not talk to me now, either. Very well."
    show zethe at offscreenright with move
    play sound "audio/steps.mp3"
    "He turned on his heel and walked out the door."
    yuki shocked
    "Yuki's mouth hung open in shock. What a surprising day."
    yuki sad
    yN "I should go home and sleep on it."
    yuki None
    play sound "audio/meow_1.mp3"
    "Aurelia sat in the corner, her tail wagging in interest."
    scene black with fade
    return

label mother_call:
    scene black with fade
    yuki None
    scene bg lab with fade
    "A few more days passed. Yuki sat in his room working on a particularly difficult assignment. Aurelia was in the corner, curled up and snoring loudly."
    yuki sad
    "But Yuki couldn't concentrate. His hands shook as he tried to read the words on his notebook."
    yuki sad blush
    "Yuki knew from the calendar that it was the day he dreaded."
    yuki sad
    "After a few more hours of thoroughly unproductive work, Yuki sat the pen down on the desk."
    yuki
    y "Hah..."
    yuki shocked startle
    # TODO: chime?
    "Yuki's messenger note, the one on the wall, began to flash brightly. He flinched, but collected himself enough to answer."
    yuki
    "A holographic projection of Yuki's mother shone in front of him."
    yuki sad
    y "Mother."
    mom "Hello, my boy. How are you doing?"
    "Yuki stared at her. Her arms were weak and frail. She looked feeble."
    yuki
    y "I'm... I'm alright. What about you?"
    mom "Dear, I'm afraid to say... I don't have much time left."
    yuki sad blush
    "Yuki had heard this declaration before. But it still felt like he got the wind knocked out of him. Yuki clutched his stomach."
    yuki sad
    y "Mother..."
    mom "Don't look so upset, dear."
    "He knew his mother would protest to his next words, but Yuki said them anyway."
    yuki
    y "I will come to see you at once."
    "His mother's voice turned angry."
    mom "No! Do you not realize how far I am? It would take you at least three months by sea."
    y "I won't use sea. I'll teleport. I must see you."
    mom "Yuki... It's not worth it. There are no teleportation runes anywhere near here, so you'd still have to—"
    yuki angry blush
    y "I KNOW!"
    "Yuki felt guilty for raising his voice. Tears pricked at his eyes."
    yuki sad
    y "I... I know, mother. There's no point. There's nothing that can be done."
    mom "My boy..."
    yuki sad blush
    "Yuki felt his chest heave. His mother rarely called him by name. It was always 'My boy.' But now, he'd never be able to hear that sweet voice of hers again."
    yuki sad
    "Yuki knew that it was just a projection, but he reached his hands out to it."
    yuki
    y "Mother, I love you."
    mom "I love you too, my boy."
    yuki sad
    y "I can't let you go like this."
    mom "Death is not something to be feared. It should be celebrated."
    yuki sad blush
    y "But..."
    yuki sad
    mom "Yuki. I'm so proud of you. You managed to get a scholarship to such a prestigious school."
    y "I promised. I promised I would bring you out of that awful, violence-ridden place."
    "Mother's look turned stern."
    mom "It is not perfect, but {i}that place{/i} is still your home."
    "Yuki knew there was no point in arguing with her. She was as stubborn, if not more than Yuki himself. He decided to drop it. He didn't want to spend their last real conversation arguing."
    yuki
    yN "Last time, we parted too bitterly..."
    yuki happy
    "After some more conversation about various happenings in town, Mother's eyes began to droop. The connection became fuzzy."
    yuki
    mom "Oh, our time's up. Remember this, my boy. Some things happen for a reason. And I love you. Now and always."
    yuki sad
    y "I love you too, Mother."
    yuki sad blush
    "And with that, the line cut. Yuki felt his eyes water."
    yuki sad
    # TODO: chair scrape?
    "Yuki walked over to the bookshelf next to him and pulled out Mother's amulet. He clenched it in his fist."
    yuki sad blush
    yN "Perhaps I can still keep that promise."
    yuki sad
    "Deep down, Yuki felt he should..."

    menu:
        "Accept the death as inevitable":
            "Maybe it was like what Mother said."
            "Death was a vital part of the cycle of life."
            yuki sad blush
            "But even if it was inevitable, it could be delayed. That was the premise of many medicines, after all."
            "Even though he felt it wrong, nothing could stop the fire inside..."

        "Change fate":
            yuki
            yN "Isn't this why I got a second chance? To defy fate?"
            "And if fate thought she could rip his dear Mother away, she had another thing coming..."
            yuki angry
            yN "'Death shouldn't be feared.' As if I'm scared of it!"
            yuki angry blush
            yN "Do your worst, fate. I won't be defeated."
    scene black with fade
    yuki None
    return

label assignment:
    scene bg classroom with fade
    "Yuki sat in the classroom, nervous. It was the final class of the day."
    yuki
    "He tapped his finger on the desk. The past few weeks, he'd been researching various healing techniques."
    yuki sad
    "None of them said anything about terminal illnesses. He knew that from his previous life at Vednore, so he was researching different books this time."
    "Still, they turned up nothing."
    yuki
    prof "For the final grade of the year, you will have to partner with another classmate for a special assignment."
    yuki sad
    "The year had passed by in the blink of an eye. He clutched Mother's amulet. As long as it glowed, it was proof she was alive."
    "But the light was dimming. There wasn't much time."
    "Normally Yuki found Professor Chen's lectures interesting. Now he just wanted it to be done with."
    yuki
    prof "You have two options. You can partner up with another magician to create a new spell."
    play sound "audio/class_murmur.mp3"
    "The class went crazy with whispers. All spells that students performed were taken from old books. Sometimes, they were tweaked to fit modern needs."
    "But no one {i}ever{/i} created their own."
    # TODO: cough
    "Professor Chen cleared his throat."
    prof "But I realize that is a monumental feat, not one that many desire. As a result, there is a second option."
    prof "You may partner with a student from the {i}Juris{/i} program to make a magical product."
    yuki sad
    "A magical product required not just the magic component, but a detailed legal contract to ensure no issues arose."
    "In his previous life, Yuki partnered with Quinn to make the eternal garden in the center of the school."
    "It wasn't really a product that could be sold on a shelf, but they got a perfect grade anyway."
    yuki sad blush
    "This time, Yuki felt more conflicted. Quinn's attitude was very different."
    "Since he didn't push her, she was much more spontaneous and excited, which made him feel that they may have a real chance together..."
    yuki sad blush sweat
    "On the other hand, Zethe's curious behavior drew Yuki's eye as well. Before, he just considered Zethe a worthy rival. But now, he felt something else..."

    "What should Yuki do?"

    menu:
        "Make a magical product with Quinn":
            yuki blush
            "It was a different timeline, but Yuki still deeply cared about Quinn. Maybe even deeper now that he knew her true nature."
            # claaroom dusk
            yuki
            "After class, Yuki waited in the hallway for Quinn to come out."
            show quinn shocked at offscreenleft
            pause 0.0
            show quinn shocked at center with move
            # show quinn shocked with dissolve
            q "Yuki?"
            y "Hi Quinn. I just wanted to ask you something."
            show quinn neutral blush
            yuki blush
            "Her cheeks flushed red."
            yuki
            q "L-Like?"
            y "O-Oh, don't worry. It's nothing personal."
            show quinn sad -blush
            yuki sad
            "For a second, Quinn looked disappointed. But she quickly recovered."
            show quinn neutral
            q "Oh. Well. Go ahead!"
            yuki
            "Her reaction was strange, but Yuki didn't think too much of it."
            y "I wanted to know if you were willing to partner with me for the final assignment?"
            show quinn shocked
            "Quinn looked surprised."
            show quinn shocked blush
            q "You want to partner with {i}me?{/i}"
            y "Is... Is there a problem?"
            show quinn sad -blush sweat
            q "No, uh, I thought you had an issue with me."
            yuki sweat
            "Yuki blinked."
            yuki
            y "What made you think that?"
            show quinn neutral sweat
            q "I-It's nothing. It was just a misunderstanding, that's all."
            yuki sad
            "Yuki chewed the inside of his lip. In his previous life, they did the flashy garden display."
            "But Yuki basically did the entire thing by himself, with Quinn barely giving any input."
            show quinn neutral -sweat
            yuki sad sweat
            "Yuki felt guilty."
            yuki
            y "So... what do you want to do?"
            show quinn happy
            "Quinn's eyes lit up."
            q "I want to make a small stove for ill and disabled people. Something that will let them cook simple meals without difficulty."
            yuki shocked
            "Yuki was surprised."
            yuki sad
            y "I didn't know you were interested in that."
            show quinn shocked
            "Quinn pouted."
            show quinn sad
            q "You never asked."
            yuki sad blush
            "Yuki thought for a moment. She was right: he knew she loved plants and flowers, but that was it."
            yuki
            y "Sounds good. Let's discuss the details later?"
            show quinn neutral
            q "Sure! We can meet at my dorm."
            scene black with fade
            # play sound "audio/steps.mp3"
            yuki None
            "After exchanging Holo Note information and discussing timings, Yuki made his way back to his dorms."
            scene lab #dorm?
            show zethe at center
            with fade
            z "..."
            yuki
            y "Zethe."
            z "Yuki."
            "Yuki crossed his arms and waited for Zethe to speak."
            show zethe sad
            z "About the final grade of the year."
            y "Yes?"
            show zethe neutral sweat
            z "Do you have a partner yet?"
            yuki sad
            "Yuki studied Zethe's features. He looked strangely nervous."
            yuki
            y "Yes, I'm partnered with Quinn."
            show zethe shocked blush sweat
            "Zethe's face instantly fell."
            "Yuki remembered he had a massive crush on Quinn."
            yuki happy
            yN "Must suck."
            "He patted Zethe's shoulder and walked past him wordlessly."
            scene black with fade
            call quinn from _call_quinn

        "Create a new spell with Zethe":
            yuki happy
            "Yuki knew he was up for a new challenge. And he knew just the person to take it on with."
            yuki
            "After class, Yuki stood outside the door. He watched various students shuffle out and discuss different ideas."
            show zethe at offscreenright
            pause 0.0
            show zethe at center with move
            # show zethe with dissolve
            "Finally, he spotted Zethe."
            show zethe shocked
            y "Zethe."
            show zethe
            z "Yuki."
            y "I have something to ask you."
            show zethe shocked sweat
            "Zethe's eyes grew wide as saucers."
            z "Huh?"
            yuki shocked
            "Yuki was surprised by Zethe's reaction."
            yuki
            y "It's... not about a duel."
            z "Okay..."
            "Zethe's expression still didn't change."
            show zethe shocked sweat blush
            y "...It's nothing personal, either."
            show zethe neutral -blush sweat
            "Zethe's face immediately fell, but he straighted himself."
            show zethe neutral -sweat
            z "Is that so? Can't you explain it in a proper manner?"
            "Yuki shook his head."
            y "Do you want to create a new spell together?"
            show zethe shocked
            "Zethe's jaw dropped in visible shock."
            z "Do you even know what you propose?"
            yuki happy
            show zethe angry
            y "Yes. Unless... you don't think you can do it?"
            show zethe angry blush
            "Predictably, Zethe took the bait."
            show zethe angry -blush
            z "Of {i}course{/i} I can. You're the one who'd struggle to keep up."
            yuki
            "Yuki brought his hand to his mouth in a fake yawn."
            show zethe neutral
            "Zethe scoffed."
            yuki happy
            "Yuki felt a smile stretch across his face. Something about Zethe brought out his inner child. Competitive yet immature."
            show zethe angry
            z "What are you laughing at?"
            yuki
            y "At your inevitable defeat."
            show zethe neutral
            "Zethe took a moment to think."
            z "No one can lose in a group project."
            yuki happy
            y "I suppose I would, when you invetably fall behind."
            show zethe neutral blush at startle
            z "You...!"
            # Anim?
            "After some more childish bickering, Yuki realized they were getting no where."
            yuki
            show zethe neutral -blush
            y "What should the spell do?"
            z "Good question."
            show zethe sad
            yuki sad
            y "..."
            z "..."
            y "..."
            yuki shocked
            show zethe neutral
            z "How about... a massive phoneix."
            yuki shocked sweat
            y "That does... what exactly?"
            z "It will be a large bird. Made of fire. That flies."
            y "Zethe, I know what a phoneix {i}is.{/i}"
            show zethe happy
            z "Great. So there's no problems there."
            yuki sad
            show zethe neutral
            "Yuki rubbed a hand on his forehead. What had he signed up for...?"
            yuki
            y "Alright. Give me your information so we can figure out something actually do-able."
            show zethe neutral blush sweat
            "Zethe protested, but eventually exchanged Holo Note information and discussed timings."
            show zethe neutral -blush -sweat
            y "We can meet at my dorm room."
            z "That works."
            show quinn shocked at offscreenleft
            pause 0.0
            show quinn shocked at center
            show zethe at offscreenright
            with move
            "After splitting ways with Zethe, Yuki sees Quinn in the hallway."
            q "Yuki?"
            y "Oh hello, Quinn."
            show quinn neutrual
            q "Hi. I was um... just wondering if you hand a partner for the final project?"
            yuki sweat
            "Yuki blinked."
            yuki
            y "Yeah, I do. I'm partnering up with Zethe."
            show quinn sad blush
            q "Oh! Oh. Okay then. Just... I was just checking."
            yuki sad
            show quinn sad blush at offscreenright with move
            # play sound "audio/quinn_run_away.mp3"
            "Yuki could've sworn he saw sadness reflected in her eyes. Before he could say anything, she quickly scurried away."
            yuki sad blush
            yN "Did she... did she want to partner with me for it?"
            yuki sad
            "Yuki shook his head. That wasn't possible. Quinn wasn't ever so forward."
            call zethe from _call_zethe

    return

label research:
    scene bg library night_closed with fade
    # TODO night sprites?
    yuki None
    "Yuki sneaked into the library at night."
    "Although the library had several magic protection locks, Yuki got through because..."

    if passed:
        "After passing the first exam, Professor Chen trusted Yuki a lot more."
        "Naturally, Yuki eventually found himself entrusted with the keys."

    else:
        "He failed the first exam, but worked on his raw magical skill a lot more."
        "He easily passed through the complex web of security with finesse."
    yuki
    yN "So naive..."
    yuki sad
    play sound "audio/yuki_magic_chime.mp3"
    "He went straight to the back of the library and chanted a spell."
    scene black with fade
    play sound "audio/steps.mp3"
    scene lab with fade
    yuki None
    "Yuki felt at ease in his lab. He went around to the spell books and flipped through them."
    "The spells here were far more difficult, complex, and dangerous than any he'd done before."
    yuki
    yN "As if that would stop me."
    yuki sad
    "The final one was in a language he couldn't understand. The glyphs followed no rhyme or reason."
    yuki shocked sweat
    "After intense study, he realized that it was because they changed everytime he opened it."
    yuki sweat
    yN "Now...!"
    yuki sad
    play sound "audio/yuki_magic_chime.mp3"
    "He closed his eyes and funneled silent magic through it until it shattered."
    # Find a diff one from the class.
    play sound "audio/mini_boom.mp3"
    yuki shocked startle
    y "What the?!"
    yuki shocked sweat
    "Yuki opened his eyes."
    yuki sad
    "The only remains of the book was writing etched on the ground."
    "It was in..."
    yuki shocked blush sweat
    yN "Blood?!"
    yuki shocked
    "It read, 'In order to save a life, something of equal value must be sacrified. Be prepared.'"
    yuki angry # smash efx
    "Yuki slammed his fist on the table."
    yuki angry blush
    yN "This isn't helpful!"
    yuki sad
    "He stared down at the fading amulet."
    yuki sad blush
    yN "I failed last time. It won't happen again."
    scene black with fade
    yuki None

    "Although this experiment was a failure, it wasn't the only thing occupying Yuki's mind."
    return #?

label finalMother:
    "A significant amount of time passed. It was nearing the end of the year, yet "
    "Yuki sat down at his desk. Once again, his eyes flitted to the calendar."
    "He tapped his foot."
    y "How much longer..."
    "Finally, the messenger note on his wall began to chime."
    y "..."
    "Blankly, Yuki accepted it."
    y "...Mother."
    mom "Yuki."
    "Yuki stared at her blankly. He spent the last few days tired and exhausted. He couldn't muster up the energy to cry."
    mom "It's going to happen soon. I'm going to pass on."
    y "I see."
    mom "I do not like the look in your eye."
    y "...What?"
    mom "Do not do anything foolish, boy."
    y "I'm not."
    mom "I believe in you. You will not do anything reckless."
    #possible dialogue choice
    y "...Very well."
    "Yuki felt miserable lying to his mother, but he didn't want her to worry."
    "They talked for an hour about mundane things: what was happening in the village and all the local gossip."
    mom "{i}cough{/i}"
    y "Mother!"
    "Yuki instictively reached out, before realizing he couldn't."
    mom "My boy. I love you."
    "Yuki felt hot tears pool up in his eyes."
    y "I-I love you too. Always and forever."
    "The line cut."
    "Yuki got up from his chair, and hurried. There wasn't much time left."

    #lab
    "Yuki stood in his lab. The preparations took longer than he'd originally expected, and his Mother was about to pass in a few hours."
    "He took a deep breath."
    "Yuki clutched the amulet tightly in his palm. Yuki raised his hands and opened his mouth to chant."
    "Suddenly, he heard a voice call out to him."

    #call respective LI


