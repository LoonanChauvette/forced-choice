

class Staircase(): 
    def __init__(self, initial_level):

        # Parameters
        self.current_level = initial_level
        self.step_size = 2
        self.n_down = 2
        self.max_reversal = 4
        
        # Status
        self.current_step = 0
        self.direction = "ascending"
        self.plateau = 0
        self.reversals = 0

        # Data
        self.data=[]
        self.reversal_data = []

    def debug(self):
        print(f"Current step : {self.current_step}")
        print(f"Current level : {self.current_level}")
        print(f"Direction : {self.direction}")	
        print(f"Reversals : {self.reversals}")
        print(f"Reversal data : {self.reversal_data}")
        print(f"Plateau : {self.plateau}")
        print(f"______________")

    def decrement(self):
        self.current_level -= self.step_size

    def increment(self):
        self.current_level += self.step_size

    def switch_direction(self):
        return "ascending" if self.direction == "descending" else "descending"

    def reversal(self):
        self.reversal_data.append(self.current_level)
        if self.reversals >= self.max_reversal:
            print("complete")
            exit()
        self.reversals += 1
        self.direction = self.switch_direction()
        self.plateau = 0
        if self.direction == "descending":
            self.decrement()
        elif self.direction == "ascending":
            self.increment()

    def step(self, answer): 
        self.current_step += 1
        self.data.append((self.current_step, self.current_level))

        if answer == "correct" and self.direction == "ascending":
            self.plateau += 1
            if self.plateau >= self.n_down:
                self.reversal()

        elif answer == "correct" and self.direction == "descending":
            self.decrement()

        elif answer == "incorrect" and self.direction == "ascending":
            self.plateau = 0
            self.increment()

        elif answer == "incorrect" and self.direction == "descending":
            self.reversal()
            
if __name__ == "__main__":
    staircase = Staircase(initial_level=50)
    staircase.debug()
    staircase.step("correct")
    staircase.debug()
    staircase.step("correct")
    staircase.step("correct")
    staircase.step("correct")
    staircase.step("correct")
    staircase.debug()

    staircase.step("incorrect")
    staircase.debug()
    staircase.step("correct")
    staircase.debug()
    staircase.step("incorrect")
    staircase.debug()
    staircase.step("correct")
    staircase.step("correct")
    staircase.debug()
