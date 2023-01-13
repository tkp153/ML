#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.max_epoch = 20
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        self.data_dir = "/root/ML/dataset_folk/images"
        self.train_ann = "/root/ML/dataset_folk/annotations/train_annotations.json"
        self.val_ann = "/root/ML/dataset_folk/annotations/validation_annotations.json"

        self.num_classes = 2

        self.eval_interval = 1
