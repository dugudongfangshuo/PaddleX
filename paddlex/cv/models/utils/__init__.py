# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

seg_pretrain_weights_dict = {
    'UNet': ['CITYSCAPES'],
    'DeepLabV3P': ['CITYSCAPES', 'PascalVOC'],
    'FastSCNN': ['CITYSCAPES'],
    'HRNet': ['CITYSCAPES', 'PascalVOC'],
    'BiSeNetV2': ['CITYSCAPES']
}

det_pretrain_weights_dict = {
    'YOLOv3_MobileNetV1': ['COCO', 'PascalVOC'],
    'YOLOv3_DarkNet53': ['COCO'],
    'YOLOv3_ResNet50_vd_dcn': ['COCO'],
    'YOLOv3_MobileNetV3': ['COCO', 'PascalVOC'],
    'FasterRCNN_ResNet50_vd': ['COCO'],
    'FasterRCNN_ResNet50_vd_fpn': ['COCO'],
    'FasterRCNN_ResNet50': ['COCO'],
    'FasterRCNN_ResNet50_fpn': ['COCO'],
    'FasterRCNN_ResNet34_fpn': ['COCO'],
    'FasterRCNN_ResNet34_vd_fpn': ['COCO'],
    'FasterRCNN_ResNet101_fpn': ['COCO'],
    'FasterRCNN_ResNet101_vd_fpn': ['COCO']
}
