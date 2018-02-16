from yandex_translate import YandexTranslate
translate = YandexTranslate('trnsl.1.1.20180216T133517Z.9eb599729cc6f038.adb96ddcd04c34e7cae27de0693a36930d6b1c08')

class YandexTranslator:

    def __init__(self, input_text, output_lang, input_lang = ''):
        if input_lang == '':
            self.lang = '' + output_lang + ''
        else:
            self.lang = '' + output_lang + '-' + input_lang + ''
        self.text = input_text

    def transl(self, text, lang):
        output = translate.translate(text, lang).get('text')
        answer = output[0]
        return answer

        

if __name__ == '__main__':
    input_text = 'привет?'
    # input_lang = 'ru'
    output_lang = 'en'
    
    yad = YandexTranslator(input_text, output_lang)
    # print(yad.lang, yad.text)
    print(yad.transl(yad.text, yad.lang))
    # print(yad.detect_lang(yad.text))