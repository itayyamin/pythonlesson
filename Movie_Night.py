# This function collects votes and groups names by the movie they chose.
# Input: number of voters, and for each: their name and movie choice.
# Output: Dictionary { movie_title: [list_of_names] }
def group_votes_by_movie(n):
    movie_votes = {}
    for _ in range(n):
        name = input("Enter your name: ")
        movie = input("Enter the movie you vote for: ")
        if movie not in movie_votes:
            movie_votes[movie] = []
        movie_votes[movie].append(name)
    return movie_votes

# This function prints each movie and how many people voted for it.
# Input: Dictionary { movie_title: [list_of_names] }
# Output: Prints vote counts per movie.
def print_vote_summary(movie_votes):
    print("\nVoting Summary:")
    for movie, voters in movie_votes.items():
        print(f"{movie}: {len(voters)} vote(s) - Voted by: {', '.join(voters)}")

def main():
    n = int(input("How many people are voting? "))
    movie_votes = group_votes_by_movie(n)
    print_vote_summary(movie_votes)

if __name__ == "__main__":
    main()
