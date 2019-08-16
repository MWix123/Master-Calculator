
movement = false;
cursorCurrentParent = "equation-input";

function initAlt(id){
	var dropdowns = document.getElementsByClassName("dropdown");
	for(var i = 0; i < dropdowns.length; i++){
		dropdowns[i].onclick = function(){
			if(this.style.transform == "rotate(90deg)"){
				this.style.transform = "rotate(0deg)";
				this.nextElementSibling.nextElementSibling.style.display = "none";
			}else{
				this.style.transform = "rotate(90deg)";
				this.nextElementSibling.nextElementSibling.style.display = "block";
			}
		}
	}

	var menu = document.getElementById(id);
	menu.style.color = "#fff000";
	menu.previousElementSibling.style.transform = "rotate(90deg)";
	menu.nextElementSibling.style.display = "block";
}

function init(){
	var dropdowns = document.getElementsByClassName("dropdown");
	for(var i = 0; i < dropdowns.length; i++){
		dropdowns[i].onclick = function(){
			if(this.style.transform == "rotate(90deg)"){
				this.style.transform = "rotate(0deg)";
				this.nextElementSibling.nextElementSibling.style.display = "none";
			}else{
				this.style.transform = "rotate(90deg)";
				this.nextElementSibling.nextElementSibling.style.display = "block";
			}
		}
	}

	cursorCurrentParent = "equation-input";

	var input = document.getElementById("equation-input");
	var textarea = document.getElementById("id_textarea");
	var cursor = document.getElementById("cursor");

	textarea.innerHTML = "";

	input.addEventListener("keypress", function(event){
		
		cursor = document.getElementById("cursor");

		var character = String.fromCharCode(event.keyCode);
		
		var newNode = document.createElement("div");
		var newContent = document.createTextNode(character);
		if(event.keyCode == 94){
			newInnerNode = document.createElement("div");
			newInnerNode.className = "input-item";
			newNode.className = "sup";
			newNode.id = "sup-" + cursor.className;
			newNode.appendChild(newInnerNode);
			character = "^{}";
		}else{
			newNode.className = "input-item";
			newNode.appendChild(newContent);
		}


		insertAtCursor(newNode, character);

		textarea = document.getElementById("id_textarea");

		textarea.focus();

		
	});

	input.addEventListener("keydown", function(event){
		cursor = document.getElementById("cursor");
		var classNum = Number(cursor.className);
		var prevNum = classNum;
		movement = false; //used to handle case where non-arrow key is entered
		
		switch(event.keyCode){
			case 37: //left arrow key
				if(classNum > 1 || cursorCurrentParent != "equation-input"){
					classNum -= 1;
					cursor.className = classNum;
					classNum = -classNum;
					movement = true;
				}
				break;
			case 39: //right arrow key
				if(classNum < input.children.length-1 || cursorCurrentParent != "equation-input"){
					classNum += 1;
					cursor.className = classNum;
					movement = true;
				}
				break;
			case 8: //backspace key
				classNum = removeItem(classNum);
				break;
			default:
				break;
		}

		if(classNum != prevNum && movement){
			moveCursor(classNum);
		}
	});

	setInterval(function(){
		cursor = document.getElementById("cursor");
		if(cursor.style.opacity == 0){
			cursor.style.opacity = 1;
		}else{
			cursor.style.opacity = 0;
		}
	}, 530);
}

function moveCursor(position){

	newId = false;

	moveBack = false;
	if(position < 0){
		position *= -1;
		moveBack = true;
	}

	var input = document.getElementById(cursorCurrentParent);

	var inputItems = input.children;

	if(cursorCurrentParent.substring(0,3) == "num" && position >= inputItems.length){
		cursorCurrentParent = "den-" + cursorCurrentParent.substring(4,cursorCurrentParent.length);
		
		newInputItems = document.getElementById(cursorCurrentParent).parentElement.children[1];
		newPosition = 1;
		cursorPosition = (position < 1) ? 1 : inputItems.length - 1;

		newInputItems.insertBefore(inputItems[cursorPosition], newInputItems.children[newPosition]);
		var cursor = document.getElementById("cursor");
		cursor.className = newPosition;		

	}else if(cursorCurrentParent.substring(0,3) == "den" && position < 1){
		cursorCurrentParent = "num-" + cursorCurrentParent.substring(4,cursorCurrentParent.length);

		newInputItems = document.getElementById(cursorCurrentParent).parentElement.children[0];
		newPosition = newInputItems.children.length;
		cursorPosition = 1;

		newInputItems.appendChild(inputItems[cursorPosition]);
		var cursor = document.getElementById("cursor");
		cursor.className = newPosition;		

	}else if(position < 1 || position >= inputItems.length){
		cursorCurrentParent = "equation-input";
		newInputItems = document.getElementById(cursorCurrentParent);
		newPosition = Number(input.id.substring(4,input.id.length));

		newPosition = (position < 1) ? newPosition : newPosition+1;
		cursorPosition = (position < 1) ? 1 : inputItems.length - 1;

		if(input.className == "sup"){
			input.style.border = "none";
		}

		newInputItems.insertBefore(inputItems[cursorPosition], newInputItems.children[newPosition]);
		
		var cursor = document.getElementById("cursor");
		cursor.className = newPosition;
		return "";
	}


	for(var i = 1; i < inputItems.length; i++){	
		changeAmount = (moveBack) ? -1 : 1;
		if(inputItems[i].className == position && inputItems[i + changeAmount].className == "sup"){ //exponentials
			inputItems[i].className = (!moveBack) ? "1" : inputItems[i+changeAmount].children.length;
			
			if(moveBack){
				inputItems[i+changeAmount].appendChild(inputItems[i]);
			}else{
				if(inputItems[i+changeAmount].children.length <= 1){
					inputItems[i+changeAmount].appendChild(inputItems[i]);
				}else{
					inputItems[i+changeAmount].insertBefore(inputItems[i], inputItems[i+changeAmount].children[1]);
				}
				
			}
			
			smallOffset = (moveBack) ? -1 : 0;

			cursorCurrentParent = inputItems[i+smallOffset].id;
			inputItems[i+smallOffset].style.border = "2px solid darkgreen";

			newId = true;

			i = inputItems.length;
		}else if(inputItems[i].className == position && inputItems[i + changeAmount].className == "fraction"){ //fraction
			
			numChild = (!moveBack) ? 0 : 1;
			inputItems[i].className = (!moveBack) ? "1" : inputItems[i+changeAmount].children[numChild].children.length;

			if(moveBack){
				inputItems[i+changeAmount].children[numChild].appendChild(inputItems[i]);
			}else{
				if(inputItems[i+changeAmount].children[numChild].children.length <= 1){
					inputItems[i+changeAmount].children[numChild].appendChild(inputItems[i]);
				}else{
					inputItems[i+changeAmount].children[numChild].insertBefore(inputItems[i], inputItems[i+changeAmount].children[numChild].children[1]);
				}
			}

			smallOffset = (moveBack) ? -1 : 0;

			cursorCurrentParent = inputItems[i+smallOffset].children[numChild].id;
			
			newId = true;

			i = inputItems.length;
		}else if(inputItems[i].className == position){
			
			var tempContent = inputItems[i].innerHTML;
			
			changeAmount = (moveBack) ? -1 : 1;
			
			inputItems[i].innerHTML = inputItems[i + changeAmount].innerHTML;
			inputItems[i].className = inputItems[i + changeAmount].className;
			
			inputItems[i].id = "";
			inputItems[i].style.opacity = 1;
			
			inputItems[i + changeAmount].innerHTML = tempContent;
			inputItems[i+changeAmount].className = position;
			inputItems[i+changeAmount].id = "cursor";

			i = inputItems.length;
		}
	}

	return "";
}

function removeItem(position){
	var input = document.getElementById(cursorCurrentParent);
	var inputItems = input.children;

	if(position == 1){
		return position;
	}

	for(var i = 1; i < inputItems.length; i++){
		if(inputItems[i].className == position){
			input.removeChild(inputItems[i-1]);

			inputItems[i-1].className = i-1;
			position = i-1;

			if(i < inputItems.length){
				if(inputItems[i].className == "sup"){
					inputItems[i].id = "sup-" + (i-1);
				}else if(inputItems[i].className == "fraction"){
					inputItems[i].id = "frac-" + (i-1);
					inputItems[i].children[0].id = "num-" + (i-1);
					inputItems[i].children[1].id = "den-" + (i-1);
				}
			}

			interpretEquation();
			
			return position;
		}
	}

	return 1; //should never be reached
}

function shiftContainers(position, direction){
	var inputItems = document.getElementById("equation-input").children;

	for(var i = position; i < inputItems.length; i++){
		if(inputItems[i].className == "sup"){
			newPosition = Number(inputItems[i].id.substring(4,inputItems[i].id.length));
			newPosition += direction;
			inputItems[i].id = "sup-" + newPosition;
		}else if(inputItems[i].className == "fraction"){
			newPosition = Number(inputItems[i].id.substring(5,inputItems[i].id.length));
			newPosition += direction;
			inputItems[i].id = "frac-" + newPosition;
			inputItems[i].children[0].id = "num-" + newPosition;
			inputItems[i].children[1].id = "den-" + newPosition;
		}
	}
}


function validateDerivativeVariable(term){
	var variable = document.getElementById('derivative-variable');
	if(!variable.value.substring(variable.value.length-1,variable.value.length).match(/[A-Za-z]/i)){
		variable.value = variable.value.substring(0,variable.value.length-1);
		variable.className = "error";
		document.getElementById("derivative-error").innerHTML = "You may only enter a variable.";
	}else if(variable.value.length > 1){
		variable.value = variable.value.substring(0,1);
		variable.className = "error";
		document.getElementById("derivative-error").innerHTML = "You may only choose one variable to take the " + term + " of.";
	}else{
		document.getElementById("derivative-error").innerHTML = "";
		variable.className = "";
	}

	if(term == "definite integral"){
		document.getElementById("id_text").innerHTML = variable.value + "?" + document.getElementById("upper-limit").value + "?" + document.getElementById("lower-limit").value;
	}else{
		document.getElementById("id_text").innerHTML = variable.value;
	}
}

function updateRows(elem){
	var matrixOne = document.getElementById("matrix-1").children[0];
	if(elem.id != "num-rows-1" && elem.id != "num-cols-1"){
		var matrixTwo = document.getElementById("matrix-2").children[0];
	}

	if(isNaN(elem.value[elem.value.length-1])){
		elem.value = elem.value.substring(0, elem.value.length-1);
		return;
	}
	
	//only allows numbers in the range 1 <= x <= 5
	if(Number(elem.value) > 5){
		elem.value = 5;
	}else if(Number(elem.value) < 1){
		elem.value = 1;
	}

	if(elem.id == "num-rows" || elem.id == "num-rows-1" || elem.id == "num-rows-2"){
		numRows = Number(elem.value);

		if(elem.id == "num-rows" || elem.id == "num-rows-1"){
			deltaRows = matrixOne.children.length - numRows;
		}else{
			deltaRows = matrixTwo.children.length - numRows;
		}
		if(deltaRows > 0){
			while(deltaRows > 0){
				if(elem.id == "num-rows" || elem.id == "num-rows-1"){
					matrixOne.removeChild(matrixOne.children[matrixOne.children.length-1]);
					matrixOne = document.getElementById("matrix-1").children[0];
				}

				if(elem.id == "num-rows" || elem.id == "num-rows-2"){
					matrixTwo.removeChild(matrixTwo.children[matrixTwo.children.length-1]);
					matrixTwo = document.getElementById("matrix-2").children[0];
				}

				deltaRows--;
			}
		}else if(deltaRows < 0){
			insideText = "";
			matrixLength = (elem.id == "num-rows-2") ? matrixTwo.children[0].children.length : matrixOne.children[0].children.length;
			for(var i = 0; i < matrixLength; i++){
				insideText += "<td class='column'><textarea></textarea></td>";
			}
			while(deltaRows < 0){

				if(elem.id == "num-rows" || elem.id == "num-rows-1"){
					newNode = document.createElement("tr");
					newNode.className = "row";
					newNode.innerHTML = insideText;
					matrixOne.appendChild(newNode);
				}


				if(elem.id == "num-rows" || elem.id == "num-rows-2"){
					newNode = document.createElement("tr");
					newNode.className = "row";
					newNode.innerHTML = insideText;
					matrixTwo.appendChild(newNode);
				}
				deltaRows++;
			}
		}
	}else{
		numCols = Number(elem.value);
		deltaCols = (elem.id == "num-cols-2") ? matrixTwo.children[0].children.length - numCols : matrixOne.children[0].children.length - numCols;
		
		matrixLength = (elem.id == "num-cols-2") ? matrixTwo.children.length : matrixOne.children.length;
		if(deltaCols > 0){
			for(var i = 0; i < matrixLength; i++){
				temp = deltaCols;
				while(temp > 0){

					if(elem.id == "num-cols" || elem.id == "num-cols-1"){
						matrixOne.children[i].removeChild(matrixOne.children[i].children[matrixOne.children[i].children.length-1]);
					}

					if(elem.id == "num-cols" || elem.id == "num-cols-2"){
						matrixTwo.children[i].removeChild(matrixTwo.children[i].children[matrixTwo.children[i].children.length-1]);
					}
					temp--;
				}
			}

		}else if(deltaCols < 0){
			insideText = ""
			while(deltaCols < 0){
				insideText += "<td class='column'><textarea></textarea></td>";
				deltaCols++;
			}
			
			for(var i = 0; i < matrixLength; i++){
				if(elem.id == "num-cols" || elem.id == "num-cols-1"){
					matrixOne.children[i].innerHTML += insideText;
				}

				if(elem.id == "num-cols" || elem.id == "num-cols-2"){
					matrixTwo.children[i].innerHTML += insideText;
				}
			}
		}
	}
}

function updateBothMatrices(operation){

	var matrixOne = document.getElementById("matrix-1").children[0];
	a = copyFieldsToMatrix(matrixOne);

	if(operation == "addition" || operation == "multiplication"){
		var matrixTwo = document.getElementById("matrix-2").children[0];
		b = copyFieldsToMatrix(matrixTwo);
	}

	var textarea = document.getElementById("id_textarea");


	if(operation == "addition"){
		var sign = document.getElementById("matrix-operation");
		textarea.innerHTML = a + "|" + b + "|" + matrixOne.children.length + "|" +
		matrixOne.children[0].children.length + "|" + sign.value;
	}else if(operation == "multiplication"){
		textarea.innerHTML = a + "|" + b + "|" + matrixOne.children.length + "|" +
		matrixOne.children[0].children.length + "|" + matrixTwo.children.length + "|" + matrixTwo.children[0].children.length;
	}else{
		textarea.innerHTML = a + "|" + matrixOne.children.length + "|" +
		matrixOne.children[0].children.length;
	}
	

}

function copyFieldsToMatrix(matrix){
	copyMatrix = [];
	for(var i = 0; i < matrix.children.length; i++){
		temp = [];
		for(var j = 0; j < matrix.children[i].children.length; j++){
			value = matrix.children[i].children[j].children[0].value;
			if(value == ""){
				temp.push(0);
			}else{
				valid = true;
				for(var k = 0; k < value.length; k++){
					if(isNaN(value[k]) && value[k] != "/" && value[k] != "." &&
						 value[k] != "-" && value[k] != "*" && value[k] != "(" && value[k] != ")"){
						valid = false;
					}
				}
				if(valid){
					temp.push(value);
				}else{
					temp.push(0);
				}
			}
		}
		copyMatrix.push(temp);
	}
	return copyMatrix;
}

function updateLimits(){
	document.getElementById("id_text").innerHTML = document.getElementById("derivative-variable").value + "?" + document.getElementById("upper-limit").value + "?" + document.getElementById("lower-limit").value;
}

function updateNumSystems(elem){
	if(isNaN(elem.value[elem.value.length-1])){
		elem.value = elem.value.substring(0, elem.value.length-1);
		return;
	}
	
	//only allows numbers in the range 1 <= x <= 5
	if(Number(elem.value) > 5){
		elem.value = 5;
	}else if(Number(elem.value) < 1){
		elem.value = 1;
	}

	var inputs = document.getElementsByClassName("system-textarea");
	difference = Number(elem.value) - inputs.length;

	if(difference < 0){ //inputs need to be removed
		while(difference < 0){
			inputs[inputs.length-1].parentNode.removeChild(inputs[inputs.length-1]);
			difference++;
		}
	}else if(difference > 0){ //inputs need to be added
		while(difference > 0){
			newNode = document.createElement("textarea");
			newNode.className = "system-textarea";
			newNode.oninput = updateSystemOfEquations;
			inputs[inputs.length-1].parentElement.insertBefore(newNode,inputs[inputs.length-1]);
			difference--;
		}
	}
}

function updateSystemOfEquations(){
	var inputs = document.getElementsByClassName("system-textarea");
	
	var textarea = document.getElementById("id_textarea");

	textarea.innerHTML = "";
	for(var i = 0; i < inputs.length; i++){
		textarea.innerHTML += inputs[i].value + "|";
	}

	textarea.innerHTML = textarea.innerHTML.substring(0,textarea.innerHTML.length-1);
}