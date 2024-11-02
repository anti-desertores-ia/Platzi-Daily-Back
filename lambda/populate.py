from source.model import User, Challenge, UserChallenges
from source.service import UserData, ChallengeData, UserChallengeData
from source.utils import get_json_dict


def add_users():
    mock_data = get_json_dict("source/data/mock/users.json")
    users = []

    for user in mock_data or []:
        users.append(User.parse_obj(user))

    print("USERS:", UserData().insert_user_bulk(users))


def add_challenges():
    mock_data = get_json_dict("source/data/mock/challenges.json")
    users = []

    for user in mock_data or []:
        users.append(Challenge.parse_obj(user))

    print("CHALLENGES:", ChallengeData().insert_challenge_bulk(users))


def add_user_challenges():
    mock_data = get_json_dict("source/data/mock/user_challenge.json")
    user_challenges = []

    for user in mock_data or []:
        user_challenges.append(UserChallenges.parse_obj(user))

    print(
        "USER CHALLENGES:",
        UserChallengeData().insert_user_challenges_bulk(user_challenges),
    )


options = {
    "users": add_users,
    "challenges": add_challenges,
    "user_challenges": add_user_challenges,
}

if __name__ == "__main__":
    for key in options:
        add_data = input(f"Add {key} data (y|n): ").lower() == "y"

        if add_data:
            options.get(key)()
