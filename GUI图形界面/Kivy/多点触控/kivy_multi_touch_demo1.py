# -*- coding: utf-8 -*-
'''
kivy学习笔记—触控手势的识别
https://blog.csdn.net/cloveses/article/details/80411730


'''

from kivy.gesture import GestureDatabase
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.gesture import Gesture
 
# 构建需要响应的手势数据
ges_strs = {
    'left_to_right_line':'ds...', # 这里为什么必须很长的字符串 ？？表示不解
    'right_to_left_line':'df...',# 这里为什么必须很长的字符串 ？？表示不解
    'bottom_to_top_line':'eNq1m...'# 这里为什么必须很长的字符串 ？？表示不解
}
gestures = GestureDatabase()
 
for name,ges_str in ges_strs.items():
    gesture = gestures.str_to_gesture(ges_str)#TODO bug
    gesture.name = name
    gestures.add_gesture(gesture)
 
 
class MyGesure(BoxLayout):
    def on_touch_down(self,touch): # 检测开始触摸动作
        touch.ud['gesture_path'] = [(touch.x,touch.y)] #记录动作坐标
        super().on_touch_down(touch)
 
    def on_touch_move(self,touch):# 检测开始划动动作
        touch.ud['gesture_path'].append((touch.x,touch.y))#记录划动坐标
        super().on_touch_move(touch)
 
    def on_touch_up(self,touch):#当手指抬起时
        # print(touch.ud['gesture_path'])
        if 'gesture_path' in touch.ud:
            gesture = Gesture()
            gesture.add_stroke(touch.ud['gesture_path'])
            gesture.normalize()
            match = gestures.find(gesture,minscore=0.9)
            if match:
                print('ha ha:',match[1].name)
        super().on_touch_up(touch)
 
class MygestureApp(App):
    def build(self):
        return MyGesure()
 
MygestureApp().run()