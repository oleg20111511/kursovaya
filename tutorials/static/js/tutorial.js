"use strict";
var started = false;
var currentTutorial = 0;
var tutorialBlock = undefined;
var buttonBlock = undefined;
var buttonField = undefined;

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


//Оформление блока кнопки
function addNextButton() {
	let buttonFieldHeight = (window.innerHeight * 0.2) + 'px';

	//    Создание блока для кнопки
	let field = document.createElement("div");
	field.style.height = buttonFieldHeight;
	field.onclick = function() {
	proceed()
	};

	field.style.width = '100%'
	buttonBlock.appendChild(field);
	buttonField = field;

	//Создание кнопки
	let paragraph = document.createElement("p");
	paragraph.id = 'button';
	paragraph.innerHTML = 'Далее';
	field.appendChild(paragraph);

	//aesthetics:
	paragraph.addEventListener('mouseenter', function() {
	paragraph.style.color = '#7B68EE';
	})
	paragraph.addEventListener('mouseleave', function() {
	paragraph.style.color = 'white';
	})
	// Вертикально выравнивает параграф внутри блока
	let margin = (field.clientHeight - paragraph.clientHeight) / 2;
	paragraph.style.marginTop = margin + 'px';
	//    ***********
}

//Загружает список обучений, задаёт высоту, после полной загрузки запускает changeTutorial
window.onload = function() {
	//    aesthetics:
	document.getElementById('main').style.height = window.innerHeight + 'px';
	if (window.innerHeight > window.innerWidth) {
	document.getElementById('main').style.width = '90%';
	}
	document.getElementById('question').style.height = (window.innerHeight * 0.8) + 'px';
	document.getElementById('answers').style.height = (window.innerHeight * 0.2) + 'px';
	//  ***********

	tutorialBlock = document.getElementById('question');
	buttonBlock = document.getElementById('answers')

	addNextButton();

	changeTutorial();
}

//aesthetics:
window.onresize = function() {
	document.getElementById('main').style.height = window.innerHeight + 'px';
	if (window.innerHeight > window.innerWidth) {
		document.getElementById('main').style.width = '90%';
	} else {
		document.getElementById('main').style.width = '50%';
	}
	document.getElementById('question').style.height = (window.innerHeight * 0.8) + 'px';
	document.getElementById('answers').style.height = (window.innerHeight * 0.2) + 'px';

	if (started) {
		let image = document.getElementById('image');
		if (image != null) {
			if (image.clientWidth == 0){
				setTimeout(window.onresize, 1000)
			}
			image.style.width = 'auto';
			image.style.height = '60%';
			if(image.clientWidth > tutorialBlock.clientWidth){
				image.style.width = '90%';
				image.style.height = 'auto';
			}
		}

		let buttonFieldHeight = undefined
		buttonFieldHeight = (window.innerHeight * 0.2) + 'px';
		buttonField.style.height = buttonFieldHeight
	}
}

//Заполняет блок вопроса
function loadTutorial(tutorial) {
	if (tutorial.template == true){
		tutorialBlock.innerHTML = '';
		if(tutorial.image) tutorialBlock.innerHTML += `<img style='height:60%;' id="image" src="${tutorial.image}">`;
		if(tutorial.text) tutorialBlock.innerHTML += `<h1>${tutorial.text}</h1>`;
		if(tutorial.audio) tutorialBlock.innerHTML += `<audio controls><source src="${tutorial.audio}"></audio>`;
	} else {
		tutorialBlock.innerHTML = '';
		let iframe = document.createElement('iframe');
		iframe.src = tutorial.filelink;
		iframe.style.height = '100%';
		iframe.style.width = '100%';
		iframe.style.border = 'none';
		tutorialBlock.appendChild(iframe);
	}
}

//Отображает текущую обучалку
function changeTutorial() {
	let tutorial = tutorials[currentTutorial];
	loadTutorial(tutorial);

	started = true;
	window.onresize();
}

// button.onclick
function proceed(right) {
	started = false;
	currentTutorial++;
	//Очистка блока ответов, создание кнопки далее.
	if (currentTutorial == tutorials.length) {
		showResults();
	} else {
		changeTutorial();
	}
}

//Отображение страницы с поощрением
function showResults() {
	window.location += '/finish';
}
