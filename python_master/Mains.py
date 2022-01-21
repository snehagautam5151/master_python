import enum

class Drivetrain(enum.Enum):
    manual = 1
    automatic = 2
    electric = 3
    
for dt in (Drivetrain):
    print(dt)

	