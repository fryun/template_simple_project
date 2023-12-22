import os
import pathlib

CONSTANTA_INT = ["VAR_INT_1", "VAR_INT_2"]
CONSTANTA_BOOL = ["VAR_BOOL_1"]
BOOL_TRUE = "true"

CONFIG_SYMBOL = "="


class Config:
    ROOT_DIR = str(pathlib.Path(__file__).parent.parent.absolute())

    VAR_INT_1:int
    VAR_INT_2:int
    VAR_BOOL_1:bool

    def __init__(self) -> None:
        # print("Load config from config.txt")
        with open("config.txt", "r") as f:
            for line in f.readlines():
                if CONFIG_SYMBOL not in line:
                    continue
                
                text = line.split("=")
                var = text[0]
                value = text[1].replace("\n","")
                
                if var in CONSTANTA_INT:
                    self.__setattr__(var, int(value))
                elif var in CONSTANTA_BOOL:
                    if value == BOOL_TRUE:
                        self.__setattr__(var, True)
                    else:
                        self.__setattr__(var, False)
                else:
                    self.__setattr__(var, value)


config = Config()

