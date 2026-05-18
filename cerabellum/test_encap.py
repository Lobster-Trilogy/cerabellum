from config import Config
from encapsulator import encapsulate
from visualiser import visualise
from formatter import format_script 

config = Config("data/characters.yaml")
lelouch = config.get_character("lelouch")
print(encapsulate(lelouch))
print(visualise(lelouch))
format_script("act1_standardDeviation_notation_1.md", "output/act1_testoutput.rpy")