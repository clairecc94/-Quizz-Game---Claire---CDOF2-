class Question:
    def __init__(self,difficulty,answer):
        self.questions = self.Create_Question
        self.difficulty = difficulty
        self.theme = ["Science","History","Geography"]
        self.answer = answer
        self.correct = False

    def Create_Question(self):
        questions = [
        # Science
        Question(
            theme="Science",
            difficulty="Easy",
            question="What planet is known as the Red Planet?",
            options=["Earth", "Mars", "Venus", "Jupiter"],
            correct_answer="Mars"
        ),
        Question(
            theme="Science",
            difficulty="Medium",
            question="What is the chemical symbol for water?",
            options=["H2O", "O2", "CO2", "HO"],
            correct_answer="H2O"
        ),
        Question(
            theme="Science",
            difficulty="Hard",
            question="What is the name of the first element on the periodic table?",
            options=["Oxygen", "Hydrogen", "Helium", "Carbon"],
            correct_answer="Hydrogen"
        ),

        # History
        Question(
            theme="History",
            difficulty="Easy",
            question="Who was the first President of the United States?",
            options=["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"],
            correct_answer="George Washington"
        ),
        Question(
            theme="History",
            difficulty="Medium",
            question="In what year did World War II end?",
            options=["1941", "1945", "1939", "1950"],
            correct_answer="1945"
        ),
        Question(
            theme="History",
            difficulty="Hard",
            question="Who was the ruler of France during the French Revolution?",
            options=["Louis XVI", "Napoleon Bonaparte", "Charles X", "Henry IV"],
            correct_answer="Louis XVI"
        ),

        # Geography
        Question(
            theme="Geography",
            difficulty="Easy",
            question="What is the capital city of France?",
            options=["Berlin", "Madrid", "Paris", "Rome"],
            correct_answer="Paris"
        ),
        Question(
            theme="Geography",
            difficulty="Medium",
            question="What is the largest desert in the world?",
            options=["Sahara", "Gobi", "Antarctic Desert", "Arabian Desert"],
            correct_answer="Antarctic Desert"
        ),
        Question(
            theme="Geography",
            difficulty="Hard",
            question="Which country has the most natural lakes?",
            options=["Canada", "Brazil", "Russia", "United States"],
            correct_answer="Canada"
        )]
        return questions


    def is_correct(self):
        if self.answer.lower == self.questions.correct_answer.lower:
            self.correct = True
        else :
            self.correct = False

    
    def get_question(self,theme,difficulty):
        for q in self.questions:
            if q.theme == theme and q.difficulty == difficulty:
                return q
