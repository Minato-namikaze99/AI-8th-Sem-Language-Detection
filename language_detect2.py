import fasttext

# Download a language identification model from fasttext
model = fasttext.load_model('lid.176.ftz')  # Pre-trained model available on fasttext's website

def detect_language(sentence):
    predictions = model.predict(sentence)
    return predictions[0][0].replace('__label__', '')


lang1="I am a student learning Python programming." #english
lang2="Я студент, изучающий программирование на Python." #russian
lang3="私はPythonプログラミングを学んでいる学生です。" #japanese
lang4="আমি পাইথন প্রোগ্রামিং শেখার একজন ছাত্র।" #bengali

print("The sentence \""+lang1+"\" has the following language code - "+detect_language(lang1))
print("The sentence \""+lang2+"\" has the following language code - "+detect_language(lang2))
print("The sentence \""+lang3+"\" has the following language code - "+detect_language(lang3))
print("The sentence \""+lang4+"\" has the following language code - "+detect_language(lang4))
