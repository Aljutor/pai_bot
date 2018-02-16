from yandex_translate import YandexTranslate
translate = YandexTranslate('trnsl.1.1.20180216T133517Z.9eb599729cc6f038.adb96ddcd04c34e7cae27de0693a36930d6b1c08')

class YandexTranslator:

    def __init__(self, input_text, output_lang = 'English', input_lang = ''):
        if input_lang == '':
            self.lang = '' + output_lang + ''
        else:
            self.lang = '' + output_lang + '-' + input_lang + ''
        self.text = input_text

    def transl(self, text, lang):
        output = translate.translate(text, lang).get('text')
        answer = output[0]
        return answer

    def select_lang(self, some_text):
        d = {}

        with open("l.txt" , "r+") as file:

            for line in file:

                a = line.split(' ')
                a[2] = a[2].split('\n')[0]
                d.update({a[0]: a[2].lower()})

        for k, v in d.items():
            if v == some_text:
                return k
            else:
                return None

        

if __name__ == '__main__':
    input_text = 'привет?'
    # input_lang = 'ru'
    # output_lang = 'en'
    
    yad = YandexTranslator(input_text)
    # print(yad.lang, yad.text)
    print(yad.transl(yad.text, yad.lang))
    # print(yad.detect_lang(yad.text))