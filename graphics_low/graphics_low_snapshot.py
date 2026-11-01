"""原始画质快照。

快照必须全局只有一份：config/graphics_low_snapshot.yml（不带实例目录）。
原因是一条龙会按账号顺序跑多个实例，如果每个实例各存一份快照，
第二个实例跑降画质时自己的快照是空的，就会把已经调低的档位当成
「原始档位」记下来，之后恢复画质恢复的是低画质。

游戏客户端本身也只有一套全局画质设置，所以全局一份与实际情况一致。
"""

from __future__ import annotations

from one_dragon.base.config.yaml_config import YamlConfig

MODULE_NAME = 'graphics_low_snapshot'


class GraphicsLowSnapshotConfig(YamlConfig):
    """降画质前记下的原始档位，全局唯一。"""

    def __init__(self) -> None:
        YamlConfig.__init__(self, MODULE_NAME)

    @property
    def original_fps(self) -> str:
        """原始帧率，空串表示没记录到。"""
        return self.get('original_fps', '')

    @original_fps.setter
    def original_fps(self, new_value: str) -> None:
        self.update('original_fps', new_value)

    @property
    def original_render_scale(self) -> str:
        """原始渲染精度，空串表示没记录到。"""
        return self.get('original_render_scale', '')

    @original_render_scale.setter
    def original_render_scale(self, new_value: str) -> None:
        self.update('original_render_scale', new_value)

    @property
    def original_antialias(self) -> str:
        """原始抗锯齿，空串表示没记录到。"""
        return self.get('original_antialias', '')

    @original_antialias.setter
    def original_antialias(self, new_value: str) -> None:
        self.update('original_antialias', new_value)

    @property
    def snapshot_date(self) -> str:
        """记录日期，格式 YYYY-MM-DD。"""
        return self.get('snapshot_date', '')

    @snapshot_date.setter
    def snapshot_date(self, new_value: str) -> None:
        self.update('snapshot_date', new_value)

    def clear(self) -> None:
        """清空快照，下次运行重新记录。"""
        self.original_fps = ''
        self.original_render_scale = ''
        self.original_antialias = ''
        self.snapshot_date = ''
