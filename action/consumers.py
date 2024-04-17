import json
import threading
import time
from datetime import timedelta

from channels.generic.websocket import WebsocketConsumer
from django.utils import timezone

from action.models import AccessRecord


class ActionConsumer(WebsocketConsumer):
    last_query_time = None
    group_name = 'dashboard_updates'
    interval = 3  # 定时器间隔
    stop_thread = threading.Event()  # 事件用于通知线程何时停止

    def connect(self):
        self.channel_layer.group_add(self.group_name, self.channel_name)
        self.accept()

        # 创建并启动定时器线程
        self.timer_thread = threading.Thread(target=self.timer_event)
        self.timer_thread.daemon = True
        self.timer_thread.start()

    def disconnect(self, close_code):
        # 设置事件，通知线程停止
        self.stop_thread.set()
        self.channel_layer.group_discard(self.group_name, self.channel_name)

    def get_records(self):
        actions = self.get_data()
        records = []
        for action in actions:
            record = {
                'user': action.userid.name,
                'building': action.buildingid.name,
                'createdat': action.createdat.strftime('%Y-%m-%d %H:%M:%S'),
                'status': action.status
            }
            records.append(record)
        return records

    def send_records(self, records):
        # 将数据转换为 JSON 字符串
        json_data = json.dumps(records)
        # 直接发送数据到 WebSocket 连接
        self.send(text_data=json_data)

    def receive(self, text_data=None, bytes_data=None):
        pass

    def timer_event(self):
        while not self.stop_thread.is_set():
            try:
                time.sleep(self.interval)
                # 获取数据并发送给前端
                records = self.get_records()
                self.send_records(records)
                print(f"定时器事件：成功")
            except Exception as e:
                print(f"定时器事件：发生了一个错误：{e}")
        print("定时器线程已停止")

    def get_data(self):
        # 如果是第一次查询，获取过去两秒钟内的记录
        building_id = self.scope['url_route']['kwargs']['building_id']
        if self.last_query_time is None:

            two_seconds_ago = timezone.now() + timedelta(hours=8) - timezone.timedelta(seconds=self.interval)
            self.last_query_time = timezone.now() + timedelta(hours=8)  # 更新上次查询时间点
            acc_obj = AccessRecord.objects.filter(createdat__gt=two_seconds_ago, buildingid=building_id)
        else:
            # 否则，获取自上次查询以来新创建的记录
            acc_obj = AccessRecord.objects.filter(createdat__gt=self.last_query_time, buildingid=building_id)
            self.last_query_time = timezone.now() + timedelta(hours=8)  # 更新上次查询时间点

        print(acc_obj.values('createdat'))
        print(timezone.now() + timedelta(hours=8))

        return acc_obj

