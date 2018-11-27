import movie.media as media
import movie.fresh_tomatoes as fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        'A story of a boy and his toys that come to life',
                        'https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=6ziBFh3V1aM')

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
