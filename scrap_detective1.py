
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import random

console = Console()
console.clear()
console.print("[bold cyan]=== SCRAP DETECTIVE ===[/bold cyan]\n", justify="center")
input("[dim]Press Enter to start[/dim]")
console.clear()



inventory = []
money = [0]


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
        Luck2 = random.randint(1,100)
        if Luck2 <= 55:
            console.print("[#FFFF00] You get 1 cent [#FFFF00]")
            money[0] += 1
        elif Luck2 <= 63:
            console.print("[#FFFF00] You get a piece of bread [#FFFF00]")
            inventory.append("bread")
        elif Luck2 <= 65:
            console.print("[#FFFF00] You get 3 cents [#FFFF00]")
            money[0] += 3
        elif Luck2 <= 67:
            console.print("[#FFFF00] You get 4 cents [#FFFF00]")
            money[0] += 4
        elif Luck2 <= 100:
            console.print("[#FFFF00] You get 2 cents [#FFFF00]")
            money[0] += 2
intro = Panel(
    "HELLO, adventurer/freak. I'm the narrator, a multi-dimensional or multiversal being. I have many names like storyteller or chronicler. Well enough chit-chat about myself; now let me tell you about it. You are here to enjoy an unbelievable adventure in a mysterious world that is half cruel, then your world. You will continue as a kid named Rumpaul Blumpkin. And now you have to figure out about him and everything else yourself. Now click to continue and bye, adventurer/freak.",
    title="[bold E6E6E6]Introduction[/bold E6E6E6]"
)

console.print(intro)
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
    "[bold #715EFF]Freaky :[/bold #715EFF] [red]ahh!![/red] [#FFFF00]Who the hell are you[/#FFFF00] [red]ah![/red] [#FFFF00]Why are you beating me[/#FFFF00] [red]ah! ahh!![/red] [#FFFF00]What's my fault[/#FFFF00] [red]uhh!! ah![/red]"
)
dim()
console.print(
    "[bold #FFA500]Fruit shop owner :[/bold #FFA500] [#FFFF00]run you disgusting shit, don't want to see a beggar scrap face in front of my fruit shop shop spreading diseases and negativity [/#FFFF00]"
)
dim()
console.print(
    "[bold #715EFF]Freaky :[/bold #715EFF] [red]ahh!![/red]"
)
dim()
console.print(
    "[#E6E6E6]then u ran away from there [/#E6E6E6]"
)
dim()
# scene 2 starts

scene2 = Panel(
    " [black on cyan] Scene 2 [/black on cyan ]",
    expand=False,
    border_style="cyan"
)

scene2a = Align.center(scene2)
console.print(scene2a)

console.print("[#E6E6E6] After running for a while freaky, you now arrived at the old bridge and while huffing and crying you said [#E6E6E6]")
dim()
console.print(
    "[bold #715EFF] Freaky : [/bold #715EFF] [#FFFF00]Huff... Sob... Huff.. why sniff.. why he beat me like this sniff.. ah! Ugh! My leg still hurts, did i do crime or sin? I wasn't even sleeping outside sob.. Huff... his shop I was on the other side of the road sniff.. i will surely punish him in future ughh!! But what should I do now?"
)
dim()
C1 = console.input("[#E6E6E6 on #FFFF00] 1. drink water[/#E6E6E6 on #FFFF00]\t\t[#E6E6E6 on #FFFF00] 2. eat food[/#E6E6E6 on #FFFF00]\t\t\t")

if C1 == "1":
    console.print(
        "[#FFFF00] Yeah I should drink some water from river then should rest [#FFFF00]"
    )
elif C1 == "2":
    console.print("[#FFFF00] result : how can I even think that I have nothing to eat maybe I should try my luck and start begging or do something for my thrust first [/#FFFF00]")
    beg()
dim()
console.print(
    "[#E6E6E6] (After deciding to drink some water freaky, you came down the bridge and drank some water and washed your face and legs with it and then rested on the ground for almost half a hour )[/#E6E6E6]"
)
dim()
#scene 3

scene3 = Panel(
    "[#E6E6E6 on #FFFF00] Scene 3 [/#E6E6E6 on #FFFF00]",
        expand=False,
            border_style="cyan"
)
scene3a = Align.center(scene3)
console.print(scene3a) 

console.print(
    "As you were lying on the ground, resting you started thinking about the situation with that fruit shop owner earlier in market and said.- "
)
dim()
console.print(
    "[#715EFF]Freaky :[/#715EFF] [#FFFF00]hmm... my leg is not hurting anymore and my anger is also vanished, so now as I thought about the incident happened with that fat man in the market I think maybe there is also some fault of mine, if I were in his place maybe I would also have... hmm... no... beating a kid is still not right but I think I should not hold a grudge against him on such a small thing like this and I should forgive him hmm...[/#FFFF00]"
)
dim()
console.print(
    "[#E6E6E6](Then you say in the ground and said.-)[/#E6E6E6]"
)
dim()
console.print(
    "[#715EFF]Freaky :[/#715EFF][#FFFF00] yes I forgive him for this[#FFFF00]"
)
dim()
#scene 4

scene4 = Panel(
    "[#E6E6E6 on #FFFF00] Scene 4 [/#E6E6E6 on #FFFF00]",
    expand=False,
    border_style="cyan"
)

scene4a = Align.center(scene4)
console.print(scene4a)

console.print(
    "[#E6E6E6]Then after five minutes your eyes goes underneath the bridge and saw the old beggar drinking beer by seeing this you said.-[/#E6E6E6]"
)
dim()
console.print(
    """[#715EFF]Freaky :[/#715EFF] [#FFFF00]hmm... I think this all started because of that old drunk head if he hadn't made me run, i wouldn't be sleeping on roadside in front of that fruit shop and got beaten by that fat man it's all that old man's fault, well when I found that place  underneath the bridge I was so happy, I spent two weeks of peaceful nights there and then one day suddenly that old man came and said that this place belonged to him and I should get out of his place and forcefully took my watch and my hat and then beaten me till I ran away from there...
    Hm.. yeah I guess maybe that place was really his and while he was gone I came there and thought tha- ... That I finally found a home a real home... Hm nevermind but still he stole my watch and hat and I have to take them back but later, currently I have to think about food[/#FFFF00]"""
)
dim()
# start of scene 5
scene5 = Panel(
    "[#E6E6E6 on #FFFF00] Scene 5 [/#E6E6E6 on #FFFF00]",
    expand=False,
    border_style="cyan"
)

scene5a = Align.center(scene5)
console.print(scene5a)

console.print(
    "[#E6E6E6]Then sitting on the ground you started thinking what can you do next and then said.-",
)
dim()
console.print(
    """[#715EFF]Freaky :[/#715EFF] [#FFFF00]hm.. what am I gonna do next begging is almost worthless this city is full of heartless souls, maybe if I were only a little bit cute and not have a face like a ugly mug then I think people would spare something more often, well so I have to think of something else hm if people would hire me for labour or house help then my life would have been like heaven but why would someone will hire a frail kid like me, so maybe... I can look for some adventurer quest I know it pays very less wages and I can't even do the hard more paying quest like hunting but seeing my luck in begging this is a far better option[/#FFFF00]"""
)
dim()
