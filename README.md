# First Impression / 《第一印象》

基于简·奥斯汀《傲慢与偏见》改编的 Ren'Py 图像小说式叙事游戏原型。

## 当前进度

- 第一章《梅里屯舞会》：剧情与 Ren'Py 脚本已同步
- 第二章《尼日斐花园》：剧情与 Ren'Py 原型脚本已同步
- Android 横屏 UI：已同步
- 第一章 PNG 背景与人物立绘：本地原型包中已完成，GitHub 二进制资源待单独补齐
- 第三章及以后：后续继续开发

## 仓库结构

```text
game/
├─ script.rpy
├─ mobile_ui.rpy
├─ chapter01/
│  ├─ 01_breakfast_scene.rpy
│  ├─ ...
│  └─ 08_chapter_result.rpy
├─ chapter02/
│  ├─ 00_core.rpy
│  ├─ ...
│  └─ 08_ch02_result.rpy
├─ images/                 # PNG 资源待补齐
└─ audio/

docs/
├─ chapter02.md
├─ mobile_android.md
└─ asset_manifest.md
```

这样后续第三、第四章可以继续增加：

```text
game/chapter03/
game/chapter04/
```

无需反复覆盖整个项目。

## 运行状态

当前 GitHub 仓库已经包含第一、第二章的完整剧情脚本和公共 UI 代码。  
由于 GitHub 连接器本轮无法直接从本地工作区传输 PNG 二进制文件，直接 clone 当前仓库时第一章图片资源仍需要按照 `docs/asset_manifest.md` 补齐。

现有“第一、二章可运行原型 ZIP”仍保留为完整试玩来源。

## Android

当前项目按横屏试玩方向设计。Android 打包建议先构建 Universal APK 真机测试。

## 开发约定

- 公共定义与入口：`game/script.rpy`
- 第一章：`game/chapter01/`
- 第二章：`game/chapter02/`
- 后续章节继续按 `chapterNN/` 拆分
- 重要变化写入 `CHANGELOG.md`
- ZIP / APK 成品后续建议放 GitHub Releases，不反复提交到源码目录

## 版权

原作《Pride and Prejudice》已进入公版领域。现代改编文本、界面和项目视觉素材属于本项目开发资源。正式公开或商业发布前，应再次核查字体、音效及其他第三方素材授权。
