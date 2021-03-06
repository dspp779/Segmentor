#!/usr/bin/python
# -*- coding: utf8 -*-
#
#    This file is part of the NAER Segmentor  -
#    Copyright (c) 2016 National Academy for Educational Research
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


# ==========================================
# use crf POS tagger
# ==========================================
from __future__ import print_function, unicode_literals
import re
import json


class Tokenizer:
    # regular expression for tokenize document to sentences

    __to_sents_rule = re.compile("([^\n]+)[\n]*")

    # 中文字元
    __ch = "[\u4E00-\u9fa5]"

    # 英文字元
    __eng = "[a-zA-Z0-9_ａ-ｚＡ-Ｚ０-９－＿]"

    # 英文字元+符號
    __eng_sym = "[a-zA-Z0-9_ａ-ｚＡ-Ｚ０-９－＿\\/,.&\-]"

    # 其他字元
    __other = "[^\w\u4E00-\u9fa5\s]"

    # regular expression for tokenize to words
    __to_tokens_rule = re.compile('{0}|{1}{2}*|{3}'.format(__ch, __eng, __eng_sym, __other))

    @staticmethod
    def ToSents(doc):
        """split a document into sentences"""
        # sents = [m.group(0).strip() for m in re.finditer(Tokenizer.__to_sents_rule, doc)]
        # return sents
        # https://docs.python.org/3/library/stdtypes.html#str.splitlines
        return doc.splitlines()

    @staticmethod
    def ToTokens(sent):
        """split a sentence into Chinese chars or English words"""
        tokens = [data for data in Tokenizer.__to_tokens_rule.findall(sent)]
        return tokens

if __name__ == '__main__':
    a = "asdadsfa\nadsfasdf\n\nasdfasdf\r\n"
    L = Tokenizer.ToSents(a)
    print(L)
    Tokenizer.splitRule = re.compile('[^ ]*[ ]')
    a = "asdadsfa adsfasdf\nasdfasdf "
    L = Tokenizer.ToSents(a)
    print(L)
    a = "這是中文 asdadsfa adsf中文asdf 這是中文 國家教 育研 究院\n研究國\n家教育asdfasdf "
    print(a)
    L = Tokenizer.ToTokens(a)
    print(json.dumps(L, ensure_ascii=False))
