# CodeNames-Decoder/Encoder-Engine

This project represents a way to "cheat" on the popular board game CodeNames.

## About the game

The board consists of a square grid of Red, Blue, and Empty tiles with one Black tile.

Every tile contains a word. There are two teams, Red and Blue, each having a spymaster and players who guess cards with words on them. Each team must tap on tiles corresponding to clues given by the spymaster. The clue must be a single word / phrase.

The team that starts first is assigned 9 tiles to correctly guess, and other other team must guess 8. However, only the spymasters know which tiles actually correspond to each team, and must guide their team-mates to select the correct tiles. As a team si guessing tiles, if it guesses an incorrect tile, one of several things can happen, given the kind of tile they guessed.

1. If the tile was blank, they must stop guessing, and it is now the other team's turn.
2. If the tile was of the opposite team, it counts in favor of the opposing team, and the color is revealed.
3. If the black card is revealed, the team that guessed incorrectly immediately loses the game.

## About this project
Usually the team which can better associate cryptic clues to win the game do well. However, the strategy that this project serves to demonstrate is a kind of hack.

The grid is treated as a 2-dimensional NumPy array with 4 kinds of cards. From the perspective of the spymaster (sitting opposite the guessing players), a binary encoding is created going from top to bottom, and left to right, as follows:

- A 1 for every tile that the spymaster's team needs to correctly guess.
- A 0 for all all other tiles. However, this must be explicitly included in the encoding to ensure the entire board is comprehensively encoded as a binary string.

This binary string is converted to a decimal number, which the spymaster can give out as a clue. This number should be unique for the board. 

Now, all the guessing players need to do is to reverse the above process, i.e., convert the decimal number to binary, and generate the board again. Therefore, they know exactly which tiles to guess, and can therefore win in a single turn.

This project provides helper functions to do this process, helpfully reversing the perspective of the grid, to make it easier for players to re-create the grid from the decimal number.