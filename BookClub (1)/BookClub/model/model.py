def calc_similarity_score(member, all_members_ratings, correlation_calculator):
    readers_ratings = all_members_ratings[member]
    return [(name, correlation_calculator(readers_ratings, ratings))
            for name, ratings in all_members_ratings.items() if name != member]


def find_two_most_similar_members(name, member_and_rating_list):
    pass


def create_recommended_booklist(entered_member_ratings, similar_member1_ratings, similar_member2_ratings, booklist):
    pass

