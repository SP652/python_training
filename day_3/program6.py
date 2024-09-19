class Patient:
    def __init__(self,id,name) -> None:
        self.name=name
        self.id=id

    def __str__(self) -> str:
        return f'id:{self.id},name:{self.name}'
    
    def __repr__(self) -> str:
        return self.__str__()