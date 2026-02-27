from random import randint
from time import sleep
import os
import sys
sys.stdout.reconfigure(encoding='utf-8') # needed for emojis on windows
from animations import play, morningAni, fightAni, fireballAni, potionAni, gameOverAni, victoryAni, spellbookAni

clear = lambda: os.system('cls')

heroName = "Hero"

hero = {
	"hp": 100,
	"xp": 0,
	"spellbook": False,
	"fireball": False,
	"superpotion": 0
}

day = 1


def showStat():
	clear()
	print("=== 🗡️  DUNGEON CRAWLER 🗡️  ===")
	print("    ", heroName)
	print()
	print("❤️  HP:", hero["hp"], " | ⭐ XP:", hero["xp"])
	print()
	# show whats in the backpack
	print("🎒 Backpack: ", end="")
	if hero["spellbook"] or hero["fireball"] or hero["superpotion"] > 0:
		if hero["spellbook"]:
			print("📖 Spellbook ", end="")
		if hero["fireball"]:
			print("🔥 Fireball ", end="")
		if hero["superpotion"] > 0:
			print("🧪 Superpotion x" + str(hero["superpotion"]), end="")
		print()
	else:
		print("empty")
	print("==============================")
	print()


def reset():
	global hero, day
	hero["hp"] = 100
	hero["xp"] = 0
	hero["spellbook"] = False
	hero["fireball"] = False
	hero["superpotion"] = 0
	day = 1


def fight():
	global hero
	print("⚔️  A goblin jumps out of the shadows!")

	if hero["fireball"]:
		play(fireballAni)
		damage = 0
		print("🔥", heroName, "throws a fireball! The goblin burns to ashes!")
	else:
		play(fightAni)
		damage = randint(10, 30)
		print("The goblin fights back!")

	xp = randint(10, 25)
	sleep(0.5)

	hero["hp"] = hero["hp"] - damage
	hero["xp"] = hero["xp"] + xp

	if damage > 0:
		print("💔", heroName, "took", damage, "damage!")
	print("⭐", heroName, "gained", xp, "XP!")

	if hero["hp"] <= 0:
		gameOver()
		return

	# superpotion can only drop if hero has spellbook, 15% chance
	if hero["spellbook"] and randint(0, 100) < 15:
		hero["superpotion"] = hero["superpotion"] + 1
		print("✨ The goblin dropped a superpotion!", heroName, "puts it in the backpack.")


def noFight():
	print("👀", heroName, "sneaks past the goblin and explores the dungeon...")
	sleep(1)

	# 60% chance to find a potion
	if randint(0, 100) < 60:
		print("🧪", heroName, "found a mysterious potion!")
		drink = input("Drink it? [Y/n] ").lower()

		if drink == '' or 'y' in drink:
			play(potionAni)

			# spellbook makes all potions safe
			if hero["spellbook"]:
				potionEffect = randint(1, 20)
			else:
				potionEffect = randint(-20, 20)

			hero["hp"] = hero["hp"] + potionEffect

			# hp cant go above 100
			if hero["hp"] > 100:
				hero["hp"] = 100

			if potionEffect >= 0:
				print("😊 Healing potion! +" + str(potionEffect) + " HP")
			else:
				print("🤮 It was poison! " + str(potionEffect) + " HP")

			if hero["hp"] <= 0:
				gameOver()
				return
		else:
			print(heroName, "threw the potion away.")
	else:
		print("The corridors are empty.", heroName, "found nothing.")


def gameOver():
	play(gameOverAni)
	showStat()
	print("💀", heroName, "has fallen...")
	print("The dungeon claims another soul.")
	print()
	input("Press ENTER to play again")
	startGame()


def endGame():
	if hero["xp"] == 0:
		play(gameOverAni)
		showStat()
		print("💀", heroName, "survived but gained no experience...")
		print("The dungeon breaks those who hide from battle.")
		print()
		input("Press ENTER to play again")
		startGame()
	else:
		play(victoryAni)
		showStat()
		print("🎉", heroName, "escaped the dungeon!")
		print("Final score:", hero["xp"], "XP")
		print()
		input("Press ENTER to play again")
		startGame()


def startGame():
	global day, heroName
	reset()

	clear()
	print("=== 🗡️  DUNGEON CRAWLER 🗡️  ===")
	print()
	name = input("What is your hero's name? ")
	if name.strip() == "":
		heroName = "Hero"
	else:
		heroName = name.strip()
	print()
	print(heroName, "wakes up in a dark dungeon...")
	print("It will take 10 days to find the way out.")
	print("The dungeon is full of goblins. Good luck.")
	print()
	input("Press ENTER to begin...")

	while day <= 10:
		play(morningAni, speed=0.15)
		showStat()
		print("📅 Day", day, "of 10")
		print()

		# MORNING - superpotion
		if hero["superpotion"] > 0:
			print("🧪 You have", hero["superpotion"], "superpotion(s) in your backpack.")
			drink_super = input("Drink a superpotion? [Y/n] ").lower()
			if drink_super == '' or 'y' in drink_super:
				hero["hp"] = 100
				hero["superpotion"] = hero["superpotion"] - 1
				print("✨", heroName, "drinks the superpotion! HP fully restored!")
				sleep(1)

		# FIGHT or NOT
		print("A goblin is lurking nearby...")
		want_to_fight = input('Fight the goblin? [Y/n] ').lower()
		print()

		if want_to_fight == '' or 'y' in want_to_fight:
			fight()
		else:
			noFight()

		# EVENING - find spellbook on day 5
		if day == 5 and not hero["spellbook"]:
			play(spellbookAni)
			print("📖 As evening falls,", heroName, "finds an ancient spellbook!")
			print("   It reveals the secrets of potions and arcane magic.")
			hero["spellbook"] = True

		# EVENING - learn fireball if spellbook + enough xp
		if hero["spellbook"] and hero["xp"] >= 100 and not hero["fireball"]:
			sleep(1)
			print()
			print("🔥 The spellbook glows!", heroName, "learned the Fireball spell!")
			hero["fireball"] = True

		print()
		input("Press ENTER to continue...")
		day = day + 1

	endGame()


# start the game
startGame()
