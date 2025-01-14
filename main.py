import random

class Question:
    def __init__(self, difficulty, answer):
        self.questions = self.Create_Question()
        self.difficulty = difficulty
        self.theme = ["Science", "History", "Geography","Art", "Sport"]
        self.answer = answer
        self.correct = False
        self.current_question = None

    def Create_Question(self):
        questions = [
            # Science
            {
                "theme": "Science",
                "difficulty": "Easy",
                "question": "What planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Venus", "Jupiter"],
                "correct_answer": "Mars",
            },
            {
                "theme": "Science",
                "difficulty": "Medium",
                "question": "What is the chemical symbol for water?",
                "options": ["H2O", "O2", "CO2", "HO"],
                "correct_answer": "H2O",
            },
            {
                "theme": "Science",
                "difficulty": "Hard",
                "question": "What is the name of the first element on the periodic table?",
                "options": ["Oxygen", "Hydrogen", "Helium", "Carbon"],
                "correct_answer": "Hydrogen",
            },
            # History
            {
                "theme": "History",
                "difficulty": "Easy",
                "question": "Who was the first President of the United States?",
                "options": ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"],
                "correct_answer": "George Washington",
            },
            {
                "theme": "History",
                "difficulty": "Medium",
                "question": "In what year did World War II end?",
                "options": ["1941", "1945", "1939", "1950"],
                "correct_answer": "1945",
            },
            {
                "theme": "History",
                "difficulty": "Hard",
                "question": "Who was the ruler of France during the French Revolution?",
                "options": ["Louis XVI", "Napoleon Bonaparte", "Charles X", "Henry IV"],
                "correct_answer": "Louis XVI",
            },
            # Geography
            {
                "theme": "Geography",
                "difficulty": "Easy",
                "question": "What is the capital city of France?",
                "options": ["Berlin", "Madrid", "Paris", "Rome"],
                "correct_answer": "Paris",
            },
            {
                "theme": "Geography",
                "difficulty": "Medium",
                "question": "What is the largest desert in the world?",
                "options": ["Sahara", "Gobi", "Antarctic Desert", "Arabian Desert"],
                "correct_answer": "Antarctic Desert",
            },
            {
                "theme": "Geography",
                "difficulty": "Hard",
                "question": "Which country has the most natural lakes?",
                "options": ["Canada", "Brazil", "Russia", "United States"],
                "correct_answer": "Canada",
            },
            # Art
            {
                "theme": "Art",
                "difficulty": "Easy",
                "question": "Who painted the Mona Lisa?",
                "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
                "correct_answer": "Leonardo da Vinci",
            },
            {
                "theme": "Art",
                "difficulty": "Medium",
                "question": "Which artist is famous for the painting 'The Persistence of Memory'?",
                "options": ["Claude Monet", "Salvador Dalí", "Vincent van Gogh", "Pablo Picasso"],
                "correct_answer": "Salvador Dalí",
            },
            {
                "theme": "Art",
                "difficulty": "Hard",
                "question": "In what year was Picasso's painting 'Guernica' completed?",
                "options": ["1937", "1945", "1929", "1951"],
                "correct_answer": "1937",
            },
            # Sport
            {
                "theme": "Sport",
                "difficulty": "Easy",
                "question": "How many players are there in a soccer team on the field?",
                "options": ["10", "11", "12", "9"],
                "correct_answer": "11",
            },
            {
                "theme": "Sport",
                "difficulty": "Medium",
                "question": "In which year were the first modern Olympic Games held?",
                "options": ["1896", "1900", "1924", "1888"],
                "correct_answer": "1896",
            },
            {
                "theme": "Sport",
                "difficulty": "Hard",
                "question": "Which country has won the most FIFA World Cups?",
                "options": ["Germany", "Italy", "Argentina", "Brazil"],
                "correct_answer": "Brazil",
            },
        ]
        return questions

    def is_correct(self):
        """Check if the answer is correct for the current question."""
        if self.current_question and self.answer.lower() == self.current_question["correct_answer"].lower():
            self.correct = True
        else:
            self.correct = False

    def get_question(self, theme, difficulty):
        return [
            q
            for q in self.questions
            if q["theme"] == theme and q["difficulty"] == difficulty
        ]
class Game:
    def __init__(self):
        self.score = 0
        self.congratulations = [
            "Great job! That's correct! 🎉",
            "Well done, you nailed it! 🌟",
            "Amazing, that's the right answer! 🚀",
            "Fantastic! Keep it up! 🏆",
            "Impressive work, that's correct! 🙌",
            "You're unstoppable! Excellent answer! 🔥",
            "Brilliant! You're on a roll! 💡",
            "Spot on! You're a genius! 🧠",
            "Correct! You're crushing it! 🏅",
            "Nice work! You're doing amazing! 🎯",
            "Perfect answer! Keep the streak alive! 🎶",
            "That's it! You're on fire! 🔥",
            "Excellent! Keep those answers coming! 💪",
            "You’ve got it! Great thinking! 🧐",
            "Absolutely correct! You’re a star! 🌟",
        ]

        self.encouragements = [
            "Don't worry, you'll get the next one! 💪",
            "Keep going, you can do it! 🌟",
            "That was close, try again! 🔄",
            "No problem, you'll get it next time! 🌈",
            "Don't give up, you're doing great! ✨",
            "Mistakes are part of learning! Keep at it! 📘",
            "You’re improving with every question! 🔧",
            "Almost there! Keep your head up! 🌟",
            "Don't sweat it, you'll ace the next one! 🍀",
            "Stay positive! You're doing well! 😊",
            "You're on the right track, keep going! 🛤️",
            "Take a deep breath and try again! 🌬️",
            "You’ve got this, don’t lose hope! 🌈",
            "Every mistake is a step towards success! 🪜",
            "Stay focused! Success is just ahead! 🎯",
        ]


    def display_question(self, question):
        print(f"Theme: {question['theme']} | Difficulty: {question['difficulty']}")
        print(question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

    def get_user_answer(self, question):
        while True:
            try:
                user_input = int(input("Enter the number of your choice: "))
                if 1 <= user_input <= len(question["options"]):
                    return question["options"][user_input - 1]
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play(self, question_obj, theme, difficulty):
        questions = question_obj.get_question(theme, difficulty)

        if not questions:
            print("No questions available for this theme and difficulty.")
            return

        for question in questions:
            print("\n" + "=" * 40)
            self.display_question(question)
            question_obj.current_question = question
            user_answer = self.get_user_answer(question)

            # Check if the answer is correct
            question_obj.answer = user_answer
            question_obj.is_correct()

            if question_obj.correct:
                print("Correct!")
                print(random.choice(self.congratulations))
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {question['correct_answer']}")
                print(random.choice(self.encouragements))

        print("\n" + "=" * 40)
        print(f"End of round. Your score: {self.score}")

    def start(self):
        print("Welcome to the Quiz Game!")
        question_obj = Question(difficulty="", answer="")

        while True:
            print("\nAvailable Themes: Science, History, Geography, Art, Sport")
            theme = input("Choose a theme: ").capitalize()
            if theme not in question_obj.theme:
                print("Invalid theme. Please choose from the available themes.")
                continue

            print("\nAvailable Difficulties: Easy, Medium, Hard")
            difficulty = input("Choose a difficulty: ").capitalize()
            if difficulty not in ["Easy", "Medium", "Hard"]:
                print("Invalid difficulty. Please choose from Easy, Medium, or Hard.")
                continue

            self.play(question_obj, theme, difficulty)

            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again != "yes":
                break

        print("\nThanks for playing! Final Score:", self.score)


if __name__ == "__main__":
    game = Game()
    game.start()
