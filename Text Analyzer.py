class TextAnalizer():
    def __init__(self, textPath = '', stopWordsPath = '', specialCharacters = []):
       
       self.textPath = textPath
       self.cleanTextList = self.remove_stop_words(textPath, stopWordsPath, specialCharacters)

    def clear_special_characters(self, text, specialCharacters):
        cleanText = ''
        specialCharactersSet = set(specialCharacters)
    
        for char in text:
          if char == '\n':
             char = ' '
          if char not in specialCharactersSet:
             cleanText += char
        
        return cleanText
    
    def get_stop_words_list(self, stopWordsPath):
       try:
          file = open(stopWordsPath, encoding='utf-8')
          stopwords = file.read()
          file.close()

          stopwordsList = stopwords.split('\n')
          
          for stopword in stopwordsList:
             stopword = stopword.strip()

          return stopwordsList
       
       except Exception as error:
        print(f"Error: {error}")

    def get_clean_text_list(self, textPath, specialCharacters):
       try:
          file = open(textPath, encoding='utf-8')
          text = file.read()
          file.close()

          cleanText = self.clear_special_characters(text, specialCharacters)

          cleanText = cleanText.lower()

          cleanTextList = cleanText.split(' ')
          
          while '' in cleanTextList:
             cleanTextList.remove('')

          return cleanTextList
       except Exception as error:
        print(f"Error: {error}")

    def remove_stop_words(self, textPath = '', stopWordsPath = '', specialCharacters = []):
       cleanTextList = self.get_clean_text_list(textPath, specialCharacters)
       stopWordsList = self.get_stop_words_list(stopWordsPath)

       for stopWord in stopWordsList:
          for cleanText in cleanTextList:
            if stopWord == cleanText:
             cleanTextList.remove(stopWord)

       return cleanTextList
    
    def write_clean_text(self):
       with open(self.textPath + '_ooutput.txt', 'w', encoding='utf-8') as outputFile:
          for cleanText in self.cleanTextList:
             outputFile.write(f'{cleanText}\n')
       

filePath = 'raw-text.txt'
stopWordsPath = 'stop-words.txt'
specialCharacters = ['.', '¡', '!', '?', ',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')']

textAnalyzer = TextAnalizer(filePath, stopWordsPath, specialCharacters)

print(textAnalyzer.cleanTextList)
textAnalyzer.write_clean_text()
