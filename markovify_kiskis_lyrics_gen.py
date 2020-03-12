#Генерируем тексты песен Кис Кис цепями Маркова
import markovify

with open("kiskis_lyrics.txt",encoding='utf-8') as f:
    text = f.read()
text_model = markovify.Text(text)
for i in range(10):
    print(text_model.make_short_sentence(380))