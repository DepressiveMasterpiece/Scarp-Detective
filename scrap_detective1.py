import time
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import random

time.sleep(1.5)
console = Console()
time.sleep(1)

inventory = []
money = [0.0]        # mable coins (the only currency in the game)
flags = {
    "considered_murder": False,   # Scene 10: picked the "throw a stone" option first
    "tempted_by_locket": False,   # Scene 10: picked "take the locket" option first
}


def dim():
    console.print(
        "[dim]Press enter to continue...[/dim]"
    )
    input()


def beg():
    Luck = random.randint(1, 100)
    if Luck <= 97:
        console.print("[#FFFF00] Um I am really that ugly nobody is even listing or looking at me , I should beg more [#FFFF00]")
    elif Luck <= 100:
        Luck2 = random.randint(1, 100)
        if Luck2 <= 55:
            console.print("[#FFFF00] You get 0.01 mable coins [#FFFF00]")
            money[0] += 0.01
        elif Luck2 <= 63:
            console.print("[#FFFF00] You get a piece of bread [#FFFF00]")
            inventory.append("bread")
        elif Luck2 <= 65:
            console.print("[#FFFF00] You get 0.03 mable coins [#FFFF00]")
            money[0] += 0.03
        elif Luck2 <= 67:
            console.print("[#FFFF00] You get 0.04 mable coins [#FFFF00]")
            money[0] += 0.04
        elif Luck2 <= 100:
            console.print("[#FFFF00] You get 0.02 mable coins [#FFFF00]")
            money[0] += 0.02


def introduction():
    intro = Panel(
        "HELLO, adventurer/freak. I'm the narrator, a multi-dimensional or multiversal being. I have many names like storyteller or chronicler. Well enough chit-chat about myself; now let me tell you about it. You are here to enjoy an unbelievable adventure in a mysterious world that is half cruel, then your world. You will continue as a kid named Rumpaul Blumpkin. And now you have to figure out about him and everything else yourself. Now click to continue and bye, adventurer/freak.",
        title="[bold E6E6E6]Introduction[/bold E6E6E6]"
    )
    console.print(intro)
    dim()


def scene1():
    intro1 = Panel(
        " [#E6E6E6 on #FFFF00] Scene 1 [/#E6E6E6 on #FFFF00] ", 
        expand=False, 
        border_style="cyan"
    )
    dim()

    intro1a = Align.center(intro1)
    console.print(intro1a)
    
    # Scene 1 narrator
    console.print(
        "After an usual cold and a bit stormy night, the sun shines again and make the day bright, even in this despair there is a hope in slight --Narrator"
    )
    dim()

    # scene 1 first
    console.print(
        "[bold]??? :[/bold] Freaky, you are sleeping innocently on the roadside but he doesn't know what is going to happen with him in future. Suddenly a big fat guy starts coming towards you with anger and started hitting freaky, you on your legs with a thick stick and said  die you ugly shit!!"
    )
    dim()
    console.print(
        "[bold #715EFF]Freaky :[/bold #715EFF] [red]ahh!![/red] [#E79700]Who the hell are you[/#E79700] [red]ah![/red] [#E79700]Why are you beating me[/#E79700] [red]ah! ahh!![/red] [#E79700]What's my fault[/#E79700] [red]uhh!! ah![/red]"
    )
    dim()
    console.print(
        "[bold #FFA500]Fruit shop owner :[/bold #FFA500] [#E79700]run you disgusting shit, don't want to see a beggar scrap face in front of my fruit shop shop spreading diseases and negativity [/#E79700]"
    )
    dim()
    console.print(
        "[bold #715EFF]Freaky :[/bold #715EFF] [red]ahh!![/red]"
    )
    dim()
    console.print(
        "[#E79700]then u ran away from there [/#E79700]"
    )
    dim()


def scene2():
    scene2_panel = Panel(
        " [black on cyan] Scene 2 [/black on cyan ]",
        expand=False,
        border_style="cyan"
    )

    scene2a = Align.center(scene2_panel)
    console.print(scene2a)

    console.print("[#E6E6E6] After running for a while freaky, you now arrived at the old bridge and while huffing and crying you said [#E6E6E6]")
    dim()
    console.print(
        "[bold #715EFF] Freaky : [/bold #715EFF] [#E79700]Huff... Sob... Huff.. why sniff.. why he beat me like this sniff.. ah! Ugh! My leg still hurts, did i do crime or sin? I wasn't even sleeping outside sob.. Huff... his shop I was on the other side of the road sniff.. i will surely punish him in future ughh!! But what should I do now?[/#E79700]"
    )
    dim()
    C1 = console.input("[#E79700] 1. drink water[/#E79700]\n[#E79700] 2. eat food[#E79700]\t\t\t")

    if C1 == "1":
        console.print(
            "[#E79700] Yeah I should drink some water from river then should rest [#E79700]"
        )
    elif C1 == "2":
        console.print("[#E79700] result : how can I even think that I have nothing to eat maybe I should try my luck and start begging or do something for my thrust first [/#E79700]")
        beg()
    dim()
    console.print(
        "[#E6E6E6] (After deciding to drink some water freaky, you came down the bridge and drank some water and washed your face and legs with it and then rested on the ground for almost half a hour )[/#E6E6E6]"
    )
    dim()


def scene3():
    scene3_panel = Panel(
        "[#E6E6E6 on #FFFF00] Scene 3 [/#E6E6E6 on #FFFF00]",
        expand=False,
        border_style="cyan"
    )
    scene3a = Align.center(scene3_panel)
    console.print(scene3a) 

    console.print(
        "As you were lying on the ground, resting you started thinking about the situation with that fruit shop owner earlier in market and said.- "
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]hmm... my leg is not hurting anymore and my anger is also vanished, so now as I thought about the incident happened with that fat man in the market I think maybe there is also some fault of mine, if I were in his place maybe I would also have... hmm... no... beating a kid is still not right but I think I should not hold a grudge against him on such a small thing like this and I should forgive him hmm...[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6](Then you say in the ground and said.-)[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF][#E79700] yes I forgive him for this[#E79700]"
    )
    dim()


def scene4():
    scene4_panel = Panel(
        "[#E6E6E6 on #FFFF00] Scene 4 [/#E6E6E6 on #FFFF00]",
        expand=False,
        border_style="cyan"
    )

    scene4a = Align.center(scene4_panel)
    console.print(scene4a)

    console.print(
        "[#E6E6E6]Then after five minutes your eyes goes underneath the bridge and saw the old beggar drinking beer by seeing this you said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        """[#715EFF]Freaky :[/#715EFF] [#E79700]hmm... I think this all started because of that old drunk head if he hadn't made me run, i wouldn't be sleeping on roadside in front of that fruit shop and got beaten by that fat man it's all that old man's fault, well when I found that place  underneath the bridge I was so happy, I spent two weeks of peaceful nights there and then one day suddenly that old man came and said that this place belonged to him and I should get out of his place and forcefully took my watch and my hat and then beaten me till I ran away from there...
        Hm.. yeah I guess maybe that place was really his and while he was gone I came there and thought tha- ... That I finally found a home a real home... Hm nevermind but still he stole my watch and hat and I have to take them back but later, currently I have to think about food[/#E79700]"""
    )
    dim()


def scene5():
    scene5_panel = Panel(
        "[#E6E6E6 on #FFFF00] Scene 5 [/#E6E6E6 on #FFFF00]",
        expand=False,
        border_style="cyan"
    )

    scene5a = Align.center(scene5_panel)
    console.print(scene5a)

    console.print(
        "[#E6E6E6]Then sitting on the ground you started thinking what can you do next and then said.-",
    )
    dim()
    console.print(
        """[#715EFF]Freaky :[/#715EFF] [#E79700]hm.. what am I gonna do next begging is almost worthless this city is full of heartless souls, maybe if I were only a little bit cute and not have a face like a ugly mug then I think people would spare something more often, well so I have to think of something else hm if people would hire me for labour or house help then my life would have been like heaven but why would someone will hire a frail kid like me, so maybe... I can look for some adventurer quest I know it pays very less wages and I can't even do the hard more paying quest like hunting but seeing my luck in begging this is a far better option[/#E79700]"""
    )
    dim()


def scene6():
    scene6_panel = Panel(
        "[#E6E6E6 on #FFFF00] Scene 6 [/#E6E6E6 on #FFFF00]",
        expand=False,
        border_style="cyan"
    )

    scene6a = Align.center(scene6_panel)
    console.print(scene6a)

    console.print(
        "[#E6E6E6]After deciding to do it you stand up and went to old adventurer guild, after arriving outside of it you, freaky said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]I have to do it.[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]Then you enter inside and the first thing you saw was the emptiness, there was no one except the counter staff, he was a skinny and tired by seeing him you thought.[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky's thought :[/#715EFF] [#E79700]that person looks very scary and lifeless but I have to focus on my work.[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]Then you looked for the quest board yourself and you found it on the left wall and then you choose.-[/#E6E6E6]"
    )
    dim()
    board = Panel(
        "[#E79700]1. Hunt three wild boars - 13 coins\n2. Chop 15 medium sized ockle wood - 10 coins\n3. Gather a bunch of red marin flower - 2.50 coins[/#E79700]",
        title="[bold #E79700]Quest Board[/bold #E79700]",
    )

    console.print(board)

    int5 = console.input(
        "[#E6E6E6]select one of quest from number of quest for eg 1 for 1st quest: "
    )

    while True:
        if int5 == "1":
            console.print("[#E6E6E6]killing three wild boars with my bare hands and am I crazy to even think that.[/#E6E6E6]")
            break
        elif int5 == "2":
            console.print("[#E6E6E6]hmm I could do that if I have an axe but I didn't have one so I can't.[/#E6E6E6]")
            break
        elif int5 == "3":
            console.print("[#E6E6E6]huh, this is something I can do,I know it will take time and wage is also low but it's the only thing I can do currently that guarantees money.[/#E6E6E6]")
            break
        else:
            int5 = console.input(
                "[red]Invalid choice. Select one of the quests (1, 2, or 3):[/red]"
            )
    dim()


def scene7():
    scene7_panel = Panel(
        "[#E6E6E6 on #FFFF00] Scene 7 [/#E6E6E6 on #FFFF00]",
        expand=False,
        border_style="cyan"
    )

    scene7a = Align.center(scene7_panel)
    console.print(scene7a)
    
    console.print(
        "Counter Staff :[#E79700][dim](I am tired in creaking voice)[dim] are you going to stare at quest board All day or gonna do some real work.[/#E79700]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]uh, um sorry I'm just going [/#E79700]"
    )
    dim()
    console.print(
        "(Outside of old adventurer guild)"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]that person looks scary and tired I think he really hates his job, well as far as I heard these red flowers are found in the west will forest, it's a bit tiring going to other side of city[/#E79700]"
    )
    dim()
    console.print(
        "(Half an hour later, on the outskirts of city)"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]huhh, finally I arrived here now I can see the forest but where are the flowers I can't see any from here, wait there is a man at some distance I should ask him[/#E79700]"
    )
    dim()
    console.print(
        "The you, freaky get to the man who was at some distance, he was a old man looking like a farmer."
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]um, hello sir[/#E79700]"
    )
    dim()
    console.print(
        "[#3c9d2a]Old Farmers[/#3c9d2a]: [#E79700]oh boy, I don't have any money to spare so don't disturb me[/#E79700]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]no sir, I was not begging I just wanted to ask you about something [/#E79700]"
    )
    dim()
    console.print(
        "[#3c9d2a]old farmer[/#3c9d2a] : [#E79700]ok, what?[/#E79700]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]I heard that near the west will forest there are lot of red flowers, but from here I can't see any so can you tell me which direction should I go[/#E79700]"
    )
    dim()
    console.print(
        "[#3c9d2a]old farmer[/#3c9d2a] : [#E79700]okay, tell me what is the name of flowers you are looking for[/#E79700]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky [/#715EFF]: [#E79700]umm, red marin flowers I guess[/#E79700]"
    )
    dim()
    console.print(
        "[#3c9d2a]old farmer[/#3c9d2a] : [#E79700]hm, well do you know the difference between red marin and red marim flower [/#E79700]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]uh, no[/#E79700]"
    )
    dim()
    console.print(
        "[#3c9d2a]old farmer[/#3c9d2a] : [#E79700]so remember clearly, do you want red marin or red marim [/#E79700]"
    )
    dim()
    
    s7a = console.input(
        "[#715EFF]Freaky [/#715EFF]:[#E79700]um, it was[/#E79700]\n[#E6E6E6]1. red marin\n2. red marim[/#E6E6E6]\n[#E79700]Select 1 or 2[/#E79700]\t"
    )

    while True:
        if s7a == "1":
            console.print(
                "freaky's thoughts - [#E79700]yeah it was definitely red marin flowers[/#E79700]"
            )
            break
        elif s7a == "2":
            console.print(
                "freaky's thoughts - [#E79700]red marim hmm, no no no what happened to my memory it was definitely red marin[/#E79700] "
            )
            break
        else:
            console.print(
                "[red]error select again[/red]"
            )
            s7a = console.input(
                "[#715EFF]Freaky [/#715EFF]:[#E79700]um, it was[/#E79700]\n[#E6E6E6]1. red marin\n2. red marim[/#E6E6E6]\n[#E79700]Select 1 or 2[/#E79700]"
            )
    dim()
    console.print(
        "[#3c9d2a]old farmer[/#3c9d2a] : [#E79700]tell fast boy i don't have all day [/#E79700]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]uh, sorry I was definitely red marin[/#E79700]"
    )
    dim()
    console.print(
        "[#3c9d2a]Old farmer[/#3c9d2a] - [#E79700]listen boy they both look almost same and grow alongside eachother but the biggest difference in them is in red marin there are golden design strips in bottom which marin doesn't, [/#E79700]so Then he points his hand towards a tree and said.-\nOld farmer - [#E79700]do you see that tree over there when you arrive there you will see those flowers, now go fast kid I have other work[/#E79700] "
    )
    dim()
    console.print(
        "[#715EFF]Freaky[/#715EFF] :[#E79700] ok, sir[/#E79700]"
    )
    dim()
    console.print(
        "Then you go to the tree he pointed and when you arrived their you see a vast area full of flowers, then you get close to them and thought -"
    )
    dim()
    console.print(
        "Freaky's thoughts - [#E79700]hm, so which flowers should I collect[/#E79700]"
    )
    dim()
    console.print(
        "[#E79700]1. The one with golden strips \n2. The one without golden strips [/#E79700]"
    )
    
    scene7b = console.input(
        "[dim] Select 1 or 2[/dim]\t"
    )
    while True:
        if scene7b == "1":
            console.print(
                "[#E79700]yeah as that old man told me marin has golden strips [/#E79700]"
            )
            break
        elif scene7b == "2":
            console.print(
                "[#E79700]what happened to me, that old man clearly told me it was the one with golden strips, maybe it's because of hunger [/#E79700]"
            )
            break
        else:
            console.print(
                "[red]error select again[/red]"
            )
            scene7b = console.input(
                "[dim] Select 1 or 2[/dim]"
            )
    dim()
    console.print(
        "Then you started to plucking them but after a moment, a thought came to your mind and you said.-"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]wait, how will I carry these flowers I don't have a basket or something like that, hmm... Oh I can use my shirt to carry these[/#E79700]"
    )
    dim()
    console.print(
        "Then you took off your shirt and began collecting flowers in it. After 20 minutes you gathered a bunch of flowers, you tied the shirt into a knot and said.-"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]huu, finally I think this much flowers are enough now I should go back[/#E79700]"
    )
    dim()
    console.print(
        "Then after arriving at the tree you look back take a breath and said.- "
    )
    dim()
    console.print(
        "[#715EFF]Freaky[/#715EFF] : [#E79700]The smell of these flowers, the breezing air and the hot sun, I'm feeling something that I never felt before, I never saw before, i never thought before, I want to describe this in words but... maybe later, I'm hungry and I should hurry[/#E79700]"
    )
    dim()


def scene8():
    scene8_panel = Panel(
        "[#E6E6E6 on #FFFF00] Scene 8 [/#E6E6E6 on #FFFF00]",
        expand=False,
        border_style="cyan"
    )

    scene8a = Align.center(scene8_panel)
    console.print(scene8a)

    console.print(
        "then you walked down the way to guild with happiness and satisfaction in your heart while saying something in your mind.-"
    )
    dim()
    console.print(
        "[#715EFF dim]Freaky's thought :[/#715EFF dim] [#E79700]well first time in feeling something like this, first time im not depended on luck for money , well I know wages are low and work is tiring but still this is far better then begging on luck, are those other beggars very lazy or really stupid or am I a genius [/#E79700]"
    )
    dim()
    console.print(
        "Talking to yourself you didn't realised that you have already arrived outside the guild and after realising it you said.-"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]wow, finally this moment has came now I will go inside take the money and then buy some tasty bread[/#E79700]"
    )
    dim()

def banner(n):
    console.print(Align.center(Panel(
        f"[#E6E6E6 on #FFFF00] Scene {n} [/#E6E6E6 on #FFFF00]",
        expand=False,
        border_style="cyan"
    )))


def scene9():
    banner(9)

    console.print(
        "[#E6E6E6]Excitedly you opened the door and saw the emptiness of that place again, the dreadfulness and the silence, but this time it didn't bother you that much. So you went straight to the counter and said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]hello, sir[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]You, Freaky, see the same person at the counter that you saw before. He ignored you, maybe because he was deep in a book, or because he didn't want to reply.[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]hello sir, I'm here[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]He finally spoke, in a dreadful and unpleasant voice.[/#E6E6E6]"
    )
    dim()
    console.print(
        "[bold #C46A6A]Counter staff :[/bold #C46A6A] [#E79700]augh! I was reading an interesting part but you broke my focus[/#E79700]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]um, sorry for that[/#E79700]"
    )
    dim()
    console.print(
        "[bold #C46A6A]Counter staff :[/bold #C46A6A] [#E79700]huf, well now that you've already broken my focus, tell me fast[/#E79700]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]well, I came here for that flower quest, I've completed it[/#E79700]"
    )
    dim()
    console.print(
        "[bold #C46A6A]Counter staff :[/bold #C46A6A] [#E79700]hm, ok. You see that basket in the left corner? Put those flowers in it[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]You did as he said. After putting the flowers in the basket you put your shirt back on, turned around, went to the counter and said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]sir, I completed the quest, so can you give me my reward please[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]He looked at you for a second, then took money from the drawer under the table and placed it on the counter. You looked at the money. It was just 0.50 mable coins. Seeing this, you said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#E79700]1. Sir, there is some mistake, my original reward is 2.50 mable coins\n2. Sir, my reward is 2.50 mable[/#E79700]"
    )
    s9a = console.input(
        "[dim] Select 1 or 2[/dim]\t"
    )
    while True:
        if s9a == "1":
            console.print(
                "[#715EFF]Freaky :[/#715EFF] [#E79700]sir, there is some mistake, my original reward is 2.50 mable coins[/#E79700]"
            )
            break
        elif s9a == "2":
            console.print(
                "[#715EFF]Freaky :[/#715EFF] [#E79700]sir, my reward is 2.50 mable[/#E79700]"
            )
            break
        else:
            console.print(
                "[red]error select again[/red]"
            )
            s9a = console.input(
                "[dim] Select 1 or 2[/dim]\t"
            )
    dim()
    console.print(
        "[#E6E6E6]After hearing this he slapped you angrily and, with a scary expression, he said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[bold #C46A6A]Counter staff :[/bold #C46A6A] [#E79700]what did you say, you damn thin pig?! You should be grateful that I even gave you a reward[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]You cried and said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]but sir, I've really worked hard for this, please have mercy, I beg you[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]With that same scary expression he said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[bold #C46A6A]Counter staff :[/bold #C46A6A] [#E79700]you are so stubborn, thin pig. Ok, listen: if you were not a helpless little boy I wouldn't even have given you those 0.50 mable. You know why? [/#E79700][bold](then he shouted)[/bold] [#E79700]You don't have! Fucking!! Guild permit!![/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]You got a little confused because you didn't know anything about a guild permit, and in a crying voice you said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#E79700]1. What is this guild permit? Sir\n2. How can I get this? Sir[/#E79700]"
    )
    s9b = console.input(
        "[dim] Select 1 or 2[/dim]\t"
    )
    while True:
        if s9b == "1":
            console.print(
                "[#715EFF]Freaky :[/#715EFF] [#E79700]what is this guild permit? Sir[/#E79700]"
            )
            dim()
            console.print(
                "[bold #C46A6A]Counter staff :[/bold #C46A6A] [#E79700]are you dumb? You can't understand that without this permit you can't receive a reward after completing a quest? And if you want it, you have to pay the guild 1000 Synth coins[/#E79700]"
            )
            break
        elif s9b == "2":
            console.print(
                "[#715EFF]Freaky :[/#715EFF] [#E79700]how can I get this? Sir[/#E79700]"
            )
            dim()
            console.print(
                "[bold #C46A6A]Counter staff :[/bold #C46A6A] [#E79700]how can you get this? Ok, listen closely, I will only tell you once: by paying the guild 1000 Synth coins![/#E79700]"
            )
            break
        else:
            console.print(
                "[red]error select again[/red]"
            )
            s9b = console.input(
                "[dim] Select 1 or 2[/dim]\t"
            )
    dim()
    console.print(
        "[bold #C46A6A]Counter staff :[/bold #C46A6A] [#E79700]now go away, I want to read this book in peace[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]After hearing all this, your hope turned into despair. You cried and said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]ok, have a good day sir[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]Then you took the money from the table and ran away in tears.[/#E6E6E6]"
    )
    money[0] += 0.50
    console.print(
        "[bold #E79700]+0.50 mable coins[/bold #E79700]"
    )
    dim()


def scene10():
    banner(10)

    console.print(
        "[#E6E6E6]After coming out of the guild you, Freaky, ran straight for a while. Out of breath, you stopped near the old bridge and said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]sob.. sob.. Huff.. I'm... hungry sob.. Huff.. I have.. sob.. no time to complain Huff.. about my situation sob.. now I have to.. huf.. depend on my luck and start begging again sob..[/#E79700]"
    )
    dim()

    # Scripted begging: the first three tries always fail, the fourth always succeeds
    attempt = 0
    while attempt < 4:
        b10 = console.input(
            "[#FFFF00]1. Beg[/#FFFF00]\t"
        )
        if b10 != "1":
            console.print(
                "[red]error select again[/red]"
            )
            continue
        attempt += 1
        if attempt == 1:
            console.print(
                "[#FFFF00] Nobody even looked at me... I should try again [/#FFFF00]"
            )
        elif attempt == 2:
            console.print(
                "[#FFFF00] A woman crossed the street just to avoid me... again [/#FFFF00]"
            )
        elif attempt == 3:
            console.print(
                "[#FFFF00] Someone muttered 'get a job' and walked past... one more time [/#FFFF00]"
            )
        else:
            console.print(
                "[#FFFF00] Someone dropped a coin in front of you. You get 0.50 mable coins [/#FFFF00]"
            )
            money[0] += 0.50
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]oh finally, now I have enough money to buy bread[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]After that you, Freaky, went to the bakery where you saw the owner. You went to him and said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]I want a bread[/#E79700]"
    )
    dim()
    console.print(
        "[bold #FFA500]Bakery owner :[/bold #FFA500] [#E79700]and do you have money?[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]Then you took out your money and gave it to him. He gave you a bread.[/#E6E6E6]"
    )
    money[0] -= 1.00
    inventory.append("bread")
    console.print(
        "[bold #E79700]-1.00 mable coins, +1 bread[/bold #E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]You took it and went straight to the old bridge. When you arrived there, you sat down beside the river and ate your bread, then said.-[/#E6E6E6]"
    )
    inventory.remove("bread")
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]if I think about the whole situation now, I think what that scary guy said was right. According to the rules it was illegal to even give me those 0.50 mable, and the only thing he did wrong was slapping me. If I had known this rule I wouldn't have asked for the full reward. I think I can forgive him this time, because he showed kindness by giving me those 0.50 mable coins.[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]You rested there for a while, then stood up and went to the market and begged for hours, but nobody gave you anything. After the sun went down and night came, people started closing their shops. You were tired and decided to leave. When you arrived near the old bridge you said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]I think this is the right time, I should check if the drunk old beggar...[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]Then you went to the inner side of the bridge and saw the old beggar sleeping. Seeing him, you said.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky :[/#715EFF] [#E79700]ok, this is the right time, I should...[/#E79700]"
    )
    dim()
    console.print(
        "[#E79700]1. Find a big stone and throw it on his head, and take my belongings\n2. Walk silently towards him and carefully check his pockets[/#E79700]"
    )
    s10a = console.input(
        "[dim] Select 1 or 2[/dim]\t"
    )
    while True:
        if s10a == "1":
            flags["considered_murder"] = True
            console.print(
                "[#715EFF]Freaky :[/#715EFF] [#E79700]how did this thought even come to my mind? How can I think to murder someone? I think it's better to silently walk towards him and check his pockets[/#E79700]"
            )
            break
        elif s10a == "2":
            console.print(
                "[#715EFF]Freaky :[/#715EFF] [#E79700]yeah, this seems right[/#E79700]"
            )
            break
        else:
            console.print(
                "[red]error select again[/red]"
            )
            s10a = console.input(
                "[dim] Select 1 or 2[/dim]\t"
            )
    dim()
    console.print(
        "[#E6E6E6]Then you walked towards him carefully, without making any noise. After getting close to him you carefully started checking his pockets, but suddenly.-[/#E6E6E6]"
    )
    dim()
    console.print(
        "[bold #3c9d2a]Drunk old beggar :[/bold #3c9d2a] [#E79700]hghwa.. where's my beer... Hghwawa..[/#E79700]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky's thoughts :[/#715EFF] [#E79700]oh God! I thought he was going to wake up. I should do this more carefully[/#E79700]"
    )
    dim()
    console.print(
        "[#E6E6E6]After some tries you found three items. The first was your pocket watch, the second was your hat, and the third was a locket with a photo of a woman in it. When you found it you thought.-[/#E6E6E6]"
    )
    inventory.append("pocket watch")
    inventory.append("hat")
    console.print(
        "[bold #E79700]+ pocket watch, + hat[/bold #E79700]"
    )
    dim()
    console.print(
        "[#715EFF]Freaky's thoughts :[/#715EFF] [#E79700]hmm, this locket seems a bit important to him...[/#E79700]"
    )
    dim()
    console.print(
        "[#E79700]1. I should take this locket as his punishment\n2. No, I can't steal it, it's important to him[/#E79700]"
    )
    s10b = console.input(
        "[dim] Select 1 or 2[/dim]\t"
    )
    while True:
        if s10b == "1":
            flags["tempted_by_locket"] = True
            console.print(
                "[#715EFF]Freaky :[/#715EFF] [#E79700]no, what am I thinking? If I do this, then what will be the difference between him and me[/#E79700]"
            )
            break
        elif s10b == "2":
            console.print(
                "[#715EFF]Freaky :[/#715EFF] [#E79700]yeah, I should leave it[/#E79700]"
            )
            break
        else:
            console.print(
                "[red]error select again[/red]"
            )
            s10b = console.input(
                "[dim] Select 1 or 2[/dim]\t"
            )
    dim()
    console.print(
        "[#E6E6E6]Then, without making any noise, you got out of there to find a new place to sleep.[/#E6E6E6]"
    )
    dim()


# Game Execution Flow
if __name__ == "__main__":
    introduction()
    scene1()
    scene2()
    scene3()
    scene4()
    scene5()
    scene6()
    scene7()
    scene8()
    scene9()
    scene10()
# V1 end