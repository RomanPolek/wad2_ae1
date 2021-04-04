
function update_questions() {
    var questions = document.getElementById("question_container").children
    for(var i = 0; i < questions.length; i++) {
        var question = questions[i]

        question.getElementsByTagName("h2")[0].innerHTML = "question " + (i + 1)
        var inputs = question.getElementsByTagName("input")
        inputs[0].name = "question_" + i
        var counter = 0;
        for(var j = 1; j < inputs.length; j++) {
            if(j % 2 == 1) {
                inputs[j].name = "correct_answer_" + i
                inputs[j].value = counter
            }
            else {
                inputs[j].name = "answer_" + i + "_" + counter
                counter++
            }
        }
    }
}

function exam_add_question() {
    var question = document.createElement("div")
    question.classList = "question"

    var title = document.createElement("h2")
    question.appendChild(title)

    var content = document.createElement("input")
    content.setAttribute("required", "required")
    content.placeholder = "content"
    question.appendChild(content)

    for(var i = 0; i < 5; i++) {
        var answer = document.createElement("div")

        var radio = document.createElement("input")
        radio.type = "radio"
        if(i==0)radio.setAttribute("checked", "checked")
        answer.appendChild(radio)

        var inp = document.createElement("input")
        inp.setAttribute("required", "required")
        inp.placeholder = "answer " + (i + 1)
        answer.appendChild(inp)

        question.appendChild(answer)
    }

    var remove_button_wrapper = document.createElement("div")
    remove_button_wrapper.style.textAlign = "right"

    var remove_button = document.createElement("button")
    remove_button.classList = "gray_button round_button"
    remove_button.innerHTML = "-"
    remove_button.type = "button"
    remove_button.onclick = function() {
        question.remove()
        update_questions()
    }.bind(question)

    remove_button_wrapper.appendChild(remove_button)
    question.appendChild(remove_button_wrapper)

    document.getElementById("question_container").appendChild(question)

    update_questions()
}