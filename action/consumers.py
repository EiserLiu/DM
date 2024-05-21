import asyncio
import os

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import timedelta

from django.conf.global_settings import MEDIA_ROOT
from django.utils import timezone
from .models import AccessRecord  # 假设你的模型是AccessRecord
import json


class ActionConsumer(AsyncWebsocketConsumer):
    group_name = 'dashboard_updates'
    interval = 3  # 定时器间隔，单位为秒
    last_query_time = None

    async def connect(self):
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

        # 创建并启动定时任务
        self.timer_task = asyncio.create_task(self.timer_event())

    async def disconnect(self, close_code):
        # 取消定时任务
        if not self.timer_task.done():
            self.timer_task.cancel()

        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    @database_sync_to_async
    def get_records_sync(self):
        if self.last_query_time is None:
            # 如果还没有查询时间，从某个初始时间开始
            self.last_query_time = timezone.now()

            # 获取当前时间
        current_time = timezone.now()

        # 查询从上次查询时间之后的所有记录
        acc_obj = AccessRecord.objects.filter(createdat__gt=self.last_query_time)

        # 更新查询时间为当前时间（确保在下一次循环时只查询新数据）
        self.last_query_time = current_time
        # 转换为字典列表
        records = {"data": [
            {
                'user': action.userid.name if action.userid else None,
                'building': action.buildingid.name if action.buildingid else None,
                'created_at': action.createdat.strftime('%Y-%m-%d %H:%M:%S'),
                'status': action.status,
                'image': action.userid.image.url if action.userid.image else None,
            }
            for action in acc_obj
        ]}
        if records['data']:
            count = acc_obj.count()
            records['count'] = count
            print(records)
        return records

    async def send_records(self, records):
        # 将数据转换为 JSON 字符串并发送
        if records['data'] != None:
            await self.send(text_data=json.dumps(records))

    async def timer_event(self):
        while True:
            try:
                await asyncio.sleep(self.interval)
                records = await self.get_records_sync()  # 使用异步版本的方法
                if records:
                    await self.send_records(records)
            except asyncio.CancelledError:
                # 定时任务被取消时退出循环
                break
            except Exception as e:
                # 异常处理，可以记录日志或执行其他操作
                print(f"发生错误: {e}")
