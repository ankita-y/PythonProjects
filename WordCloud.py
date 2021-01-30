from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

stopwords = set(STOPWORDS)
def count_word(letters):
    #split the values
    words = letters.split()
    comment_Word =''
    for word in words:
        word.lower()
        comment_Word += "".join(word)+" "

    #comment_Word += " ".join(words)+" "

    wordcloud = WordCloud(width=800, height = 200, background_color='black',
                          stopwords = stopwords,min_font_size=7).generate(comment_Word)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()

print(count_word("python Django Data DataScience debug ML AI javascript HTML CSS Flask agile"))
