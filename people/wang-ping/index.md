# 王平

## 基本信息

| 字段 | 内容 |
| --- | --- |
| 人物 ID | `wang-ping` |
| 中文名 | 王平 |
| 机构/身份线索 | 同济大学生命科学与技术学院时任院长 |
| 收录原因 | 耿同学讲故事公开质疑其团队 Nature 论文数据异常 |
| 状态 | 已列入初始名单，待补齐论文截图 |

## 耿同学视频线索

- 视频标题：[同济大学，百万经费的nature论文，数据造假过于明显！强烈建议王教授下次造假使用随机数生成器！](https://www.bilibili.com/video/BV1NEDnBbEkA/)
- 发布时间：2026-04-14

## 论文内证据重点

- 论文题名线索：`Human HDAC6 senses valine abundancy to regulate DNA damage`。
- 待核对位置：论文正文图表、补充数据表、原始数据文件。
- 已知待截图异常：多列数据固定差值约 `0.3`、末位数字集中为 `5`、列间存在规律性加减关系。

## 下一步

- [x] 已尝试下载论文正文和补充材料；当前 shell 网络访问 Nature 返回代理 403，详见 [`../../data/download_attempts.csv`](../../data/download_attempts.csv)。
- [ ] 建立 `papers/` 下的论文条目。
- [ ] 截取具体图号、表号和数据列。
- [ ] 在 `evidence/` 中为每个异常点建立可跳转证据页。
