#THIS APP WILL TAKE USER INPUT AND RECCOMEND CLUB USE BASED ON AVERAGE DISTANCE...
#USER WILL INDICATE WHETHER THEY ARE A SHORT, MID OR LONG HITTER
#DISTANCE IS IN YARDS
#AVERAGE DISTANCE DATA FROM https://www.golflink.com/tips_5459_average-distance-each-golf-club.html#Men

#THIS PROGRAM IS MEANT TO BE SIMPLE AND SHOW MY UNDERSTANDING OF LOOPS, CLASSES, FUNCTIONS, & OBJECT ORIENTED PROGRAMMING

import sys

class Program():
    def __init__ (self):
                                #sand #pitch #nine #eight #seven  #six  #five  #four  #three  #hybrid #three_wood  #driver
        self.clubs_short_male = [(60), (80), (95), (110), (120), (130), (140), (150), (160),   (170),    (180),     (200)]
                                #[0]                      #[4]                        #[8]                          #[11]

                              #sand  #pitch #nine  #eight #seven  #six  #five  #four  #three  #hybrid #three_wood  #driver
        self.clubs_mid_male = [(80), (105), (115), (130), (140), (145), (150), (160), (180),   (195),    (215),     (230)]
                              #[0]                        #[4]                        #[8]                          #[11]

                                #sand #pitch  #nine  #eight #seven #six   #five  #four  #three   #hybrid  #three_wood #driver
        self.clubs_long_male = [(100), (120), (130), (140), (150), (160), (170), (180), (200),   (210),    (235),     (260)]
                                #[0]                        #[4]                        #[8]                          #[11]

                                  #sand #pitch #nine #eight #seven  #six  #five  #four  #three  #hybrid #three_wood  #driver
        self.clubs_short_female = [(40), (50), (55),  (60),  (65),  (70), (80),  (90),  (100),   (105),    (125),     (150)]
                                  #[0]                       #[4]                       #[8]                          #[11]

                                #sand #pitch #nine #eight #seven  #six  #five  #four  #three  #hybrid #three_wood  #driver
        self.clubs_mid_female = [(50), (60), (70), (80),  (90),  (100), (110), (120), (125),   (135),    (150),     (175)]
                                #[0]                      #[4]                        #[8]                          #[11]

                                 #sand #pitch #nine #eight  #seven #six   #five  #four  #three   #hybrid  #three_wood #driver
        self.clubs_long_female = [(60), (80), (95), (110),  (120), (130), (140), (150),  (160),   (170),    (180),     (200)]
                                 #[0]                       #[4]                         #[8]                          #[11]

        #self.gender_ask()
        #self.sml_ask()
        #self.start_app()
        self.app()

    def app(self):
        print('Hello! Welcome to my Golf Club Reccomendation app. Simply enter your distance to the hole (in yards) and the program will reccomend a club to use based on gender and average hit distance.')
        self.gender_ask()
        self.sml_ask()
        self.start_app()
        again = input('Go again? [enter y or n]: ')
        if again == 'y':
            self.app()
        else:
            sys.exit()


    def sml_ask(self):
        self.answer = input('Are you a Short(s), Mid(m), or Long(l) hitter?\n**EX-> Short hitter five iron = 140 yards \n** --> Mid hitter five iron = 150 yards \n** --> Long hitter five iron = 170\n[enter s, m, or l]: ')
        print(self.answer)

    def gender_ask(self):
        self.mfanswer = input('Are you Male or Female? [enter m or f]: ')
        print(self.mfanswer)

    def distance_ask(self):
        hole_distance = int(input('Enter distance in yards to hole: [numbers only] '))
        return hole_distance


    def start_app(self):
        print('***If you are Tee-ing off 290 yards or further from the hole, \nuse the Driver.***\n')
        hole_distance = self.distance_ask()
        if self.mfanswer == 'm':

            if self.answer == 's':
                if hole_distance >= self.clubs_short_male[0] and hole_distance < self.clubs_short_male[1]:
                    print('Reccomendation: Sand Wedge')
                elif hole_distance >= self.clubs_short_male[1] and hole_distance < self.clubs_short_male[2]:
                    print('Reccomendation: Pitching Wedge')
                elif hole_distance >= self.clubs_short_male[2] and hole_distance < self.clubs_short_male[3]:
                    print('Reccomendation: Nine Iron')
                elif hole_distance >= self.clubs_short_male[3] and hole_distance < self.clubs_short_male[4]:
                    print('Reccomendation: Eight Iron')
                elif hole_distance >= self.clubs_short_male[4] and hole_distance < self.clubs_short_male[5]:
                    print('Reccomendation: Seven Iron')
                elif hole_distance >= self.clubs_short_male[5] and hole_distance < self.clubs_short_male[6]:
                    print('Reccomendation: Six Iron')
                elif hole_distance >= self.clubs_short_male[6] and hole_distance < self.clubs_short_male[7]:
                    print('Reccomendation: Five Iron')
                elif hole_distance >= self.clubs_short_male[7] and hole_distance < self.clubs_short_male[8]:
                    print('Reccomendation: Four Iron')
                elif hole_distance >= self.clubs_short_male[8] and hole_distance < self.clubs_short_male[9]:
                    print('Reccomendation: Three Iron')
                elif hole_distance >= self.clubs_short_male[9] and hole_distance < self.clubs_short_male[10]:
                    print('Reccomendation: Hybrid')
                elif hole_distance >= self.clubs_short_male[10] and hole_distance < self.clubs_short_male[11]:
                    print('Reccomendation: Three Wood')
                elif hole_distance >= self.clubs_short_male[11] and hole_distance < self.clubs_short_male[12]:
                    print('Reccomendation: Driver')
                elif hole_distance < self.clubs_short_male[0] and hole_distance > 15:
                    print('Pitch onto green')
                elif hole_distance < 15:
                    print('Read the line... and putt!')
                else:
                    print('Reccomendation: Driver')

            elif self.answer == 'm':
                if hole_distance >= self.clubs_mid_male[0] and hole_distance < self.clubs_mid_male[1]:
                    print('Reccomendation: Sand Wedge')
                elif hole_distance >= self.clubs_mid_male[1] and hole_distance < self.clubs_mid_male[2]:
                    print('Reccomendation: Pitching Wedge')
                elif hole_distance >= self.clubs_mid_male[2] and hole_distance < self.clubs_mid_male[3]:
                    print('Reccomendation: Nine Iron')
                elif hole_distance >= self.clubs_mid_male[3] and hole_distance < self.clubs_mid_male[4]:
                    print('Reccomendation: Eight Iron')
                elif hole_distance >= self.clubs_mid_male[4] and hole_distance < self.clubs_mid_male[5]:
                    print('Reccomendation: Seven Iron')
                elif hole_distance >= self.clubs_mid_male[5] and hole_distance < self.clubs_mid_male[6]:
                    print('Reccomendation: Six Iron')
                elif hole_distance >= self.clubs_mid_male[6] and hole_distance < self.clubs_mid_male[7]:
                    print('Reccomendation: Five Iron')
                elif hole_distance >= self.clubs_mid_male[7] and hole_distance < self.clubs_mid_male[8]:
                    print('Reccomendation: Four Iron')
                elif hole_distance >= self.clubs_mid_male[8] and hole_distance < self.clubs_mid_male[9]:
                    print('Reccomendation: Three Iron')
                elif hole_distance >= self.clubs_mid_male[9] and hole_distance < self.clubs_mid_male[10]:
                    print('Reccomendation: Hybrid')
                elif hole_distance >= self.clubs_mid_male[10] and hole_distance < self.clubs_mid_male[11]:
                    print('Reccomendation: Three Wood')
                elif hole_distance >= self.clubs_mid_male[11] and hole_distance < self.clubs_mid_male[12]:
                    print('Reccomendation: Driver')
                elif hole_distance < self.clubs_mid_male[0] and hole_distance > 15:
                    print('Pitch onto green')
                elif hole_distance < 15:
                    print('Read the line... and putt!')
                else:
                    print('Reccomendation: Driver')

            elif self.answer == 'l':
                if hole_distance >= self.clubs_long_male[0] and hole_distance < self.clubs_long_male[1]:
                    print('Reccomendation: Sand Wedge')
                elif hole_distance >= self.clubs_long_male[1] and hole_distance < self.clubs_long_male[2]:
                    print('Reccomendation: Pitching Wedge')
                elif hole_distance >= self.clubs_long_male[2] and hole_distance < self.clubs_long_male[3]:
                    print('Reccomendation: Nine Iron')
                elif hole_distance >= self.clubs_long_male[3] and hole_distance < self.clubs_long_male[4]:
                    print('Reccomendation: Eight Iron')
                elif hole_distance >= self.clubs_long_male[4] and hole_distance < self.clubs_long_male[5]:
                    print('Reccomendation: Seven Iron')
                elif hole_distance >= self.clubs_long_male[5] and hole_distance < self.clubs_long_male[6]:
                    print('Reccomendation: Six Iron')
                elif hole_distance >= self.clubs_long_male[6] and hole_distance < self.clubs_long_male[7]:
                    print('Reccomendation: Five Iron')
                elif hole_distance >= self.clubs_long_male[7] and hole_distance < self.clubs_long_male[8]:
                    print('Reccomendation: Four Iron')
                elif hole_distance >= self.clubs_long_male[8] and hole_distance < self.clubs_long_male[9]:
                    print('Reccomendation: Three Iron')
                elif hole_distance >= self.clubs_long_male[9] and hole_distance < self.clubs_long_male[10]:
                    print('Reccomendation: Hybrid')
                elif hole_distance >= self.clubs_long_male[10] and hole_distance < self.clubs_long_male[11]:
                    print('Reccomendation: Three Wood')
                elif hole_distance >= self.clubs_long_male[11] and hole_distance < self.clubs_long_male[12]:
                    print('Reccomendation: Driver')
                elif hole_distance < self.clubs_long_male[0] and hole_distance > 15:
                    print('Pitch onto green')
                elif hole_distance < 15:
                    print('Read the line... and putt!')
                else:
                    print('Reccomendation: Driver')

        elif self.mfanswer == 'f':

            if self.answer == 's':
                if hole_distance >= self.clubs_short_female[0] and hole_distance < self.clubs_short_female[1]:
                    print('Reccomendation: Sand Wedge')
                elif hole_distance >= self.clubs_short_female[1] and hole_distance < self.clubs_short_female[2]:
                    print('Reccomendation: Pitching Wedge')
                elif hole_distance >= self.clubs_short_female[2] and hole_distance < self.clubs_short_female[3]:
                    print('Reccomendation: Nine Iron')
                elif hole_distance >= self.clubs_short_female[3] and hole_distance < self.clubs_short_female[4]:
                    print('Reccomendation: Eight Iron')
                elif hole_distance >= self.clubs_short_female[4] and hole_distance < self.clubs_short_female[5]:
                    print('Reccomendation: Seven Iron')
                elif hole_distance >= self.clubs_short_female[5] and hole_distance < self.clubs_short_female[6]:
                    print('Reccomendation: Six Iron')
                elif hole_distance >= self.clubs_short_female[6] and hole_distance < self.clubs_short_female[7]:
                    print('Reccomendation: Five Iron')
                elif hole_distance >= self.clubs_short_female[7] and hole_distance < self.clubs_short_female[8]:
                    print('Reccomendation: Four Iron')
                elif hole_distance >= self.clubs_short_female[8] and hole_distance < self.clubs_short_female[9]:
                    print('Reccomendation: Three Iron')
                elif hole_distance >= self.clubs_short_female[9] and hole_distance < self.clubs_short_female[10]:
                    print('Reccomendation: Hybrid')
                elif hole_distance >= self.clubs_short_female[10] and hole_distance < self.clubs_short_female[11]:
                    print('Reccomendation: Three Wood')
                elif hole_distance >= self.clubs_short_female[11] and hole_distance < self.clubs_short_female[12]:
                    print('Reccomendation: Driver')
                elif hole_distance < self.clubs_short_female[0] and hole_distance > 15:
                    print('Pitch onto green')
                elif hole_distance < 15:
                    print('Read the line... and putt!')
                else:
                    print('Reccomendation: Driver')

            if self.answer == 'm':
                if hole_distance >= self.clubs_mid_female[0] and hole_distance < self.clubs_mid_female[1]:
                    print('Reccomendation: Sand Wedge')
                elif hole_distance >= self.clubs_mid_female[1] and hole_distance < self.clubs_mid_female[2]:
                    print('Reccomendation: Pitching Wedge')
                elif hole_distance >= self.clubs_mid_female[2] and hole_distance < self.clubs_mid_female[3]:
                    print('Reccomendation: Nine Iron')
                elif hole_distance >= self.clubs_mid_female[3] and hole_distance < self.clubs_mid_female[4]:
                    print('Reccomendation: Eight Iron')
                elif hole_distance >= self.clubs_mid_female[4] and hole_distance < self.clubs_mid_female[5]:
                    print('Reccomendation: Seven Iron')
                elif hole_distance >= self.clubs_mid_female[5] and hole_distance < self.clubs_mid_female[6]:
                    print('Reccomendation: Six Iron')
                elif hole_distance >= self.clubs_mid_female[6] and hole_distance < self.clubs_mid_female[7]:
                    print('Reccomendation: Five Iron')
                elif hole_distance >= self.clubs_mid_female[7] and hole_distance < self.clubs_mid_female[8]:
                    print('Reccomendation: Four Iron')
                elif hole_distance >= self.clubs_mid_female[8] and hole_distance < self.clubs_mid_female[9]:
                    print('Reccomendation: Three Iron')
                elif hole_distance >= self.clubs_mid_female[9] and hole_distance < self.clubs_mid_female[10]:
                    print('Reccomendation: Hybrid')
                elif hole_distance >= self.clubs_mid_female[10] and hole_distance < self.clubs_mid_female[11]:
                    print('Reccomendation: Three Wood')
                elif hole_distance >= self.clubs_mid_female[11] and hole_distance < self.clubs_mid_female[12]:
                    print('Reccomendation: Driver')
                elif hole_distance < self.clubs_mid_female[0] and hole_distance > 15:
                    print('Pitch onto green')
                elif hole_distance < 15:
                    print('Read the line... and putt!')
                else:
                    print('Reccomendation: Driver')

            if self.answer == 'l':
                if hole_distance >= self.clubs_long_female[0] and hole_distance < self.clubs_long_female[1]:
                    print('Reccomendation: Sand Wedge')
                elif hole_distance >= self.clubs_long_female[1] and hole_distance < self.clubs_long_female[2]:
                    print('Reccomendation: Pitching Wedge')
                elif hole_distance >= self.clubs_long_female[2] and hole_distance < self.clubs_long_female[3]:
                    print('Reccomendation: Nine Iron')
                elif hole_distance >= self.clubs_long_female[3] and hole_distance < self.clubs_long_female[4]:
                    print('Reccomendation: Eight Iron')
                elif hole_distance >= self.clubs_long_female[4] and hole_distance < self.clubs_long_female[5]:
                    print('Reccomendation: Seven Iron')
                elif hole_distance >= self.clubs_long_female[5] and hole_distance < self.clubs_long_female[6]:
                    print('Reccomendation: Six Iron')
                elif hole_distance >= self.clubs_long_female[6] and hole_distance < self.clubs_long_female[7]:
                    print('Reccomendation: Five Iron')
                elif hole_distance >= self.clubs_long_female[7] and hole_distance < self.clubs_long_female[8]:
                    print('Reccomendation: Four Iron')
                elif hole_distance >= self.clubs_long_female[8] and hole_distance < self.clubs_long_female[9]:
                    print('Reccomendation: Three Iron')
                elif hole_distance >= self.clubs_long_female[9] and hole_distance < self.clubs_long_female[10]:
                    print('Reccomendation: Hybrid')
                elif hole_distance >= self.clubs_long_female[10] and hole_distance < self.clubs_long_female[11]:
                    print('Reccomendation: Three Wood')
                elif hole_distance >= self.clubs_long_female[11] and hole_distance < self.clubs_long_female[12]:
                    print('Reccomendation: Driver')
                elif hole_distance < self.clubs_long_female[0] and hole_distance > 15:
                    print('Pitch onto green')
                elif hole_distance < 15:
                    print('Read the line... and putt!')
                else:
                    print('Reccomendation: Driver')

if __name__ == '__main__' :
        Program()
