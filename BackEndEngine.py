import pandas as pd
import apiHandler as ah
import trainerEngine as te
import pandas as pd



class BackEndEngine:
    
    def __init__(self, token):
        self.__token = token
        self.__posts = ah.PostsGrabber(self.__token)
        self.__demographics = ah.PageDemographic(self.__token)
        self.__trainer = te.TrainerEngine()

    def displayTrainData(self, postIter = 3):
        """1 postIter = 25posts. Ex: If postIter = 3, it will try to get at most 75 posts if available"""
        self.__posts.execute(counts= postIter)
        self.__trainer.getTrainedDF(dataFrame= self.__posts.getDF())
        self.__trainer.displayDF()
        self.__trainer.exportCSV()
    def getPageDemographicsData(self):
        return self.__demographics.getDemographics()




# token = "EAAZA9cOuu2jsBAFRbLZCghgCwoRt5nj1tUVMfQoHdUwRF8EGEgzQtmsI3v9iLDIBPv3UEdnDeJ6hBZALiZASydZCZAiCL4wVPV4afQkfz3WFDZAYmzzqbpFdb2YcgaZBfQ11j24Ud78TXkjTiJP2E0b9S3n1WaBocnFkzdcim3kpz8SdsnZB6aaAu"


# eng = BackEndEngine(token= token)


# eng.displayTrainData()


3#fb.ap(page_fans_city) 
# page_fans_gender_age  
# page_fan_adds/days (loop)
# page_fan_removes (loop)

1 # # PageLikes/Dislikes:  (page_fan_adds/page_fan_removes)
# manitouClass.getPage()
# [
#     ["day","months","likes"],[],[]
# ]
# item[1][2]

2# Gender: 
# page_fans_gender_age
# class.getFanGenderAge()
# [
#     ["Gender","14-16","TotalNumbers" ],[],[]
# ]

#page_impressions




