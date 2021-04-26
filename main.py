from Logic import Logic
from UI import UI


def main():
    logic = Logic()
    logic.get_max_scores_from_file()
    UI(logic)


main()
