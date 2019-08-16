#import numpy as np
#import compiler
import sympy as sp

def testEquationCalculator(equation):

	#saves unaltered form of equation
	originalEquation = equation	

	#iterates through and replaces special characters with their
	#mathematical equivalents for performing the necessary computation
	counter = len(equation)
	i = 0
	while counter > 0:
		if equation[i] == "^":
			equation = equation[0:i] + "**" + equation[i+1:len(equation)]
			counter += 1
		elif equation[i] == "{":
			equation = equation[0:i] + "(" + equation[i+1:len(equation)]		
		elif equation[i] == "}":
			equation = equation[0:i] + ")" + equation[i+1:len(equation)]		

		counter -= 1
		i += 1
	
	#attempts to evaluate the expression and throws an 
	#error message if eval() is unable to compute it
	returnString = ""
	try:
		returnString = "$" + originalEquation + " = " + str(eval(equation)) + "$"
	except:
		returnString = "Error, unable to process the following  equation: $" + originalEquation + "$"
	
	return returnString

def solveForVariable(equation):
	#converts equation to the format required by sympy
	formattedEquation = formatInput(equation)

	#extracts the individual mathematical terms in the equation	
	terms = parseTerms(formattedEquation)

	equalityOperator = "="

	#determines if there is an equals sign in the entered
	#equation and adjusts format for sympy solver	
	for i in range(0,len(formattedEquation)):
		if formattedEquation[i] == "=" or formattedEquation[i] == "≤" or formattedEquation[i] == "≥":
			equalityOperator = formattedEquation[i]
			formattedEquation = formattedEquation[0:i] + "-(" + formattedEquation[i+1:len(formattedEquation)] + ")"
			i = len(formattedEquation)
	
	#extracts the variables entered in and converts them into
	#sympy symbols so computation can be performed
	variables = getVariables(formattedEquation)
	for v in variables:
		sp.var(v)

	#attempts to solve equation and produces an error if unable to	
	returnString = ""
	try:
		result = sp.solve(formattedEquation, x)
		
		#iterates through the returned list to format
		#the list of values as a solution set
		returnString = "x " + equalityOperator + " "
		for answer in result:
			returnString += str(answer) + ", "
		returnString = returnString[0:len(returnString)-2]
		returnString = formatLaTex(returnString)
	except:
		returnString = equation + " No solution"
	
	return returnString

def standardDerivative(equation, variable):
	formattedEquation = formatInput(equation)
	equalsLocation = -1

	#converts the variable being differentiated to a sympy symbol	
	sp.var(variable)
	variable = sp.Symbol(variable)	

	#determines if there was an equals sign in the entered equation
	for i in range(0, len(formattedEquation)):
		if formattedEquation[i] == "=":
			equalsLocation = i
	try:
		#if there is an equals sign, evaluates the derivatives
		#of both sides individually and then rejoins them after
		if equalsLocation != -1:
			temp1 = formattedEquation[0:equalsLocation]
			temp2 = formattedEquation[equalsLocation+1:len(formattedEquation)]
			temp1 = str(sp.diff(temp1, variable))
			temp2 = str(sp.diff(temp2, variable))
			returnString = temp1 + "=" + temp2
			returnString = formatLaTex(returnString)
		else:
			returnString = str(sp.diff(formattedEquation, variable))
			returnString = formatLaTex(returnString)

		#iterates result and simplifies log(e) to 1
		found = returnString.find("log(e)")
		while found != -1:
			returnString = returnString[0:found] + returnString[found+6:len(returnString)]
			found = returnString.find("log(e)")
	except:
		returnString = "Unable to take derivative of: " + formatLaTex(formattedEquation)
	
	return returnString

def indefiniteIntegral(equation, variable):
	formattedEquation = formatInput(equation)
	equalsLocation = -1

	#converts the variable being integrated to a sympy symbol	
	sp.var(variable)
	variable = sp.Symbol(variable)	

	#determines if there was an equals sign in the entered equation
	for i in range(0, len(formattedEquation)):
		if formattedEquation[i] == "=":
			equalsLocation = i
	
	try:
		#if there is an equals sign, evaluates the integral
		#of both sides individually and then rejoins them after
		if equalsLocation != -1:
			temp1 = formattedEquation[0:equalsLocation]
			temp2 = formattedEquation[equalsLocation+1:len(formattedEquation)]
			temp1 = str(sp.integrate(temp1, variable))
			temp2 = str(sp.integrate(temp2, variable))
			returnString = temp1 + "=" + temp2
			returnString = formatLaTex(returnString)
		else:
			returnString = str(sp.integrate(formattedEquation, variable))
			returnString = formatLaTex(returnString) + "$ + C$"

		#iterates result and simplifies log(e) to 1
		found = returnString.find("log(e)")
		while found != -1:
			returnString = returnString[0:found] + returnString[found+6:len(returnString)]
			found = returnString.find("log(e)")
	except:
		returnString = "Unable to take integral of: " + formatLaTex(formattedEquation)
	
	return returnString

def definiteIntegral(equation, variable):
	formattedEquation = formatInput(equation)
	equalsLocation = -1
	
	#parses data from form fields	
	index = variable.find("?")
	higherIndex = variable.find("?", index+1)
	lowerLimit = variable[index+1:higherIndex]
	upperLimit = variable[higherIndex+1:len(variable)]
	variable = variable[0:index]


	sp.var(variable)
	variable = sp.Symbol(variable)	

	for i in range(0, len(formattedEquation)):
		if formattedEquation[i] == "=":
			equalsLocation = i

	#takes definite integral of the entered equation
	try:
		if equalsLocation != -1:
			temp1 = formattedEquation[0:equalsLocation]
			temp2 = formattedEquation[equalsLocation+1:len(formattedEquation)]
			temp1 = str(sp.integrate(temp1, (variable,upperLimit, lowerLimit)))
			temp2 = str(sp.integrate(temp2, (variable,upperLimit, lowerLimit)))
			returnString = temp1 + "=" + temp2
			returnString = formatLaTex(returnString)
		else:
			returnString = str(sp.integrate(formattedEquation, (variable, upperLimit, lowerLimit)))
			returnString = formatLaTex(returnString)

		found = returnString.find("log(e)")
		while found != -1:
			returnString = returnString[0:found] + returnString[found+6:len(returnString)]
			found = returnString.find("log(e)")
	except:
		returnString = "Unable to take integral of: " + formatLaTex(formattedEquation)
	
	return returnString


def ODESolver(equation, variable):
	formattedEquation = formatInput(equation)
	equalsLocation = -1

	#sets up sympy function used as a wrapper for the entered variable	
	f = sp.Function("f")	

	#converts the variable to f(variable) to fir sympy formatting
	index = formattedEquation.find(variable)
	while index != -1:
		formattedEquation = formattedEquation[0:index] + "f(" + variable + ")"  + formattedEquation[index+1:len(formattedEquation)]
		index = formattedEquation.find(variable, index + 3)
		

	#converts derivative apostrophes to the sympy diff() function
	index = formattedEquation.find("\'\'")
	while index != -1:
		formattedEquation = formattedEquation[0:index] + ".diff(" + variable + ",2)"  + formattedEquation[index+2:len(formattedEquation)]
		index = formattedEquation.find("\'\'", index + 1)
	
	index = formattedEquation.find("\'")
	while index != -1:
		formattedEquation = formattedEquation[0:index] + ".diff()"  + formattedEquation[index+1:len(formattedEquation)]
		index = formattedEquation.find("\'", index + 1)


	#converts entered variables to sympy symbols	
	variables = getVariables(formattedEquation)
	for v in variables:
		sp.var(v)
	
	sp.var(variable)
	variable = sp.sympify("f(" + variable + ")")	
		
	for i in range(0, len(formattedEquation)):
		if formattedEquation[i] == "=":
			equalsLocation = i
	
	#attempts to solve ODE equation
	try:
		if equalsLocation != -1:
			temp1 = formattedEquation[0:equalsLocation]
			temp2 = formattedEquation[equalsLocation+1:len(formattedEquation)]
			temp1 = str(sp.dsolve(temp1, variable))
			temp2 = str(sp.dsolve(temp2, variable))
			returnString = temp1 + "=" + temp2
			returnString = formatLaTex(returnString)
		else:
			formattedEquation = sp.sympify(formattedEquation)
			returnString = str(sp.dsolve(formattedEquation, variable))
			returnString = formatLaTex(returnString)

		found = returnString.find("log(e)")
		while found != -1:
			returnString = returnString[0:found] + returnString[found+6:len(returnString)]
			found = returnString.find("log(e)")

	
		#converts from sympy format to more intuitive format	
		index = returnString.find(",")
		if index != -1:
			returnString = str(variable) + " = " + returnString[index+2:len(returnString)-2]

		index = returnString.find("exp")
		while index != -1:
			returnString = returnString[0:index] + "e^" + returnString[index+3:len(returnString)]
			if returnString[index+2] == "(":
				index += 2
				returnString = returnString[0:index] + "{" + returnString[index+1:len(returnString)]
				numRightParenthesis = 1
				oldPosition = index
				while numRightParenthesis > 0:
					index += 1
					if returnString[index] == ")":
						numRightParenthesis -= 1
					elif returnString[index] == "(":
						numRightParenthesis += 1
				returnString = returnString[0:index] + "}" + returnString[index+1:len(returnString)]
			index = returnString.find("exp", index)
				
		returnString = formatLaTex(str(returnString))
			
	except:
		returnString = "Unable to find the solution of: " + formatLaTex(equation)
	
	return returnString


#iterates through string and returns a list 
#of the unique characters it contains
def getVariables(equation):
	variables = []
	for x in equation:
		tracked = False
		for v in variables:
			if x == v:
				tracked = True
		if not tracked and x.isalpha():
			variables.append(x)
	
	return variables

#converts symbols in input to the symbols need for
#calculating the corresponding function in sympy
def formatInput(equation):
	counter = len(equation)
	i = 0
	while counter > 0:
		if (equation[i].isdigit() and equation[i+1].isalpha()):
			equation = equation[0:i+1] + "*" + equation[i+1:len(equation)]
			counter += 1
		elif equation[i] == "^":
			equation = equation[0:i] + "**" + equation[i+1:len(equation)]
			counter += 1
		elif equation[i] == "{":
			equation = equation[0:i] + "(" + equation[i+1:len(equation)]		
		elif equation[i] == "}":
			equation = equation[0:i] + ")" + equation[i+1:len(equation)]		
		elif equation[i] == "π":
			checked = False
			if i != 0:
				if equation[i-1].isalpha() or equation[i-1].isdigit():
					equation = equation[0:i] + "*pi" + equation[i+1:len(equation)]		
					checked = True
					counter += 1
			if not checked:
				if equation[i+1].isalpha():
					equation = equation[0:i] + "pi*" + equation[i+1:len(equation)]		
					counter += 1	
				else:
					equation = equation[0:i] + "pi" + equation[i+1:len(equation)]		
			counter += 1
		
		counter -= 1
		i += 1
		if i == len(equation)-1:
			if equation[i] == "}":
				equation = equation[0:i] + ")"
			counter = 0

	return equation


#iterates through input and extracts the individual terms
#in the equation i.e. operators, numbers, variables, etc
def parseTerms(equation):
	terms = []
	currentTerm = ""
	for i in range(0,len(equation)):
		if isOperator(equation[i]):
			if currentTerm == "":
				terms.append(equation[i])
			else:
				terms.append(currentTerm)
				terms.append(equation[i])
			currentTerm = ""
		else:
			currentTerm += equation[i]
	
	if currentTerm != "":
		terms.append(currentTerm)

	return terms

#determines if a character is an operator
def isOperator(character):
	if not character.isdigit() and not character.isalpha():
		return True

	return False

#formats the output from sympy into an easier to read
#format for rendering using LaTex onm the destination page
def formatLaTex(equation):
	terms = parseTerms(equation)
	for i in range(0,len(terms)):
		if terms[i] == "sqrt":
			terms[i] = "\sqrt"
			i += 1
			terms[i] = "{"
			numRightParenthesis = 1
			oldPosition = i
			while numRightParenthesis > 0:
				i += 1
				if terms[i] == ")":
					numRightParenthesis -= 1
				elif terms[i] == "(":
					numRightParenthesis += 1
			terms[i] = "}"
			i = oldPosition
		elif terms[i] == "I":
			terms[i] = "i"
		elif terms[i] == "pi":
			terms[i] = "{\pi}"
		elif terms[i] == "*":
			if terms[i+1] == "*":
				numRightParenthesis = 1 if terms[i+2] == "(" else 0
				terms[i] = "^"
				terms[i+1] = "{"
				if numRightParenthesis == 1:
					terms[i+2] = ""
				i += 2
				oldPosition = i
				while numRightParenthesis > 0:
					i += 1
					if terms[i] == ")":
						numRightParenthesis -= 1
					elif terms[i] == "(":
						numRightParenthesis += 1
				if i == oldPosition:
					terms.insert(i+1,"}")
				else:
					terms[i] = "}"
					i = oldPosition
			elif terms[i + 1].isalpha():
				terms[i] = ""


	returnString = "".join(terms)	
	return "$" + returnString + "$"


def matrix_multiplication(equation):

	#parses the terms from the form fields
	equationParts = equation.split("|") 	

	
	matrixOneString = equationParts[0]
	matrixTwoString = equationParts[1]
	numOneRows = int(equationParts[2])
	numOneCols = int(equationParts[3])
	numTwoRows = int(equationParts[4])
	numTwoCols = int(equationParts[5])

	#multiplcation cannot be performed if not in format n x m * m x k
	if numOneCols != numTwoRows:
		return "Error, the number of columns in matrix 1 must equal the number of rows in matrx 2"

	#converts string of comma seperated values into a 2d matrix
	matrixOne = convertStringToMatrix(matrixOneString, numOneRows, numOneCols)
	matrixTwo = convertStringToMatrix(matrixTwoString, numTwoRows, numTwoCols)

	#converts to sympy matrices	
	matrixOne = sp.Matrix(matrixOne)
	matrixTwo = sp.Matrix(matrixTwo)

	#attempts matrix multiplcation and then converts 
	#sympy matrix result into a matrix in LaTex format
	returnString = ""	
	try:
		resultMatrix = matrixOne*matrixTwo
		resultMatrix = resultMatrix.tolist()

		returnString = "$\\left[\\begin{matrix}"
		for i in range(0,len(resultMatrix)):
			for j in range(0,len(resultMatrix[i])):
				if j == len(resultMatrix[i]) - 1:
					returnString += str(resultMatrix[i][j])
				else:	
					returnString += str(resultMatrix[i][j]) + " &"
			returnString += "\\"
			returnString += "\\"
		returnString += "\\end{matrix}\\right]$"
	except:
		returnString = "Error, unable to perform matrix multiplication"

	return returnString

def matrix_addition(equation):
	
	#parses terms from form fields
	equationParts = equation.split("|")

	matrixOneString = equationParts[0]
	matrixTwoString = equationParts[1]
	numRows = int(equationParts[2])
	numCols = int(equationParts[3])
	operation = equationParts[4]

	#converts string of values to matrices
	matrixOne = convertStringToMatrix(matrixOneString, numRows, numCols)
	matrixTwo = convertStringToMatrix(matrixTwoString, numRows, numCols)

	#performs matrix addition or subtraction by 
	#adding/subtracting the value at every coordinate
	#with the value at that same coordinates in the other matrix	
	resultMatrix = []
	if operation == "+":
		for i in range(0,numRows):
			temp = []
			for j in range(0,numCols):
				temp.append(eval(matrixOne[i][j]+"+"+matrixTwo[i][j]))
			resultMatrix.append(temp)
	else:
		for i in range(0,numRows):
			temp = []
			for j in range(0,numCols):
				temp.append(eval(matrixOne[i][j]+ "-" + matrixTwo[i][j]))
			resultMatrix.append(temp)
	
	#convert sympy matrix to LaTex formatted matrix
	returnString = "$\\left[\\begin{matrix}"
	for i in range(0,len(resultMatrix)):
		for j in range(0,len(resultMatrix[i])):
			if j == len(resultMatrix[i]) - 1:
				returnString += str(resultMatrix[i][j])
			else:	
				returnString += str(resultMatrix[i][j]) + " &"
		returnString += "\\"
		returnString += "\\"
	returnString += "\\end{matrix}\\right]$"
	
	return returnString

#uses entered row and column length to convert a list of 
#comma seperated values into the corresponding 2d matrix
def convertStringToMatrix(field, numRows, numCols):
	matrix = []
	index = 0
	for i in range(0,numRows):
		temp = []
		for j in range(0,numCols):
			nextIndex = field.find(",",index)
			if nextIndex == -1:
				nextIndex = len(field)
			temp.append(field[index:nextIndex])
			index = nextIndex + 1
		matrix.append(temp)
	
	return matrix


def solveSystemOfEquations(equation):
	#seperates the equations into a list
	equations = equation.split("|")

	#extracts variables from the entered equation 
	#and converts them into sympy symbols
	variables = getVariables(equation)
	for i in range(0, len(variables)):
		sp.var(variables[i])
		variables[i] = sp.sympify(variables[i])	

	#finds location of equality operator if present and converts
	#equation to the form required for the sympy solver		
	for i in range(0, len(equations)):
		equations[i] = formatInput(equations[i])
		for j in range(0,len(equations[i])):
			if equations[i][j] == "=" or equations[i][j] == "≤" or equations[i][j] == "≥":
				equations[i] = equations[i][0:j] + "-(" + equations[i][j+1:len(equations[i])] + ")"
				j = len(equations[i])
		equations[i] = sp.sympify(equations[i])


	#solves system of equations 
	returnString = ""
	try:
		result = sp.linsolve(equations, variables)
		
		if type(result).__name__ == "EmptySet":
			returnString = "No solution"
		else:
			result = list(list(result)[0])
			for i in range(0, len(variables)):
				returnString += str(variables[i]) + " = " + str(result[i]) + ", "
			returnString = returnString[0:len(returnString)-2]
		
	except:
		returnString = "Error, unable to evaluate system of equations"

	return returnString


def matrix_RREF(equation):
	#parses terms from form fields
	equations = equation.split("|")
	matrixString = equations[0]
	numRows = int(equations[1])
	numCols = int(equations[2])

	matrix = convertStringToMatrix(matrixString, numRows, numCols)
	matrix = sp.Matrix(matrix)

	#performs row reduction algorithm and returns LaTex formatted matrix
	returnString = ""
	try:
		matrix = matrix.rref()
		resultMatrix = list(matrix)[0].tolist()
		returnString = "$\\left[\\begin{matrix}"
		for i in range(0,len(resultMatrix)):
			for j in range(0,len(resultMatrix[i])):
				if j == len(resultMatrix[i]) - 1:
					returnString += str(resultMatrix[i][j])
				else:	
					returnString += str(resultMatrix[i][j]) + " &"
			returnString += "\\"
			returnString += "\\"
		returnString += "\\end{matrix}\\right]$"
	except:
		returnString = "Error, unable to put in RREF form"


	return returnString

def matrix_determinant(equation):
	#parses terms from form fields
	equations = equation.split("|")
	matrixString = equations[0]
	numRows = int(equations[1])
	numCols = int(equations[2])
	
	matrix = convertStringToMatrix(matrixString, numRows, numCols)
	matrix = sp.Matrix(matrix)

	#computes determinant of matrix and returns value
	returnString = ""
	try:
		returnString = matrix.det()
	except:
		returnString = "Error, unable to take determinant"

	return returnString


def matrix_transpose(equation):
	#parses terms from form fields
	equations = equation.split("|")
	matrixString = equations[0]
	numRows = int(equations[1])
	numCols = int(equations[2])
	
	matrix = convertStringToMatrix(matrixString, numRows, numCols)
	matrix = sp.Matrix(matrix)

	#finds transpose of entered matrix and returns the LaTex formatted matrix
	returnString = ""
	try:
		matrix = matrix.T
		
		resultMatrix = matrix.tolist()
		returnString = "$\\left[\\begin{matrix}"
		for i in range(0,len(resultMatrix)):
			for j in range(0,len(resultMatrix[i])):
				if j == len(resultMatrix[i]) - 1:
					returnString += str(resultMatrix[i][j])
				else:	
					returnString += str(resultMatrix[i][j]) + " &"
			returnString += "\\"
			returnString += "\\"
		returnString += "\\end{matrix}\\right]$"
	except:
		returnString = "Error, unable to transpose"


	return returnString


def matrix_inverse(equation):
	#parses terms from form fields
	equations = equation.split("|")
	matrixString = equations[0]
	numRows = int(equations[1])
	numCols = int(equations[2])
	
	matrix = convertStringToMatrix(matrixString, numRows, numCols)
	matrix = sp.Matrix(matrix)

	#fnids inverse of matrix and returns LaTex formatted matrix
	returnString = ""
	try:
		matrix = matrix**-1
		
		resultMatrix = matrix.tolist()
		
		returnString = "$\\left[\\begin{matrix}"
		for i in range(0,len(resultMatrix)):
			for j in range(0,len(resultMatrix[i])):
				if j == len(resultMatrix[i]) - 1:
					returnString += str(resultMatrix[i][j])
				else:	
					returnString += str(resultMatrix[i][j]) + " &"
			returnString += "\\"
			returnString += "\\"
		returnString += "\\end{matrix}\\right]$"
	except:
		returnString = "Error, matrix is not invertible"


	return returnString


def matrix_eigenvalues(equation):
	#parses terms from form fields
	equations = equation.split("|")
	matrixString = equations[0]
	numRows = int(equations[1])
	numCols = int(equations[2])

	matrix = convertStringToMatrix(matrixString, numRows, numCols)
	matrix = sp.Matrix(matrix)

	#determines eigenvalues of matrix and 
	#returns them as a comma seperated list
	returnString = ""
	try:
		result = matrix.eigenvals()
		returnString = "$\lambda = "
		#key is th eigenvalue, value is multiplicity
		for value in result:
			returnString += str(value) + ", "
		returnString = returnString[0:len(returnString)-2] + "$"
	except:
		returnString = "Error, unable to find eigenvalues"


	return returnString
