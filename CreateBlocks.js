"use strict";
var content = undefined;

window.onload = function() {
  content = document.getElementById('content');
  for (let i = 0; i < blocks.length; i++) {
    let block = document.createElement("div");
    if (i + 1 % 4 == 0) {
      block.className = "levelBlock FL CB";
    } else {
      block.className = "levelBlock FL";
    }
    block.style.backgroundImage = `url(${blocks[i][0]})`;
    block.onclick = function() {
      loadGroup(blocks[i]);
    }
    content.appendChild(block);
    block.style.height = (block.clientWidth * 0.56) + 'px';
  }
  let par = document.createElement('p');
  par.className = 'CB adjustHeight';
  content.appendChild(par);
}

function loadGroup(group) {
  content.innerHTML = "";
  for (let i = 1; i < group.length; i++) {
    let block = document.createElement("div");
    if (i + 1 % 4 == 0) {
      block.className = "levelBlock FL CB";
    } else {
      block.className = "levelBlock FL";
    }
    block.style.backgroundImage = `url(${group[i].bg})`;
    block.onclick = function() {
      proceed(group[i].link);
    }
    content.appendChild(block);
    block.style.height = (block.clientWidth * 0.56) + 'px';
  }
  let par = document.createElement('p');
  par.className = 'CB adjustHeight';
  content.appendChild(par);
}

function proceed(link) {
  localStorage.setItem('fileLink', link);
  window.location = 'engine/engine.html';
}


//aesthetics:
window.onresize = function() {
  let wrongSizedBlocks = content.children;
  for (let i = 0; i < wrongSizedBlocks.length; i++) {
    wrongSizedBlocks[i].style.height = (wrongSizedBlocks[i].clientWidth * 0.56) + 'px';
  }
}
