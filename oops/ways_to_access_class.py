class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

## CODE DUPLICATION || NOT IDEAL

# class GingerChai(Chai):
#     def __init__(self,type_,strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level

## EXPLICIT CALL || CAN BE USED BUT NOT PREFERRED

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level

## SUPER() || SHOULD BE USED

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level