function populateEquations(){
	var numVars = document.getElementById("simplex-vars").value;
	var numConstraints = document.getElementById("simplex-constraints").value;

	console.log("vars: " + numVars + ", constraints: " + numConstraints);

	var simplexEquations = document.getElementsByClassName("simplex-equations");
	var constraintsContainer = document.getElementById("simplex-constraint-container");
	
	constraintsContainer.innerHTML = "<br />";
	for(var i = 0; i < numConstraints; i++){
		constraintsContainer.innerHTML += "<div class='simplex-equations'></div><br /><br />";
	}

	for(var i = 0; i < simplexEquations.length; i++){
		simplexEquations[i].innerHTML = "";
		for(var j = 0; j < numVars; j++){
			simplexEquations[i].innerHTML += "<textarea class='container-field'></textarea> <span>x<sub>" + (j+1) + "</sub></span>";
			
			if(j != (numVars - 1)){
				simplexEquations[i].innerHTML += " + ";
			}else if(i != 0){
				simplexEquations[i].innerHTML += " <select class='simplex-inequality'><option value='less'>&le;</option><option value='more'>&ge;</option></select> <textarea class='container-field simplex-b'></textarea>";
			}
		}
	}

	var containers = document.getElementsByClassName("container-field");
	for(var i = 0; i < containers.length; i++){
		//console.log();
		//containers[i].oninput = updateSimplex();
	}
}

function updateSimplex(){
	var textarea = document.getElementById("id_textarea");

	var numVars = document.getElementById("simplex-vars").value;
	var numConstraints = document.getElementById("simplex-constraints").value;
	
	var simplexEquations = document.getElementsByClassName("simplex-equations");
	var constraintsContainer = document.getElementById("simplex-constraint-container");

	textarea.innerHTML = numVars + "|" + numConstraints + "|" + document.getElementById("simplex-version").value + ",";
	for(var i = 0; i < simplexEquations.length; i++){
		//var constants = simplexEquations.children;
		console.log(simplexEquations[i].innerHTML);
		for(var j = 0; j < numVars; j++){
			//console.log(simplexEquations[i].children[j*2]);
			var temp = simplexEquations[i].children[j*2].value;
			
			if(temp == ""){
				temp = 0;
			}
			
			textarea.innerHTML += temp;

			if(j != (numVars - 1)){
				textarea.innerHTML += ",";
			}
			//textarea.innerHTML += simplexEquations
			//console.log(j*2);
		}

		//console.log((numVars*2));
		//console.log("Length:" + simplexEquations[i].children.length);
		if(i != 0){
			console.log(simplexEquations[i].children[(numVars*2)].value);
			var temp = simplexEquations[i].children[(numVars*2)+1].value;
			
			if(temp == ""){
				temp = 0;
			}

			textarea.innerHTML += "," + simplexEquations[i].children[(numVars*2)].value + "," + temp + "|";
		}else{
			textarea.innerHTML += "|";
		}
		//console.log(simplexEquations[i].children[(numVars*2)-1].value);
		//textarea.innerHTML += simplexEquations[i].children[(numVars*2)].value + ", " + simplexEquations[i].children[(numVars*2)+1].value + "|";
	}

	alert(textarea.innerHTML);

}