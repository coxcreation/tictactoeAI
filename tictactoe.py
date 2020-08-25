#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#                                                                             #
# Program: tictactoe.py                                                       #
# Written by: Eric Cox                                                        #
# Copyright: (C) 2017, Eric Cox. All Rights Reserved.                         #
# Purpose: Create an AI to play TicTacToe in a means with will allow it to    #
#      win or end the game in a draw.                                         #
#                                                                             #
###############################################################################
import os
import sys

class ticTacToeGame:
	playerSymbols=['X','O']
	totalOutcomes=0
	turnWins=[0,0,0,0,0,0,0,0,0,0]
	turnMoves=[0,0,0,0,0,0,0,0,0,0]
	turn9Wins=0
	
	def __init__(self, gBoard, turn):
		self.gameBoard=gBoard
		self.turn=turn
		ticTacToeGame.totalOutcomes+=1
		ticTacToeGame.turnMoves[self.turn]+=1
		self.winner=''
		self.winnerChildX=0
		self.winnerChildO=0
		self.gameOver=self.isGameOver()
		self.childMoves=[]
		if self.gameOver is False:
			self.populateChildMoves(self.gameBoard)
			for child in self.childMoves:
				self.winnerChildX+=child.winnerChildX
				self.winnerChildO+=child.winnerChildO
		else:
			ticTacToeGame.turnWins[self.turn]+=1
			if self.winner=='X':
				self.winnerChildX+=1
			elif self.winner=='O':
				self.winnerChildO+=1
		
	def populateChildMoves(self,gb):
		# print("Turn: "+str(self.turn))
		for x in range(len(gb)):
			if gb[x]==' ':
				nextTurn = self.turn+1
				gameMove = []
				for loc in gb:
					gameMove.append(loc)
				gameMove[x] = ticTacToeGame.playerSymbols[self.turn%2]
				childGame = ticTacToeGame(gameMove,nextTurn)
				#print("Position: "+str(x)+" Board:"+str(gameMove))
				self.childMoves.append(childGame)
					
					
	def getChildMoves(self):
		return self.childMoves
	def isGameOver(self):
		if (self.gameBoard[0]==self.gameBoard[1] and self.gameBoard[1]==self.gameBoard[2] and self.gameBoard[0] != ' '):
			self.winner=self.gameBoard[0]
			return True
		elif (self.gameBoard[3]==self.gameBoard[4] and self.gameBoard[3]==self.gameBoard[5] and self.gameBoard[3] != ' '):
			self.winner=self.gameBoard[4]
			return True
		elif (self.gameBoard[6]==self.gameBoard[7] and self.gameBoard[6]==self.gameBoard[8] and self.gameBoard[6] != ' '):
			self.winner=self.gameBoard[7]
			return True
		elif (self.gameBoard[0]==self.gameBoard[3] and self.gameBoard[3]==self.gameBoard[6] and self.gameBoard[0] != ' '):
			self.winner=self.gameBoard[0]
			return True
		elif (self.gameBoard[1]==self.gameBoard[4] and self.gameBoard[4]==self.gameBoard[7] and self.gameBoard[1] != ' '):
			self.winner=self.gameBoard[1]
			return True
		elif (self.gameBoard[2]==self.gameBoard[5] and self.gameBoard[5]==self.gameBoard[8] and self.gameBoard[2] != ' '):
			self.winner=self.gameBoard[2]
			return True
		elif (self.gameBoard[0]==self.gameBoard[4] and self.gameBoard[4]==self.gameBoard[8] and self.gameBoard[0] != ' '):
			self.winner=self.gameBoard[0]
			return True
		elif (self.gameBoard[2]==self.gameBoard[4] and self.gameBoard[4]==self.gameBoard[6] and self.gameBoard[2] != ' '):
			self.winner=self.gameBoard[2]
			return True
		else:
			return False
		
				

def printBoard(gameArray):
	letterArray=['a','b','c','d','e','f','g','h','i']
	gameString="┌─┬─┬─┐ ┌─┬─┬─┐\n│0│1│2│ │a│b│c│\n├─┼─┼─┤ ├─┼─┼─┤\n│3│4│5│ │d│e│f│\n├─┼─┼─┤ ├─┼─┼─┤\n│6│7│8│ │g│h│i│\n└─┴─┴─┘ └─┴─┴─┘"
	if len(gameArray)==9:
		for x in range(len(gameArray)):
			gameString=gameString.replace(letterArray[x],gameArray[x])
		gameString="Number: Board: \n"+gameString
		return gameString
	else:
		return "Error: Array mismatch"

print("Loading AI")
game1 = ticTacToeGame([' ',' ',' ',' ',' ',' ',' ',' ',' '],0)
print(str(ticTacToeGame.totalOutcomes))
print(ticTacToeGame.turnMoves)
print(ticTacToeGame.turnWins)

while game1.gameOver is False and game1.gameBoard.count(' ')>0:
	print(printBoard(game1.gameBoard))
	nexLoc = input("Where should 'X' play?: ")
	if int(nexLoc)>=0 and int(nexLoc)<9 and game1.gameBoard[int(nexLoc)]==' ':
		tempBoard=[]
		for space in game1.gameBoard:
			tempBoard.append(space)
		tempBoard[int(nexLoc)]='X'
		for child in game1.childMoves:
			if child.gameBoard == tempBoard:
				game1=child
		
		
		#Below is where the AI starts, it works by picking the move with the smallest difference between X and O victories
		print(printBoard(game1.gameBoard))
		if game1.gameOver is False and game1.gameBoard.count(' ')>0:
			maxWinO=0
			minWinX=1000000
			minDiff=3000
			newMove=game1.childMoves[0]
			for child in game1.childMoves:
				print("X:"+str(child.winnerChildX)+" O:"+str(child.winnerChildO)+" Diff:"+str(abs(child.winnerChildX-child.winnerChildO)))
			for child in game1.childMoves:
				#print("X:"+str(child.winnerChildX)+" O:"+str(child.winnerChildO))
				if child.winnerChildX==0 and child.winnerChildO>0:
					newMove=child
					print("a")
					break
				#The diff cannot be equal to 196 because on the first move the lowest diff can be this when X goes on 1,3,5,7 and
				# the AI response was to pic a corner which would allow an X win in 2 moves
				elif abs(child.winnerChildX-child.winnerChildO)<minDiff and abs(child.winnerChildX-child.winnerChildO)!=196:
					tempMinDiff=minDiff
					tempNewMove=newMove
					for cPrime in child.childMoves:
						if cPrime.gameOver and cPrime.winner=='X':
							minDiff=tempMinDiff
							newMove=tempNewMove
							print("b")
							break
						elif child is not None:
							minDiff=abs(child.winnerChildX-child.winnerChildO)
							newMove=child
				#Use this code to make a competitive but beatable AI
				"""
				elif child.winnerChildX<minWinX:
					tempMinWinX=minWinX
					tempNewMove=newMove
					for cPrime in child.childMoves:
						if cPrime.gameOver and cPrime.winner=='X':
							minWinX=tempMinWinX
							newMove=tempNewMove
							print("c")
							break
						elif child is not None:
							minWinX=child.winnerChildX
							newMove=child
				"""
			game1 = newMove

print("\n\n\n\n\n"+printBoard(game1.gameBoard))
print("Game Over!")
if game1.gameOver:
	print(game1.winner+" Won!")
else:
	print("Game is a draw.")
