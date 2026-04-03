from p8 import anagram_check

print("Running Anagram Tests...")

print("listen, silent:", anagram_check("listen", "silent"))
print("debit card, Bad credit:", anagram_check("debit card", "Bad credit"))
print("hello, bye:", anagram_check("hello", "bye"))
print("restful, fluster:", anagram_check("restful", "fluster"))
print("listen, silentt:", anagram_check("listen", "silentt"))
print("Conversation, Voices, rant on:", anagram_check("Conversation", "Voices, rant on"))

assert anagram_check("listen", "silent") == True
assert anagram_check("debit card", "Bad credit") == True
assert anagram_check("hello", "bye") == False
assert anagram_check("restful", "fluster") == True
assert anagram_check("listen", "silentt") == False
assert anagram_check("Conversation", "Voices, rant on") == True

print("Test p8 passed\n")