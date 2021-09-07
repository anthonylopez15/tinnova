


class Elections(object):
    def __init__(self, total_voters, valid_votes, white_votes, null_votes):
        self.__total_voters = total_voters
        self.__valid = valid_votes
        self.__white_votes = white_votes
        self.__null = null_votes

    def calculate_valid_votes(self):
        return self.__valid / self.__total_voters * 100

    def calculate_white_votes(self):
        return self.__white_votes / self.__total_voters * 100

    def calculate_null_votes(self):
        return self.__null / self.__total_voters * 100


if __name__ == '__main__':
    elections = Elections(1000, 800, 150, 50)
    valid = elections.calculate_valid_votes()
    white_votes = elections.calculate_white_votes()
    null_votes = elections.calculate_null_votes()

    print(f"Valid Votes is: {valid}%")
    print(f"White Votes is: {white_votes}%")
    print(f"Null Votes is: {null_votes}%")