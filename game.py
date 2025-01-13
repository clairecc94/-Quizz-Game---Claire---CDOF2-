from question import get_question
class Game:
    def __init__(self):
        self.score = 0
        self.current_question_index = 0

    def display_question(self, question):
        print(f"Theme: {question.theme} | Difficulty: {question.difficulty}")
        print(question.question)
        for i, option in enumerate(question.options, start=1):
            print(f"{i}. {option}")

    def get_user_answer(self, question):
        while True:
            try:
                user_input = int(input("Enter the number of your choice: "))
                if 1 <= user_input <= len(question.options):
                    return question.options[user_input - 1]
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play(self,question, theme, difficulty):
        for t in question.theme:
                questions = get_question(t, difficulty)

            if not questions:
                print("No questions available for this theme and difficulty.")
                return

            for question in questions:
                print("\n" + "=" * 40)
                self.display_question(question)
                user_answer = self.get_user_answer(question)

                if question.is_correct(user_answer):
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer was: {question.correct_answer}")

        print("\n" + "=" * 40)
        print(f"End of round. Your score: {self.score}")

    def start(self):
        print("Welcome to the Quiz Game!")
        while True:
            print("\nAvailable Difficulties: Easy, Medium, Hard")
            difficulty = input("Choose a difficulty: ").capitalize()

            self.play(question,difficulty)

            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again != "yes":
                break

        print("\nThanks for playing! Final Score:", self.score)

