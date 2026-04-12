class DGameManager():
    def __init__(self):
        print("game manager starting up")

# example of how to support console get and set:
#
# class DGameManager:
#     def __init__(self):
#         self.state = {
#             "hp": 100,
#             "gold": 50,
#             "level": 1
#         }

#     def get_stat(self, key):
#         return self.state.get(key, "N/A")

#     def set_stat(self, key, value):
#         if key in self.state:
#             # Try to match the type of the existing value
#             target_type = type(self.state[key])
#             self.state[key] = target_type(value)
#             return True
#         return False