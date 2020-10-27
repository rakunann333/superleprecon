import os

# change file name
# basepath 名前を変えるファイルの場所。
# before_word 変更前の一部の言葉。
# after_word 変更後の一部の言葉。
# !
# ?
# *
# TODO

def namechange(basepath, before_word, after_word):
    names = [i for i in os.listdir(basepath) if before_word in i]
    for name in names:
        name_replaced = name.replace(before_word, after_word)
        os.rename(os.path.join(basepath, name),os.path.join(basepath, name_replaced))