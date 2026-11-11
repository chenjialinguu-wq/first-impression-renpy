# First Impression / 《第一印象》

基于简·奥斯汀《傲慢与偏见》改编的 Ren'Py 图像小说式叙事游戏原型。

## 当前进度

- 第一章《梅里屯舞会》：可运行试玩版
- 第二章《尼日斐花园》：可运行原型版
- Android 横屏 UI：已加入基础适配
- 第三章及以后：后续继续开发

## 目录结构

```text
game/
├─ script.rpy          # 第一章、公共变量、入口
├─ chapter02.rpy       # 第二章
├─ mobile_ui.rpy       # Android 横屏 UI
├─ images/
│  ├─ *.png            # 第一章背景
│  └─ characters/      # 人物立绘
└─ audio/

docs/
├─ chapter02.md
├─ mobile_android.md
└─ asset_manifest.md
```

后续章节建议继续采用 `game/chapter03.rpy`、`game/chapter04.rpy` 的方式增加，不把所有剧情重新塞回 `script.rpy`。

## 运行

1. 安装 Ren'Py。
2. 创建/打开一个 Ren'Py 项目。
3. 将本仓库的 `game/` 目录复制到项目根目录并合并。
4. 从 Ren'Py Launcher 启动项目。

## Android

当前项目按横屏试玩方向设计。Android 打包建议先构建 Universal APK 真机测试。

## 资源说明

仓库中的 PNG 使用适合游戏运行和版本管理的优化尺寸；文件名与脚本路径保持不变。原始高分辨率生成素材建议另行归档，不直接作为 Git 主仓库的日常版本。

## 开发约定

- 新章节：`game/chapterNN.rpy`
- 公共变量/入口：`game/script.rpy`
- 每次重要试玩节点在 `CHANGELOG.md` 记录
- ZIP/APK 成品后续建议放 GitHub Releases，而不是反复提交到源码目录

## 版权

原作《Pride and Prejudice》已进入公版领域。项目中的现代改编文本、界面和视觉素材属于本项目开发资源。正式公开或商业发布前应再次核查字体、音效及其他第三方素材授权。
