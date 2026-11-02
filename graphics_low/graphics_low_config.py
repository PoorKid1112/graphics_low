"""降低画质插件的配置。

只存三个目标档位。原始档位不在这里 —— 快照要全局一份，放在
graphics_low_snapshot.py 对应的 config/graphics_low_snapshot.yml 里。
"""

from one_dragon.base.operation.application.application_config import ApplicationConfig

from . import graphics_low_const


class GraphicsLowConfig(ApplicationConfig):

    def __init__(self, instance_idx: int, group_id: str) -> None:
        ApplicationConfig.__init__(
            self,
            app_id=graphics_low_const.APP_ID,
            instance_idx=instance_idx,
            group_id=group_id,
        )

    @property
    def target_fps(self) -> str:
        """目标帧率，取值必须和游戏下拉框文字一致。"""
        return self.get('target_fps', '30')

    @target_fps.setter
    def target_fps(self, new_value: str) -> None:
        self.update('target_fps', new_value)

    @property
    def target_render_scale(self) -> str:
        """目标渲染精度。"""
        return self.get('target_render_scale', '0.8')

    @target_render_scale.setter
    def target_render_scale(self, new_value: str) -> None:
        self.update('target_render_scale', new_value)

    @property
    def target_antialias(self) -> str:
        """目标抗锯齿。"""
        return self.get('target_antialias', '关闭')

    @target_antialias.setter
    def target_antialias(self, new_value: str) -> None:
        self.update('target_antialias', new_value)

    @property
    def target_font(self) -> str:
        """「其他」页的目标字体，取值必须和游戏下拉框文字一致。"""
        return self.get('target_font', '全局细体')

    @target_font.setter
    def target_font(self, new_value: str) -> None:
        self.update('target_font', new_value)
