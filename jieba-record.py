#coding:utf-8
import jieba

#分为全模式和精准模式，默认为精准模式
seg_list=jieba.cut('刚好遇见你，留下足迹多美丽',cut_all=False)
print("/".join(seg_list))

#制定字典，包含词库里没有的词,详细见github地址
#https://github.com/fxsjy/jieba
