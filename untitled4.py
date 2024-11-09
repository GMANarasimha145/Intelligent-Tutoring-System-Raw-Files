import nltk
from nltk.tokenize import sent_tokenize
import random

# Define the input text for which you want to generate quiz questions
input_text = """
C Programming is a foundational language in the world of computer science and software development. It was developed in the early 1970s by Dennis Ritchie at Bell Labs and has since become one of the most widely used and influential programming languages. Known for its efficiency, flexibility, and portability, C has been the basis for the development of many other languages, including C++, Java, and Python. Its syntax is relatively simple and straightforward, making it an excellent choice for beginners to learn programming concepts. C is often used in system programming, embedded programming, and developing operating systems due to its ability to directly interact with hardware and low-level system components.

One of the key features of C Programming is its powerful support for pointers, which allow developers to directly manipulate memory addresses. While this can be challenging for novice programmers, it offers significant advantages in terms of performance and flexibility. Additionally, C provides a rich set of built-in functions and libraries that facilitate various tasks such as input/output operations, string manipulation, and mathematical computations. Its modular structure encourages the development of reusable code components, promoting code maintainability and scalability. Despite its age, C remains a vital language in the software industry, with applications ranging from embedded systems in consumer electronics to high-performance computing in scientific research. Mastering C Programming not only equips individuals with valuable skills but also fosters a deeper understanding of computer architecture and software development principles.
"""

# Tokenize input text into sentences
sentences = sent_tokenize(input_text)

# Define the number of true/false questions to generate
num_questions = 5

# Randomly select sentences to form true/false statements
random_sentences = random.sample(sentences, min(num_questions, len(sentences)))

# Generate true/false quiz questions
quiz_questions = []
for i, sentence in enumerate(random_sentences):
    # Formulate true/false statement
    statement = sentence.strip() + " True or False?"
    
    # Determine the correct answer (True or False)
    correct_answer = random.choice([True, False])
    
    # Generate the question and answer pair
    if correct_answer:
        question = f"Q{i+1}: {statement}"
        answer = f"A{i+1}: True"
    else:
        question = f"Q{i+1}: {statement}"
        answer = f"A{i+1}: False"
    
    quiz_questions.append((question, answer))

# Print generated quiz questions and answers
for question, answer in quiz_questions:
    print(question)
    print(answer)
    print()
