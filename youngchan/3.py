quote = input("What is the quote?\n")
author = input("Who said it?\n")
print("\n", author, " says,", "\n\"", quote, "\"", sep="")

author_quote = {"Simone de Beauvoir": "Change your life today. Don't gamble on the future, act now, without delay.",
                "Og Mandino": "Failure will never overtake me if my determination to succeed is strong enough.",
                "Charles R. Swindoll": "Life is 10% what happens to you and 90% how you react to it.",
                "Nelson Mandela": "It always seems impossible until it's done.",
                "Confucius": "It does not matter how slowly you go as long as you do not stop."}

for author in author_quote:
    print("\n", author, " says,", "\n\"", author_quote[author], "\"", sep="")
