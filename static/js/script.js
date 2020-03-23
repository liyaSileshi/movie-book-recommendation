
const movie = document.getElementById('movie')
const book = document.getElementById('book')
const movieForm = document.getElementById('movieForm')
const bookForm = document.getElementById('bookForm')
let all_movies = Array.from(document.querySelectorAll('p.recmovie'))

console.log(all_movies)

movie.addEventListener('change', validateChoice)
book.addEventListener('change', validateChoice)


function validateChoice() {
    if(document.getElementById('movie').checked == true){
        console.log(document.getElementById('movie').value)
        movieForm.style['visibility'] = 'visible';
        bookForm.style['visibility'] = 'hidden';

    }
    else if(document.getElementById('book').checked == true){
        console.log(document.getElementById('book').value)
        bookForm.style['visibility'] = 'visible';
        movieForm.style['visibility'] = 'hidden';
    }   
}


