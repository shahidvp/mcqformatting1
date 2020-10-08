#mcqformatting
Its a simple python gui application using GUI.
The application takes in text data and formats it to a specific pattern, returns the same text if no match is found.
The main use case was copying text from pdf where new line character get lost in the destination formatting, so it replaces new line characters with a space.
The uses are copying a question ( numbered in the format "n." where n is any number) and a set of answers (numbered in the format "n)" where n is any number). 
User can copy the text to the application text field. After pressing the convert button, it return the formatted text from which the user can copy.
example for formatted text:
      1. How old are you ?
      1) One
      2) Too old
      3) Yound
      4) No answer
      
The input should also be similar to this.



Notes:
My use case was creating a set of multiple choice questions in google forms copied from a pdf, usually google forms saves every change made which makes editing online a bit slow, so a preformated text saves a lot of time. 
