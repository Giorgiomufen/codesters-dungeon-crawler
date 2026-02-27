from time import sleep
import os

clear = lambda: os.system('cls')

def play(animation, speed=0.2):
	for step in animation:
		clear()
		print()
		print(step)
		print()
		sleep(speed)

# waking up
morningAni = [
	'   😔',
	'   😪',
	'   😔',
	'   😪',
	'   😔',
	'   😑',
	'   😑',
	'   😒',
	'   😒',
	'   😐'
]

# normal fight
fightAni = [
	'😠      👹',
	'😠      👹',
	'😠      👹',
	' 😠    👹 ',
	'  😠  👹  ',
	'   😠🤜👹  ',
	'  😠   👹  ',
	' 😡🤛👹   ',
	'  😠  👹  ',
	'   😠🤜💀  ',
	'  😠   💀  ',
	'  😠   💀  '
]

# fireball fight
fireballAni = [
	'😠      👹',
	'😠      👹',
	'😠🔥    👹',
	'😠🔥    👹',
	'😠 🔥   👹',
	'😠  🔥  👹',
	'😠   🔥 👹',
	'😠    🔥👹',
	'😠      💥',
	'😠      💥',
	'😠      💀',
	'😠      💀'
]

# drinking a potion
potionAni = [
	'   🧪',
	'   🧪',
	'  🧪 ',
	' 😮🧪',
	' 😮🧪',
	' 😯  ',
	' 😯  ',
	' 😶  '
]

# death
gameOverAni = [
	'   😨',
	'   😰',
	'   😵',
	'   😵',
	'   💀',
	'   💀',
	'   ⚰️',
	'   ⚰️'
]

# winning
victoryAni = [
	'   😃',
	'   😃',
	'  🎉😃🎉',
	'  🎉😃🎉',
	' 🎊🎉😃🎉🎊',
	' 🎊🎉😃🎉🎊',
	'🏆🎊🎉😃🎉🎊🏆',
	'🏆🎊🎉😃🎉🎊🏆'
]

# finding the spellbook
spellbookAni = [
	'   ✨',
	'  ✨✨',
	' ✨📖✨',
	' ✨📖✨',
	'  ✨📖✨ ',
	'   📖   ',
	'   📖   ',
	'  ✨📖✨ '
]
