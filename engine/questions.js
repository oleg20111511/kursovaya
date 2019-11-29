"use strict"
var questions = [];


//Пример добавления вопроса в список:
//type: 0 #Один правильный вариант
//type: 1 #Несколько правильных вариантов
//type: 2 #Ввести ответ вручную
/*

для type 0:
var любое_имя = {
    content: 'ссылка на html документ с вопросом',
    type: 0,
    rightAnswer: 'текст правильного ответа',
    wrongAnswers: [
        'текст неправильного ответа n1',
        'текст неправильного ответа n3',
        'текст неправильного ответа n2',
        ...
        'текст неправильного ответа n27',
    ],
    correct: 'ссылка на html документ, отображаемый в случае правильного ответа',
    wrong: 'ссылка на html документ, отображаемый в случае неверного ответа (в него желательно добавить объяснения)'
}
questions.push(любое_имя);

***************

для type 1:
var любое_имя = {
    content: 'ссылка на html документ с вопросом',
    type: 1,
    rightAnswers: [
        'текст правильного ответа 1',
        'текст правильного ответа 2',
        ...
    ],
    wrongAnswers: [
        'текст неправильного ответа n1',
        'текст неправильного ответа n3',
        'текст неправильного ответа n2',
        ...
        'текст неправильного ответа n27',
    ],
    correct: 'ссылка на html документ, отображаемый в случае правильного ответа',
    wrong: 'ссылка на html документ, отображаемый в случае неверного ответа (в него желательно добавить объяснения)'
}
questions.push(любое_имя);

************

для type 2:
var любое_имя = {
    content: 'ссылка на html документ с вопросом',
    type: 1,
    rightAnswers: [
        'Вариант ответа 1',
        'Вариант ответа 2',
        ...
    ],
    correct: 'ссылка на html документ, отображаемый в случае правильного ответа',
    wrong: 'ссылка на html документ, отображаемый в случае неверного ответа (в него желательно добавить объяснения)'
}
questions.push(любое_имя);

************
*/

var q1 = {
    content: 'questions/1/q1.html',
    type: 0,
    rightAnswer: 'Вариант1!',
    wrongAnswers: [
        'Вариант2!',
        'Вариант3!',
        'Вариант4!',
        'Вариант5!'
    ],
    correct: 'questions/correct1.html',
    wrong: 'questions/wrong1.html'
}
questions.push(q1);

var q2 = {
    content: 'questions/1/q2.html',
    type: 1,
    rightAnswers: [
        'Вариант1!!',
        'Вариант5!!'
    ],
    wrongAnswers: [
        'Вариант2!',
        'Вариант3!',
        'Вариант4!'
    ],
    correct: 'questions/correct1.html',
    wrong: 'questions/wrong2.html'
}
questions.push(q2);

var q3 = {
    content: 'questions/1/q3.html',
    type: 2,
    rightAnswers: [
        'Вариант 1!',
        'Вариант 1',
        'вариант 1',
        'вариант первый',
        'Вариант I'
    ],
    correct: 'questions/correct1.html',
    wrong: 'questions/wrong1.html'
}
questions.push(q3);

var q4 = {
    content: 'questions/1/q4.html',
    type: 0,
    rightAnswer: 'Вариант1!',
    wrongAnswers: [
        'Вариант2!',
        'Вариант3!',
        'Вариант4!',
        'Вариант5!'
    ],
    correct: 'questions/correct1.html',
    wrong: 'questions/wrong1.html'
}
questions.push(q4);

var q5 = {
    content: 'questions/1/q5.html',
    type: 1,
    rightAnswers: [
        'Вариант1!!',
        'Вариант5!!'
    ],
    wrongAnswers: [
        'Вариант2!',
        'Вариант3!',
        'Вариант4!'
    ],
    correct: 'questions/correct1.html',
    wrong: 'questions/wrong2.html'
}
questions.push(q5);

var q6 = {
    content: 'questions/1/q6.html',
    type: 2,
    rightAnswers: [
        'Вариант 1!',
        'Вариант 1',
        'вариант 1',
        'вариант первый',
        'Вариант I'
    ],
    correct: 'questions/correct1.html',
    wrong: 'questions/wrong1.html'
}
questions.push(q6);
