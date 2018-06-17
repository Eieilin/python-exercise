class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
              The Gothons of Planet Percal #25 have invaded your ship and
              destroyed your entire crew. You are the last ...
              """))
        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                  Quick on the draw you yank out 
                  it at the 
                  """))
            return 'death'
        elif action == "dodge!":
            print(dedent("""
                  Like a world class 
                  slide right as the
                  """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                  Lucky for you they made you learn 
                  the academy.
                  """))
            return 'laser_weapon_armory'
        
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

