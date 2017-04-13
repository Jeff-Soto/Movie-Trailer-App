from media import Movie
import fresh_tomatoes

# create movie objects
revenant = Movie("The Revenant",
                 "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
                 "https://www.youtube.com/watch?v=LoebZZ8K5N0")
batmanVsSuperman = Movie("Batman Vs Superman",
                         "https://s-media-cache-ak0.pinimg.com/originals/17/2b/3c/172b3c412f68d96695a4f58b3149cf0f.jpg",
                         "https://www.youtube.com/watch?v=xe1LrMqURuw")
zootopia = Movie("Zootopia",
                 "https://lumiere-a.akamaihd.net/v1/images/movie_poster_zootopia_866a1bf2.jpeg?region=0,0,300,450",
                 "https://www.youtube.com/watch?v=bY73vFGhSVk")
rush = Movie("Rush",
             "http://assets.flicks.co.nz/images/movies/poster/08/08aee6276db142f4b8ac98fb8ee0ed1b_500x735.jpg",
             "https://www.youtube.com/watch?v=lzNbGH1oZJc")

#create movie list
movies = [revenant, batmanVsSuperman,zootopia,rush]

# pass movies list to open_movies_page func
fresh_tomatoes.open_movies_page(movies)
