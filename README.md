# AI-8th-Sem-Language-Detection

This is a GitHub repository that I made to submit my AI Assignment. 

At first, we need to instal the necessary libraries using the command 
```
pip install -r requirements.txt
```

The `language_detect1.py` uses the _langdetect_ library which has a support for only 55 languages.

The `language_detect2.py` uses the _fasttext_ library which has a support for only 176 languages, but it uses a model to detect languages. In here, the model _lid.176.ftz_ was used as it is the smallest and the compressed version of their actual model. Although it gives us a reasonably less accuracy and speed compared to the actual model, in the current scenario, this fits the best to our needs.
