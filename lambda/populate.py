from source.model import User, Stats, StreakDay, DayCover, Course, Path
from source.service import UserData
from source.utils import get_json_dict

mock_data = get_json_dict("source/data/mock/users.json")
users = []

for user in mock_data.get("users", []):
    users.append(User.parse_obj(user))


print(UserData().insert_user_bulk(users))
