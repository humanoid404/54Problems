noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
word = input("Enter a word: ")

print("Do you {} your {} {} {}? That's hilarious!".format(verb, adjective, noun, adverb))

if not len(word) > 4:
    print("... and eventually, everyone died. The End.")
else:
    print("""Suddenly an alien invasion occurred, destroying humanity in the process.
However, you and your comrades who were space traveling during the incident have survived.
You are stunned as you realize the phone call you denied to answer this morning was the last communication to ever happen in the entire human history.
'This is too much' says Hanks.
Hanks is the kind of fellow who groans at his cursed existence every early morning.
'We've decided to leave Reality. Will you join with us?' he asks.
'What do you mean by "leaving reality?". We are trapped by your own existence!'
'Desperate times require desperate measures ... including ending your lives.'""")
    choice = input("Your comrades are committing suicide. Will you join?")
    if choice:
        print("""As you depart from this world, you begin to forget your existence.
Why did this happen?
What brought me here in the first place?
Who am I?
And then suddenly you remember who you are, why you are here, and that there is nothing to worry about what has happened.
Everything wasn't real.
Your entire existence was just a dream of somebody else.
The End.""")
    else:
        print("""You refuse to die.
Now you are the sole survivor of the planet Earth.
Nobody is here.
Nobody will be ever again.
You are all alone.
Weak and horrified.
Too scared to move, you stay still.
Among the silence.
The End.""")
