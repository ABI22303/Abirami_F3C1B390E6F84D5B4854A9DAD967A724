#define
class playing:
    def play(self):
        print("The player is playing cricket.")
      
class Batsman(Playing):
    def play(self):
        print("The batsman is batting.")
      
class Bowler(Playing):
    def play(self):
        print("The bowler is bowling.")
      
batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()