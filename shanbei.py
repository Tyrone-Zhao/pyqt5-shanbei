import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow
import requests
import json


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.url1 = "https://www.shanbay.com/api/v1/vocabtest/category/"
        self.url2 = "https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category="
        self.url3 = "https://www.shanbay.com/api/v1/vocabtest/vocabularies/"
        # 获取对应词库的url名称
        self.choices = []
        self.getVocabularyLexicon()
        # 存储获取到的单词
        self.words = []
        # 存储用户勾选的单词, 及这个单词是第几个单词
        self.words_knows = []
        self.position = []
        # 存储用户未勾选的单词
        self.not_knows = []
        # 第二次请求的内容
        self.js_src2 = None
        self.lexicon = None
        # 存储第四页内容
        self.word_ranks = []
        self.right_ranks = []
        self.wrong_words = []
        self.num = 0
        self.dic = []
        self.dic2 = {}
        self.re_dic = {}

        # 第二页按钮点击事件
        self.GMATButton.clicked.connect(lambda: self.secondButtonClicked(self.GMATButton))
        self.mbaButton.clicked.connect(lambda: self.secondButtonClicked(self.mbaButton))
        self.examButton.clicked.connect(lambda: self.secondButtonClicked(self.examButton))
        self.level4Button.clicked.connect(lambda: self.secondButtonClicked(self.level4Button))
        self.level6Button.clicked.connect(lambda: self.secondButtonClicked(self.level6Button))
        self.professionalButton.clicked.connect(lambda: self.secondButtonClicked(self.professionalButton))
        self.toeflButton.clicked.connect(lambda: self.secondButtonClicked(self.toeflButton))
        self.greButton.clicked.connect(lambda: self.secondButtonClicked(self.greButton))
        self.ieltsButton.clicked.connect(lambda: self.secondButtonClicked(self.ieltsButton))
        self.randomButton.clicked.connect(lambda: self.secondButtonClicked(self.randomButton))
        self.nextButton.clicked.connect(lambda: self.secondButtonClicked(self.randomButton))

        # 第三页按钮点击事件
        self.checkBox_all.stateChanged.connect(lambda: self.getCheckboxAllCheckable())
        self.nextButton_2.clicked.connect(lambda: self.getCheckboxCheckable())
        self.nextButton_2.clicked.connect(lambda: self.setFourthPageContent())

        # 第四页按钮点击事件
        self.choice_1.clicked.connect(lambda: self.getFourthPageChoice(self.choice_1))
        self.choice_2.clicked.connect(lambda: self.getFourthPageChoice(self.choice_2))
        self.choice_3.clicked.connect(lambda: self.getFourthPageChoice(self.choice_3))
        self.choice_4.clicked.connect(lambda: self.getFourthPageChoice(self.choice_4))
        self.choice_5.clicked.connect(lambda: self.getFourthPageChoice(self.choice_5))

    def getFourthPageChoice(self, button):
        """ 获取第四页选项 """
        if button == self.choice_1:
            answer = "A"
        elif button == self.choice_2:
            answer = "B"
        elif button == self.choice_3:
            answer = "C"
        elif button == self.choice_4:
            answer = "D"
        elif button == self.choice_5:
            answer = "E"

        if answer != self.re_dic[self.js_src2["data"][self.position[self.num - 1]]["rank"]]:
            for key in self.re_dic.keys():
                self.dic2.update({}.fromkeys(self.re_dic[key], key))
            self.wrong_words.append(
                f'{self.words_knows[self.num - 1]}:' +
                f'{self.dic2[self.re_dic[self.js_src2["data"][self.position[self.num - 1]]["rank"]]]}')
        else:
            self.right_ranks.append(str(self.js_src2["data"][self.position[self.num - 1]]["rank"]))

        if self.num == len(self.words_knows):
            payload = {
                "category": self.lexicon,
                "phase": "",
                "right_ranks": ",".join(self.right_ranks),
                "word_ranks": ",".join(self.word_ranks)
            }
            src3 = requests.post(self.url3, data=payload)
            js_src3 = json.loads(src3.text)
            self.vocabulary.setText(str(js_src3["data"]["vocab"]))
            self.vocabularyContent.setText(str(js_src3["data"]["comment"]))
            self.fourthPage.close()
            self.choiceWidget.close()
            self.word.close()
            self.wordNums.close()
        else:
            self.setFourthPageContent()

    def setFourthPageContent(self):
        """ 设置第四页内容 """
        self.dic = []
        self.dic2 = {}
        if self.words_knows:
            self.num += 1
            temp = self.js_src2["data"][self.position[self.num - 1]]["definition_choices"]
            for j in range(len(temp)):
                self.dic.append(temp[j]["rank"])
                self.dic.append(temp[j]["definition"])
                self.re_dic = dict(zip(self.dic, ["A", "A", "B", "B", "C", "C", "D", "D"]))
                exec("self.choice_{}.setText(temp[{}]['definition'])".format(j + 1, j))
            self.choice_5.setText("不认识")
            self.word.setText(self.words_knows[self.num - 1])
            self.wordNums.setText("{}/{}".format(self.num, len(self.words_knows)))
        else:
            self.fourthPage.close()
            self.choiceWidget.close()
            self.word.close()
            self.wordNums.close()

    def getCheckboxCheckable(self):
        """ 获取多选按钮是否勾选 """
        for i in range(1, 51):
            exec("""
if self.checkBox_{}.isChecked():
    self.words_knows.append(self.words[{}])
    self.position.append({})

else:
    self.not_knows.append(self.words[{}])
self.word_ranks.append(str(self.js_src2["data"][{}]["rank"]))
        """.format(i, i - 1, i - 1, i - 1, i - 1))

    def getCheckboxAllCheckable(self):
        """ 全选按钮被勾选时的处理 """
        if self.checkBox_all.checkState() == Qt.Checked:
            for i in range(1, 51):
                exec("""
self.checkBox_{}.setChecked(True)
                """.format(i))
        elif self.checkBox_all.checkState() == Qt.Unchecked:
            for i in range(1, 51):
                exec("""
self.checkBox_{}.setChecked(False)
                """.format(i))

    def getVocabularyLexicon(self):
        """ 获取对应词库的url名称 """
        src1 = requests.get(self.url1, "utf-8")
        js_src1 = json.loads(src1.text)
        for d in js_src1["data"]:
            self.choices.append(d[0])

    def secondButtonClicked(self, button):
        """ 根据点击的按钮获取要显示的单词 """
        if button == self.GMATButton:
            self.getVocabulary(self.choices[0])
        elif button == self.mbaButton:
            self.getVocabulary(self.choices[1])
        elif button == self.examButton:
            self.getVocabulary(self.choices[2])
        elif button == self.level4Button:
            self.getVocabulary(self.choices[3])
        elif button == self.level6Button:
            self.getVocabulary(self.choices[4])
        elif button == self.professionalButton:
            self.getVocabulary(self.choices[5])
        elif button == self.toeflButton:
            self.getVocabulary(self.choices[6])
        elif button == self.greButton:
            self.getVocabulary(self.choices[7])
        elif button == self.ieltsButton:
            self.getVocabulary(self.choices[8])
        elif button == self.randomButton:
            self.getVocabulary(self.choices[9])

    def getVocabulary(self, lexicon):
        """ 获取单词进行测试 """
        src2 = requests.get(self.url2 + lexicon, "utf-8")
        js_src2 = json.loads(src2.text)

        for i in range(len(js_src2["data"])):
            exec('self.checkBox_{}.setText(js_src2["data"][{}]["content"])'.format(i + 1, i))
            self.words.append(js_src2["data"][i]["content"])

        # 第二次请求的内容
        self.js_src2 = js_src2
        self.lexicon = lexicon


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

# pyrcc5 shanbeircc.qrc -o shanbeircc_rc.py
