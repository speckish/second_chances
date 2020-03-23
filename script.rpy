# Declare characters used by this game.
define y = Character("Yuki")
define z = Character("Zethe")
define q = Character("Quinn")
define mom = Character("Mother")
define prof = "Professor"

# This refers to his narration.
define yN = Character("Yuki", what_italic=True, what_suffix=")", what_prefix="(")
define cat = Character("Cat", what_italic=True)

define he = "he"
define hed = "he'd"
define hewas = "he was"
define his = "his"
define He = "He"
define him = "him"
define himself = "himself"
define His = "His"

default passed = True

style window:
    left_padding 150

label start:
    "<This line is here for testing.>"
    call hook
    scene bg yukis_cabin_inside morning with fade
    yuki
    "Yuki stared out the window."
    yuki sad
    "Ever since [hed] left civilization ten years ago, it always felt like [hewas] floating through life."
    yuki
    y "Hmm..."
    yuki sad
    "[He] looked around his tiny cabin. Although it was small, it was all [he] needed. There was a time when [hed] held greater ambitions but..."
    yuki sad blush
    y "...Stop. Stop thinking about it."
    yuki
    "Yuki walked to the corner of the room where his makeshift kitchen was. [He] took a rusty, brown kettle from the cupboard and set it on the stove."
    "Reaching down, [he] removed the metal lid from [his] wooden water bucket. Then, he took a cup and poured some water into the kettle."
    "[He] lifted his hands over the kettle."
    play sound "audio/yuki_magic_chime.mp3"
    yuki angry
    y "{i}Calefaciens Aquam.{/i}"
    yuki happy
    "The water started to boil. Yuki's mouth twitched in a slight smile. Using magic was one of the few things that made [him] happy."
    yuki
    play sound "audio/meow_1.mp3"
    y "What's that?"
    yuki sweat
    "Yuki could've sworn [he] heard a cat's meow."
    play sound "audio/meow_2.mp3"
    yuki shocked sweat
    y "That's definitely not my imagination."
    yuki
    "Yuki quickly walked across [his] cabin and opened the door."
    play sound "audio/meow_3.mp3"
    yuki shocked
    y "Why is a cat here?"
    yuki shocked sweat
    "[He] felt a strange shiver down his spine, as if someone was watching [him]."
    yuki sad blush
    y "I can't just leave this poor thing here."
    yuki sad
    "Yuki looked down at the shivering kitten in [his] arms."
    yN "Maybe there's still some good I can do."
    yuki
    play sound "audio/meow_1.mp3"
    "[He] gently cradled the kitten and stood up. After returning to the cabin, [he] laid the cat down on a desk."
    y "Hm..."
    yuki sad
    "It'd been a long time since Yuki had to use any sort of healing magic, but that wasn't going to stop [him]."
    yuki
    "[He] took a deep breath and tried to remember the important spells."
    yuki angry
    "({i}Leve vulnus sanaret{/i}? No, that won't be enough.)"
    yuki
    "Yuki took a deep breath and tried to compose [himself]. Scenes from the past flashed in [his] mind."
    yuki angry blush
    y "No. You know better than this, Yuki."
    yuki
    "Yuki closed [his] eyes and took several deep breaths. [He] opened [his] eyes and looked down at the cat, this time with more clarity."
    yuki angry
    play sound "audio/yuki_magic_chime.mp3"
    y "{i}Sana lacerationes.{/i}"
    yuki
    "Yuki channeled a significant amount of magic through [his] palms, but nothing happened."
    yuki shocked
    y "Huh...?"
    yuki shocked sweat
    "The cat writhed in pain, looking no better than earlier."
    yuki shocked sweat blush
    y "What is going on?!"
    yuki shocked blush
    yN "Maybe it's still not strong enough?"
    yuki blush
    "[He] took a deep breath and tried again."
    yuki angry
    play sound "audio/yuki_magic_chime.mp3"
    y "{i}Restituere salutem.{/i}"
    yuki sad
    "It was the strongest healing spell [he] knew. Yet it still did nothing."
    yuki sad blush
    "The cat writhed in pain. But [he] couldn't stop now."
    yuki angry
    y "Hnngh."
    yuki sad blush
    "After a deep breath, [he] pushed more magic through his palms. [He] felt a burning sensation run through [his] veins, but grit [his] teeth and continued."
    yuki angry blush sweat
    y "Hf... Hf..."
    yuki sad blush sweat
    "Despite the excruciating pain, Yuki pushed harder."
    play sound "audio/yuki_magic_chime.mp3"
    yuki angry blush sweat
    y "{i}Fin...is...{/i}"
    yuki shocked blush sweat
    "[He] completed the spell and opened his eyes."
    yuki shocked sweat
    "The cat still lay motionless on the desk."
    yuki sad
    y "Argh!"
    "Yuki felt frustration bubble in [his] chest. [He] knew there was nothing [he] could do now that wouldn't make it worse."
    yuki shocked
    "Then [he] suddenly remembered."
    yuki shocked blush
    play sound "audio/kettle_whistle.mp3"
    y "Crap, the kettle!"
    yuki shocked
    play sound "audio/steps.mp3"
    "[He] ran back to the kitchen to inspect the damage. Since [he] didn't close the kettle, the water boiled over and burnt the countertop."
    yuki angry
    y "What a mess..."
    yuki sad
    "[He] grabbed a washcloth and began to wipe away the messy burns. Thankfully [hed] fireproofed the kitchen, ensuring the damage wasn't worse."
    play sound "audio/meow_1.mp3"
    yuki
    "Yuki jolted."
    yuki shocked
    y "That sound..."
    play sound "audio/steps.mp3"
    "[He] ran back to the desk and saw the kitten sitting up straight, looking completely unhurt."
    yuki angry
    y "You're alright!"
    yuki
    play sound "audio/meow_1.mp3"
    cat "Yes, I am. Thank you mortal."
    yuki shocked
    "Yuki jumped in shock."
    y "Y-You're talking?!"
    play sound "audio/meow_4.mp3"
    cat "Hmph. Is there something so wrong with that?"
    yuki sad
    y "N-No, it's just that... I'm pretty sure animals don't talk."
    yN "Except for Guardian Spirits, but they're supposed to be fictional!"
    "Yuki shook [his] head."
    yuki
    y "So uh, since you apparently talk, mind telling me what got you here in this neck of woods?"
    "Yuki was fully certain that there were no animals living near [his] cabin. [His] magic wards made sure of it.
    yuki sad
    But recently [hed] been slacking off, which might've explained why there was a cat."
    yuki
    play sound "audio/meow_3.mp3"
    cat "Hmph. I was looking to help humans, but they just called me a monster and attacked me!"
    "The cat looked at me curiously."
    yuki sad
    play sound "audio/meow_1.mp3"
    cat "But you're not like most mortals, are you?"
    "Yuki shuddered under the cat's scrutinous gaze."
    y "I'm... uh..."
    "[He] struggled to formulate words. It'd been a decade since he spoke to a human, how was he going to talk to a cat?!"
    yuki
    "The cat continued."
    play sound "audio/meow_3.mp3"
    cat "My name is Aurelia Cornelius the 4th. But you can call me Aurelia. You've earned the honor!"
    yuki shocked
    y "The... honor?"
    play sound "audio/meow_2.mp3"
    cat "Yes. As a Guardian Spirit, I have the duty to grant one true desire of the mortal that saved me."
    yuki sad
    y "Is that so?"

    menu:
        "In that case, I'll ask for..."
        "Eternal youth.":
            yuki happy
            y "I'll have eternal youth."
            yuki
            play sound "audio/meow_1.mp3"
            cat "What a typical wish."
            yuki sad
            play sound "audio/meow_3.mp3"
            cat "You realize that when you die all alone in this tiny shack, it doesn't matter if you look gorgeous while doing it?"
            yuki angry
            y "H-Hey!"
            yuki sad
            "Yuki knew her words were true, but that didn't stop them from stinging [his] heart."

        "Unlimited money.":
            yuki happy
            y "I'll have unlimited money."
            yuki
            play sound "audio/meow_1.mp3"
            cat "What a typical wish."
            yuki sad
            play sound "audio/meow_3.mp3"
            cat "No matter how much money you have, there's no way you can spend it living in this tiny hut."
            yuki angry
            y "H-Hey!"
            yuki sad
            "Yuki knew her words were true, but that didn't stop them from stinging [his] heart."

        "Infinite wishes.":
            yuki
            "Feeling smug, Yuki continued."
            yuki happy
            y "Infinite wishes."
            yuki
            play sound "audio/meow_1.mp3"
            cat "What a typical wish."
            yuki sad
            play sound "audio/meow_3.mp3"
            cat "If I had enough power to grant you infinite desires, I wouldn't be lying injured near your tiny shack."
            yuki angry
            y "It's not a shack, it's a cabin! And I prefer to call it 'cozy.'"
            yuki sad
            "Aurelia narrowed her eyes, so I decided not to challenge her words further."

    call wish_granted
    call first_day
    call classroom
    call cafeteria
    call library
    call mother_call
    call assignment

    return

label wish_granted:
    yuki angry
    y "But you were supposed to grant my wish!"
    yuki sad
    "Aurelia shook her head. I didn't know it was possible for a cat to look so disappointed, but Aurelia pulled it off well."
    yuki
    play sound "audio/meow_2.mp3"
    cat "Although I can grant human desires, there are two clauses."
    cat "The desire must be within my power. Although I'm really strong—"
    yuki angry
    "Yuki coughed."
    yuki
    play sound "audio/meow_5.mp3"
    cat "AHEM. I still have limits. And the second is..."
    "Yuki looked at Aurelia in anticipation."
    yuki sad
    y "The second is?"
    yuki shocked
    play sound "audio/meow_1.mp3"
    cat "The human can't decide the wish."
    y "Wha—"
    play sound "audio/eerie_wind.mp3"
    yuki shocked blush
    "A loud gust suddenly knocked the breath out of Yuki's lungs."
    yuki angry blush
    scene black with fade
    y "What's happening?!"
    yuki shocked blush
    "[He] looked around, but [his] cabin was gone. Instead, he saw [himself] floating in the sky, the wind wrapping around him."
    y "Where—"
    cat "This is your mind, human. Clearly it is turbulent..."
    "Yuki felt the most inner, vulnerable parts of [himself] coming to the surface."
    yuki angry blush
    y "No... NO! STOP! STOP RIGHT NOW!"
    "Yuki frantically waved [his] arms around, trying to stop the onslaught of emotions threatening to choke [him]."
    yuki shocked blush
    "Aurelia looked almost sympathetic, but didn't stop."
    "She sighed and looked Yuki in the eye."
    play sound "audio/meow_1.mp3"
    cat "Your greatest desire is in my power but... it's going to be troublesome."
    yuki angry blush
    y "What are you—?!"
    yuki shocked blush
    "The edges of Yuki's vision faded and the world went black."
    scene black with fade
    return

label first_day:
    "Yuki felt dizzy and confused."
    yuki shocked
    yN "Where... where am I?"
    scene bg school with fade
    "[He] looked around. He was sitting under a large, shady tree. From the corner of his eye, he saw college students hurridly walking."
    yuki sad
    "Some were casting low-level magic spells, causing haphazard accidents. Others were frantically scribbling through notebooks."
    yuki
    "It was a familiar sight, definitely something Yuki knew by heart."
    y "This is... this is The Vednore Academy of the Elite."
    "It was the greatest post-secondary education institute in the nation, if not the world."
    "But most importantly it was..."
    yuki sad
    yN "Where I'd studied."
    y "But..."
    yuki
    "Yuki noticed something in the center of the campus. More accurately, something missing."
    yuki sad
    yN "That was where—"
    "His thoughts were interrupted by approaching footsteps. He looked up at the sound."
    show quinn at offscreenleft
    pause 0.0
    show quinn shocked at center with move
    yuki shocked
    q "U-Um... are you alright?"
    show quinn neutral
    "I stared at the woman in front of me, shocked."
    yuki shocked blush
    yN "Quinn?!"
    show quinn shocked
    q "You seem a bit unwell... d-do you need to go to the infirmary?"
    show quinn neutral
    "Yuki looked up at the face he hadn't seen in a decade, yet would never forget. It was Quinn. The one he'd loved so dearly."
    yuki blush
    "She reached into a pocket hidden in the side of her skirt and pulled out a handkerchief."
    show quinn happy
    q "You can use this if you need to."
    "Her smile was nervous, but clearly she wanted to help. It was what drew Yuki in years ago, what made him fall in love."
    yuki blush sad
    "But now, all it brought him was pain."
    show quinn neutral
    "Yuki stood up and dusted him lap."
    yuki
    y "I'm fine."
    yuki happy
    "He forced a tight smile."
    show quinn sad sweat
    y "Thanks."
    show quinn sad at offscreenleft with move
    "He ignored her concerned pleas and walked toward the center of the campus. There was a large statue with some guy Yuki never bothered learning the name of."
    yuki
    "Most notably, the large garden around it he'd made with Quinn as a sign of their enduring happiness was not there."
    yuki sad
    "Combined with the fact that she didn't recognize Yuki..."
    yuki shocked sweat
    yN "Am I... in the past?"
    play sound "audio/meow_5.mp3"
    cat "Ding ding ding! You're correct!"
    yuki shocked
    "Yuki whipped his head around, trying to find the source of the voice. The people around him started whispering to each other, staring at him."
    yuki sad blush
    "He blushed, feeling embarrased."
    play sound "audio/meow_1.mp3"
    cat "I'm {i}inside{/i} your head, don't you realize?"
    yuki sad
    y "Uh..."
    play sound "audio/meow_2.mp3"
    cat "Because of this, I'm stuck in the past too. How annoying."
    yN "S-Sorry?"
    "It felt strange to be talking to a voice inside his head."
    yuki shocked
    play sound "audio/meow_6.mp3"
    cat "Now, hurry up and get to class before things get bad!"
    yuki neutral
    yN "Okay, okay... so bossy..."
    play sound "audio/steps.mp3"
    scene black with fade
    yuki None
    return

label hook:
    scene black with fade
    play sound "audio/quinn_gasp.mp3"
    pause 0.85
    play sound "audio/glass_break.mp3"
    pause 0.5
    scene lab
    show quinn sad
    with fade
    pause 0.25
    q "I don't love you."
    yuki angry
    "Yuki reeled back in shock."
    yuki shocked blush
    y "Quinn...?"
    yuki shocked sweat
    show quinn sad blush at yell
    q "I said, I DON'T LOVE YOU!"
    yuki sad
    show quinn sad
    "His normally soft-spoken lover now spat the words at him with venom."
    yuki sad sweat
    y "W-What... listen, we can talk this out!"
    yuki sad blush
    show quinn sad blush
    "She raised her palms to her face and wiped away tears."
    show quinn shocked blush
    q "No. There's nothing to talk about. I don't want to see you anymore."
    show quinn sad blush at offscreenright with move
    play sound "audio/quinn_run_away.mp3"
    "Quinn ran, her footsteps echoing through the corridor."
    yuki angry
    "Yuki looked around. There were a dozen animal corpses strewn at his feet. Bottles containing half-finished potions were everywhere. Some were at his desk
    for testing, others lay broken on the floor."
    yuki sad
    y "I just wanted to save Mother. I didn't want her to die!"
    yuki angry blush
    "Tears streamed down his face as he looked at the chaos around him."
    yuki angry blush
    y "Where did I go wrong?"
    scene black with fade
    yuki None
    # "Yuki felt dizzy and disoriented, but did [his] best to look around."
    # y "Where am I?"
    # "[He] felt soft, cushioned covers under him. A nostalgic scent surrounded him."
    # yN "(...This is...)"
    # "Yuki threw the comforter off [him] and jumped to [his] feet."
    # y "There's no mistaking it. This is the "
    return

label classroom:
    scene classroom with fade
    prof "As it is currently the first class of the year, we are beginning with a test of skill."
    yuki
    "Yuki knew exactly what this so called \"test\" was supposed to do."
    "Professor Chen was notorious for baiting the newcomers into doing dangerous acts to prove how unstable their minds were."
    yuki sad
    "Looking back, Yuki knew what a great professor he was. But at the time, he thought Dr. Chen was cowardly and weak for disrespecting power."
    prof "As the bright new class of the Academy, you have demonstrated your skill well. However, this is Vednore."
    "The professor narrowed his eyes."
    prof "Every single student is excellent. You are not special in anyway."
    play sound "audio/class_murmur.mp3"
    "The classroom buzzed with heated murmors as the students began arguing among themselves, perfectly proving his point."
    yuki shocked
    prof "Silence!"
    "Shocked, the class went quiet."
    "In the corner of the class were the Juris students. They were the highest ranked students that were not in the Magicae program."
    yuki sad blush
    show quinn sad at offscreenright, seated
    pause 0.0
    show quinn sad at center, seated with dissolve
    "They nervously took notes and observed. Among the students was Quinn."
    y "..."
    yuki sad
    show quinn
    prof "...And that is why, today we are having a test where students demonstrate their power. There are no restrictions, because all of you are far so weak
    it is uneccesary."
    "The students uncomfortably shifted."
    yuki neutral
    yN "You fools, this is what he wants."
    "Yuki knew he wasn't one to judge, considering he was in their position back then as well. But he couldn't help feeling a bit smug."
    yuki sad
    show zethe at offscreenleft
    pause 0.0
    show zethe at one_two, seated
    show quinn at two_two, seated
    with dissolve
    "Among the rattled students was Zethe."
    yuki sad blush
    "Yuki felt his blood boil when he saw him. It was a conditioned reflex at that point."
    "Zethe was one of those students who had everything. He was born to powerful and wealthy nobles, and had immense ability at magic."
    yuki shocked blush
    "And an infuriating habit of constantly challenging Yuki to matches."
    yuki sad
    "Yuki took deep breaths to steady himself as the various students were called in front, one by one."
    yuki
    "Each demonstrated their unique abilities. A definite part of it was to impress the Juris students who were watching in awe."
    yuki sad
    "After every demonstration, Professor Chen looked more and more disappointed. This frustrated the students, who began to make mistakes."
    yuki shocked sweat
    show quinn shocked sweat at startle
    show zethe angry
    play sound "audio/mini_boom.mp3"
    "Student" "UWAAAAAAAAH!!"
    play sound "audio/water_pour.mp3"
    "The student's hair caught on fire. The students sitting down began to laugh heartily as Professor Chen cast a water spell to drench it."
    yuki sad
    show zethe neutral
    prof "Tsk tsk."
    yuki
    show quinn sad -sweat
    "After several more demonstrations, some successful, most botched, Zethe's name was called."
    hide quinn with dissolve
    show zethe at center with move
    y "Hm..."
    yuki sad
    "Yuki peered curiously to see what Zethe would do. Last time, he was so caught up in his own thoughts to bother about him."
    "Zethe raised his palm forward and began moving his fingers in a complicated motion. A beautiful, intricate flower of fire danced on his fingertips."
    yuki sad blush
    y "Wow..."
    yuki sad
    show zethe sad blush
    play sound "audio/zethe_magic_chime.mp3"
    "Suddenly, Zethe scrunched his eyebrows together and threw his other hand in front. The flower of fire was covered in a gorgeous icy shell."
    yuki shocked
    show zethe neutral -blush
    "The entire class audibly gasped."
    yuki shocked sweat
    "Inside the icicle casing, Yuki saw the fire dancing intricatly. It was truly impressive."
    yuki angry
    show quinn at offscreenleft, seated
    pause 0.0
    show quinn blush at one_two with move
    show zethe happy
    "Then, Zethe winked and handed it to Quinn, who blushed and refused it."
    yuki angry blush
    y "...!"
    yuki blush
    show zethe
    "The annoyance inside him was familiar, but Yuki did his best to supress it."
    show quinn shocked blush
    show zethe happy
    z "Hm... I will keep it for the next time we meet."
    yuki angry
    show quinn neutral blush
    yN "He thinks he's so smooth..."
    yuki angry blush
    show zethe at two_two, seated with move
    "Yuki would never admit it, but there was a part of him that was impressed by the gesture."
    show quinn -blush
    yuki sad
    "Even though Yuki knew it was coming, he still felt a fizzle down his spine at the Professor's next words."
    yuki shocked
    show quinn shocked
    show zethe happy
    prof "Yuki Zen’Ichirou, please step forward."
    show quinn neutral
    "Yuki straightened out his clothes and walked down to the front of the lecture hall."
    show zethe neutral
    prof "Perform one magical action that demonstrates your abilities best."
    yN "Hm..."
    show quinn sad
    show zethe happy
    "Yuki could play the part of the stupid, ambitious student and cast a powerful spell. This would be the best option to fly under the radar and not pick up anyone's
    suspicions."
    show zethe neutral
    show quinn neutral
    "He could also refuse to do a powerful spell, instead opting for something simple. This would impress the Professor and get him in his good graces, but would make him more suspicious."
    show quinn sad
    yN "What should I do?"

    menu:
        "Cast a powerful and flashy spell.":
            $ passed = False
            yuki sad
            "Yuki's specialization during school was healing. Considering there was nothing to heal, it was best to try something more flashy."
            yuki
            "He shut his eyes and thought of a beautiful creature. An image of a lovely monarch butterfly came to mind."
            yN "This should do."
            "He lifted his palm in the air and spoke the words."
            yuki blush
            show quinn shocked
            "He felt his chest heave from exhaustion."
            yuki sad
            show zethe happy
            yN "This should be easy... why is this so hard?"
            yuki sad blush
            show quinn sad sweat
            "He remembered the previous events. His emotions felt rattled and out of control."
            y "Urk..."
            show quinn shocked
            show zethe shocked sweat
            yuki shocked blush
            play sound "audio/yuki_magic_chime.mp3"
            "A beautiful, white monarch butterfly made of wind emerged from his finger tips. It was made of wisps of breeze that precariously stood on his hand."
            yuki shocked
            show quinn shocked -sweat
            show zethe shocked -sweat
            y "Phew... I did it!"
            play sound "audio/class_murmur.mp3"
            "The entire class gasped. Even Professor Chen looked surprised."
            show zethe shocked blush
            z "...!"
            show quinn shocked blush
            q "Wow..."
            yuki shocked blush
            yN "These looks are totally... worth it..."
            yuki sad
            "Yuki felt his head hurt. The tediousness of the spell, combined with his fragile mental state were weighing on him far worse than he'd thought."
            yuki sad
            show quinn sad -blush
            show zethe sad -blush
            yN "I...I..."
            show zethe shocked
            "As if by instinct, I caught Zethe's shocked gaze."
            show zethe shocked blush
            yuki sad blush
            yN "At least now I outdid you..."
            scene black with fade
            call infirmary_start
            z "Everyone failed the test."
            "Yuki wasn't surprised, but he groaned."
            y "I figured."
            z "You know, you are quite strong."
            "Yuki raised an eyebrow."
            y "I feel a 'but...' coming."
            "He smirked."
            z "Oh? Apparently I am quite predictable."
            "There was no way Yuki could say that he'd already dealt with this before, so he resorted to a simpler retort."
            y "I'm always a step ahead."
            "Quinn shook her head."
            q "Both of you, Yuki's really injured! Don't make it worse."
            "I smiled weakly at her concern. She really was the same."
            "Zethe frowned, but didn't say much else."
            z "Hurry up and get better so I can truly defeat you. Next time, in a real duel."
            "Yuki chuckled."
            y "Careful what you wish for."

        "Refuse and cast a basic spell.":
            "Yuki shook his head. He wasn't about to fall for the bait."
            "He took a deep breath and held out his palm."
            y "..."
            "After concentrating a little, a small bubble formed."
            "It floated to the top and popped."
            z "..."
            q "..."
            prof "..."
            y "That was my demonstration. Thank you very much."
            "The entire class began to boo, but Yuki stayed stoic. He wasn't about to let a class of rowdy kids get him down."
            "Professor Chen clapped his hands twice. The sound was so loud, the entire class went quiet."
            prof "Students. In front of us is the only student who passsed the examination."
            "The class began to whisper and murmur, but Professor Chen waved his hand and they went silent again."
            "He paced the room."
            prof "Being in control is the most important skill a magician can have."
            "He stopped in front of Zethe, who clicked his tongue."
            prof "Unfortunately, most learn it too late. In fact, in the year..."
            "His words droned on. Although the spell was extremely easy, the exhaustion of the day's events caught up to him. Yuki felt his eyelids droop."
            yN "Don't... sleep..."
            "But Yuki couldn't help it. As if by instinct, he caught Quinn's eyes. They were full of concern."
            yN "Even now, huh? I guess I am a fool...."

            call infirmary_start
            z "You were the only one who passed the test."
            "Even though he'd expected it, Yuki felt a small thrill through his spine."
            y "I know."
            q "I'm glad you didn't do anything rash."
            "Her voice was soft, but Yuki felt her relief through it."
            z "You are definitely far stronger than that. I will be keeping an eye out."
            q "Zethe, don't talk like that."
            z "But it is true!"
            "He glared."
            z "There is something he's keeping from us."
            "Yuki felt a shudder run through his body."
            yN "Keep calm..."
            y "Too bad, I don't need to rely on parlor tricks to show my worth."
            z "You called that a {i}parlor trick?!{/i}"
            y "Yes, that's right. I did."
            "Zethe looked angry, but the pink tinting his cheeks was from more than just that. Yuki had got to him."

    return

label infirmary_start:
    play sound "audio/thud.mp3"
    pause 0.5
    play sound "audio/quinn_gasp.mp3"
    yuki None
    "There was a loud thud when Yuki's body hit the floor."
    yN "Where... where am I?"
    "Yuki tried to open his eyes, but they felt like lead."
    z "Is he ever going to wake up?"
    q "D-Don't say something like that!"
    scene bg infirmary afternoon
    show quinn sad at one_two
    show zethe happy at two_two
    with fade
    "Yuki's eyes flew open."
    q "Oh, you're awake!"
    z "Finally."
    y "What are you doing here?"
    z "Us? We are simply here to tell you that..."

    return

label infirmary_end:
    z "It's infuriating. That professor does not understand what true power is!"
    "Yuki gazed up at Zethe from the bed. It was exactly how he'd thought years ago."
    q "No, I think Professor Chen has a point. Being reckless and rushing headfirst... I-I don't think that's the best way to do things."
    "Zethe's gaze softened at her response."
    z "Maybe, but..."
    "Looking at the two of them interact as if they were long-lost friends made my heart clench."
    y "Both of you. Leave."
    q "W-What? But you haven't recovered!"
    y "I said {b}leave.{/b}"
    q "No!"
    "Yuki was shocked at her protest. She never did this in the past. Probably because he'd never asked her to leave."
    q "The infirmary teacher is not present. I won't let you stay alone like this. I-If something happens, it would be really bad."
    y "Okay."
    "Yuki was touched, but he didn't want to admit it."
    z "Ugh. I suppose I will be here as well."
    y "No one asked you to stay."
    z "As if I care. Besides, that teacher's lesson was completely unfair to begin with. Power is important, he doesn't understand that."
    "It may have been so. But Yuki truly believed that..."

    menu:
        "Power is everything":
            y "Power is truly everything. However, remaining calm is part and parcel of being powerful."
            z "Is that so?"
            "Zethe looked intrigued, but Quinn didn't share his attitude."
            q "I-I don't think so. Being powerful is not everything. There's a lot more to life."
            y "Maybe, but—{i}yawn{/i}"


        "Power is not everything.":
            y "Your thinking is childish, Zethe. Power is not everything."
            "Zethe glared."
            z "It does not matter if you believe me childish. The truth remains the truth."
            "Quinn smiled."
            q "I agree, Yuki. You're right. There's a lot more to life than just strength."
            y "Yeah, especially since—{i}yawn{/i}"

    "Yuki blushed sheepishly. Quinn giggled, and Zethe smirked."
    "Yuki felt his eyes close. Perhaps another nap was in order."

    return
