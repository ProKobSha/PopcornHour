
document.addEventListener('DOMContentLoaded', () => {
    console.log("Página cargada correctamente.");
   
    const movieTitle = document.querySelector('.movie-title');
    if (movieTitle) {
        movieTitle.addEventListener('click', () => {
            alert("¡Has hecho clic en el título de la película!");
        });
    }
});
