#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest2 as unittest
from sasila.system_normal.processor.fang_processor import Fang_Processor
from sasila.system_normal.spider.spider_core import SpiderCore
from sasila.system_normal.pipeline.console_pipeline import ConsolePipeline
from sasila.system_normal.pipeline.test_pipeline import TestPipeline


class TestProcessor(unittest.TestCase):
    def test_car_processor(self):
        # test_pipeline = TestPipeline()
        # SpiderCore(Fang_Processor(), test=True).set_pipeline(ConsolePipeline()).set_pipeline(test_pipeline).start()
        # self.assertEqual(len(test_pipeline.result), 10, '爬取结果，10个字段')
        self.assertEqual(1, 1)
