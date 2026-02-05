# -*- coding: utf-8 -*-
"""
Banana 图像生成插件入口文件
"""

from dify_plugin import Plugin, DifyPluginEnv


class BananaPlugin(Plugin):
    def __init__(self):
        super().__init__()


plugin = BananaPlugin()


def main():
    plugin.run()


if __name__ == "__main__":
    main()
