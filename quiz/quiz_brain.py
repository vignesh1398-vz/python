class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def ask_question(self):
        index = self.question_number
        return f"Q.{ index + 1 } { self.question_list[index].text } :"

    def evaluate(self, answer):
        if answer == self.question_list[self.question_number].answer:
            self.score += 1