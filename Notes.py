import pyperclip

name = input("Enter your name: ")
subject_pronoun = input("Enter your subject pronoun (he/she/they): ")
object_pronoun = input("Enter your object pronoun (him/her/them): ")
possessive_pronoun = input("Enter your possessive pronoun (his/her/their): ")
clean_task = input("Enter the cleaning task you want to perform: ")

# Labeled phrases
phases = [
    f"(CRR Not Home)Towards improving {possessive_pronoun} independent living skills, {name} did not work on any goals throughout the shift due to being away from the home. Staff will remain available to {name} should {subject_pronoun} have any needs as {subject_pronoun} works towards improving {possessive_pronoun} independent living skills.",
    f"(Respite Not Home){name} was away from the home in the community throughout the entire shift. Staff will remain available to {object_pronoun} should {subject_pronoun} have any needs while {subject_pronoun} continues {possessive_pronoun} respite stay.",
    f"(Respite)Staff observed that {subject_pronoun} had socialized with {possessive_pronoun} peers throughout the shift. Staff observed {name} completing {possessive_pronoun} household task, needing no assistance. {name} reported independently for {possessive_pronoun} evening medications and was observed by staff as {subject_pronoun} dispensed each medication, stating name and dosage. Staff will remain available, should {subject_pronoun} have any needs for {possessive_pronoun} respite stay. Staff observed that {subject_pronoun} had socialized with {possessive_pronoun} peers throughout the shift. Staff observed {name} completing {possessive_pronoun} household task, needing no assistance. {name} reported independently for {possessive_pronoun} evening medications and was observed by staff as {subject_pronoun} dispensed each medication, stating name and dosage. Staff will remain available, should {subject_pronoun} have any needs for {possessive_pronoun} respite stay.",
    f"(Housekeeping)Towards improving on {possessive_pronoun} housekeeping skills, {name} was able to {clean_task} without being prompted by staff. Staff observed that {subject_pronoun} was able to complete the task without needing staff assistance. Staff will continue to be available, should {subject_pronoun} require any assistance from staff, to improve {possessive_pronoun} housekeeping skills.",
    f"(Managing Medications)Towards the goal of independently managing medications, {name} was able to report on time and also recite back the names and dosages of the medication dispensed to staff. Staff will continue to remain available for {name} if {subject_pronoun} needs any assistance, as {subject_pronoun} works towards independently managing {possessive_pronoun} medications.",
    f"( Healthy Food)Towards working on making healthy food choices, staff observed that {name} was able to eat a balanced diet. Staff will remain available to {object_pronoun}, should {subject_pronoun} have any needs of assistance, as {subject_pronoun} works towards improving {possessive_pronoun} diet."
]

print("Select a phrase:")
for i, phrase in enumerate(phases):
    print(f"{i+1}. {phrase}")

try:
    selection = int(input("Enter the number of the phrase you want to copy: "))
    selected_phrase = phases[selection-1].replace("{name}", name).replace("{subject_pronoun}", subject_pronoun).replace("{object_pronoun}", object_pronoun).replace("{possessive_pronoun}", possessive_pronoun)
    print(f"Selected phrase: {selected_phrase}")
    # Copy the selected phrase to the clipboard using the pyperclip module
    pyperclip.copy(selected_phrase)
    print("Phrase copied to clipboard!")
except (ValueError, IndexError):
    print("Invalid selection. Please enter a number between 1 and 4.")

input("Press Enter to exit.")
