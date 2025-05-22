import emoji

def show_marks(marks):
    if marks >= 90:
        print(emoji.emojize(":smile_cat:", language="alias"))
    elif marks >= 80:
        print(emoji.emojize(":smile:", language="alias"))
    elif marks >= 60:
        print(emoji.emojize(":grinning:", language="alias"))
    else:
        print(emoji.emojize(":crying_cat_face:", language="alias"))

# Get input and call the function
show_marks(int(input("Enter your marks: ")))