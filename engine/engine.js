"use strict";

var started = false;
var currentQuestion = 0;
var answersBlock = undefined;
var questionsBlock = undefined;
var explanatoryBlock = undefined;
var rightAnswerPos = undefined;
var questionType = undefined;
var answerParagraphs = [];
var results = 0;
var answerFields = [];
var chosenFields = [];

//Функция перемешивания массивов
function shuffle(a) {
  var j, x, i;
  for (i = a.length - 1; i > 0; i--) {
    j = Math.floor(Math.random() * (i + 1));
    x = a[i];
    a[i] = a[j];
    a[j] = x;
  }
  return a;
}


//Заполнение параграфов с ответами
function fillAnsweParagraphs(type, answersAmount) {
  let question = questions[currentQuestion];
  if (type == 0) {
    rightAnswerPos = Math.floor((Math.random() * answersAmount));
    let shuffledWrongAnswers = shuffle(question.wrongAnswers).slice(0);
    for (let i = 0; i < answerParagraphs.length; i++) {
      if (i == rightAnswerPos) {
        answerParagraphs[i].innerHTML = question.rightAnswer;
      } else {
        answerParagraphs[i].innerHTML = shuffledWrongAnswers[0];
        shuffledWrongAnswers.shift();
      }
    }
  } else {
    rightAnswerPos = [];

    for (let i = 0; i < question.rightAnswers.length; i++) {
      let calculateRAP = Math.floor((Math.random() * (answersAmount - 1)));
      while (rightAnswerPos.indexOf(calculateRAP) > -1) {
        calculateRAP = Math.floor((Math.random() * (answersAmount - 1)));
      }
      rightAnswerPos.push(calculateRAP);
    }
    rightAnswerPos.sort();
    let copyRAP = rightAnswerPos.slice(0);

    let shuffledRightAnswers = shuffle(question.rightAnswers).slice(0);
    let shuffledWrongAnswers = shuffle(question.wrongAnswers).slice(0);
    for (let i = 0; i < answerParagraphs.length; i++) {
      if (copyRAP.indexOf(i) > -1) {
        answerParagraphs[i].innerHTML = shuffledRightAnswers[0];
        shuffledRightAnswers.shift();
        copyRAP.shift();
      } else if (i == answerParagraphs.length - 1) {
        answerParagraphs[i].innerHTML = 'Далее';
      } else {
        answerParagraphs[i].innerHTML = shuffledWrongAnswers[0];
        shuffledWrongAnswers.shift();
      }
    }
  }
}

//Создание пояснительного текста
function createExplanatoryBlock(type) {
  let question = questions[currentQuestion];
  explanatoryBlock = document.createElement("div");
  explanatoryBlock.style.height = window.innerHeight * 0.08 + 'px';
  explanatoryBlock.style.width = "100%";
  answersBlock.appendChild(explanatoryBlock)
  let explanatoryHeader = document.createElement("h2");
  let explanation = undefined;
  switch (type) {
    case 0:
      explanation = 'Выберите вариант ответа:'
      break;
    case 1:
      let rightAnswersAmount = question.rightAnswers.length;
      let ending = undefined;
      switch (rightAnswersAmount) {
        case 2:
        case 3:
        case 4:
          ending = 'а';
          break;
        default:
          ending = 'ов';
      }
      explanation = `Выберите ${rightAnswersAmount} вариант${ending} ответа:`
      break;
    case 2:
      explanation = 'Введите ответ:';
      break;
  }
  explanatoryHeader.innerHTML = explanation;
  explanatoryBlock.className = 'explanation';
  explanatoryBlock.appendChild(explanatoryHeader);
}

//Оформление блока ответов
function fillAnswerBlocks(type, answersAmount, answerFieldHeight) {
  let question = questions[currentQuestion];
  answerParagraphs = [];
  answerFields = [];

  let answerBlocksAmount = answersAmount;
  if (type == 1) answerBlocksAmount += 1;
  //    Создание блоков для ответа
  for (let i = 0; i < answerBlocksAmount; i++) {
    let field = document.createElement("div");
    field.style.height = answerFieldHeight;
    //0 = переход на следующую страницу, 1 = выделение варианта
    field.onclick = function() {
      let buttonType = 0;
      if ((type == 1) && (i == answerBlocksAmount - 1)) buttonType = 1;
      chooseAnswer(i, buttonType);
    };
    if (i % 2 == 0) {
      field.style.float = "left";
      field.style.clear = "both";
    } else {
      field.style.float = "right";
    }
    answersBlock.appendChild(field);
    answerFields.push(field);

    let paragraph = document.createElement("p");
    paragraph.id = `a${i}`;
    field.appendChild(paragraph);

    answerParagraphs.push(document.getElementById(`a${i}`));

    //aesthetics:
    paragraph.addEventListener('mouseenter', function() {
      paragraph.style.color = '#7B68EE';
    })
    paragraph.addEventListener('mouseleave', function() {
      paragraph.style.color = (paragraph.chosen) ? '#DDA0DD' : 'white';
    })
  }
  if (answerBlocksAmount % 2 == 1) {
    answerFields[answerFields.length - 1].style.width = "100%";
  }

  //    Заполнение параграфов вариантами ответов
  fillAnsweParagraphs(type, answersAmount);

  //    aesthetics:
  for (let i = 0; i < answerFields.length; i++) {
    let margin = (answerFields[i].clientHeight - answerParagraphs[i].clientHeight) / 2;
    answerParagraphs[i].style.marginTop = margin + 'px';
  }
  //    ***********
}

//Загружает список вопросов, после полной загрузки запускает start()
window.onload = function() {
  let fileLink = localStorage.getItem('fileLink');
  let questionList = document.createElement('script');
  questionList.src = fileLink;
  questionList.onload = () => start();
  document.head.append(questionList);
}

//Перемешивает вопросы, задаёт высоту
function start() {
  shuffle(questions);

  //    aesthetics:
  document.getElementById('main').style.height = window.innerHeight + 'px';
  if (window.innerHeight > window.innerWidth) {
    document.getElementById('main').style.width = '90%';
  }
  document.getElementById('question').style.height = (window.innerHeight * 0.6) + 'px';
  document.getElementById('answers').style.height = (window.innerHeight * 0.4) + 'px';
  //  ***********

  questionsBlock = document.getElementById('question');
  answersBlock = document.getElementById('answers')

  changeQuestion();
}

//aesthetics:
window.onresize = function() {
  document.getElementById('main').style.height = window.innerHeight + 'px';
  if (window.innerHeight > window.innerWidth) {
    document.getElementById('main').style.width = '90%';
  } else {
    document.getElementById('main').style.width = '50%';
  }
  document.getElementById('question').style.height = (window.innerHeight * 0.6) + 'px';
  document.getElementById('answers').style.height = (window.innerHeight * 0.4) + 'px';

  if (started) {
    let iframe = document.getElementById('question');
    let iframeContainer = iframe.contentWindow.document.getElementById('container');
    let image = iframe.contentWindow.document.getElementById('image');
    iframeContainer.style.height = (window.innerHeight * 0.6) + 'px';
    if (image != null && image.clientWidth > window.innerWidth * 0.45) {
      image.style.width = '90%';
      image.style.height = 'auto';
    } else if (image != null) {
      image.style.width = 'auto';
      image.style.height = '60%';
    }


    if (questions[currentQuestion].type != 2) {
      let answersAmount = answersBlock.childElementCount;
      let answerFieldHeight = undefined;
      //                                     0.4 * место для ответов(0.85)
      answerFieldHeight = (window.innerHeight * 0.32 / Math.ceil((answersAmount - 1) / 2)) + 'px';
      //                                     0.4 * место для объяснения(0.15)
      explanatoryBlock.style.height = window.innerHeight * 0.08 + 'px';
      for (let i = 0; i < answerFields.length; i++) {
        answerFields[i].style.height = answerFieldHeight;
      }
    } else {

    }
  }
}

//Создаёт поле для ввода и кнопку далее
function createInput() {
  let inputBlock = document.createElement("div");
  inputBlock.style.width = "100%";
  let input = document.createElement("input");
  input.type = "text";
  inputBlock.appendChild(input);
  answersBlock.appendChild(inputBlock);

  let next = document.createElement("button");
  next.type = "button";

  next.innerHTML = "Далее";
  next.id = "next";
  next.onclick = function() {
    let answer = input.value;
    chooseAnswer(answer, -1);
  }
  answersBlock.appendChild(next);
}

//Отображает текущий вопрос
function changeQuestion() {
  questionsBlock.src = questions[currentQuestion].content;
  answersBlock.innerHTML = ' ';
  let question = questions[currentQuestion];
  questionType = question.type;
  createExplanatoryBlock(questionType);

  let answersAmount = undefined;
  let answerFieldHeight = undefined;
  //Просчёт высоты блоков для ответа, старт функции заполнения
  switch (questionType) {
    case 0:
      answersAmount = 1 + question.wrongAnswers.length;
      answerFieldHeight = (window.innerHeight * 0.32 / Math.ceil((answersAmount) / 2)) + 'px';
      fillAnswerBlocks(questionType, answersAmount, answerFieldHeight);
      break;
    case 1:
      chosenFields = [];
      answersAmount = question.rightAnswers.length + question.wrongAnswers.length;
      answerFieldHeight = (window.innerHeight * 0.32 / Math.ceil((answersAmount) / 2)) + 'px';
      fillAnswerBlocks(questionType, answersAmount, answerFieldHeight);
      break;
    case 2:
      createInput();
      break;
  }
  started = true;
}

//Выделение кнопки
function chooseButton(option) {
  let rightAnswersAmount = questions[currentQuestion].rightAnswers.length;
  let button = answerFields[option];
  let index = chosenFields.indexOf(option)
  let chosen = (index != -1) ? true : false;
  let paragraph = button.firstChild;
  if (chosen) {
    paragraph.chosen = false;
    chosenFields.splice(index, 1);
    paragraph.style.color = '#7B68EE';

  } else {
    paragraph.chosen = true;
    if (chosenFields.length == rightAnswersAmount) return;
    chosenFields.push(option);
    paragraph.style.color = '#DDA0DD';
  }
}

//Вызывается при нажатии на ответ
function chooseAnswer(option, buttonType) {
  if (!started) return;
  let questionType = questions[currentQuestion].type;
  let right = false;

  switch (questionType) {
    case 0:
      if (option == rightAnswerPos) {
        right = true;
        results = results + 1;
      } else {
        right = false;
      }
      proceed(right);
      break;
    case 1:
      switch (buttonType) {
        case 0:
          chooseButton(option);
          break;
        case 1:
          let rightAnswersAmount = questions[currentQuestion].rightAnswers.length;
          if (chosenFields.length < rightAnswersAmount) return;
          let j = 0;
          for (let i = 0; i < rightAnswersAmount; i++) {
            if (rightAnswerPos.indexOf(chosenFields[i]) > -1) j++;
          }
          j = j / rightAnswersAmount;
          results = results + j;
          right = (j == 1) ? true : false;
          proceed(right);
          break;
      }
      break;
    case 2:
      if (option == "") return;
      right = questions[currentQuestion].rightAnswers.indexOf(option) > -1;
      if (right) results++;
      proceed(right);
      break;
  }

}

//Переход на страницу результата
function proceed(right) {
  switch (right) {
    case true:
      questionsBlock.src = questions[currentQuestion].correct;
      break;
    case false:
      questionsBlock.src = questions[currentQuestion].wrong;
      break;
  }

  //Очистка блока ответов, создание кнопки далее.
  let button = document.createElement('button');
  button.innerHTML = 'Далее';
  answersBlock.innerHTML = ' ';
  answersBlock.appendChild(button);
  button.onclick = function() {
    if (currentQuestion == questions.length) {
      showResults();
    } else {
      changeQuestion();
    }
  };

  currentQuestion++;
}

//Отображение результатов, сделаю потом
function showResults() {
  let result = 100 * results / questions.length;
  document.getElementById('main').innerHTML = result + '%';
}
