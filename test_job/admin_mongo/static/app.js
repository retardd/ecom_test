window.onload = function() {
    var addInputButton = document.getElementById("addInput");
    var inputContainer = document.getElementById("inputContainer");
    var inputCount = 2;
 
    addInputButton.onclick = function() {
        var newDiv = document.createElement("div");
        var newInput1 = document.createElement("input")
        newInput1.type = "text";
        newInput1.name = "input" + inputCount;
        newInput1.id = "input" + inputCount;
        newInput1.placeholder = "Введите имя поля";

        inputCount++;

        var newInput2 = document.createElement("input")
        newInput2.type = "text";
        newInput2.name = "input" + inputCount;
        newInput2.id = "input" + inputCount;
        newInput2.placeholder = "Введите тип поля";

        inputCount++;
 
        newDiv.appendChild(newInput1);
        newDiv.appendChild(newInput2);
        inputContainer.appendChild(newDiv);

    }
}