from QuestionsParser import QuestionsParser

PATH_TO_PDF = "./Questions.pdf"


def main():
    answers = QuestionsParser(PATH_TO_PDF, remainder_mod=(0, 5)).parse_google()
    answers.write_to_file("./tests/result_lecture_3_test.docx", header="Answers OOP Lecture 3")


if __name__ == "__main__":
    main()
