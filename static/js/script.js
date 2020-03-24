const movieForm = document.getElementById('movieForm');
const bookForm = document.getElementById('bookForm');
const addWatchList = document.getElementById('addWatchList');
const submitChoice = document.getElementById('submitChoice');
let choiceSelector = document.getElementById('choice');

let all_movies = Array.from(document.querySelectorAll('p.recmovie'));
let fav_movies = [];
let userdata;
getUserData();



addWatchList.addEventListener('click', addLocal)


all_movies.forEach(movie => movie.addEventListener('click', () => {
    console.log(movie.innerHTML) //the value of the p tag
    movie.style.opacity = 0.2;  //validates that it's selected
    if(fav_movies.indexOf(movie.innerHTML) === -1){
        //if item does not exist in the array
        fav_movies.push(movie.innerHTML)
    }
    console.log(fav_movies)
})) 


function getChoice(e) {
  e.preventDefault()
  let userOption = choiceSelector.options[choiceSelector.selectedIndex].value
  console.log(userOption)
}



// function validateChoice() {
//     if(document.getElementById('movie').checked == true){
//         console.log(document.getElementById('movie').value)
//         movieForm.style['visibility'] = 'visible';
//         bookForm.style['visibility'] = 'hidden';

//     }
//     else if(document.getElementById('book').checked == true){
//         console.log(document.getElementById('book').value)
//         bookForm.style['visibility'] = 'visible';
//         movieForm.style['visibility'] = 'hidden';
//     }   
// }

function getUserData() {
    if (localStorage.getItem("movies")) {
      userdata = JSON.parse(localStorage.getItem("movies"))
    } else {
      userdata = {
        fav_movies : [] //empty out the movies array
      }
    }
  }


  //adds it to local storage
function addLocal(){ 
    fav_movies.forEach(movie => {
        console.log('works')
        if (userdata.fav_movies.includes(movie)){
        console.log("don't add")
        }
        else {
        console.log('add')
        console.log(movie)
        userdata.fav_movies.push(movie)
        const json = JSON.stringify(userdata)
        // Save to localStorage
        localStorage.setItem("movies", json)
        }
    })
}
