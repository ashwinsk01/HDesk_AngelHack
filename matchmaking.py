def matchmaking(): 
    Prob_MajorCat = {
        "Healthcare Infrastructure Development" : ["a1"] , 
        "Clean Water and Sanitation Projects" : ["a2" ] ,
        "Renewable Energy Solutions" : ["a3" , ] ,
        "Education System Overhaul" : ["a4" , ] ,
        "Affordable Housing Initiatives" : ["a5"] ,
        "Sustainable Agriculture Projects" : ["a6"] ,
        "Urban Public Transport Improvement" : ["a7"] ,
        "Waste Management Solutions" : ["a8"] ,
        "Rural Electrification Programs" : ["a9"] ,
        "Conservation of Natural Resources" : ["a10"] ,
    } 

    #Healthcare Infrastructure Development
    HID = {  
        "Hospital Establishment" : ["M2" , False],
        "Free Treatment" : ["M1", True]
    }

    Prob_MinorCat = {
        "Community Health Awareness Programs" : ["b1"] ,
        "Recycling and Waste Segregation Initiatives" : ["b2"] ,
        "Vocational Training for Employment" : ["b3"] ,
        "Public Park and Recreation Facility Upgrades" : ["b4"] ,
        "Digital Literacy Campaigns" : ["b5"] ,
        "Local Sports and Fitness Programs" : ["b6"] ,
        "Street Lighting and Safety Measures" : ["b7"] ,
        "Green Spaces and Urban Gardens" : ["b8"] ,
        "Community Libraries and Learning Centers" : ["b9"] ,
        "Public Art and Cultural Events" : ["b10"] ,
    }

    #Street Lighting and Safety Measures
    Electrics = {
        "Street Lamps Establishment" : ["L1" , False] ,
        "Speed Bump Reflectors" : ["L2" , True ]
    }

    investorCat = input("enter interested serial : ")

 

    def prob_Chk(cat):
        for key,value in cat.items():
            if value[1] == True:
                print(key)
            else:
                pass


 

    def display_Prob(investoraCat) :
        if investoraCat[0] == "a" :
            for i,y in Prob_MajorCat.items():
                if y == "a1" :
                    prob_Chk(HID)
                else :
                    pass
        elif investorCat[0] == "b" :
            for i,y in Prob_MajorCat.items():
                if y == "b1" :
                    prob_Chk(Electrics)
        else :
            pass


    display_Prob(investoraCat=investorCat)

matchmaking()

    

        
     
            
 


