import numpy
import math
import re
import random
import sys

pokemonByStatTotal = (
	(0x7b, 0, 'CATERPIE'),
	(0x70, 0, 'WEEDLE'),
	(0x85, 2, 'MAGIKARP'),
	(0x7c, 2, 'METAPOD'),
	(0x71, 2, 'KAKUNA'),
	(0x6b, 0, 'ZUBAT'),
	(0x24, 0, 'PIDGEY'),
	(0xa5, 0, 'RATTATA'),
	(0x05, 0, 'SPEAROW'),
	(0x3b, 0, 'DIGLETT'),
	(0x64, 2, 'JIGGLYPUFF'),
	(0x0f, 1, 'NIDORAN_F'),
	(0x03, 2, 'NIDORAN_M'),
	(0x6d, 0, 'PARAS'),
	(0x6c, 0, 'EKANS'),
	(0x4c, 2, 'DITTO'),
	(0x4d, 0, 'MEOWTH'),
	(0x5c, 0, 'HORSEA'),
	(0x52, 0, 'VULPIX'),
	(0x60, 0, 'SANDSHREW'),
	(0x47, 0, 'POLIWAG'),
	(0xbc, 0, 'BELLSPROUT'),
	(0xa9, 0, 'GEODUDE'),
	(0x58, 2, 'DRATINI'),
	(0x41, 0, 'VENONAT'),
	(0x39, 0, 'MANKEY'),
	(0x6a, 0, 'MACHOP'),
	(0x17, 0, 'SHELLDER'),
	(0xb0, 2, 'CHARMANDER'),
	(0x94, 1, 'ABRA'),
	(0x46, 1, 'DODUO'),
	(0x19, 0, 'GASTLY'),
	(0xb1, 2, 'SQUIRTLE'),
	(0x25, 1, 'SLOWPOKE'),
	(0x99, 2, 'BULBASAUR'),
	(0x54, 1, 'PIKACHU'),
	(0xb9, 0, 'ODDISH'),
	(0x2f, 1, 'PSYDUCK'),
	(0x11, 0, 'CUBONE'),
	(0x9d, 0, 'GOLDEEN'),
	(0x04, 0, 'CLEFAIRY'),
	(0xad, 0, 'MAGNEMITE'),
	(0x3a, 0, 'SEEL'),
	(0x0d, 0, 'GRIMER'),
	(0x4e, 0, 'KRABBY'),
	(0x0a, 1, 'EXEGGCUTE'),
	(0x66, 2, 'EEVEE'),
	(0x30, 0, 'DROWZEE'),
	(0x06, 0, 'VOLTORB'),
	(0x18, 0, 'TENTACOOL'),
	(0x37, 0, 'KOFFING'),
	(0x1b, 1, 'STARYU'),
	(0x12, 0, 'RHYHORN'),
	(0x96, 0, 'PIDGEOTTO'),
	(0x21, 0, 'GROWLITHE'),
	(0x40, 1, 'FARFETCHD'),
	(0x62, 2, 'OMANYTE'),
	(0x5a, 2, 'KABUTO'),
	(0xa8, 0, 'NIDORINA'),
	(0xa7, 1, 'NIDORINO'),
	(0x6e, 0, 'POLIWHIRL'),
	(0x22, 1, 'ONIX'),
	(0x0b, 0, 'LICKITUNG'),
	(0xbd, 0, 'WEEPINBELL'),
	(0x27, 0, 'GRAVELER'),
	(0x7d, 0, 'BUTTERFREE'),
	(0x72, 0, 'BEEDRILL'),
	(0xba, 0, 'GLOOM'),
	(0xaa, 1, 'PORYGON'),
	(0x26, 1, 'KADABRA'),
	(0x09, 2, 'IVYSAUR'),
	(0xb2, 2, 'CHARMELEON'),
	(0xb3, 2, 'WARTORTLE'),
	(0x2e, 0, 'PARASECT'),
	(0x76, 0, 'DUGTRIO'),
	(0x29, 0, 'MACHOKE'),
	(0x93, 1, 'HAUNTER'),
	(0xa3, 0, 'PONYTA'),
	(0xa6, 0, 'RATICATE'),
	(0x59, 2, 'DRAGONAIR'),
	(0x91, 0, 'MAROWAK'),
	(0x65, 0, 'WIGGLYTUFF'),
	(0x1e, 0, 'TANGELA'),
	(0x2d, 0, 'ARBOK'),
	(0x90, 0, 'PERSIAN'),
	(0x5d, 0, 'SEADRA'),
	(0x23, 0, 'FEAROW'),
	(0x61, 0, 'SANDSLASH'),
	(0x77, 0, 'VENOMOTH'),
	(0x28, 0, 'CHANSEY'),
	(0x9e, 0, 'SEAKING'),
	(0x82, 0, 'GOLBAT'),
	(0x75, 0, 'PRIMEAPE'),
	(0x2b, 0, 'HITMONLEE'),
	(0x2c, 0, 'HITMONCHAN'),
	(0x48, 0, 'JYNX'),
	(0x74, 0, 'DODRIO'),
	(0x2a, 2, 'MR_MIME'),
	(0x36, 0, 'MAGNETON'),
	(0x78, 0, 'DEWGONG'),
	(0x8a, 0, 'KINGLER'),
	(0x97, 0, 'PIDGEOT'),
	(0x8d, 0, 'ELECTRODE'),
	(0x8e, 0, 'CLEFABLE'),
	(0x81, 0, 'HYPNO'),
	(0x55, 0, 'RAICHU'),
	(0x01, 0, 'RHYDON'),
	(0xbb, 0, 'VILEPLUME'),
	(0xbe, 0, 'VICTREEBEL'),
	(0x08, 1, 'SLOWBRO'),
	(0x8f, 0, 'WEEZING'),
	(0x02, 0, 'KANGASKHAN'),
	(0x35, 0, 'ELECTABUZZ'),
	(0x3c, 0, 'TAUROS'),
	(0x31, 0, 'GOLEM'),
	(0x33, 0, 'MAGMAR'),
	(0x63, 2, 'OMASTAR'),
	(0x5b, 2, 'KABUTOPS'),
	(0x80, 1, 'GOLDUCK'),
	(0x95, 1, 'ALAKAZAM'),
	(0xa4, 0, 'RAPIDASH'),
	(0x88, 0, 'MUK'),
	(0x0e, 1, 'GENGAR'),
	(0x1a, 0, 'SCYTHER'),
	(0x1d, 0, 'PINSIR'),
	(0x10, 0, 'NIDOQUEEN'),
	(0x07, 0, 'NIDOKING'),
	(0x53, 1, 'NINETALES'),
	(0x7e, 0, 'MACHAMP'),
	(0x6f, 0, 'POLIWRATH'),
	(0x9b, 0, 'TENTACRUEL'),
	(0xab, 0, 'AERODACTYL'),
	(0x0c, 0, 'EXEGGUTOR'),
	(0x98, 0, 'STARMIE'),
	(0x9a, 2, 'VENUSAUR'),
	(0x8b, 0, 'CLOYSTER'),
	(0x69, 0, 'VAPOREON'),
	(0x68, 0, 'JOLTEON'),
	(0x67, 0, 'FLAREON'),
	(0x1c, 2, 'BLASTOISE'),
	(0xb4, 2, 'CHARIZARD'),
	(0x13, 0, 'LAPRAS'),
	(0x16, 0, 'GYARADOS'),
	(0x84, 0, 'SNORLAX'),
	(0x14, 0, 'ARCANINE'),
	(0x4a, 1, 'ARTICUNO'),
	(0x4b, 1, 'ZAPDOS'),
	(0x49, 1, 'MOLTRES'),
	(0x42, 1, 'DRAGONITE'),
	(0x15, 2, 'MEW'),
	(0x83, 2, 'MEWTWO')
)

encounterChances = (
	51./51., #51/256
	51./51., #51/256
	51./39., #39/256
	51./25., #25/256
	51./25., #25/256
	51./25., #25/256
	51./13., #13/256
	51./13., #13/256
	51./11., #11/256
	51./6.   #03/256
)

settings = {
	'strength-variance': 0.08,
	'level-variance': 0.09,
	'trainer-level-variance': 0.077,
	'wild-level-multiplier': 1.5,
	'trainer-level-multiplier': 2.0,
	'trainer-strength-variance': 0.12,
}

romImage = None
targetFile = sys.argv[1]
outFile = 'randomized.gbc'
wildMonAddr = 0xd0dd
wildMonEnd = 0xd5c6
trainerMonAddr = 0x39d99
trainerMonEnd = 0x3a52d
fishingMonAddr = 0xe97d
fishingMonEnd = 0xe9c4


def getRandomPokemon(mean, variance, rarityModifier=0):
	for _ in range(100):
		index = int(round(mean + len(pokemonByStatTotal) * numpy.random.normal(0, variance)))
		if index >= 0 and index < len(pokemonByStatTotal):
			if random.randint(1, 101) >= rarityModifier * 50 * pokemonByStatTotal[index][1]:
				print(pokemonByStatTotal[index][2])
				print('.')
				return pokemonByStatTotal[index][0]
	print('failed to get pokemon in range')
	return 0x15 # MEW


def getRandomLevel(mean, variance):
	for _ in range(100):
		level = int(round(numpy.random.normal(1, variance) * mean))
		if level >= 2 and level <= 254:
			print(level)
			return level
	print('failed to get level in range')
	return 254


def getStrengthIndex(id):
	for i in range(0, len(pokemonByStatTotal)):
		if pokemonByStatTotal[i][0] == id:
			return i
	print(ERROR)
	return None


def randomizeWildPokemon():
	if not romImage:
		return

	nextType = 'head'
	slotIndex = 0
	byteIndex = wildMonAddr

	while byteIndex != wildMonEnd:
		#print('{}: {}, {}'.format(hex(byteIndex), romImage[byteIndex], slotIndex))
		if slotIndex == 10:
			nextType = 'head'
			slotIndex = 0
		slotMod = encounterChances[slotIndex]

		if romImage[byteIndex] == 0x00:
			nextType = 'head'
			slotIndex = 0
		elif nextType == 'head':
			nextType = 'level'
		elif nextType == 'level':
			levelMultiplier = settings['wild-level-multiplier'] + (slotMod - 1) / 15
			meanLevel = romImage[byteIndex] * levelMultiplier
			varianceMultiplier = 1 + (slotMod - 1) / 15
			romImage[byteIndex] = getRandomLevel(meanLevel, settings['level-variance'] * varianceMultiplier)
			nextType = 'pokemon'
		elif nextType == 'pokemon':
			slotMod = encounterChances[slotIndex]
			strengthBonus = 4 * (slotMod) - 1
			variance = settings['strength-variance'] * varianceMultiplier * (1 + (slotMod - 1) / 30)
			boop = getStrengthIndex(romImage[byteIndex])
			romImage[byteIndex] = getRandomPokemon(boop + strengthBonus, variance, 1 / slotMod)
			slotIndex += 1
			nextType = 'level'
		else:
			print('error')

		byteIndex += 1


def randomizeTrainerPokemon():
	if not romImage:
		return

	nextType = 'head'
	uniformLevel = False;
	byteIndex = trainerMonAddr

	while byteIndex != trainerMonEnd:
		#print('{}: {}'.format(hex(byteIndex), hex(romImage[byteIndex])))
		if romImage[byteIndex] == 0x00:
			nextType = 'head'
		elif nextType == 'head':
			if romImage[byteIndex] == 0xff:   
				uniformLevel = False
				nextType = 'level'
			else:
				newLevel = (romImage[byteIndex] - 7) * settings['trainer-level-multiplier']
				if newLevel < romImage[byteIndex]:
					newLevel = romImage[byteIndex]
				romImage[byteIndex] = getRandomLevel(newLevel, settings['trainer-level-variance'])
				uniformLevel = True
				nextType = 'pokemon'
		elif nextType == 'level':
			newLevel = (romImage[byteIndex] - 7) * settings['trainer-level-multiplier']
			if newLevel < romImage[byteIndex]:
				newLevel = romImage[byteIndex]
			romImage[byteIndex] = getRandomLevel(newLevel, settings['trainer-level-variance'])
			nextType = 'pokemon'
		elif nextType == 'pokemon':
			boop = getStrengthIndex(romImage[byteIndex])
			romImage[byteIndex] = getRandomPokemon(boop + 15, settings['trainer-strength-variance'])
			if uniformLevel:
				nextType = 'pokemon'
			else:
				nextType = 'level'
		else:
			print('error')

		byteIndex += 1

		
def randomizeFishingPokemon():
	if not romImage:
		return

	nextType = 'head'
	monCount = 0
	byteIndex = fishingMonAddr
	while byteIndex != fishingMonEnd:
		print('{}: {}'.format(hex(byteIndex), hex(romImage[byteIndex])))
		if nextType == 'head':
			monCount = romImage[byteIndex]
			nextType = 'level'
		elif nextType == 'level':
			meanLevel = romImage[byteIndex] * settings['wild-level-multiplier']
			romImage[byteIndex] = getRandomLevel(meanLevel, settings['level-variance'] * 3)
			nextType = 'pokemon'
		elif nextType == 'pokemon':
			boop = getStrengthIndex(romImage[byteIndex])
			romImage[byteIndex] = getRandomPokemon(boop, settings['strength-variance'] * 3)
			monCount -= 1
			if monCount == 0:
				nextType = 'head'
			else:
				nextType = 'level'


		byteIndex += 1


def main():
	readDataFromFile()

	randomizeWildPokemon()
	randomizeTrainerPokemon()
	randomizeFishingPokemon()

	writeToFile()

def readDataFromFile():
	global romImage
	with open(targetFile, 'rb') as f:
		romImage = bytearray(f.read())

def writeToFile():
	with open(outFile, 'wb') as f:
		f.write(romImage)

main()