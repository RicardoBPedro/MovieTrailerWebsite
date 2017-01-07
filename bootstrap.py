import media
import movie_trailer_website

transcedence = media.Movie("Transcedence",
                           "Dr. Will Caster (Johnny Depp) is the foremost researcher in the field of Artificial Intelligence, working to create a sentient machine that combines the collective intelligence of everything ever known with the full range of human emotions. His highly controversial experiments have made him famous, but they have also made him the prime target of anti-technology extremists who will do whatever it takes to stop him. However, in their attempt to destroy Will, they inadvertently become the catalyst for him to succeed—to be a participant in his own transcendence. For his wife Evelyn (Rebecca Hall) and best friend Max Waters (Paul Bettany), both fellow researchers, the question is not if they can...but if they should. Their worst fears are realized as Will's thirst for knowledge evolves into a seemingly omnipresent quest for power, to what end is unknown. The only thing that is becoming terrifyingly clear is there may be no way to stop him.",
                           "https://i.jeded.com/i/transcendence.29748.jpg",
                           "https://www.youtube.com/watch?v=VCTen3-B8GU")

middle_man = media.Movie("Middle Man",
                         "Middle Men is a 2009 American drama film directed by George Gallo and written by Gallo and Andy Weiss. It stars Luke Wilson, Giovanni Ribisi, Gabriel Macht and James Caan.[4] The movie is based on the experiences of Christopher Mallick who was previously associated with the internet billing companies Paycom and ePassporte. Christopher Mallick has been accused of stealing millions of dollars from his customers at ePassporte to fund the creation of the film.",
                         "https://image.tmdb.org/t/p/w1000/vFiSz5iJ8ipcUlb4ZmY7Pl7rXcI.jpg",
                         "https://www.youtube.com/watch?v=UbjjoantaFE")

iron_man = media.Movie("Iron Man",
                       "Paramount Pictures and Marvel Studios' big screen adaptation of Marvel's legendary Super Hero Iron Man will launch into theaters on May 2, 2008. Oscar nominee Robert Downey Jr. stars as Tony Stark/Iron Man in the story of a billionaire industrialist and genius inventor who is kidnapped and forced to build a devastating weapon. Instead, using his intelligence and ingenuity, Tony builds a high-tech suit of armor and escapes captivity. When he uncovers a nefarious plot with global implications, he dons his powerful armor and vows to protect the world as Iron Man. The film also stars Oscar winner Gwyneth Paltrow and Oscar nominees Terrance Howard and Jeff Bridges and will be directed by Jon Favreau.",
                       "http://vignette1.wikia.nocookie.net/ironman/images/c/cd/Photo(980).jpg/revision/latest?cb=20141103103235",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

iron_man_2 = media.Movie("Iron Man 2",
                        "Iron Man 2 is a 2010 American superhero film based on the Marvel Comics character Iron Man, produced by Marvel Studios and distributed by Paramount Pictures.1 It is the sequel to 2008's Iron Man, and is the third film in the Marvel Cinematic Universe. Directed by Jon Favreau and written by Justin Theroux, the film stars Robert Downey Jr., Gwyneth Paltrow, Don Cheadle, Scarlett Johansson, Sam Rockwell, Mickey Rourke, and Samuel L. Jackson. ",
                        "http://dramaindo.com/wp-content/uploads/2016/05/Iron-Man-2.jpg",
                        "https://www.youtube.com/watch?v=wKtcmiifycU")

iron_man_3 = media.Movie("Iron Man 3",
                        "Iron Man 3 is an upcoming American superhero film featuring the Marvel Comics character Iron Man, produced by Marvel Studios and distributed by Walt Disney Pictures.1 It will be the sequel to Iron Man and Iron Man 2 and will be the seventh installment in the Marvel Cinematic Universe, being the first major release in that franchise since the crossover film The Avengers. Shane Black is set to direct a screenplay by himself and Drew Pearce, which will be based on the \"Extremis\" story arc by Warren Ellis. Jon Favreau, who directed the first two films, serves as executive producer, along with Kevin Feige. Robert Downey, Jr. reprises his role as Tony Stark, with Gwyneth Paltrow, Don Cheadle and Favreau reprising their roles as Pepper Potts, James Rhodes and Happy Hogan, respectively. Guy Pearce, Rebecca Hall, Stephanie Szostak, James Badge Dale and Ben Kingsley round out the film's principal cast.",
                        "http://cdn.collider.com/wp-content/uploads/Iron-Man-3-IMAX-poster1.jpg",
                        "https://www.youtube.com/watch?v=oYSD2VQagc4")

spider_man = media.Movie("Spider-Man",
                         "Spider-Man: Homecoming Trailer #1 (2017): Check out the FIRST trailer for reboot of the Spider-Man franchise starring Robert Downey Jr., Marisa Tomei and Tom Holland! Be sure to be the first to check out more trailers and movie teasers/clips dropping soon @MovieclipsTrailers. ",
                         "http://cdn.collider.com/wp-content/uploads/amazing-spider-man-movie-poster.jpg",
                         "https://www.youtube.com/watch?v=n9DwoQ7HWvI")

movies = [transcedence, middle_man, iron_man, iron_man_2, iron_man_3, spider_man]

movie_trailer_website.open_movies_page(movies)










