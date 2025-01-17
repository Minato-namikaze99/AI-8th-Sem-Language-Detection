# Python program to demonstrate 
 
from langdetect import detect

# gives the output as language codes

lang1="I am a student learning Python programming." #english
lang2="Я студент, изучающий программирование на Python." #russian
lang3="私はPythonプログラミングを学んでいる学生です。" #japanese
lang4="আমি পাইথন প্রোগ্রামিং শেখার একজন ছাত্র।" #bengali

print("The sentence \""+lang1+"\" has the following language code - "+detect(lang1))
print("The sentence \""+lang2+"\" has the following language code - "+detect(lang2))
print("The sentence \""+lang3+"\" has the following language code - "+detect(lang3))
print("The sentence \""+lang4+"\" has the following language code - "+detect(lang4))
