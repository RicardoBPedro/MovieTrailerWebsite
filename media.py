import webbrowser

class Movie():
    def __init__(self, title, storyline, posterImage, trailerYoutube):
        self.title = title
        self.storyline = storyline
        self.posterImage = posterImage
        self.trailerYoutube = trailerYoutube

    def play_trailer(self):
        webbrowser.open(self.trailerYoutube)
