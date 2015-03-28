#! /usr/bin/python
# coding: utf-8

# Filename transduce.py by linlin
# coding=utf-8


import re
import sys
import locale

reload(sys)
sys.setdefaultencoding('utf-8')
locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')

#content = '让 我们 我们 是 嗯 不错 的 Paris in that that spring'

for content in sys.stdin:
###########################################
    if len(sys.argv) == 2:
		if sys.argv[1] == "-d":

			rule9_2 = re.compile(ur'(是\s{0,2}不\s{0,2}是)')
			subText = rule9_2.sub(ur'是       不       是',content.decode('utf8'))
			del content
			content = subText

			rule9_3 = re.compile(ur'(可\s{0,2}不\s{0,2}可)')
			subText = rule9_3.sub(ur'可       不       可',content.decode('utf8'))
			del content
			content = subText

			rule9_4 = re.compile(ur'(..)(个).{1,4}(不是|不|不对|没|不不|呃|嗯|恩|哦)(.{0,5}.\2.)')
			subText = rule9_4.sub(ur'<\4>', content.decode('utf8'))
			del content
			content = subText

			rule9_6 = re.compile(ur'(.{4,9}).{0,3}(,|，|、|[\u4e00-\u9fa5]{1,2}).{0,2}\1')
			subText = rule9_6.sub(ur' <\1> ', content.decode('utf8'))
			del content
			content = subText

			rule9_1 = re.compile(ur'(.)([\u4e00-\u9fa5]{1,4}).{1,4}(不是|不|不对|没|不不|呃|嗯|恩)(.{0,5}.\2.)')
			subText = rule9_1.sub(ur' <\4> ', content.decode('utf8'))
			del content
			content = subText

			rule9 = re.compile(ur'(.)([\u4e00-\u9fa5]{1,3}).{0,3}((不是)|没|(不不)|呃|嗯|恩)(.{0,3}\2)')
			subText = rule9.sub(ur' <\6> ', content.decode('utf8'))
			del content
			content = subText

			rule9_5 = re.compile(ur'([\u4e00-\u9fa5]{1,3})\s(哦|呃|嗯|啊).{0,2}(不|没)\s([\u4e00-\u9fa5]{1,3})')
			subText = rule9_5.sub(ur' <\4 > ', content.decode('utf8'))
			del content
			content = subText

			rule1 = re.compile(ur'([\u4e00-\u9fa5]{2,4})(.{0,3})\s{0,2}\1')
			subText = rule1.sub(ur' <\2 \1> ',content.decode('utf8'))
			del content
			content = subText

			rule1_1 = re.compile(ur'(我|你|他|我们).{0,2}(首先).{0,1}\1')
			subText = rule1_1.sub(ur' <\2 \1> ',content.decode('utf8'))
			del content
			content = subText

			rule3 = re.compile(ur'([,.。，])\s{0,2}就([^说是][^说是])')
			subText = rule3.sub(ur' <\1\2> ', content.decode('utf8'))
			del content
			content = subText

			rule4 = re.compile(ur'(呢|嘛|啊|哦)([^，,.。][^，,.。])')
			subText = rule4.sub(ur'<\2>',content.decode('utf8'))
			del content
			content = subText

			rule5_1 = re.compile(ur'([\u4e00-\u9fa5])[^\u4e00-\u9fa5]{1,3}\1')
			subText = rule5_1.sub(ur'<\1> ',content.decode('utf8'))
			del content
			content = subText

			rule2_1 = re.compile(ur'这个.?问')
			subText = rule2_1.sub(ur'这   个 问',content.decode('utf8'))
			del content
			content = subText

			rule2_2 = re.compile(ur'(他|我们|它).?这个')
			subText = rule2_2.sub(ur' \1 这   个 ',content.decode('utf8'))
			del content
			content = subText

			rule2 = re.compile(ur'嗯|呃|恩|哦|唉|哎|这个')
			subText = rule2.sub(ur'< >',content.decode('utf8'))
			del content
			content = subText

			rule1 = re.compile(ur'([\u4e00-\u9fa5]{2,4})(\w{0,3})\s*(\w{0,3})\1')
			subText = rule1.sub(ur' <\2 \1> ',content.decode('utf8'))
			del content
			content = subText

			rule1_3 = re.compile(ur'各\s.{1,3}各')
			subText = rule1_3.sub(ur'<各>',content.decode('utf8'))
			del content
			content = subText
		else:
			content = "不指定参数为正常模式， 指定-d为调试模式！"
#############################################
    else:

		rule9_2 = re.compile(ur'(是\s{0,2}不\s{0,2}是)')
		subText = rule9_2.sub(ur'是                  不 是',content.decode('utf8'))
		del content
		content = subText

		rule9_3 = re.compile(ur'(可\s{0,2}不\s{0,2}可)')
		subText = rule9_3.sub(ur'可                   不 可',content.decode('utf8'))
		del content
		content = subText

		rule9_4 = re.compile(ur'(..)(个).{1,4}(不是|不|不对|没|不不|呃|嗯|恩|哦)(.{0,5}.\2.)')
		subText = rule9_4.sub(ur'\4', content.decode('utf8'))
		del content
		content = subText

		rule9_6 = re.compile(ur'(.{4,9}).{0,3}(,|，|、|[\u4e00-\u9fa5]{1,2}).{0,2}\1')
		subText = rule9_6.sub(ur'\1', content.decode('utf8'))
		del content
		content = subText

		rule9_1 = re.compile(ur'(.)([\u4e00-\u9fa5]{1,4}).{1,4}(不是|不|不对|没|不不|呃|嗯|恩)(.{0,5}.\2.)')
		subText = rule9_1.sub(ur'\4', content.decode('utf8'))
		del content
		content = subText

		rule9 = re.compile(ur'(.)([\u4e00-\u9fa5]{1,3}).{0,3}((不是)|没|(不不)|呃|嗯|恩)(.{0,3}\2)')
		subText = rule9.sub(ur'\6', content.decode('utf8'))
		del content
		content = subText

		rule9_5 = re.compile(ur'([\u4e00-\u9fa5]{1,3})\s(哦|呃|嗯|啊).{0,2}(不|没)\s([\u4e00-\u9fa5]{1,3})')
		subText = rule9_5.sub(ur'\4', content.decode('utf8'))
		del content
		content = subText

		rule1 = re.compile(ur'([\u4e00-\u9fa5]{2,4})(.{0,3})\s{0,2}\1')
		subText = rule1.sub(ur'\2 \1',content.decode('utf8'))
		del content
		content = subText

		rule1_1 = re.compile(ur'(我|你|他|我们).{0,2}(首先).{0,1}\1')
		subText = rule1_1.sub(ur'\2 \1',content.decode('utf8'))
		del content
		content = subText

		rule3 = re.compile(ur'([,.。，])\s{0,2}就([^说是][^说是])')
		subText = rule3.sub(ur'\1\2', content.decode('utf8'))
		del content
		content = subText

		rule4 = re.compile(ur'(呢|嘛|啊|哦)([^，,.。][^，,.。])')
		subText = rule4.sub(ur'\2',content.decode('utf8'))
		del content
		content = subText

		rule5_1 = re.compile(ur'([\u4e00-\u9fa5])[^\u4e00-\u9fa5]{1,3}\1')
		subText = rule5_1.sub(ur'\1',content.decode('utf8'))
		del content
		content = subText

		rule2_1 = re.compile(ur'这个.?问')
		subText = rule2_1.sub(ur'这  个 问',content.decode('utf8'))
		del content
		content = subText

		rule2_2 = re.compile(ur'(他|我们|它).?这个')
		subText = rule2_2.sub(ur'\1 这   个',content.decode('utf8'))
		del content
		content = subText

		rule2 = re.compile(ur'嗯|呃|恩|哦|唉|哎|这个')
		subText = rule2.sub(ur'',content.decode('utf8'))
		del content
		content = subText

		rule1 = re.compile(ur'([\u4e00-\u9fa5]{2,4})(\w{0,3})\s*(\w{0,3})\1')
		subText = rule1.sub(ur'\2 \1',content.decode('utf8'))
		del content
		content = subText

		rule1_3 = re.compile(ur'各\s.{1,3}各')
		subText = rule1_3.sub(ur'各',content.decode('utf8'))
		del content
		content = subText

###################################################

print(content.encode('utf8'))

#  print("Times of substitute: %i" %nCountSubs)
