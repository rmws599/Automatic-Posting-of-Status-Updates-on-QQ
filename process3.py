import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        device_session, _, _ = xbot_visual.mobile.connect_device(connect_source="specific", connect_mode="appium", ingore_failed_device=True, auto_unlock=False, unlockType="pin", mobile_password=xbot_visual.decrypt(""), custom_name="23049RAD8C", _block=("子流程3", 1, "连接手机"))
        xbot_visual.mobile.element.click(session=device_session, element=package.selector("框架容器"), clicks="click", delay_after="1", anchor_type="center", _block=("子流程3", 2, "点击元素(手机)"))
    finally:
        pass
