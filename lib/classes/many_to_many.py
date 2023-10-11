class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
    @property
    def title(self):
        return self._title
   
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0 and not hasattr(self, "title"):
            self._title = title
        
    def add_result(self, result):
        if isinstance(result, Result):
            self._results.append(result)
        else:
            print("Result must be an instance of the Result class")
     

    def results(self):
        return self._results
        pass

    def players(self):
        return list(set(self._players))
        pass

    def average_score(self, player):
        scores = [result.score for result in self._results if result.player == player]
        if len(scores) > 0:
            return sum(scores) / len(scores)
        else:
            return 0
        pass

class Player:
    def __init__(self, username):
        self.username = username
        
        self.played_games = []
        self._games = []
        self._results = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if type(username) == str and 2 <= len(username) <= 16:
            self._username = username
        else:
            print("Username must be a string between 2 and 16 characters")
        
    def add_result(self, result):
        if isinstance(result, Result):
            return list(result)
        else: 
            print("Result mjust be an instance of the Result class")


    def results(self):
        return self._results
        pass

    def games_played(self):
        games = set()
        for result in self._results:
            games.add(result.game)
        return list(games)
        pass

    def played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False

    def num_times_played(self, game):
        count = 0
        for result in self._results:
            if result.game == game:
                count += 1
        return count
        pass

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        self.player._results.append(self)
        self.player._games.append(self.game)

        self.game._results.append(self)
        self.game._players.append(player)

        Result.all.append(self)

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if type(score) == int and 1 <= 5000 and not hasattr(self, "score"):
            self._score = score
        else:
            print("Score must be an integer between one and 5000")
        
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            print("Player must be an instance of the Player class")
        

    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            print("Game must be an instance of the Game class")