import webbrowser

class Movie():
    """ Class that represents movie """
    def __init__(self, title, storyline, posterImage, trailerYoutube):
        """ Method that inicialize the fields of class Movie """
        self.title = title
        self.storyline = storyline
        self.posterImage = posterImage
        self.trailerYoutube = trailerYoutube

    def play_trailer(self):
        """ Mothod that plays the trailer of it object """
        webbrowser.open(self.trailerYoutube)
