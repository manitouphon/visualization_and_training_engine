import json
import BackEndEngine as be



class LoadData:
    def setToken(self, token =  ""):
        self.__token = token 
        self.__engine = be.BackEndEngine(token)
        self.__demographics = self.__engine.getPageDemographicsData()
        print(json.dumps(self.__demographics, indent=4))


    def get_like(self): 
        ls = self.__demographics["demographics"]["new_likes"]
        date = ls[0]
        likes = ls[1]
        return [date,likes]
    def get_removed(self): 
        ls = self.__demographics["demographics"]["new_removed"]
        date = ls[0]
        removes = ls[1]
        return [date,removes]

    def get_location(self): 
        ls = self.__demographics["demographics"]["city"]
        cityName = ls[0]
        for x in range(len(cityName)):
            result = cityName[x].replace(", Cambodia", "")
            cityName[x] = result

        values = ls[1]
        percent = ls[2]

        return [cityName,values,percent]

    def get_gender_age(self):
        ls = self.__demographics["demographics"]["gender_age"]
        group = ls[0]
        values = ls[1]
        percent = ls[2]
        return [group,values,percent]
    def get_gender(self):
        ls = self.__demographics["demographics"]["gender"]
        return ls

    def get_lat_long(self):
        ls = self.__demographics["demographics"]["lat_long"]
        return ls 

    



# token = 'EAATQYSSfNaoBAKDvV3NwbvYGjwDqUrXQu8kAVOqO9aXc2nPc6JxJPoLijWPEdZCXMHbf0TZC4RtBljIgr207H4v3AP2AUfMW3Ardx7UfZBw6GHiC6RT0dhgn5G1lHkZC0ArzL0JWyvjBzZCgkkF7JhaANbRlYZAAw0gyH9nsPWNTQaGLwm36Hz3labyvKe7LrBQwNbo2t7gAZDZD'

# item = LoadData(token=token)
# x = item.get_like()

# like = Importfile()
# print(like.get_like())
# print(x)

