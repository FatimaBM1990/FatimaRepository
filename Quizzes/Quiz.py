import random

questions = {
    'js': {
        'easy': [
            ("What does JS stand for?", "JavaScript"),
            ("Which company developed JavaScript?", "Netscape"),
            ("Which symbol is used for comments in JavaScript?", "//"),
            ("What keyword is used to declare a variable in JavaScript?", "var"),
            ("How do you write 'Hello World' in an alert box?", "alert('Hello World')"),
            ("Which method is used to write HTML output in JavaScript?", "document.write()"),
            ("What is the correct syntax for referring to an external script?", "<script src='filename.js'>"),
            ("How do you create a function in JavaScript?", "function myFunction()"),
            ("How do you call a function named 'myFunction'?", "myFunction()"),
            ("How to write an IF statement in JavaScript?", "if (condition)")
        ],
        'medium': [
            ("How do you add a comment in JavaScript?", "// comment"),
            ("What is the correct way to write a JavaScript array?", "var colors = ['red', 'green', 'blue']"),
            ("How do you round the number 7.25 to the nearest integer?", "Math.round(7.25)"),
            ("How do you find the number with the highest value of x and y?", "Math.max(x, y)"),
            ("What is the correct JavaScript syntax for opening a new window?", "window.open()"),
            ("JavaScript is the same as Java.", "False"),
            ("Which event occurs when the user clicks on an HTML element?", "onclick"),
            ("How do you declare a JavaScript variable?", "var x"),
            ("What is the correct way to write a JavaScript object?", "var obj = {key: 'value'}"),
            ("Which operator is used to assign a value to a variable?", "=")
        ],
        'hard': [
            ("How do you write a conditional statement for executing some statements only if 'i' is equal to 5?", "if (i == 5)"),
            ("How can you detect the client's browser name?", "navigator.appName"),
            ("How to insert a comment that has more than one line?", "/* comment */"),
            ("What will the following code return: Boolean(10 > 9)", "True"),
            ("What is the correct JavaScript syntax to change the content of the HTML element below?", "document.getElementById('demo').innerHTML = 'Hello'"),
            ("Where is the correct place to insert a JavaScript?", "Both the <head> section and the <body> section are correct"),
            ("What is the correct syntax for referring to an external script called 'xxx.js'?", "<script src='xxx.js'>"),
            ("An external JavaScript must contain the <script> tag.", "False"),
            ("How do you create a function in JavaScript named myFunction?", "function myFunction()"),
            ("How do you write a JavaScript array?", "var array = ['item1', 'item2']")
        ]
    },
    'css': {
        'easy': [
            ("What does CSS stand for?", "Cascading Style Sheets"),
            ("Which HTML attribute is used to define inline styles?", "style"),
            ("Which property is used to change the background color?", "background-color"),
            ("Which CSS property controls the text size?", "font-size"),
            ("Which property is used to change the font of an element?", "font-family"),
            ("How do you make the text bold?", "font-weight"),
            ("Which property is used to change the text color?", "color"),
            ("How do you add a background color for all <h1> elements?", "h1 {background-color: #fff}"),
            ("How do you add a background color for a div element?", "div {background-color: #fff}"),
            ("How do you select an element with id 'demo'?", "#demo")
        ],
        'medium': [
            ("Which property is used to change the left margin of an element?", "margin-left"),
            ("How do you make each word in a text start with a capital letter?", "text-transform: capitalize"),
            ("How do you select elements with class name 'test'?", ".test"),
            ("Which property is used to change the right margin of an element?", "margin-right"),
            ("Which property is used to change the left padding of an element?", "padding-left"),
            ("Which property is used to change the right padding of an element?", "padding-right"),
            ("Which property is used to center text?", "text-align: center"),
            ("How do you display a border like this: The top border = 10 pixels, bottom border = 5 pixels, left border = 20 pixels and right border = 1pixel?", "border-width: 10px 1px 5px 20px"),
            ("Which property is used to change the top margin of an element?", "margin-top"),
            ("How do you make a list that lists its items with squares?", "list-style-type: square")
        ],
        'hard': [
            ("Which CSS property is used to change the text color of an element?", "color"),
            ("Which CSS property controls the text size?", "font-size"),
            ("How do you make each word in a text start with a capital letter?", "text-transform: capitalize"),
            ("Which property is used to change the background color?", "background-color"),
            ("Which CSS property is used to change the left margin of an element?", "margin-left"),
            ("Which property is used to change the top padding of an element?", "padding-top"),
            ("Which property is used to change the bottom padding of an element?", "padding-bottom"),
            ("How do you select an element with id 'demo'?", "#demo"),
            ("Which property is used to change the top margin of an element?", "margin-top"),
            ("How do you make each word in a text start with a capital letter?", "text-transform: capitalize")
        ]
    },
    'html': {
        'easy': [
            ("What does HTML stand for?", "HyperText Markup Language"),
            ("What is the correct HTML element for inserting a line break?", "<br>"),
            ("What is the correct HTML element for the largest heading?", "<h1>"),
            ("How can you make a numbered list?", "<ol>"),
            ("How can you make a bulleted list?", "<ul>"),
            ("What is the correct HTML element to define important text?", "<strong>"),
            ("What is the correct HTML element to define emphasized text?", "<em>"),
            ("Which HTML element is used to specify a footer for a document or section?", "<footer>"),
            ("What is the correct HTML element to define a paragraph?", "<p>"),
            ("What is the correct HTML element to define a table?", "<table>")
        ],
        'medium': [
            ("Which character is used to indicate an end tag?", "/"),
            ("What is the correct HTML for adding a background color?", "<body style='background-color:yellow;'>"),
            ("Choose the correct HTML element to define the title of a document.", "<title>"),
            ("Which HTML attribute specifies an alternate text for an image, if the image cannot be displayed?", "alt"),
            ("What is the correct HTML for creating a hyperlink?", "<a href='http://www.google.com'>Google</a>"),
            ("Which HTML element defines navigation links?", "<nav>"),
            ("Which HTML attribute specifies a unique id for an element?", "id"),
            ("How can you open a link in a new tab/browser window?", "<a href='url' target='_blank'>"),
            ("Which HTML element is used to specify a header for a document or section?", "<header>"),
            ("What is the correct HTML for inserting an image?", "<img src='image.jpg' alt='MyImage'>")
        ],
        'hard': [
            ("Which HTML attribute is used to define inline styles?", "style"),
            ("Which HTML element is used to specify a footer for a document or section?", "<footer>"),
            ("Which HTML element defines navigation links?", "<nav>"),
            ("What is the correct HTML for creating a hyperlink?", "<a href='http://www.google.com'>Google</a>"),
            ("How can you open a link in a new tab/browser window?", "<a href='url' target='_blank'>"),
            ("Which HTML element is used to specify a header for a document or section?", "<header>"),
            ("Which character is used to indicate an end tag?", "/"),
            ("How can you make a numbered list?", "<ol>"),
            ("How can you make a bulleted list?", "<ul>"),
            ("What is the correct HTML element to define a table?", "<table>")
        ]
    },
    'python': {
        'easy': [
            ("What is the correct file extension for Python files?", ".py"),
            ("How do you create a variable with the numeric value 5?", "x = 5"),
            ("What is the correct syntax to output 'Hello World' in Python?", "print('Hello World')"),
            ("Which method can be used to remove any whitespace from both the beginning and the end of a string?", "strip()"),
            ("Which operator is used to multiply numbers?", "*"),
            ("Which operator is used to add together two values?", "+"),
            ("Which operator is used to divide two numbers?", "/"),
            ("Which operator can be used to compare two values?", "=="),
            ("Which statement is used to stop a loop?", "break"),
            ("Which method can be used to return the length of a string?", "len()")
        ],
        'medium': [
            ("How do you create a variable with the floating number 2.8?", "x = 2.8"),
            ("How do you create a variable with the numeric value 5?", "x = 5"),
            ("What is the correct file extension for Python files?", ".py"),
            ("Which method can be used to return a string in upper case letters?", "upper()"),
            ("Which method can be used to replace parts of a string?", "replace()"),
            ("Which operator can be used to compare two values?", "=="),
            ("Which statement is used to stop a loop?", "break"),
            ("Which method can be used to remove any whitespace from both the beginning and the end of a string?", "strip()"),
            ("Which method can be used to return the length of a string?", "len()"),
            ("How do you insert COMMENTS in Python code?", "#")
        ],
        'hard': [
            ("Which collection is ordered, changeable, and allows duplicate members?", "list"),
            ("Which collection is unordered, changeable, and does not allow duplicate members?", "dictionary"),
            ("How do you start writing a function in Python?", "def myFunction():"),
            ("How do you start writing a for loop in Python?", "for x in range(0, 10):"),
            ("How do you start writing an if statement in Python?", "if x > y:"),
            ("How do you start writing a while loop in Python?", "while x > y:"),
            ("How do you create a dictionary in Python?", "myDict = {'key': 'value'}"),
            ("How do you access a specific element in a list?", "myList[0]"),
            ("How do you add an element to a list?", "myList.append('element')"),
            ("How do you remove an element from a list?", "myList.remove('element')")
        ]
    }
}

def get_questions(language, difficulty):
    return random.sample(questions[language][difficulty], 10)

def ask_question(question):
    print(question[0])
    answer = input("Your answer: ")
    return answer.lower() == question[1].lower()

def main():
    print("Welcome to the quiz game!")
    language = input("Choose a language (js, css, html, python): ").lower()
    difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()
    
    if language not in questions or difficulty not in questions[language]:
        print("Invalid language or difficulty!")
        return

    quiz_questions = get_questions(language, difficulty)
    score = 0
    
    for question in quiz_questions:
        if ask_question(question):
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was: {question[1]}")
    
    print(f"Your final score is: {score} out of 10")

if __name__ == "__main__":
    main()
